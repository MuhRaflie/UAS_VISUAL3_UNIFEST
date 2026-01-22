import sys
from PyQt5.QtWidgets import QApplication
from customer import CustomerWindow

if __name__ == "__main__":
    print("APP START")
    app = QApplication(sys.argv)

    window = CustomerWindow()
    window.show()

    print("WINDOW SHOWN")
    sys.exit(app.exec())
