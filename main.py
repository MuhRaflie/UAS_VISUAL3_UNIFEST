import sys
from PyQt5.QtWidgets import QApplication
from controllers.dashboard_controller import DashboardController

if __name__ == "__main__":
    print("APP START")
    app = QApplication(sys.argv)
    window = DashboardController()
    window.show()
    sys.exit(app.exec_())
