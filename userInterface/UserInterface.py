import sys
import os
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import *
import PySide6
from PySide6.QtGui import QIcon, QColor, QPainter
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtGui import QRegion, QPainter, QBitmap

from MainUserInterface import Ui_MainWindow


class userInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Coffito Cafe")
        self.setWindowIcon(QIcon(r'C:\Users\Dennis\Desktop\POS System Coffito\CoffitoLogo (40 x 40 px).png'))
        

        self.word_iicon.setHidden(True)

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

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)
