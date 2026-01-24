from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QVBoxLayout
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
        self.cart = []
        self.ui.input_harga_jual.setReadOnly(True)
        self.ui.input_subtotal.setReadOnly(True)

        # resize tabel
        self.ui.table_detail_penjualan.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )

        # tombol
        self.ui.btn_tambah_item.clicked.connect(self.tambah_item)
        self.ui.btn_hapus_item.clicked.connect(self.hapus_item)
        self.ui.btn_reset_item.clicked.connect(self.reset_cart)
        self.ui.btn_menu_3.clicked.connect(self.simpan_penjualan)

        # event input
        self.ui.combo_produk.currentIndexChanged.connect(self.set_harga)
        self.ui.input_jumlah.valueChanged.connect(self.hitung_subtotal)

        # init data
        self.ui.input_tanggal.setDateTime(datetime.datetime.now())
        self.ui.combo_metode_bayar.addItems(["Cash", "Transfer", "QRIS"])
        self.load_produk()
        self.load_customer()


    # --- SEMUA METHOD DI BAWAH INI HARUS MASUK DALAM CLASS (TAB KE DALAM) ---

    def load_produk(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id_produk, nama_produk, harga_jual FROM produk")
            self.produk_list = cursor.fetchall()
            self.ui.combo_produk.clear()
            for p in self.produk_list:
                self.ui.combo_produk.addItem(f"{p[1]}", p)
            self.set_harga()
        except Exception as e:
            print(f"Error load produk: {e}")

    def set_harga(self):
        produk_data = self.ui.combo_produk.currentData()
        if produk_data:
            harga = produk_data[2]
            self.ui.input_harga_jual.setText(str(harga))
            self.hitung_subtotal()

    def hitung_subtotal(self):
        try:
            harga = int(self.ui.input_harga_jual.text() or 0)
            qty = self.ui.input_jumlah.value()
            self.ui.input_subtotal.setText(str(harga * qty))
        except:
            pass

    def tambah_item(self):
        print("Tombol Tambah Diklik") # Debugging
        try:
            qty = self.ui.input_jumlah.value()
            if qty <= 0:
                QMessageBox.warning(self, "Warning", "Jumlah harus lebih dari 0")
                return

            produk_data = self.ui.combo_produk.currentData()
            if not produk_data: return

            id_produk, nama, harga = produk_data[0], produk_data[1], produk_data[2]
            
            # Cek Stok
            stok = self.produk_model.get_stok(id_produk)
            if qty > stok:
                QMessageBox.warning(self, "Stok", f"Stok hanya sisa {stok}")
                return

            # Cek jika item sudah ada di tabel
            for i, item in enumerate(self.cart):
                if item[0] == id_produk:
                    self.cart[i] = (id_produk, nama, harga, item[3] + qty, (item[3] + qty) * harga)
                    self.refresh_table()
                    return

            self.cart.append((id_produk, nama, harga, qty, qty * harga))
            self.refresh_table()
        except Exception as e:
            print(f"Error di tambah_item: {e}")

    def hapus_item(self):
        print("Tombol Hapus Diklik") # Debugging
        row = self.ui.table_detail_penjualan.currentRow()
        if row >= 0:
            self.cart.pop(row)
            self.refresh_table()
        else:
            QMessageBox.warning(self, "Pilih Data", "Silakan klik baris pada tabel yang ingin dihapus")

    def reset_cart(self):
        self.cart.clear()
        self.refresh_table()

    def refresh_table(self):
        self.ui.table_detail_penjualan.setRowCount(0)
        total_belanja = 0
        for row_index, row_data in enumerate(self.cart):
            self.ui.table_detail_penjualan.insertRow(row_index)
            for col_index, data in enumerate(row_data):
                self.ui.table_detail_penjualan.setItem(row_index, col_index, QTableWidgetItem(str(data)))
            total_belanja += row_data[4]
        self.ui.lineEdit.setText(str(total_belanja))

    def load_customer(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id_customer, nama_customer FROM customer")
            for row in cursor.fetchall():
                self.ui.combo_customer.addItem(row[1], row[0])
        except Exception as e:
            print(e)

    def simpan_penjualan(self):
        if not self.cart:
            QMessageBox.warning(self, "Error", "Keranjang masih kosong")
            return

        try:
            id_customer = self.ui.combo_customer.currentData()
            tanggal = self.ui.input_tanggal.dateTime().toPyDateTime()
            metode = self.ui.combo_metode_bayar.currentText()
            total = sum(item[4] for item in self.cart)

            # 1️⃣ simpan header penjualan
            id_penjualan = self.model.insert_penjualan(
                tanggal,
                id_customer,
                metode,
                total
            )

            # 2️⃣ simpan detail + kurangi stok
            for item in self.cart:
                id_produk, nama, harga, qty, subtotal = item

                self.model.insert_detail(
                    id_penjualan,
                    id_produk,
                    qty,
                    harga,
                    subtotal
                )

                self.produk_model.kurangi_stok(id_produk, qty)

            QMessageBox.information(self, "Sukses", "Transaksi berhasil disimpan")

            # reset form
            self.cart.clear()
            self.refresh_table()
            self.ui.input_jumlah.setValue(0)
            self.ui.input_subtotal.clear()
            self.ui.lineEdit.clear()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            print(e)
