from PyQt5.QtWidgets import QMainWindow

from form.form_dashboard import Ui_MainWindow
from db import get_connection

from controllers.customer_controller import CustomerController
from controllers.produk_controller import ProdukController
from controllers.supplier_controller import SupplierController
from controllers.penjualan_controller import PenjualanController
from controllers.pembelian_controller import PembelianController


class DashboardController(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Database
        self.db = get_connection()

        # Child window handler
        self.child_window = None

        # Init
        self.bind_event()
        self.load_dashboard()

    # ================= EVENT =================
    def bind_event(self):
        self.ui.btn_customer.clicked.connect(self.open_customer)
        self.ui.btn_produk.clicked.connect(self.open_produk)
        self.ui.btn_supplier.clicked.connect(self.open_supplier)
        self.ui.btn_penjualan.clicked.connect(self.open_penjualan)
        self.ui.btn_pembelian.clicked.connect(self.open_pembelian)

    # ================= NAVIGATION =================
    def open_customer(self):
        self.child_window = CustomerController()
        self.child_window.show()

    def open_produk(self):
        self.child_window = ProdukController()
        self.child_window.show()

    def open_supplier(self):
        self.child_window = SupplierController()
        self.child_window.show()

    def open_penjualan(self):
        self.child_window = PenjualanController(self.db)
        self.child_window.show()

    def open_pembelian(self):
        self.child_window = PembelianController(self.db)
        self.child_window.show()

    # ================= DASHBOARD DATA =================
    def load_dashboard(self):
        try:
            cursor = self.db.cursor()

            # Total transaksi penjualan
            cursor.execute("SELECT COUNT(*) FROM penjualan")
            total_penjualan = cursor.fetchone()[0]

            # Total produk
            cursor.execute("SELECT COUNT(*) FROM produk")
            total_produk = cursor.fetchone()[0]

            # Total stok
            cursor.execute("SELECT SUM(stok) FROM produk")
            total_stok = cursor.fetchone()[0] or 0

            # Total pendapatan
            cursor.execute("SELECT SUM(total) FROM penjualan")
            total_pendapatan = cursor.fetchone()[0] or 0

            # Update UI
            self.ui.lbl_summary_penjualan.setText(
                f"penjualan : {total_penjualan} transaksi"
            )
            self.ui.lbl_summary_produk.setText(
                f"produk : {total_produk} item"
            )
            self.ui.lbl_summary_stok.setText(
                f"stok : {total_stok} unit"
            )
            self.ui.lbl_summary_pendapatan.setText(
                f"pendapatan : Rp {total_pendapatan:,.0f}"
            )

        except Exception as e:
            # untuk UAS, cukup tampilkan dialog
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Error", f"Gagal memuat dashboard\n{e}")
