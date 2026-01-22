# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form_produk(object):
    def setupUi(self, Form_produk):
        Form_produk.setObjectName("Form_produk")
        Form_produk.resize(848, 745)
        self.frame_2 = QtWidgets.QFrame(Form_produk)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 851, 751))
        self.frame_2.setStyleSheet("background-color: #d8d8d8;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        # --- Header Section ---
        self.frame_header = QtWidgets.QFrame(self.frame_2)
        self.frame_header.setEnabled(True)
        self.frame_header.setGeometry(QtCore.QRect(0, 0, 851, 100))
        self.frame_header.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_header.setStyleSheet("background-color: #ffffff;\nborder-radius: 15px;\nborder: 1px solid #ddd;")
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setObjectName("frame_header")
        
        self.lbl_logo = QtWidgets.QLabel(self.frame_header)
        self.lbl_logo.setGeometry(QtCore.QRect(10, 10, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Jersey Sharp")
        font.setPointSize(24)
        self.lbl_logo.setFont(font)
        self.lbl_logo.setObjectName("lbl_logo")

        # Buttons in Header
        self.btn_dashboard = QtWidgets.QPushButton(self.frame_header)
        self.btn_dashboard.setGeometry(QtCore.QRect(230, 10, 131, 31))
        self.btn_dashboard.setStyleSheet("background-color: #ff5757; color: white;")
        self.btn_dashboard.setObjectName("btn_dashboard")

        self.btn_produk = QtWidgets.QPushButton(self.frame_header)
        self.btn_produk.setGeometry(QtCore.QRect(370, 10, 131, 31))
        self.btn_produk.setStyleSheet("background-color: #ff5757; color: white;")
        self.btn_produk.setObjectName("btn_produk")

        self.btn_supplier = QtWidgets.QPushButton(self.frame_header)
        self.btn_supplier.setGeometry(QtCore.QRect(510, 10, 131, 31))
        self.btn_supplier.setStyleSheet("background-color: #ff5757; color: white;")
        self.btn_supplier.setObjectName("btn_supplier")

        self.btn_customer = QtWidgets.QPushButton(self.frame_header)
        self.btn_customer.setGeometry(QtCore.QRect(510, 50, 131, 31))
        self.btn_customer.setStyleSheet("background-color: #ff5757; color: white;")
        self.btn_customer.setObjectName("btn_customer")

        self.btn_penjualan = QtWidgets.QPushButton(self.frame_header)
        self.btn_penjualan.setGeometry(QtCore.QRect(230, 50, 131, 31))
        self.btn_penjualan.setStyleSheet("background-color: #ff5757; color: white;")
        self.btn_penjualan.setObjectName("btn_penjualan")

        self.btn_menu = QtWidgets.QPushButton(self.frame_header)
        self.btn_menu.setGeometry(QtCore.QRect(730, 30, 91, 31))
        self.btn_menu.setStyleSheet("background-color: #ff5757; color: white;")
        self.btn_menu.setObjectName("btn_menu")

        self.btn_pembelian = QtWidgets.QPushButton(self.frame_header)
        self.btn_pembelian.setGeometry(QtCore.QRect(370, 50, 131, 31))
        self.btn_pembelian.setStyleSheet("background-color: #ff5757; color: white;")
        self.btn_pembelian.setObjectName("btn_pembelian")

        # --- Content Section ---
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 110, 851, 641))
        self.frame_3.setStyleSheet("background-color: #ffffff;")
        self.frame_3.setObjectName("frame_3")

        # Form Input Container
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(10, 20, 821, 291))
        self.frame_6.setStyleSheet("background-color: #ff5757; color: white; padding: 10px; border-radius: 10px;")
        self.frame_6.setObjectName("frame_6")

        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame_6)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 791, 201))
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        
        # Input: Nama Produk
        self.label_nama_produk_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_nama_produk_2.setObjectName("label_nama_produk_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nama_produk_2)
        self.input_nama_produk = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.input_nama_produk.setStyleSheet("background-color: #ff6f6f; color: white; padding: 6px; border-radius: 8px;")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_nama_produk)

        # Input: Harga Beli
        self.Lbl_harga_beli_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Lbl_harga_beli_2)
        self.input_harga_beli = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.input_harga_beli.setStyleSheet("background-color: #ff6f6f; color: white; padding: 6px; border-radius: 8px;")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_harga_beli)

        # Input: Harga Jual
        self.Lbl_Harga_Jual_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Lbl_Harga_Jual_2)
        self.input_harga_jual = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.input_harga_jual.setStyleSheet("background-color: #ff6f6f; color: white; padding: 6px; border-radius: 8px;")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_harga_jual)

        # Input: Stok
        self.Lbl_Stok_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Lbl_Stok_2)
        self.input_stok = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.input_stok.setStyleSheet("background-color: #ff6f6f; color: white; padding: 6px; border-radius: 8px;")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_stok)

        # Input: Supplier
        self.supplier_Label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.supplier_Label_2)
        self.combo_supplier = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.combo_supplier.setStyleSheet("background-color: #ff6f6f; color: white; padding: 6px; border-radius: 8px;")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.combo_supplier)

        # Action Buttons
        self.btn_Simpan = QtWidgets.QPushButton(self.frame_6)
        self.btn_Simpan.setGeometry(QtCore.QRect(10, 250, 71, 31))
        self.btn_Simpan.setStyleSheet("background-color: white; color: black;")
        
        self.btn_Edit = QtWidgets.QPushButton(self.frame_6)
        self.btn_Edit.setGeometry(QtCore.QRect(90, 250, 71, 31))
        self.btn_Edit.setStyleSheet("background-color: white; color: black;")
        
        self.btn_Hapus = QtWidgets.QPushButton(self.frame_6)
        self.btn_Hapus.setGeometry(QtCore.QRect(170, 250, 71, 31))
        self.btn_Hapus.setStyleSheet("background-color: white; color: black;")
        
        self.btn_Reset = QtWidgets.QPushButton(self.frame_6)
        self.btn_Reset.setGeometry(QtCore.QRect(250, 250, 71, 31))
        self.btn_Reset.setStyleSheet("background-color: white; color: black;")

        # Table Section
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 320, 821, 301))
        self.tableWidget.setColumnCount(6)
        for i in range(6):
            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        self.retranslateUi(Form_produk)
        QtCore.QMetaObject.connectSlotsByName(Form_produk)

    def retranslateUi(self, Form_produk):
        _translate = QtCore.QCoreApplication.translate
        Form_produk.setWindowTitle(_translate("Form_produk", "Form Produk"))
        self.lbl_logo.setText(_translate("Form_produk", "UNIFEST"))
        self.btn_dashboard.setText(_translate("Form_produk", "DASHBOARD"))
        self.btn_produk.setText(_translate("Form_produk", "PRODUK"))
        self.btn_supplier.setText(_translate("Form_produk", "SUPPLIER"))
        self.btn_customer.setText(_translate("Form_produk", "CUSTOMER"))
        self.btn_penjualan.setText(_translate("Form_produk", "PENJUALAN"))
        self.btn_menu.setText(_translate("Form_produk", "Logout"))
        self.btn_pembelian.setText(_translate("Form_produk", "PEMBELIAN"))
        self.label_11.setText(_translate("Form_produk", "Kelola Produk"))
        self.label_nama_produk_2.setText(_translate("Form_produk", "Nama Produk"))
        self.Lbl_harga_beli_2.setText(_translate("Form_produk", "Harga Beli"))
        self.Lbl_Harga_Jual_2.setText(_translate("Form_produk", "Harga Jual"))
        self.Lbl_Stok_2.setText(_translate("Form_produk", "Stok"))
        self.supplier_Label_2.setText(_translate("Form_produk", "Supplier"))
        self.btn_Simpan.setText(_translate("Form_produk", "Simpan"))
        self.btn_Edit.setText(_translate("Form_produk", "Edit"))
        self.btn_Hapus.setText(_translate("Form_produk", "Hapus"))
        self.btn_Reset.setText(_translate("Form_produk", "Reset"))
        
        headers = ["ID", "Nama Produk", "Harga Beli", "Harga Jual", "Stok", "Supplier"]
        for i, text in enumerate(headers):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("Form_produk", text))

# Main block untuk menjalankan aplikasi
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form_produk = QtWidgets.QWidget()
    ui = Ui_Form_produk()
    ui.setupUi(Form_produk)
    Form_produk.show()
    sys.exit(app.exec_())