# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'admin_UI.ui'
##
# Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
                               QStackedWidget, QVBoxLayout, QWidget)
import resource1_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1011, 565)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
                                 "	background-color:#1F1F1F;\n"
                                 "	border-radius:15px;\n"
                                 "}\n"
                                 "QWidget{\n"
                                 "	background-color:#1F1F1F;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only = QWidget(self.centralwidget)
        self.icon_only.setObjectName(u"icon_only")
        self.icon_only.setStyleSheet(u"QWidget{\n"
                                     "	background-color:rgb(59,59,59)\n"
                                     "}\n"
                                     "QPushButton{\n"
                                     "	color:rgb(255,255,255);\n"
                                     "	height:30px;\n"
                                     "	border:none;\n"
                                     "	border-radius:10;\n"
                                     "	\n"
                                     "}\n"
                                     "QPushButton:checked{\n"
                                     "	background-color: #ECECEC;\n"
                                     "	color: #FF8C18;\n"
                                     "	font-weight:bold;\n"
                                     "}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, -1, 3, -1)
        self.label = QLabel(self.icon_only)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 31))
        self.label.setPixmap(
            QPixmap(u":/iCons/icons/Green Simple Monoline Badge CK Letter Logo (3).png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.dashboard1 = QPushButton(self.icon_only)
        self.dashboard1.setObjectName(u"dashboard1")
        icon = QIcon()
        icon.addFile(u":/iCons/icons/icons8-coffee-40.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/iCons/icons/icons8-coffee0-40.png",
                     QSize(), QIcon.Normal, QIcon.On)
        self.dashboard1.setIcon(icon)
        self.dashboard1.setIconSize(QSize(20, 20))
        self.dashboard1.setCheckable(True)
        self.dashboard1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard1)

        self.add_item1 = QPushButton(self.icon_only)
        self.add_item1.setObjectName(u"add_item1")
        icon1 = QIcon()
        icon1.addFile(u":/iCons/icons/icons8-add-folder-40.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/iCons/icons/icons8-add-40.png",
                      QSize(), QIcon.Normal, QIcon.On)
        self.add_item1.setIcon(icon1)
        self.add_item1.setCheckable(True)
        self.add_item1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.add_item1)

        self.update_item1 = QPushButton(self.icon_only)
        self.update_item1.setObjectName(u"update_item1")
        icon2 = QIcon()
        icon2.addFile(u":/iCons/icons/icons8-edit-40.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/iCons/icons/icons8-edit-40 (1).png",
                      QSize(), QIcon.Normal, QIcon.On)
        self.update_item1.setIcon(icon2)
        self.update_item1.setCheckable(True)
        self.update_item1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_item1)

        self.delete_item1 = QPushButton(self.icon_only)
        self.delete_item1.setObjectName(u"delete_item1")
        icon3 = QIcon()
        icon3.addFile(u":/iCons/icons/icons8-delete-40.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/iCons/icons/icons8-delete-40(1).png",
                      QSize(), QIcon.Normal, QIcon.On)
        self.delete_item1.setIcon(icon3)
        self.delete_item1.setCheckable(True)
        self.delete_item1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.delete_item1)

        self.sales_report1 = QPushButton(self.icon_only)
        self.sales_report1.setObjectName(u"sales_report1")
        icon4 = QIcon()
        icon4.addFile(u":/iCons/icons/icons8-sales-40.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/iCons/icons/icons8-sales-40(1).png",
                      QSize(), QIcon.Normal, QIcon.On)
        self.sales_report1.setIcon(icon4)
        self.sales_report1.setCheckable(True)
        self.sales_report1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.sales_report1)

        self.mng_account1 = QPushButton(self.icon_only)
        self.mng_account1.setObjectName(u"mng_account1")
        icon5 = QIcon()
        icon5.addFile(u":/iCons/icons/personalization.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.mng_account1.setIcon(icon5)
        self.mng_account1.setCheckable(True)
        self.mng_account1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.mng_account1)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(
            20, 185, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logout1 = QPushButton(self.icon_only)
        self.logout1.setObjectName(u"logout1")
        icon6 = QIcon()
        icon6.addFile(u":/iCons/icons/icons8-logout-40.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/iCons/icons/icons8-logouto-40.png",
                      QSize(), QIcon.Normal, QIcon.On)
        self.logout1.setIcon(icon6)
        self.logout1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.logout1)

        self.gridLayout.addWidget(self.icon_only, 0, 0, 1, 1)

        self.word_icon = QWidget(self.centralwidget)
        self.word_icon.setObjectName(u"word_icon")
        self.word_icon.setStyleSheet(u"QWidget{\n"
                                     "	background-color:rgb(59,59,59);\n"
                                     "}\n"
                                     "QPushButton{\n"
                                     "	color:rgb(255,255,255);\n"
                                     "	text-align:left;\n"
                                     "	height:30px;\n"
                                     "	border:none;\n"
                                     "	padding-left:10px;\n"
                                     "	border-top-left-radius:10px;\n"
                                     "	border-bottom-left-radius:10px;\n"
                                     "}\n"
                                     "QPushButton:checked{\n"
                                     "	background-color: #ECECEC;\n"
                                     "	color: #FF8C18;\n"
                                     "	font-weight:bold;\n"
                                     "}\n"
                                     "QLabel{\n"
                                     "	color:rgb(255,255,255);\n"
                                     "}\n"
                                     "")
        self.verticalLayout_4 = QVBoxLayout(self.word_icon)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.word_icon)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 31))
        self.label_2.setPixmap(
            QPixmap(u":/iCons/icons/Green Simple Monoline Badge CK Letter Logo (3).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.word_icon)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.dashboard2 = QPushButton(self.word_icon)
        self.dashboard2.setObjectName(u"dashboard2")
        self.dashboard2.setIcon(icon)
        self.dashboard2.setIconSize(QSize(20, 20))
        self.dashboard2.setCheckable(True)
        self.dashboard2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard2)

        self.add_item2 = QPushButton(self.word_icon)
        self.add_item2.setObjectName(u"add_item2")
        self.add_item2.setIcon(icon1)
        self.add_item2.setCheckable(True)
        self.add_item2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.add_item2)

        self.update_item2 = QPushButton(self.word_icon)
        self.update_item2.setObjectName(u"update_item2")
        self.update_item2.setIcon(icon2)
        self.update_item2.setCheckable(True)
        self.update_item2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_item2)

        self.delete_item1_2 = QPushButton(self.word_icon)
        self.delete_item1_2.setObjectName(u"delete_item1_2")
        self.delete_item1_2.setIcon(icon3)
        self.delete_item1_2.setCheckable(True)
        self.delete_item1_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.delete_item1_2)

        self.sales_report2 = QPushButton(self.word_icon)
        self.sales_report2.setObjectName(u"sales_report2")
        self.sales_report2.setIcon(icon4)
        self.sales_report2.setCheckable(True)
        self.sales_report2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.sales_report2)

        self.mng_account2 = QPushButton(self.word_icon)
        self.mng_account2.setObjectName(u"mng_account2")
        self.mng_account2.setIcon(icon5)
        self.mng_account2.setCheckable(True)
        self.mng_account2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.mng_account2)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(
            20, 183, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.logout2 = QPushButton(self.word_icon)
        self.logout2.setObjectName(u"logout2")
        self.logout2.setIcon(icon6)
        self.logout2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.logout2)

        self.gridLayout.addWidget(self.word_icon, 0, 1, 1, 1)

        self.Main_menu = QWidget(self.centralwidget)
        self.Main_menu.setObjectName(u"Main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.Main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.Main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
                                         "	\n"
                                         "	border:none;\n"
                                         "\n"
                                         "}")
        icon7 = QIcon()
        icon7.addFile(u":/iCons/icons/icons8-menu-40.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/iCons/icons/icons8-menu-40-1.png",
                      QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_15.setIcon(icon7)
        self.pushButton_15.setIconSize(QSize(16, 16))
        self.pushButton_15.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton_15)

        self.horizontalSpacer_2 = QSpacerItem(
            753, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.Main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(
            u"background-color:rgb(255, 255, 255)")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.label_6 = QLabel(self.dashboard_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 210, 201, 41))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.update_product = QWidget()
        self.update_product.setObjectName(u"update_product")
        self.label_8 = QLabel(self.update_product)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 190, 281, 41))
        self.label_8.setFont(font1)
        self.stackedWidget.addWidget(self.update_product)
        self.delete_product = QWidget()
        self.delete_product.setObjectName(u"delete_product")
        self.label_9 = QLabel(self.delete_product)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(230, 190, 261, 41))
        self.label_9.setFont(font1)
        self.stackedWidget.addWidget(self.delete_product)
        self.sales_report = QWidget()
        self.sales_report.setObjectName(u"sales_report")
        self.label_10 = QLabel(self.sales_report)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(260, 200, 271, 41))
        self.label_10.setFont(font1)
        self.stackedWidget.addWidget(self.sales_report)
        self.manage_account = QWidget()
        self.manage_account.setObjectName(u"manage_account")
        self.label_11 = QLabel(self.manage_account)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(220, 190, 311, 41))
        self.label_11.setFont(font1)
        self.stackedWidget.addWidget(self.manage_account)
        self.add_product = QWidget()
        self.add_product.setObjectName(u"add_product")
        self.label_7 = QLabel(self.add_product)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 200, 221, 41))
        self.label_7.setFont(font1)
        self.stackedWidget.addWidget(self.add_product)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.gridLayout.addWidget(self.Main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_15.toggled.connect(self.icon_only.setHidden)
        self.pushButton_15.toggled.connect(self.word_icon.setVisible)
        self.mng_account1.toggled.connect(self.mng_account2.setChecked)
        self.mng_account2.toggled.connect(self.mng_account1.setChecked)
        self.sales_report1.toggled.connect(self.sales_report2.setChecked)
        self.sales_report2.toggled.connect(self.sales_report1.setChecked)
        self.delete_item1.toggled.connect(self.delete_item1_2.setChecked)
        self.delete_item1_2.toggled.connect(self.delete_item1.setChecked)
        self.update_item2.toggled.connect(self.update_item1.setChecked)
        self.update_item1.toggled.connect(self.update_item2.setChecked)
        self.add_item2.toggled.connect(self.add_item1.setChecked)
        self.add_item1.toggled.connect(self.add_item2.setChecked)
        self.dashboard1.toggled.connect(self.dashboard2.setChecked)
        self.dashboard2.toggled.connect(self.dashboard1.setChecked)
        self.logout1.toggled.connect(MainWindow.close)
        self.logout2.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.dashboard1.setText("")
        self.add_item1.setText("")
        self.update_item1.setText("")
        self.delete_item1.setText("")
        self.sales_report1.setText("")
        self.mng_account1.setText("")
        self.logout1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"CoFFiTo", None))
        self.dashboard2.setText(QCoreApplication.translate(
            "MainWindow", u"Dashboard", None))
        self.add_item2.setText(QCoreApplication.translate(
            "MainWindow", u"Add Item", None))
        self.update_item2.setText(QCoreApplication.translate(
            "MainWindow", u"Update Item", None))
        self.delete_item1_2.setText(QCoreApplication.translate(
            "MainWindow", u"Delete Item", None))
        self.sales_report2.setText(QCoreApplication.translate(
            "MainWindow", u"Sales Report", None))
        self.mng_account2.setText(QCoreApplication.translate(
            "MainWindow", u"Accounts", None))
        self.logout2.setText(QCoreApplication.translate(
            "MainWindow", u"Logout", None))
        self.pushButton_15.setText("")
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Dashboard Page", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Update-Product Page", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Delete-Product Page", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Sales Report Page", None))
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Manage-Accounts Page", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Add-Product Page", None))
    # retranslateUi
