from PyQt5.QtWidgets import QMainWindow
from form.form_dashboard import Ui_MainWindow
from controllers.customer_controller import CustomerController
from controllers.produk_controller import ProdukController
from controllers.supplier_controller import SupplierController

class DashboardController(QMainWindow):
    def __init__(self):
        super().__init__()
        print("INIT DASHBOARD")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

    def open_produk(self):
        print("OPEN PRODUK")
        self.child_window = ProdukController()
        self.child_window.show()

    def open_supplier(self):
        self.supplier_window = SupplierController()
        self.supplier_window.show()



