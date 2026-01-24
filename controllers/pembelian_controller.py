from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from form.form_pembelian import Ui_Form
from models.produk_model import ProdukModel
import datetime


class PembelianController(QWidget):
    def __init__(self, db):
        super().__init__()

        # Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Database & Model
        self.db = db
        self.produk_model = ProdukModel(db)

        # Cart: (id_produk, nama, harga_beli, qty, subtotal)
        self.cart = []

        # Set default tanggal hari ini
        self.ui.input_tanggal.setDateTime(datetime.datetime.now())

        # Disable input otomatis
        self.ui.input_harga_beli.setReadOnly(True)
        self.ui.input_subtotal.setReadOnly(True)

        # Load data awal
        self.load_supplier()
        self.load_produk()

        # Event binding
        self.bind_event()

    # ================= EVENT =================
    def bind_event(self):
        self.ui.combo_produk.currentIndexChanged.connect(self.set_harga_otomatis)
        self.ui.input_jumlah.valueChanged.connect(self.hitung_subtotal)

        self.ui.btn_tambah_item.clicked.connect(self.tambah_item)
        self.ui.btn_hapus_item.clicked.connect(self.hapus_item)
        self.ui.btn_reset_item.clicked.connect(self.reset_cart)
        self.ui.btn_menu_3.clicked.connect(self.simpan_pembelian)

    # ================= LOAD DATA =================
    def load_supplier(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id_supplier, nama_supplier FROM supplier")
            data = cursor.fetchall()

            self.ui.combo_supplier.clear()
            for row in data:
                self.ui.combo_supplier.addItem(row[1], row[0])

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal load supplier\n{e}")

    def load_produk(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id_produk, nama_produk, harga_beli FROM produk")
            data = cursor.fetchall()

            self.ui.combo_produk.clear()
            for row in data:
                # Data combo: (id_produk, nama, harga_beli)
                self.ui.combo_produk.addItem(row[1], row)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal load produk\n{e}")

    # ================= INPUT LOGIC =================
    def set_harga_otomatis(self):
        produk = self.ui.combo_produk.currentData()
        if produk:
            self.ui.input_harga_beli.setText(str(produk[2]))
            self.hitung_subtotal()

    def hitung_subtotal(self):
        try:
            harga = int(self.ui.input_harga_beli.text() or 0)
            qty = self.ui.input_jumlah.value()
            self.ui.input_subtotal.setText(str(harga * qty))
        except ValueError:
            self.ui.input_subtotal.setText("0")

    # ================= CART =================
    def tambah_item(self):
        produk = self.ui.combo_produk.currentData()
        if not produk:
            return

        id_produk, nama_produk, _ = produk

        try:
            harga_beli = int(self.ui.input_harga_beli.text())
            qty = self.ui.input_jumlah.value()
        except ValueError:
            QMessageBox.warning(self, "Validasi", "Harga tidak valid")
            return

        if qty <= 0:
            QMessageBox.warning(self, "Validasi", "Jumlah harus lebih dari 0")
            return

        subtotal = harga_beli * qty
        self.cart.append((id_produk, nama_produk, harga_beli, qty, subtotal))

        self.refresh_table()
        self.ui.input_jumlah.setValue(0)

    def hapus_item(self):
        row = self.ui.table_detail_pembelian.currentRow()
        if row >= 0:
            self.cart.pop(row)
            self.refresh_table()

    def reset_cart(self):
        self.cart.clear()
        self.refresh_table()
        self.ui.lineEdit.clear()

    def refresh_table(self):
        self.ui.table_detail_pembelian.setRowCount(len(self.cart))
        total = 0

        for row, item in enumerate(self.cart):
            self.ui.table_detail_pembelian.setItem(row, 0, QTableWidgetItem(str(item[0])))
            self.ui.table_detail_pembelian.setItem(row, 1, QTableWidgetItem(item[1]))
            self.ui.table_detail_pembelian.setItem(row, 2, QTableWidgetItem(str(item[2])))
            self.ui.table_detail_pembelian.setItem(row, 3, QTableWidgetItem(str(item[3])))
            self.ui.table_detail_pembelian.setItem(row, 4, QTableWidgetItem(str(item[4])))
            total += item[4]

        self.ui.lineEdit.setText(f"Rp {total:,.0f}")

    # ================= SAVE =================
    def simpan_pembelian(self):
        if not self.cart:
            QMessageBox.warning(self, "Peringatan", "Data pembelian kosong")
            return

        try:
            id_supplier = self.ui.combo_supplier.currentData()
            tanggal = self.ui.input_tanggal.dateTime().toPyDateTime()
            id_user = 1  # sementara
            total = sum(item[4] for item in self.cart)

            cursor = self.db.cursor()

            # Insert header pembelian
            cursor.execute(
                "INSERT INTO pembelian (tanggal, id_supplier, id_user, total) VALUES (%s, %s, %s, %s)",
                (tanggal, id_supplier, id_user, total)
            )
            id_pembelian = cursor.lastrowid

            # Insert detail & update stok
            for item in self.cart:
                cursor.execute(
                    """INSERT INTO detail_pembelian
                       (id_pembelian, id_produk, jumlah, harga_beli, subtotal)
                       VALUES (%s, %s, %s, %s, %s)""",
                    (id_pembelian, item[0], item[3], item[2], item[4])
                )

                self.produk_model.tambah_stok(item[0], item[3])
                cursor.execute(
                    "UPDATE produk SET harga_beli=%s WHERE id_produk=%s",
                    (item[2], item[0])
                )

            self.db.commit()
            QMessageBox.information(self, "Sukses", "Pembelian berhasil disimpan")
            self.reset_cart()

        except Exception as e:
            self.db.rollback()
            QMessageBox.critical(self, "Error", f"Gagal simpan pembelian\n{e}")
