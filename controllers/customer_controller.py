from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from form.form_customer import Ui_Form
from controllers.penjualan_controller import PenjualanController
from controllers.pembelian_controller import PembelianController
from db import get_connection

MODE_INSERT = "insert"
MODE_EDIT = "edit"


class CustomerController(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # State
        self.mode = MODE_INSERT
        self.selected_id = None

        # Init
        self.set_mode(MODE_INSERT)
        self.load_customer()

        # Event Binding
        self.ui.btn_Simpan_2.clicked.connect(self.insert_customer)
        self.ui.btn_Edit_2.clicked.connect(self.update_customer)
        self.ui.btn_Hapus_2.clicked.connect(self.delete_customer)
        self.ui.btn_Reset_2.clicked.connect(self.reset_form)

        self.ui.btn_penjualan.clicked.connect(self.open_penjualan)
        self.ui.btn_pembelian.clicked.connect(self.open_pembelian)

        self.ui.tableWidget.cellClicked.connect(self.select_row)

    # ================= MODE =================
    def set_mode(self, mode):
        self.mode = mode
        is_insert = mode == MODE_INSERT

        self.selected_id = None if is_insert else self.selected_id
        self.ui.btn_Simpan_2.setEnabled(is_insert)
        self.ui.btn_Edit_2.setEnabled(not is_insert)

    # ================= LOAD =================
    def load_customer(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer")
        data = cursor.fetchall()
        conn.close()

        self.ui.tableWidget.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, value in enumerate(row_data):
                self.ui.tableWidget.setItem(
                    row_index,
                    col_index,
                    QtWidgets.QTableWidgetItem(str(value))
                )

    # ================= SELECT =================
    def select_row(self, row, _):
        self.selected_id = self.ui.tableWidget.item(row, 0).text()

        self.ui.input_nama_customer.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.input_telepon_customer.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.input_email_customer.setText(self.ui.tableWidget.item(row, 3).text())
        self.ui.input_alamat.setText(self.ui.tableWidget.item(row, 4).text())

        self.set_mode(MODE_EDIT)

    # ================= INSERT =================
    def insert_customer(self):
        if self.mode != MODE_INSERT:
            return

        nama = self.ui.input_nama_customer.text().strip()
        telp = self.ui.input_telepon_customer.text().strip()
        email = self.ui.input_email_customer.text().strip()
        alamat = self.ui.input_alamat.toPlainText().strip()

        if not nama or not telp:
            QMessageBox.warning(self, "Validasi", "Nama dan Telepon wajib diisi")
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO customer (nama_customer, telp, email, alamat)
            VALUES (%s, %s, %s, %s)
            """,
            (nama, telp, email, alamat)
        )
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Sukses", "Data customer berhasil disimpan")
        self.reset_form()
        self.load_customer()

    # ================= UPDATE =================
    def update_customer(self):
        if self.mode != MODE_EDIT or not self.selected_id:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        nama = self.ui.input_nama_customer.text().strip()
        telp = self.ui.input_telepon_customer.text().strip()
        email = self.ui.input_email_customer.text().strip()
        alamat = self.ui.input_alamat.toPlainText().strip()

        if not nama or not telp:
            QMessageBox.warning(self, "Validasi", "Nama dan Telepon wajib diisi")
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE customer
            SET nama_customer=%s, telp=%s, email=%s, alamat=%s
            WHERE id_customer=%s
            """,
            (nama, telp, email, alamat, self.selected_id)
        )
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Sukses", "Data customer berhasil diperbarui")
        self.reset_form()
        self.load_customer()

    # ================= DELETE =================
    def delete_customer(self):
        if not self.selected_id:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        confirm = QMessageBox.question(
            self,
            "Konfirmasi",
            "Yakin ingin menghapus data customer?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.No:
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM customer WHERE id_customer=%s",
            (self.selected_id,)
        )
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Sukses", "Data customer berhasil dihapus")
        self.reset_form()
        self.load_customer()

    # ================= RESET =================
    def reset_form(self):
        self.ui.input_nama_customer.clear()
        self.ui.input_telepon_customer.clear()
        self.ui.input_email_customer.clear()
        self.ui.input_alamat.clear()
        self.ui.tableWidget.clearSelection()
        self.set_mode(MODE_INSERT)

    # ================= NAVIGATION =================
    def open_penjualan(self):
        self.form = PenjualanController(get_connection())
        self.form.show()

    def open_pembelian(self):
        self.form = PembelianController(get_connection())
        self.form.show()
