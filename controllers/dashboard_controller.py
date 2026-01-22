from PyQt5.QtWidgets import QMainWindow
from controllers.pembelian_controller import PembelianController
from controllers.penjualan_controller import PenjualanController
from db import get_connection
import db
from form.form_dashboard import Ui_MainWindow
from controllers.customer_controller import CustomerController
from controllers.produk_controller import ProdukController
from controllers.supplier_controller import SupplierController

class DashboardController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = db
        print("INIT DASHBOARD")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = get_connection()
        self.child_window = None
        self.bind_event()

    def bind_event(self):
        self.ui.btn_customer.clicked.connect(self.open_customer)

    def open_customer(self):
        print("OPEN CUSTOMER")
        self.child_window = CustomerController()
        self.child_window.show()

    def bind_event(self):
        self.ui.btn_customer.clicked.connect(self.open_customer)
        self.ui.btn_produk.clicked.connect(self.open_produk)
        self.ui.btn_supplier.clicked.connect(self.open_supplier)
        self.ui.btn_customer.clicked.connect(self.open_customer)
        self.ui.btn_produk.clicked.connect(self.open_produk)
        self.ui.btn_supplier.clicked.connect(self.open_supplier)
        self.ui.btn_penjualan.clicked.connect(self.open_penjualan)
        self.ui.btn_pembelian.clicked.connect(self.open_pembelian)


    def open_produk(self):
        print("OPEN PRODUK")
        self.child_window = ProdukController()
        self.child_window.show()

    def open_supplier(self):
        self.supplier_window = SupplierController()
        self.supplier_window.show()

    def open_penjualan(self):
        self.form = PenjualanController(self.db)
        self.form.show()

    def open_pembelian(self):
        self.form = PembelianController(self.db)
        self.form.show()



