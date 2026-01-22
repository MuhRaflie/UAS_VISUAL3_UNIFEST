# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(852, 739)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 851, 751))
        self.frame_2.setStyleSheet("background-color: #d8d8d8;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        # --- HEADER ---
        self.frame_header = QtWidgets.QFrame(self.frame_2)
        self.frame_header.setGeometry(QtCore.QRect(0, 0, 851, 100))
        self.frame_header.setStyleSheet("background-color: #ffffff; border-radius: 15px; border: 1px solid #ddd;")
        self.frame_header.setObjectName("frame_header")
        
        self.lbl_logo = QtWidgets.QLabel(self.frame_header)
        self.lbl_logo.setGeometry(QtCore.QRect(10, 10, 171, 81))
        font = QtGui.QFont(); font.setFamily("Jersey Sharp"); font.setPointSize(24)
        self.lbl_logo.setFont(font)
        self.lbl_logo.setObjectName("lbl_logo")

        # Tombol Navigasi
        self.btn_dashboard = QtWidgets.QPushButton(self.frame_header)
        self.btn_dashboard.setGeometry(QtCore.QRect(230, 10, 131, 31))
        self.btn_dashboard.setStyleSheet("background-color: #ff5757; color: white;")
        
        self.btn_produk = QtWidgets.QPushButton(self.frame_header)
        self.btn_produk.setGeometry(QtCore.QRect(370, 10, 131, 31))
        self.btn_produk.setStyleSheet("background-color: #ff5757; color: white;")
        
        self.btn_supplier = QtWidgets.QPushButton(self.frame_header)
        self.btn_supplier.setGeometry(QtCore.QRect(510, 10, 131, 31))
        self.btn_supplier.setStyleSheet("background-color: #ff5757; color: white;")
        
        self.btn_customer = QtWidgets.QPushButton(self.frame_header)
        self.btn_customer.setGeometry(QtCore.QRect(510, 50, 131, 31))
        self.btn_customer.setStyleSheet("background-color: #ff5757; color: white;")
        
        self.btn_penjualan = QtWidgets.QPushButton(self.frame_header)
        self.btn_penjualan.setGeometry(QtCore.QRect(230, 50, 131, 31))
        self.btn_penjualan.setStyleSheet("background-color: #ff5757; color: white;")
        
        self.btn_menu = QtWidgets.QPushButton(self.frame_header)
        self.btn_menu.setGeometry(QtCore.QRect(730, 30, 91, 31))
        self.btn_menu.setStyleSheet("background-color: #ff5757; color: white;")
        
        self.btn_pembelian = QtWidgets.QPushButton(self.frame_header)
        self.btn_pembelian.setGeometry(QtCore.QRect(370, 50, 131, 31))
        self.btn_pembelian.setStyleSheet("background-color: #ff5757; color: white;")

        # --- CONTENT ---
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 110, 851, 641))
        self.frame_3.setStyleSheet("background-color: #ffffff;")
        self.frame_3.setObjectName("frame_3")

        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(10, 20, 821, 291))
        self.frame_6.setStyleSheet("background-color: #ff5757; color: white; padding: 10px; border-radius: 10px;")
        
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 291, 41))
        font = QtGui.QFont(); font.setPointSize(16)
        self.label_11.setFont(font)

        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame_6)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 791, 191))
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)

        # Form Inputs
        self.label_nama_customer = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nama_customer)
        self.input_nama_customer = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.input_nama_customer.setStyleSheet("background-color: #ff6f6f; color: white; padding: 6px; border-radius: 8px;")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_nama_customer)

        self.Lbl_telpon = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Lbl_telpon)
        self.input_telepon_customer = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.input_telepon_customer.setStyleSheet("background-color: #ff6f6f; color: white; padding: 6px; border-radius: 8px;")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_telepon_customer)

        self.Lbl_email = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Lbl_email)
        self.input_email_customer = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.input_email_customer.setStyleSheet("background-color: #ff6f6f; color: white; padding: 6px; border-radius: 8px;")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_email_customer)

        self.Lbl_alamat = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Lbl_alamat)
        self.input_alamat = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.input_alamat.setMaximumSize(QtCore.QSize(16777215, 50))
        self.input_alamat.setStyleSheet("background-color: #ff6f6f; color: white; padding: 6px; border-radius: 8px;")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_alamat)

        # Buttons
        self.btn_Simpan_2 = QtWidgets.QPushButton(self.frame_6)
        self.btn_Simpan_2.setGeometry(QtCore.QRect(10, 250, 71, 31))
        self.btn_Simpan_2.setStyleSheet("background-color: white; color: black;")
        
        self.btn_Edit_2 = QtWidgets.QPushButton(self.frame_6)
        self.btn_Edit_2.setGeometry(QtCore.QRect(90, 250, 71, 31))
        self.btn_Edit_2.setStyleSheet("background-color: white; color: black;")
        
        self.btn_Hapus_2 = QtWidgets.QPushButton(self.frame_6)
        self.btn_Hapus_2.setGeometry(QtCore.QRect(170, 250, 71, 31))
        self.btn_Hapus_2.setStyleSheet("background-color: white; color: black;")
        
        self.btn_Reset_2 = QtWidgets.QPushButton(self.frame_6)
        self.btn_Reset_2.setGeometry(QtCore.QRect(250, 250, 71, 31))
        self.btn_Reset_2.setStyleSheet("background-color: white; color: black;")

        # Table
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 320, 821, 301))
        self.tableWidget.setColumnCount(5)
        for i in range(5):
            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kelola Customer"))
        self.lbl_logo.setText(_translate("Form", "UNIFEST"))
        self.btn_dashboard.setText(_translate("Form", "DASHBOARD"))
        self.btn_produk.setText(_translate("Form", "PRODUK"))
        self.btn_supplier.setText(_translate("Form", "SUPPLIER"))
        self.btn_customer.setText(_translate("Form", "CUSTOMER"))
        self.btn_penjualan.setText(_translate("Form", "PENJUALAN"))
        self.btn_menu.setText(_translate("Form", "Logout"))
        self.btn_pembelian.setText(_translate("Form", "PEMBELIAN"))
        self.label_11.setText(_translate("Form", "Kelola Customer"))
        self.label_nama_customer.setText(_translate("Form", "Nama Customer"))
        self.Lbl_telpon.setText(_translate("Form", "Telpon"))
        self.Lbl_email.setText(_translate("Form", "Email"))
        self.Lbl_alamat.setText(_translate("Form", "Alamat"))
        self.btn_Simpan_2.setText(_translate("Form", "Simpan"))
        self.btn_Edit_2.setText(_translate("Form", "Edit"))
        self.btn_Hapus_2.setText(_translate("Form", "Hapus"))
        self.btn_Reset_2.setText(_translate("Form", "Reset"))
        
        headers = ["ID", "Nama Customer", "Telepon", "Email", "Alamat"]
        for i, text in enumerate(headers):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("Form", text))