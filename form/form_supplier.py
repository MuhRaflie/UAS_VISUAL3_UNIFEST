# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Supplier(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(851, 719)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 851, 721))
        self.frame_2.setStyleSheet("background-color: #d8d8d8;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        # --- HEADER SECTION ---
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
        button_style = "background-color: #ff5757; color: white;"
        self.btn_dashboard = QtWidgets.QPushButton(self.frame_header)
        self.btn_dashboard.setGeometry(QtCore.QRect(190, 10, 131, 31))
        self.btn_dashboard.setStyleSheet(button_style)
        
        self.btn_produk = QtWidgets.QPushButton(self.frame_header)
        self.btn_produk.setGeometry(QtCore.QRect(330, 10, 131, 31))
        self.btn_produk.setStyleSheet(button_style)
        
        self.btn_supplier = QtWidgets.QPushButton(self.frame_header)
        self.btn_supplier.setGeometry(QtCore.QRect(470, 10, 131, 31))
        self.btn_supplier.setStyleSheet(button_style)
        
        self.btn_customer = QtWidgets.QPushButton(self.frame_header)
        self.btn_customer.setGeometry(QtCore.QRect(470, 50, 131, 31))
        self.btn_customer.setStyleSheet(button_style)
        
        self.btn_penjualan = QtWidgets.QPushButton(self.frame_header)
        self.btn_penjualan.setGeometry(QtCore.QRect(190, 50, 131, 31))
        self.btn_penjualan.setStyleSheet(button_style)
        
        self.btn_menu = QtWidgets.QPushButton(self.frame_header)
        self.btn_menu.setGeometry(QtCore.QRect(730, 30, 91, 31))
        self.btn_menu.setStyleSheet(button_style)
        
        self.btn_pembelian = QtWidgets.QPushButton(self.frame_header)
        self.btn_pembelian.setGeometry(QtCore.QRect(330, 50, 131, 31))
        self.btn_pembelian.setStyleSheet(button_style)

        # --- CONTENT SECTION ---
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 110, 851, 621))
        self.frame_3.setStyleSheet("background-color: #ffffff;")
        self.frame_3.setObjectName("frame_3")

        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 831, 291))
        self.frame_6.setStyleSheet("background-color: #ff5757; color: white; padding: 10px; border-radius: 10px;")
        
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        self.label_11.setGeometry(QtCore.QRect(10, 0, 231, 41))
        font = QtGui.QFont(); font.setPointSize(16)
        self.label_11.setFont(font)

        # Form Layout
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_6)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 811, 201))
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)

        input_style = "background-color: #ff6f6f; color: white; padding: 6px; border-radius: 8px;"
        
        self.namaSupplierLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.namaSupplierLabel)
        self.input_nama_supplier = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.input_nama_supplier.setStyleSheet(input_style)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_nama_supplier)

        self.teleponLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.teleponLabel)
        self.input_telepon = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.input_telepon.setStyleSheet(input_style)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_telepon)

        self.emailLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.emailLabel)
        self.input_email = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.input_email.setStyleSheet(input_style)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_email)

        self.alamatLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alamatLabel)
        self.input_alamat = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.input_alamat.setMaximumSize(QtCore.QSize(16777215, 50))
        self.input_alamat.setStyleSheet(input_style)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input_alamat)

        # Buttons
        btn_action_style = "background-color: white; color: black;"
        self.btn_Simpan = QtWidgets.QPushButton(self.frame_6)
        self.btn_Simpan.setGeometry(QtCore.QRect(10, 250, 71, 31))
        self.btn_Simpan.setStyleSheet(btn_action_style)
        
        self.btn_Edit = QtWidgets.QPushButton(self.frame_6) # Perbaikan nama variabel dari btn_Edit_2
        self.btn_Edit.setGeometry(QtCore.QRect(90, 250, 71, 31))
        self.btn_Edit.setStyleSheet(btn_action_style)
        
        self.btn_Hapus = QtWidgets.QPushButton(self.frame_6)
        self.btn_Hapus.setGeometry(QtCore.QRect(170, 250, 71, 31))
        self.btn_Hapus.setStyleSheet(btn_action_style)
        
        self.btn_Reset = QtWidgets.QPushButton(self.frame_6)
        self.btn_Reset.setGeometry(QtCore.QRect(250, 250, 71, 31))
        self.btn_Reset.setStyleSheet(btn_action_style)

        # Table
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 310, 821, 301))
        self.tableWidget.setColumnCount(5)
        for i in range(5):
            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kelola Supplier"))
        self.lbl_logo.setText(_translate("Form", "UNIFEST"))
        self.btn_dashboard.setText(_translate("Form", "DASHBOARD"))
        self.btn_produk.setText(_translate("Form", "PRODUK"))
        self.btn_supplier.setText(_translate("Form", "SUPPLIER"))
        self.btn_customer.setText(_translate("Form", "CUSTOMER"))
        self.btn_penjualan.setText(_translate("Form", "PENJUALAN"))
        self.btn_menu.setText(_translate("Form", "Logout"))
        self.btn_pembelian.setText(_translate("Form", "PEMBELIAN"))
        self.label_11.setText(_translate("Form", "Kelola Supplier"))
        self.namaSupplierLabel.setText(_translate("Form", "Nama Supplier"))
        self.teleponLabel.setText(_translate("Form", "Telepon"))
        self.emailLabel.setText(_translate("Form", "Email"))
        self.alamatLabel.setText(_translate("Form", "Alamat"))
        self.btn_Simpan.setText(_translate("Form", "Simpan"))
        self.btn_Edit.setText(_translate("Form", "Edit"))
        self.btn_Hapus.setText(_translate("Form", "Hapus"))
        self.btn_Reset.setText(_translate("Form", "Reset"))
        
        headers = ["ID", "Nama Supplier", "Telepon", "Email", "Alamat"]
        for i, name in enumerate(headers):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("Form", name))