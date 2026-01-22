from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from form.form_pembelian import Ui_Form
from models.produk_model import ProdukModel
import datetime

class PembelianController(QWidget):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db
        self.produk_model = ProdukModel(db)
        self.cart = [] # (id_produk, nama, harga_beli, qty, subtotal)

        # Load Data
        self.load_supplier()
        self.load_produk()
        
        # Set tanggal default ke hari ini
        self.ui.input_tanggal.setDateTime(datetime.datetime.now())

        # Connect Events
        self.ui.btn_tambah_item.clicked.connect(self.tambah_item)
        self.ui.btn_hapus_item.clicked.connect(self.hapus_item)
        self.ui.btn_reset_item.clicked.connect(self.reset_cart)
        self.ui.btn_menu_3.clicked.connect(self.simpan_pembelian) # Tombol Simpan

    def load_supplier(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id_supplier, nama_supplier FROM supplier")
            data = cursor.fetchall()
            self.ui.combo_supplier.clear()
            for row in data:
                self.ui.combo_supplier.addItem(row[1], row[0]) # Text=Nama, Data=ID
        except Exception as e:
            print(f"Error load supplier: {e}")

    def load_produk(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id_produk, nama_produk, harga_beli FROM produk")
            data = cursor.fetchall()
            self.ui.combo_produk.clear()
            for row in data:
                # Simpan (id, nama, harga_beli_terakhir)
                self.ui.combo_produk.addItem(f"{row[1]}", row)
        except Exception as e:
            print(f"Error load produk: {e}")

    def tambah_item(self):
        try:
            produk_data = self.ui.combo_produk.currentData() # (id, nama, harga_beli_lama)
            if not produk_data:
                return

            id_produk = produk_data[0]
            nama_produk = produk_data[1]
            
            # Ambil inputan manual user
            try:
                harga_beli = int(self.ui.input_harga_beli.text())
                qty = self.ui.input_jumlah.value()
            except ValueError:
                QMessageBox.warning(self, "Validasi", "Harga harus angka")
                return

            if qty <= 0:
                QMessageBox.warning(self, "Validasi", "Jumlah harus > 0")
                return

            subtotal = harga_beli * qty

            # Tambahkan ke cart
            self.cart.append((id_produk, nama_produk, harga_beli, qty, subtotal))
            self.refresh_table()
            
            # Reset input
            self.ui.input_jumlah.setValue(0)
            self.ui.input_harga_beli.clear()

        except Exception as e:
            print(f"Error tambah item pembelian: {e}")

    def hapus_item(self):
        row = self.ui.table_detail_pembelian.currentRow()
        if row >= 0:
            self.cart.pop(row)
            self.refresh_table()

    def reset_cart(self):
        self.cart.clear()
        self.refresh_table()

    def refresh_table(self):
        self.ui.table_detail_pembelian.setRowCount(len(self.cart))
        total_transaksi = 0
        
        for row, item in enumerate(self.cart):
            # item: (id_produk, nama, harga, qty, subtotal)
            self.ui.table_detail_pembelian.setItem(row, 0, QTableWidgetItem(str(item[0])))
            self.ui.table_detail_pembelian.setItem(row, 1, QTableWidgetItem(item[1]))
            self.ui.table_detail_pembelian.setItem(row, 2, QTableWidgetItem(str(item[2])))
            self.ui.table_detail_pembelian.setItem(row, 3, QTableWidgetItem(str(item[3])))
            self.ui.table_detail_pembelian.setItem(row, 4, QTableWidgetItem(str(item[4])))
            total_transaksi += item[4]

        self.ui.lineEdit.setText(f"Rp {total_transaksi:,.0f}")

    def simpan_pembelian(self):
        if not self.cart:
            QMessageBox.warning(self, "Peringatan", "Data pembelian kosong")
            return

        try:
            id_supplier = self.ui.combo_supplier.currentData()
            tanggal = self.ui.input_tanggal.dateTime().toPyDateTime()
            # ID User admin hardcode sementara atau ambil dari login session jika ada
            id_user = 1 
            total = sum(item[4] for item in self.cart)

            cursor = self.db.cursor()
            
            # 1. Insert ke tabel pembelian
            # Sesuaikan nama kolom dengan database Anda (biasanya ada id_user juga)
            cursor.execute(
                "INSERT INTO pembelian (tanggal, id_supplier, id_user, total) VALUES (%s, %s, %s, %s)",
                (tanggal, id_supplier, id_user, total)
            )
            id_pembelian = cursor.lastrowid

            # 2. Insert Detail & Update Stok
            for item in self.cart:
                # item: (id_produk, nama, harga_beli, qty, subtotal)
                cursor.execute(
                    "INSERT INTO detail_pembelian (id_pembelian, id_produk, jumlah, harga_beli, subtotal) VALUES (%s, %s, %s, %s, %s)",
                    (id_pembelian, item[0], item[3], item[2], item[4])
                )
                
                # Update Stok (Tambah)
                self.produk_model.tambah_stok(item[0], item[3])
                
                # Opsional: Update harga beli terbaru di master produk
                cursor.execute("UPDATE produk SET harga_beli=%s WHERE id_produk=%s", (item[2], item[0]))

            self.db.commit()
            QMessageBox.information(self, "Sukses", "Pembelian berhasil disimpan")
            self.reset_cart()
            self.ui.lineEdit.clear()

        except Exception as e:
            self.db.rollback()
            QMessageBox.critical(self, "Error", f"Gagal simpan pembelian: {e}")
            print(e)