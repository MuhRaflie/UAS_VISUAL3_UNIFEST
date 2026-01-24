from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from form.form_supplier import Ui_Form_Supplier
from db import get_connection

MODE_INSERT = "insert"
MODE_EDIT = "edit"


class SupplierController(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_Form_Supplier()
        self.ui.setupUi(self)

        # State
        self.mode = MODE_INSERT
        self.selected_id = None

        # Init
        self.set_mode(MODE_INSERT)
        self.load_supplier()
        self.bind_event()

    # ================= EVENT =================
    def bind_event(self):
        self.ui.btn_Simpan.clicked.connect(self.insert_supplier)
        self.ui.btn_Edit.clicked.connect(self.update_supplier)
        self.ui.btn_Hapus.clicked.connect(self.delete_supplier)
        self.ui.btn_Reset.clicked.connect(self.reset_form)
        self.ui.tableWidget.cellClicked.connect(self.select_row)

    # ================= MODE =================
    def set_mode(self, mode):
        self.mode = mode
        is_insert = mode == MODE_INSERT

        self.ui.btn_Simpan.setEnabled(is_insert)
        self.ui.btn_Edit.setEnabled(not is_insert)

        if is_insert:
            self.selected_id = None

    # ================= LOAD =================
    def load_supplier(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM supplier")
            data = cursor.fetchall()
            conn.close()

            self.ui.tableWidget.setRowCount(len(data))
            for r, row in enumerate(data):
                for c, val in enumerate(row):
                    self.ui.tableWidget.setItem(
                        r, c, QtWidgets.QTableWidgetItem(str(val))
                    )
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================= SELECT =================
    def select_row(self, row, column):
        self.selected_id = self.ui.tableWidget.item(row, 0).text()

        self.ui.input_nama_supplier.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.input_telepon.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.input_email.setText(self.ui.tableWidget.item(row, 3).text())
        self.ui.input_alamat.setPlainText(self.ui.tableWidget.item(row, 4).text())

        self.set_mode(MODE_EDIT)

    # ================= INSERT =================
    def insert_supplier(self):
        if self.mode != MODE_INSERT:
            return

        data = self.get_form_data()
        if not data:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO supplier (nama_supplier, alamat, telp, email)
                VALUES (%s, %s, %s, %s)
            """, data)
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Sukses", "Supplier berhasil ditambahkan")
            self.reset_form()
            self.load_supplier()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================= UPDATE =================
    def update_supplier(self):
        if self.mode != MODE_EDIT or not self.selected_id:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        data = self.get_form_data()
        if not data:
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE supplier
                SET nama_supplier=%s,
                    alamat=%s,
                    telp=%s,
                    email=%s
                WHERE id_supplier=%s
            """, (*data, self.selected_id))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Sukses", "Supplier berhasil diperbarui")
            self.reset_form()
            self.load_supplier()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    # ================= DELETE =================
    def delete_supplier(self):
        if not self.selected_id:
            QMessageBox.warning(self, "Peringatan", "Pilih data terlebih dahulu")
            return

        confirm = QMessageBox.question(
            self,
            "Konfirmasi",
            "Yakin ingin menghapus supplier ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM supplier WHERE id_supplier=%s",
                    (self.selected_id,)
                )
                conn.commit()
                conn.close()

                QMessageBox.information(self, "Sukses", "Supplier berhasil dihapus")
                self.reset_form()
                self.load_supplier()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    # ================= HELPER =================
    def get_form_data(self):
        nama = self.ui.input_nama_supplier.text().strip()
        alamat = self.ui.input_alamat.toPlainText().strip()
        telp = self.ui.input_telepon.text().strip()
        email = self.ui.input_email.text().strip()

        if not nama or not telp:
            QMessageBox.warning(self, "Validasi", "Nama & Telepon wajib diisi!")
            return None

        return nama, alamat, telp, email

    # ================= RESET =================
    def reset_form(self):
        self.ui.input_nama_supplier.clear()
        self.ui.input_alamat.clear()
        self.ui.input_telepon.clear()
        self.ui.input_email.clear()
        self.ui.tableWidget.clearSelection()
        self.set_mode(MODE_INSERT)
