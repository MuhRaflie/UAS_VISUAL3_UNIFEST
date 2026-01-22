from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from form.form_penjualan import Ui_Form
from models.penjualan_model import PenjualanModel
from models.produk_model import ProdukModel
import datetime

class PenjualanController(QWidget):
    def __init__(self, db):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db
        self.model = PenjualanModel(db)
        self.produk_model = ProdukModel(db)
        self.cart = []  # simpan detail sementara

        # Load Data Awal
        self.load_produk()
        self.load_customer() # Error sebelumnya disini karena fungsi ini tidak ada

        # Event Listener
        self.ui.btn_tambah_item.clicked.connect(self.tambah_item) # Sesuaikan nama tombol di UI
        self.ui.btn_menu_3.clicked.connect(self.simpan_penjualan) # Tombol Simpan Transaksi
        self.ui.btn_hapus_item.clicked.connect(self.hapus_item)
        self.ui.btn_reset_item.clicked.connect(self.reset_cart)

    def load_produk(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT id_produk, nama_produk, harga_jual FROM produk")
        self.produk = cursor.fetchall()
        self.ui.combo_produk.clear()
        for p in self.produk:
            # Menyimpan ID produk sebagai user data
            self.ui.combo_produk.addItem(f"{p[1]} - Rp {p[2]}", p)

    # --- PERBAIKAN: Menambahkan Fungsi load_customer ---
    def load_customer(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id_customer, nama_customer FROM customer")
            data = cursor.fetchall()
            self.ui.combo_customer.clear()
            for row in data:
                self.ui.combo_customer.addItem(row[1], row[0]) # Tampil Nama, Simpan ID
        except Exception as e:
            print(f"Error load customer: {e}")

    def tambah_item(self):
        try:
            # PERBAIKAN: Menggunakan input_jumlah sesuai nama di form_penjualan.py
            qty = self.ui.input_jumlah.value() 
            
            if qty <= 0:
                QMessageBox.warning(self, "Warning", "Jumlah harus lebih dari 0")
                return

            produk_data = self.ui.combo_produk.currentData() # Mengambil data (id, nama, harga)
            if not produk_data:
                return

            id_produk = produk_data[0]
            nama = produk_data[1]
            harga = produk_data[2]
            subtotal = qty * harga

            # Masukkan ke keranjang sementara
            self.cart.append((id_produk, nama, harga, qty, subtotal))
            self.refresh_table()
            
            # Reset input jumlah
            self.ui.input_jumlah.setValue(0)
            
        except Exception as e:
            print(f"Error tambah item: {e}")

    def hapus_item(self):
        row = self.ui.table_detail_penjualan.currentRow()
        if row >= 0:
            self.cart.pop(row)
            self.refresh_table()
        else:
            QMessageBox.warning(self, "Peringatan", "Pilih item yang ingin dihapus dari tabel")

    def reset_cart(self):
        self.cart.clear()
        self.refresh_table()

    def refresh_table(self):
        # Sesuaikan dengan nama tabel di UI: table_detail_penjualan
        self.ui.table_detail_penjualan.setRowCount(len(self.cart))
        total_belanja = 0
        
        for row, item in enumerate(self.cart):
            # Item format: (id_produk, nama, harga, qty, subtotal)
            self.ui.table_detail_penjualan.setItem(row, 0, QTableWidgetItem(str(item[0]))) # ID
            self.ui.table_detail_penjualan.setItem(row, 1, QTableWidgetItem(item[1]))      # Nama
            self.ui.table_detail_penjualan.setItem(row, 2, QTableWidgetItem(str(item[2]))) # Harga
            self.ui.table_detail_penjualan.setItem(row, 3, QTableWidgetItem(str(item[3]))) # Qty
            self.ui.table_detail_penjualan.setItem(row, 4, QTableWidgetItem(str(item[4]))) # Subtotal
            total_belanja += item[4]

        # Update label total (lineEdit di UI Anda untuk total)
        self.ui.lineEdit.setText(f"Rp {total_belanja:,.0f}")

    def simpan_penjualan(self):
        if not self.cart:
            QMessageBox.warning(self, "Error", "Keranjang belanja masih kosong")
            return

        try:
            id_customer = self.ui.combo_customer.currentData()
            tanggal = self.ui.input_tanggal.dateTime().toPyDateTime() # Ambil dari DateTimeEdit
            total = sum(item[4] for item in self.cart)

            # 1. Insert ke tabel penjualan
            id_penjualan = self.model.insert_penjualan(tanggal, id_customer, total)

            # 2. Insert detail & Kurangi stok
            for item in self.cart:
                # item: (id_produk, nama, harga, qty, subtotal)
                self.model.insert_detail(
                    id_penjualan,
                    item[0], # id_produk
                    item[3], # qty
                    item[2], # harga
                    item[4]  # subtotal
                )
                # Update stok (kurangi)
                self.produk_model.kurangi_stok(item[0], item[3])

            QMessageBox.information(self, "Sukses", "Transaksi Penjualan Berhasil Disimpan")
            self.cart.clear()
            self.refresh_table()
            self.ui.lineEdit.clear()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan transaksi: {e}")
            print(e)