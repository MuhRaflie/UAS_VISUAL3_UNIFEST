from PyQt5.QtWidgets import QMainWindow
from form.form_dashboard import Ui_MainWindow
from controllers.customer_controller import CustomerController

# import controller lain (sementara dikomentari)
# from controllers.customer_controller import CustomerController

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

