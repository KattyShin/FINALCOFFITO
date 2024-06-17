import sys
import psycopg2
from PySide6.QtWidgets import QApplication, QMainWindow
from sidebar import mySideBar
from addItemUI import AddItemWindow
from ui_updateItemUI2 import UpdateItemWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from ui_loginPage import Login_MainWindow
from dotenv import load_dotenv
from updateAdminModal import UpdateAdminWindow
from updateStaffModal import UpdateStaffWindow


load_dotenv()
app = QApplication(sys.argv)


login_window = QMainWindow()
ui_login = Login_MainWindow()
ui_login.setupUi(login_window)

ui_login.login_successful.connect(lambda:show_sidebar(login_window))
login_window.show()

def show_sidebar(login_window):
    login_window.close()

    adminUI = mySideBar()
    adminUI.show()


# Wait for the login window to be closed
app.exec()

# window = mySideBar()
# window.show()



# addItemWindow = AddItemWindow()
# updateItemWindow = UpdateItemWindow()
# updateAdminWindow = UpdateAdminWindow()
# UpdateStaffWindow = UpdateStaffWindow()



