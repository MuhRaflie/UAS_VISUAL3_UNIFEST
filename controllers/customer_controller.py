from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controllers.pembelian_controller import PembelianController
from controllers.penjualan_controller import PenjualanController
import db
from form.form_customer import Ui_Form
from db import get_connection

MODE_INSERT = "insert"
MODE_EDIT = "edit"

class CustomerController(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db = db
        
        self.mode = MODE_INSERT
        self.selected_id = None

        self.set_mode(MODE_INSERT)
        self.load_customer()
        self.ui.btn_penjualan.clicked.connect(self.open_penjualan)
        self.ui.btn_pembelian.clicked.connect(self.open_pembelian)
        self.ui.btn_Simpan_2.clicked.connect(self.insert_customer)
        self.ui.btn_Edit_2.clicked.connect(self.update_customer)
        self.ui.btn_Hapus_2.clicked.connect(self.delete_customer)
        self.ui.btn_Reset_2.clicked.connect(self.reset_form)
        self.ui.tableWidget.cellClicked.connect(self.select_row)

    # ================= MODE =================
    def set_mode(self, mode):
        self.mode = mode

        if mode == MODE_INSERT:
            self.selected_id = None
            self.ui.btn_Simpan_2.setEnabled(True)
            self.ui.btn_Edit_2.setEnabled(False)
        else:
            self.ui.btn_Simpan_2.setEnabled(False)
            self.ui.btn_Edit_2.setEnabled(True)

    # ================= LOAD =================
    def load_customer(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer")
        data = cursor.fetchall()

        self.ui.tableWidget.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, value in enumerate(row):
                self.ui.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(str(value)))
        conn.close()

    # ================= SELECT =================
    def select_row(self, row, column):
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
            QMessageBox.warning(self, "Validasi", "Nama dan Telpon wajib diisi!")
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO customer (nama_customer, telp, email, alamat) VALUES (%s,%s,%s,%s)",
            (nama, telp, email, alamat)
        )
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Sukses", "Data berhasil disimpan")
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
            QMessageBox.warning(self, "Validasi", "Nama dan Telpon wajib diisi!")
            return

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE customer
               SET nama_customer=%s, telp=%s, email=%s, alamat=%s
               WHERE id_customer=%s""",
            (nama, telp, email, alamat, self.selected_id)
        )
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Sukses", "Data berhasil diperbarui")
        self.reset_form()
        self.load_customer()

    # ================= DELETE =================
    def delete_customer(self):
        if not self.selected_id:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        confirm = QMessageBox.question(
            self, "Konfirmasi", "Yakin ingin menghapus data?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM customer WHERE id_customer=%s",
                (self.selected_id,)
            )
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Sukses", "Data berhasil dihapus")
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

    def open_penjualan(self):
        print("OPEN PENJUALAN")
        # Sekarang self.db sudah ada dan tidak akan error lagi
        self.form = PenjualanController(self.db)
        self.form.show()

    def open_pembelian(self):
        print("OPEN PEMBELIAN")
        self.form = PembelianController(self.db)
        self.form.show()
