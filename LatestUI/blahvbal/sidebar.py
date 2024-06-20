from PySide6.QtWidgets import QMainWindow, QApplication
from addItemUI import AddItemWindow
from ui_updateItemUI2 import UpdateItemWindow
from ui_admin_UI_v3_latest import Ui_MainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtGui import QRegion, QPainter, QBitmap


class mySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Admin UI")

        self.draggable = False
        self.drag_pos = None
        self.resizing = False
        self.resize_start_pos = None
        self.resize_start_geometry = None

        self.showNormal()

        self.word_iicon.setHidden(True)
        self.center_on_screen()
        

        self.dashboard1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard2.clicked.connect(self.switch_to_dashboardPage)

        self.add_item1.clicked.connect(self.switch_to_addProductPage)
        self.add_item2.clicked.connect(self.switch_to_addProductPage)

        self.update_item1.clicked.connect(self.switch_to_updateProductPage)
        self.update_item2.clicked.connect(self.switch_to_updateProductPage)

        self.delete_item1.clicked.connect(self.switch_to_deleteProductPage)
        self.delete_item1_2.clicked.connect(self.switch_to_deleteProductPage)

        self.sales_report1.clicked.connect(self.switch_to_salesReportPage)
        self.sales_report2.clicked.connect(self.switch_to_salesReportPage)

        self.mng_account1.clicked.connect(self.switch_to_manageAccountsPage)
        self.mng_account2.clicked.connect(self.switch_to_manageAccountsPage)

        self.toolButton.clicked.connect(self.maximizeOrNormalize)

        self.add_prod_button.clicked.connect(
            self.show_add_item_window)
        self.update_prod_button.clicked.connect(
            self.show_update_item_window)

        self.AddItemWindow = AddItemWindow()
        self.UpdateItemWindow = UpdateItemWindow()

        self.dashboardTxt.setHidden(True)

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)
        self.dashboardTxt.setText("Dashboard")
        self.dashboardTxt.setHidden(False)

    def switch_to_addProductPage(self):
        self.stackedWidget.setCurrentIndex(1)
        self.dashboardTxt.setText("Add Item")
        self.dashboardTxt.setHidden(False)

    def switch_to_updateProductPage(self):
        self.stackedWidget.setCurrentIndex(2)
        self.dashboardTxt.setText("Update Item")
        self.dashboardTxt.setHidden(False)

    def switch_to_deleteProductPage(self):
        self.stackedWidget.setCurrentIndex(3)
        self.dashboardTxt.setText("Delete Item")
        self.dashboardTxt.setHidden(False)

    def switch_to_salesReportPage(self):
        self.stackedWidget.setCurrentIndex(4)
        self.dashboardTxt.setText("Sales Report")
        self.dashboardTxt.setHidden(False)

    def switch_to_manageAccountsPage(self):
        self.stackedWidget.setCurrentIndex(5)
        self.dashboardTxt.setText("Manage Accounts")
        self.dashboardTxt.setHidden(False)

    def show_add_item_window(self):
        self.AddItemWindow.show()

    def show_update_item_window(self):
        self.UpdateItemWindow.show()

    def maximizeOrNormalize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.pos().y() < 30:
                self.draggable = True
                self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            else:
                self.resizing = True
                self.resize_start_pos = event.globalPos()
                self.resize_start_geometry = self.geometry()

    def mouseMoveEvent(self, event):
        if self.draggable:
            self.move(event.globalPos() - self.drag_pos)
        elif self.resizing:
            delta = event.globalPos() - self.resize_start_pos
            new_geometry = self.resize_start_geometry.adjusted(
                0, 0, delta.x(), delta.y())
            self.setGeometry(new_geometry)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False
            self.resizing = False

    def normalizeWindow(self):
        self.showNormal()

    def center_on_screen(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()

        center_point = screen_geometry.center()

        window_rect = self.frameGeometry()
        window_rect.moveCenter(center_point)

        self.move(window_rect.topLeft())

    def set_rounded_corners(self):

        mask_region = QRegion(self.rect(), QRegion.Ellipse)
        self.setMask(mask_region)
