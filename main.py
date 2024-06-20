import sys
from PySide6.QtWidgets import QApplication
from ui_loginPage import Login_MainWindow
from dotenv import load_dotenv

load_dotenv()

def main():
    app = QApplication(sys.argv)

    login_window = Login_MainWindow()
    login_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
