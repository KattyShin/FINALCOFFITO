from PySide6.QtWidgets import QMainWindow, QApplication
from userUI import Ui_MainWindow


class userInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User Interface")

        self.word_iicon.setHidden(True)

    

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_addProductPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_updateProductPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_deleteProductPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_salesReportPage(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_manageAccountsPage(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_addProdPage(self):
        self.stackedWidget.setCurrentIndex(6)
