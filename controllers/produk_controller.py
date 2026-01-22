from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from form.form_produk import Ui_Form_produk
from db import get_connection

MODE_INSERT = "insert"
MODE_EDIT = "edit"


class ProdukController(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_produk()
        self.ui.setupUi(self)

        self.mode = MODE_INSERT
        self.selected_id = None

        self.set_mode(MODE_INSERT)
        self.load_supplier()
        self.load_produk()

        # Button events
        self.ui.btn_Simpan.clicked.connect(self.insert_produk)
        self.ui.btn_Edit.clicked.connect(self.update_produk)
        self.ui.btn_Hapus.clicked.connect(self.delete_produk)
        self.ui.btn_Reset.clicked.connect(self.reset_form)
        self.ui.tableWidget.cellClicked.connect(self.select_row)

    # ================= MODE =================
    def set_mode(self, mode):
        self.mode = mode

        if mode == MODE_INSERT:
            self.selected_id = None
            self.ui.btn_Simpan.setEnabled(True)
            self.ui.btn_Edit.setEnabled(False)
        else:
            self.ui.btn_Simpan.setEnabled(False)
            self.ui.btn_Edit.setEnabled(True)

    # ================= LOAD =================
    def load_produk(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.id_produk,
                   p.nama_produk,
                   p.harga_beli,
                   p.harga_jual,
                   p.stok,
                   s.nama_supplier
            FROM produk p
            LEFT JOIN supplier s ON p.id_supplier = s.id_supplier
        """)
        data = cursor.fetchall()
        conn.close()

        self.ui.tableWidget.setRowCount(len(data))

        for r, row in enumerate(data):
            for c, val in enumerate(row):
                self.ui.tableWidget.setItem(
                    r, c, QtWidgets.QTableWidgetItem(str(val))
                )

    def load_supplier(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_supplier, nama_supplier FROM supplier")
        suppliers = cursor.fetchall()
        conn.close()

        self.ui.combo_supplier.clear()
        for sid, nama in suppliers:
            self.ui.combo_supplier.addItem(nama, sid)

    # ================= SELECT =================
    def select_row(self, row, column):
        self.selected_id = self.ui.tableWidget.item(row, 0).text()

        self.ui.input_nama_produk.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.input_harga_beli.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.input_harga_jual.setText(self.ui.tableWidget.item(row, 3).text())
        self.ui.input_stok.setText(self.ui.tableWidget.item(row, 4).text())

        supplier_name = self.ui.tableWidget.item(row, 5).text()
        index = self.ui.combo_supplier.findText(supplier_name)
        if index >= 0:
            self.ui.combo_supplier.setCurrentIndex(index)

        self.set_mode(MODE_EDIT)

    # ================= INSERT =================
    def insert_produk(self):
        if self.mode != MODE_INSERT:
            return

        nama = self.ui.input_nama_produk.text().strip()
        beli = self.ui.input_harga_beli.text().strip()
        jual = self.ui.input_harga_jual.text().strip()
        stok = self.ui.input_stok.text().strip()
        supplier_id = self.ui.combo_supplier.currentData()

        if not nama or not beli or not jual or not stok:
            QMessageBox.warning(self, "Validasi", "Semua field wajib diisi!")
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO produk
            (nama_produk, harga_beli, harga_jual, stok, id_supplier)
            VALUES (%s,%s,%s,%s,%s)
        """, (nama, beli, jual, stok, supplier_id))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Sukses", "Produk berhasil ditambahkan")
        self.reset_form()
        self.load_produk()

    # ================= UPDATE =================
    def update_produk(self):
        if self.mode != MODE_EDIT or not self.selected_id:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        nama = self.ui.input_nama_produk.text().strip()
        beli = self.ui.input_harga_beli.text().strip()
        jual = self.ui.input_harga_jual.text().strip()
        stok = self.ui.input_stok.text().strip()
        supplier_id = self.ui.combo_supplier.currentData()

        if not nama or not beli or not jual or not stok:
            QMessageBox.warning(self, "Validasi", "Semua field wajib diisi!")
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE produk
            SET nama_produk=%s,
                harga_beli=%s,
                harga_jual=%s,
                stok=%s,
                id_supplier=%s
            WHERE id_produk=%s
        """, (nama, beli, jual, stok, supplier_id, self.selected_id))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Sukses", "Produk berhasil diperbarui")
        self.reset_form()
        self.load_produk()

    # ================= DELETE =================
    def delete_produk(self):
        if not self.selected_id:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        confirm = QMessageBox.question(
            self, "Konfirmasi",
            "Yakin ingin menghapus produk ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM produk WHERE id_produk=%s",
                (self.selected_id,)
            )
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Sukses", "Produk berhasil dihapus")
            self.reset_form()
            self.load_produk()

    # ================= RESET =================
    def reset_form(self):
        self.ui.input_nama_produk.clear()
        self.ui.input_harga_beli.clear()
        self.ui.input_harga_jual.clear()
        self.ui.input_stok.clear()
        self.ui.combo_supplier.setCurrentIndex(0)
        self.ui.tableWidget.clearSelection()
        self.set_mode(MODE_INSERT)
