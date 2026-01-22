import sys
from PyQt5.QtWidgets import QApplication
from controllers.dashboard_controller import DashboardController
from db import get_connection


if __name__ == "__main__":
    print("APP START")
    db = get_connection()
    app = QApplication(sys.argv)
    window = DashboardController()
    window.show()
    sys.exit(app.exec_())
