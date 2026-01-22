from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from form.form_supplier import Ui_Form_Supplier
from db import get_connection

MODE_INSERT = "insert"
MODE_EDIT = "edit"

class SupplierController(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_Supplier()
        self.ui.setupUi(self)

        self.mode = MODE_INSERT
        self.selected_id = None

        self.set_mode(MODE_INSERT)
        self.load_supplier()

        # Event Connect
        self.ui.btn_Simpan.clicked.connect(self.insert_supplier)
        self.ui.btn_Edit.clicked.connect(self.update_supplier)
        self.ui.btn_Hapus.clicked.connect(self.delete_supplier)
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
            print(f"Error loading supplier: {e}")

    # ================= SELECT =================
    def select_row(self, row, column):
        self.selected_id = self.ui.tableWidget.item(row, 0).text()

        self.ui.input_nama_supplier.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.input_telepon.setText(self.ui.tableWidget.item(row, 2).text()) # Perhatikan urutan kolom DB Anda
        self.ui.input_email.setText(self.ui.tableWidget.item(row, 3).text())
        # Untuk QTextEdit gunakan setText atau setPlainText
        self.ui.input_alamat.setText(self.ui.tableWidget.item(row, 4).text()) 

        self.set_mode(MODE_EDIT)

    # ================= INSERT =================
    def insert_supplier(self):
        if self.mode != MODE_INSERT:
            return

        nama = self.ui.input_nama_supplier.text().strip()
        # PERBAIKAN DI SINI: Gunakan toPlainText() untuk QTextEdit
        alamat = self.ui.input_alamat.toPlainText().strip() 
        telp = self.ui.input_telepon.text().strip()
        email = self.ui.input_email.text().strip()

        if not nama or not telp:
            QMessageBox.warning(self, "Validasi", "Nama & Telepon wajib diisi!")
            return

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO supplier (nama_supplier, alamat, telp, email)
                VALUES (%s,%s,%s,%s)
            """, (nama, alamat, telp, email))
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

        nama = self.ui.input_nama_supplier.text().strip()
        # PERBAIKAN DI SINI: Gunakan toPlainText() untuk QTextEdit
        alamat = self.ui.input_alamat.toPlainText().strip()
        telp = self.ui.input_telepon.text().strip()
        email = self.ui.input_email.text().strip()

        if not nama or not telp:
            QMessageBox.warning(self, "Validasi", "Nama & Telepon wajib diisi!")
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
            """, (nama, alamat, telp, email, self.selected_id))
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
            self, "Konfirmasi",
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

    # ================= RESET =================
    def reset_form(self):
        self.ui.input_nama_supplier.clear()
        self.ui.input_alamat.clear()
        self.ui.input_telepon.clear()
        self.ui.input_email.clear()
        self.ui.tableWidget.clearSelection()
        self.set_mode(MODE_INSERT)