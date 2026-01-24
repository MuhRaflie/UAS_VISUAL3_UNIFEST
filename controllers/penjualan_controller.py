from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from form.form_penjualan import Ui_Form
from models.penjualan_model import PenjualanModel
from models.produk_model import ProdukModel
import datetime


class PenjualanController(QWidget):
    def __init__(self, db):
        super().__init__()

        # Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Database & Model
        self.db = db
        self.model = PenjualanModel(db)
        self.produk_model = ProdukModel(db)

        # Cart: (id_produk, nama, harga, qty, subtotal)
        self.cart = []

        # Disable input otomatis
        self.ui.input_harga_jual.setReadOnly(True)
        self.ui.input_subtotal.setReadOnly(True)

        # Resize tabel
        self.ui.table_detail_penjualan.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )

        # Set tanggal & metode bayar
        self.ui.input_tanggal.setDateTime(datetime.datetime.now())
        self.ui.combo_metode_bayar.addItems(["Cash", "Transfer", "QRIS"])

        # Load data awal
        self.load_produk()
        self.load_customer()

        # Event binding
        self.bind_event()

    # ================= EVENT =================
    def bind_event(self):
        self.ui.btn_tambah_item.clicked.connect(self.tambah_item)
        self.ui.btn_hapus_item.clicked.connect(self.hapus_item)
        self.ui.btn_reset_item.clicked.connect(self.reset_cart)
        self.ui.btn_menu_3.clicked.connect(self.simpan_penjualan)

        self.ui.combo_produk.currentIndexChanged.connect(self.set_harga)
        self.ui.input_jumlah.valueChanged.connect(self.hitung_subtotal)

    # ================= LOAD DATA =================
    def load_produk(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id_produk, nama_produk, harga_jual FROM produk")
            data = cursor.fetchall()

            self.ui.combo_produk.clear()
            for row in data:
                # Data combo: (id_produk, nama, harga_jual)
                self.ui.combo_produk.addItem(row[1], row)

            self.set_harga()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal load produk\n{e}")

    def load_customer(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id_customer, nama_customer FROM customer")

            self.ui.combo_customer.clear()
            for row in cursor.fetchall():
                self.ui.combo_customer.addItem(row[1], row[0])

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal load customer\n{e}")

    # ================= INPUT LOGIC =================
    def set_harga(self):
        produk = self.ui.combo_produk.currentData()
        if produk:
            self.ui.input_harga_jual.setText(str(produk[2]))
            self.hitung_subtotal()

    def hitung_subtotal(self):
        try:
            harga = int(self.ui.input_harga_jual.text() or 0)
            qty = self.ui.input_jumlah.value()
            self.ui.input_subtotal.setText(str(harga * qty))
        except ValueError:
            self.ui.input_subtotal.setText("0")

    # ================= CART =================
    def tambah_item(self):
        qty = self.ui.input_jumlah.value()
        if qty <= 0:
            QMessageBox.warning(self, "Validasi", "Jumlah harus lebih dari 0")
            return

        produk = self.ui.combo_produk.currentData()
        if not produk:
            return

        id_produk, nama_produk, harga = produk

        # Cek stok
        stok = self.produk_model.get_stok(id_produk)
        if qty > stok:
            QMessageBox.warning(self, "Stok", f"Stok hanya tersisa {stok}")
            return

        # Jika produk sudah ada di cart → update qty
        for i, item in enumerate(self.cart):
            if item[0] == id_produk:
                qty_baru = item[3] + qty
                self.cart[i] = (
                    id_produk,
                    nama_produk,
                    harga,
                    qty_baru,
                    qty_baru * harga
                )
                self.refresh_table()
                return

        # Tambah item baru
        self.cart.append((id_produk, nama_produk, harga, qty, qty * harga))
        self.refresh_table()

    def hapus_item(self):
        row = self.ui.table_detail_penjualan.currentRow()
        if row >= 0:
            self.cart.pop(row)
            self.refresh_table()
        else:
            QMessageBox.warning(self, "Peringatan", "Pilih item yang akan dihapus")

    def reset_cart(self):
        self.cart.clear()
        self.refresh_table()

    def refresh_table(self):
        self.ui.table_detail_penjualan.setRowCount(0)
        total = 0

        for row_index, item in enumerate(self.cart):
            self.ui.table_detail_penjualan.insertRow(row_index)
            for col_index, value in enumerate(item):
                self.ui.table_detail_penjualan.setItem(
                    row_index,
                    col_index,
                    QTableWidgetItem(str(value))
                )
            total += item[4]

        self.ui.lineEdit.setText(str(total))

    # ================= SAVE =================
    def simpan_penjualan(self):
        if not self.cart:
            QMessageBox.warning(self, "Peringatan", "Keranjang masih kosong")
            return

        try:
            id_customer = self.ui.combo_customer.currentData()
            tanggal = self.ui.input_tanggal.dateTime().toPyDateTime()
            metode = self.ui.combo_metode_bayar.currentText()
            total = sum(item[4] for item in self.cart)

            # Insert header penjualan
            id_penjualan = self.model.insert_penjualan(
                tanggal,
                id_customer,
                metode,
                total
            )

            # Insert detail & update stok
            for item in self.cart:
                id_produk, _, harga, qty, subtotal = item

                self.model.insert_detail(
                    id_penjualan,
                    id_produk,
                    qty,
                    harga,
                    subtotal
                )

                self.produk_model.kurangi_stok(id_produk, qty)

            QMessageBox.information(self, "Sukses", "Transaksi berhasil disimpan")

            # Reset form
            self.cart.clear()
            self.refresh_table()
            self.ui.input_jumlah.setValue(0)
            self.ui.input_subtotal.clear()
            self.ui.lineEdit.clear()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal simpan penjualan\n{e}")
