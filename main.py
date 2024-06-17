import sys
from PySide6.QtWidgets import QApplication
from ui_loginPage import Login_MainWindow
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create instance of Login_MainWindow
    login_window = Login_MainWindow()

    # Show the login window
    login_window.show()

    # Start the application event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
