# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'addItemUIHIiFWq.ui'
##
# Created by: Qt User Interface Compiler version 6.4.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)
import PySide6


class UpdateItemWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(500, 552)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border-radius: 10px;\n"
                                  "")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(59, 59, 59);")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 25, -1, -1)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 50))
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_37 = QLabel(self.widget_3)
        self.label_37.setObjectName(u"label_37")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Poppins SemiBold"])
        font.setPointSize(26)
        font.setBold(True)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet(u"QLabel{\n"
                                    "	color:white;\n"
                                    "}")

        self.horizontalLayout.addWidget(self.label_37, 0, Qt.AlignHCenter)

        self.verticalLayout_3.addWidget(self.widget_3, 0, Qt.AlignTop)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMinimumSize(QSize(400, 0))
        self.widget_4.setMaximumSize(QSize(200, 16777215))
        self.widget_4.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_102 = QWidget(self.widget_4)
        self.widget_102.setObjectName(u"widget_102")
        self.widget_102.setMinimumSize(QSize(380, 230))
        self.widget_102.setMaximumSize(QSize(360, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.widget_102)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_38 = QLabel(self.widget_102)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setFamilies([u"Poppins SemiBold"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_38.setFont(font1)
        self.label_38.setStyleSheet(u"QLabel{\n"
                                    "	color:white;\n"
                                    "}")

        self.horizontalLayout_45.addWidget(self.label_38)

        self.label_39 = QLabel(self.widget_102)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 35))
        self.label_39.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamilies([u"Poppins Medium"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.label_39.setFont(font2)
        self.label_39.setStyleSheet(u"QLabel{\n"
                                    "	color:white;\n"
                                    "}")

        self.horizontalLayout_45.addWidget(self.label_39)

        self.horizontalSpacer_7 = QSpacerItem(
            171, 35, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_7)

        self.verticalLayout_5.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_40 = QLabel(self.widget_102)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)
        self.label_40.setStyleSheet(u"QLabel{\n"
                                    "	color:white;\n"
                                    "}")

        self.horizontalLayout_3.addWidget(self.label_40)

        self.lineEdit_7 = QLineEdit(self.widget_102)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy2)
        self.lineEdit_7.setMinimumSize(QSize(200, 35))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Poppins Medium"])
        font3.setPointSize(11)
        self.lineEdit_7.setFont(font3)
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
                                      "    background-color: #1F1F1F;\n"
                                      "    border: 1px solid #3B3B3B;\n"
                                      "    border-radius: 5px;\n"
                                      "    padding: 8px;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus {\n"
                                      "    border-color: #FF8C18; /* Change border color when line edit is focused */\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit::placeholder {\n"
                                      "    color: #808080; /* Placeholder text color */\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit::hover {\n"
                                      "    background-color: #272727; /* Change background color on hover */\n"
                                      "}\n"
                                      "")

        self.horizontalLayout_3.addWidget(self.lineEdit_7)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_57 = QLabel(self.widget_102)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font1)
        self.label_57.setStyleSheet(u"QLabel{\n"
                                    "	color:white;\n"
                                    "}")

        self.horizontalLayout_4.addWidget(self.label_57)

        self.lineEdit_8 = QLineEdit(self.widget_102)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy2.setHeightForWidth(
            self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy2)
        self.lineEdit_8.setMinimumSize(QSize(200, 35))
        self.lineEdit_8.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_8.setFont(font3)
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
                                      "    background-color: #1F1F1F;\n"
                                      "    border: 1px solid #3B3B3B;\n"
                                      "    border-radius: 5px;\n"
                                      "    padding: 8px;\n"
                                      "    color: white;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus {\n"
                                      "    border-color: #FF8C18; /* Change border color when line edit is focused */\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit::placeholder {\n"
                                      "    color: #808080; /* Placeholder text color */\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit::hover {\n"
                                      "    background-color: #272727; /* Change background color on hover */\n"
                                      "}\n"
                                      "")

        self.horizontalLayout_4.addWidget(self.lineEdit_8)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_58 = QLabel(self.widget_102)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font1)
        self.label_58.setStyleSheet(u"QLabel{\n"
                                    "	color:white;\n"
                                    "}")

        self.horizontalLayout_2.addWidget(self.label_58)

        self.comboBox_2 = QComboBox(self.widget_102)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font3)
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
                                      "    background-color: #1F1F1F;\n"
                                      "    border: 1px solid #3B3B3B;\n"
                                      "    border-radius: 5px;\n"
                                      "    padding: 8px;\n"
                                      "    color: white;\n"
                                      "    min-width: 150px; /* Set minimum width */\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::drop-down {\n"
                                      "    border: none;\n"
                                      "    subcontrol-origin: padding;\n"
                                      "    subcontrol-position: top right;\n"
                                      "    width: 20px;\n"
                                      "    background-color: transparent;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::down-arrow {\n"
                                      "    image: url(:/iCons/icons8-down-arrow-25.png); \n"
                                      "    width: 16px; \n"
                                      "    height: 16px;\n"
                                      "    subcontrol-origin: padding; \n"
                                      "    subcontrol-position: center right; \n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QComboBox::item {\n"
                                      "    background-color: #1F1F1F;\n"
                                      "	color:white;\n"
                                      "    padding: 8px;\n"
                                      "}\n"
                                      "QComboBox QAbstractItemView::item {\n"
                                      "    background-color: #272727; \n"
                                      "    padding: 8px;\n"
                                      "	border-radius:5px;\n"
                                      "	border: 1px solid #3B3B3B;\n"
                                      "    color: white; \n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::item:selected {\n"
                                      "    background-color: #FF8C18;\n"
                                      "}\n"
                                      "\n"
                                      "QComboBox::hover {"
                                      "\n"
                                      "    background-color: #272727; \n"
                                      "}\n"
                                      "QComboBox QAbstractItemView::item:hover {\n"
                                      "    background-color: #B7B7B7;\n"
                                      "}\n"
                                      "")

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(
            20, 66, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_4.addWidget(self.widget_102)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cancelUpdateBtn = QPushButton(self.widget_5)
        self.cancelUpdateBtn.setObjectName(u"cancelUpdateBtn")
        self.cancelUpdateBtn.setMinimumSize(QSize(132, 31))
        self.cancelUpdateBtn.setMaximumSize(QSize(16777215, 31))
        self.cancelUpdateBtn.toggled.connect(self.close)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.cancelUpdateBtn.setFont(font4)
        self.cancelUpdateBtn.setStyleSheet(u"QPushButton {\n"
                                           "    padding: 6px 14px;\n"
                                           "    font-family: \"Roboto\", sans-serif;\n"
                                           "    border-radius: 6px;\n"
                                           "    border: none;\n"
                                           "    color: white;\n"
                                           "    background: #FF8C18;\n"
                                           "    box-shadow: 0px 0.5px 1.5px rgba(54, 122, 246, 0.25), inset 0px 0.8px 0px -0.25px rgba(255, 255, 255, 0.2);\n"
                                           "    user-select: none;\n"
                                           "    -webkit-user-select: none;\n"
                                           "    touch-action: manipulation;\n"
                                           "    transition: background-color 0.2s, box-shadow 0.2s; \n"
                                           "}\n"
                                           "QPushButton::pressed {\n"
                                           "    background-color: #B7B7B7;\n"
                                           "    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.5) inset;\n"
                                           "	color:black;\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: #FFA54E; \n"
                                           "}")
        self.cancelUpdateBtn.setCheckable(True)
        self.cancelUpdateBtn.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.cancelUpdateBtn)

        self.pushButton_32 = QPushButton(self.widget_5)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(132, 31))
        self.pushButton_32.setMaximumSize(QSize(16777215, 31))
        self.pushButton_32.setFont(font4)
        self.pushButton_32.setStyleSheet(u"QPushButton {\n"
                                         "    padding: 6px 14px;\n"
                                         "    font-family: \"Roboto\", sans-serif;\n"
                                         "    border-radius: 6px;\n"
                                         "    border: none;\n"
                                         "    color: white;\n"
                                         "    background: #FF8C18;\n"
                                         "    box-shadow: 0px 0.5px 1.5px rgba(54, 122, 246, 0.25), inset 0px 0.8px 0px -0.25px rgba(255, 255, 255, 0.2);\n"
                                         "    user-select: none;\n"
                                         "    -webkit-user-select: none;\n"
                                         "    touch-action: manipulation;\n"
                                         "    transition: background-color 0.2s, box-shadow 0.2s; \n"
                                         "}\n"
                                         "QPushButton::pressed {\n"
                                         "    background-color: #B7B7B7;\n"
                                         "    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.5) inset;\n"
                                         "	color:black;\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: #FFA54E; \n"
                                         "}")
        self.pushButton_32.setCheckable(True)
        self.pushButton_32.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.pushButton_32)

        self.verticalLayout_4.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 25))

        self.verticalLayout_4.addWidget(self.widget_6)

        self.verticalLayout_3.addWidget(self.widget_4, 0, Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.widget_2)

        self.verticalLayout.addWidget(self.widget)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_37.setText(QCoreApplication.translate(
            "MainWindow", u"Update Item", None))
        self.label_38.setText(QCoreApplication.translate(
            "MainWindow", u"Product ID: ", None))
        self.label_39.setText(QCoreApplication.translate(
            "MainWindow", u"11234", None))
        self.label_40.setText(QCoreApplication.translate(
            "MainWindow", u"Product Name:", None))
        self.label_57.setText(QCoreApplication.translate(
            "MainWindow", u"Product Price:", None))
        self.label_58.setText(QCoreApplication.translate(
            "MainWindow", u"Select Category:", None))
        self.comboBox_2.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Coffee", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate(
            "MainWindow", u"Non-Coffee", None))

        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Choose Category", None))
        self.cancelUpdateBtn.setText(
            QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_32.setText(
            QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.dragPos)

    def hideEvent(self, event):
        self.hide()
