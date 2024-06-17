from PySide6.QtCore import Qt
from ui_admin_UI_v4 import Ui_MainWindow

GLOBAL_STATE = 0


class UIFunctions(Ui_MainWindow):

    def uiDefinitions(self, window):
        window.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
