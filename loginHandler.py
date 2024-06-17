import psycopg2
from PySide6.QtWidgets import QMessageBox

from database_config import get_database_config
from ui_loginPage import Ui_MainWindow

class Login:
    def __init__(self):
        self.login_window = Ui_MainWindow()  # Assuming Ui_MainWindow sets up QMainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.login_window)  # Correctly pass self.login_window to setupUi
        self.conn = None  # Initialize connection to None
        


    def connect_to_database(self):
        try:
            config = get_database_config()
            self.conn = psycopg2.connect(**config)
            print("Database connection established successfully!")
            return True
        except Exception as error:
            print(error)
            self.show_message_box("Database Error", str(error), QMessageBox.Critical)
            return False


    def show_message_box(self, title, message, icon=QMessageBox.Critical):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()


    def login_checker(self):
        """Checks login credentials and redirects to admin or user interface."""
        admin_user_id = 9242
        staff_user_id = 9243

        username = self.login_window.lineEdit_7.text()  # Access lineEdit_7
        password = self.login_window.lineEdit_8.text()

        try:
            if not self.conn:
                connected = self.connect_to_database()
                if not connected:
                    return False

            cur = self.conn.cursor()

            query = "SELECT USER_ID, PASS_WORD FROM USERS WHERE USERNAME = %s AND PASS_WORD = %s"
            cur.execute(query, (username, password))

            user = cur.fetchone()
            cur.close()

            if user:
                user_id, _ = user  # Unpack fetched data

                if user_id == admin_user_id:
                    print("Login as admin!")
                    self.show_message_box("Success", "Login successful as admin.", QMessageBox.Information)
                    self.admin_ui = Ui_MainWindow()  # Assuming Ui_MainWindow is the class for admin UI
                    self.admin_ui.setupUi(self)  # This sets up the UI elements defined in the Qt code

                    # Redirect to admin interface (implementation depends on your framework)
                    return True

                elif user_id == staff_user_id:
                    print("Login as staff!")
                    self.show_message_box("Success", "Login successful as staff.", QMessageBox.Information)
                    # Redirect to user interface (implementation depends on your framework)
                    return True

                else:
                    print("Login failed. Invalid username or password.")
                    self.show_message_box("Error", "Invalid username or password.", QMessageBox.Critical)
                    return False

            else:
                print("Login failed. Invalid username or password.")
                self.show_message_box("Error", "Invalid username or password.", QMessageBox.Critical)
                return False

        except (Exception, psycopg2.Error) as error:
            print("Error while checking login credentials:", error)
            self.show_message_box("Error", f"Error while checking login credentials: {error}", QMessageBox.Critical)
            return False
