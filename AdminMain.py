# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_UI_v3_latestvTXFwY.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

import resource1_rc
import main_resources
import resource1_rcc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 649)
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
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.word_iicon = QWidget(self.centralwidget)
        self.word_iicon.setObjectName(u"word_iicon")
        self.word_iicon.setMinimumSize(QSize(140, 0))
        self.word_iicon.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(49,49,49);\n"
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
        self.verticalLayout_4 = QVBoxLayout(self.word_iicon)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.word_iicon)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 31))
        self.label_2.setPixmap(QPixmap(u":/iCons/CoffitoLogo (40 x 40 px).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.word_iicon)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.dashboard2 = QPushButton(self.word_iicon)
        self.dashboard2.setObjectName(u"dashboard2")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(10)
        self.dashboard2.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/iCons/icons/icons8-coffee-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/iCons/icons/icons8-coffee0-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard2.setIcon(icon)
        self.dashboard2.setIconSize(QSize(25, 25))
        self.dashboard2.setCheckable(True)
        self.dashboard2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard2)

        self.add_item2 = QPushButton(self.word_iicon)
        self.add_item2.setObjectName(u"add_item2")
        self.add_item2.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/iCons/icons/icons8-add-folder-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/iCons/icons/icons8-add-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.add_item2.setIcon(icon1)
        self.add_item2.setIconSize(QSize(20, 20))
        self.add_item2.setCheckable(True)
        self.add_item2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.add_item2)

        self.update_item2 = QPushButton(self.word_iicon)
        self.update_item2.setObjectName(u"update_item2")
        self.update_item2.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/iCons/icons/icons8-edit-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/iCons/icons/icons8-edit-40 (1).png", QSize(), QIcon.Normal, QIcon.On)
        self.update_item2.setIcon(icon2)
        self.update_item2.setIconSize(QSize(20, 20))
        self.update_item2.setCheckable(True)
        self.update_item2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_item2)

        self.delete_item1_2 = QPushButton(self.word_iicon)
        self.delete_item1_2.setObjectName(u"delete_item1_2")
        self.delete_item1_2.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/iCons/icons/icons8-delete-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/iCons/icons/icons8-delete-40(1).png", QSize(), QIcon.Normal, QIcon.On)
        self.delete_item1_2.setIcon(icon3)
        self.delete_item1_2.setIconSize(QSize(20, 20))
        self.delete_item1_2.setCheckable(True)
        self.delete_item1_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.delete_item1_2)

        self.sales_report2 = QPushButton(self.word_iicon)
        self.sales_report2.setObjectName(u"sales_report2")
        self.sales_report2.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/iCons/icons/icons8-sales-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/iCons/icons/icons8-sales-40(1).png", QSize(), QIcon.Normal, QIcon.On)
        self.sales_report2.setIcon(icon4)
        self.sales_report2.setIconSize(QSize(20, 20))
        self.sales_report2.setCheckable(True)
        self.sales_report2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.sales_report2)

        self.mng_account2 = QPushButton(self.word_iicon)
        self.mng_account2.setObjectName(u"mng_account2")
        self.mng_account2.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/iCons/icons/personalization.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mng_account2.setIcon(icon5)
        self.mng_account2.setIconSize(QSize(20, 20))
        self.mng_account2.setCheckable(True)
        self.mng_account2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.mng_account2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 180, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.logout2 = QPushButton(self.word_iicon)
        self.logout2.setObjectName(u"logout2")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        self.logout2.setFont(font2)
        icon6 = QIcon()
        icon6.addFile(u":/iCons/icons/icons8-logout-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/iCons/icons/icons8-logouto-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.logout2.setIcon(icon6)
        self.logout2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.logout2)


        self.gridLayout_7.addWidget(self.word_iicon, 0, 1, 1, 1)

        self.Main_menu = QWidget(self.centralwidget)
        self.Main_menu.setObjectName(u"Main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.Main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.Main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	\n"
"	border:none;\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/iCons/icons/icons8-menu-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/iCons/icons/icons8-menu-40-1.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_15.setIcon(icon7)
        self.pushButton_15.setIconSize(QSize(16, 16))
        self.pushButton_15.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton_15)

        self.dashboardTxt = QLabel(self.header_widget)
        self.dashboardTxt.setObjectName(u"dashboardTxt")
        font3 = QFont()
        font3.setFamilies([u"Poppins SemiBold"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.dashboardTxt.setFont(font3)
        self.dashboardTxt.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_4.addWidget(self.dashboardTxt)

        self.horizontalSpacer_2 = QSpacerItem(684, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.Main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget{\n"
"	background-color:rgb(59,59,59);\n"
"	\n"
"}\n"
"QLabel{\n"
"	color:rgb(255,255,255);\n"
"}")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.gridLayout_2 = QGridLayout(self.dashboard_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 10)
        self.widget = QWidget(self.dashboard_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(170, 90))
        self.widget.setStyleSheet(u"background-color: #3B3B3B;\n"
"border-radius:10px;\n"
"")
        self.verticalLayout_29 = QVBoxLayout(self.widget)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, -1, 9)
        self.widget_15 = QWidget(self.widget)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 25))
        self.verticalLayout_30 = QVBoxLayout(self.widget_15)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.label_15 = QLabel(self.widget_15)
        self.label_15.setObjectName(u"label_15")
        font4 = QFont()
        font4.setFamilies([u"Poppins SemiBold"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_15.setFont(font4)

        self.verticalLayout_30.addWidget(self.label_15)


        self.verticalLayout_29.addWidget(self.widget_15)

        self.widget_19 = QWidget(self.widget)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(0, 25))
        self.horizontalLayout_29 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(12, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_19)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(50, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/iCons/icons/icons8-total-sales-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)
        self.pushButton.setIconSize(QSize(45, 50))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_29.addWidget(self.pushButton)

        self.label_5 = QLabel(self.widget_19)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setFamilies([u"Poppins Black"])
        font5.setPointSize(18)
        font5.setBold(True)
        self.label_5.setFont(font5)

        self.horizontalLayout_29.addWidget(self.label_5)


        self.verticalLayout_29.addWidget(self.widget_19)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.dashboard_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(170, 90))
        self.widget_2.setStyleSheet(u"background-color: #3B3B3B;\n"
"border-radius:10px;\n"
"")
        self.verticalLayout_33 = QVBoxLayout(self.widget_2)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, -1, 9)
        self.widget_17 = QWidget(self.widget_2)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 25))
        self.verticalLayout_34 = QVBoxLayout(self.widget_17)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(-1, -1, -1, 0)
        self.label_22 = QLabel(self.widget_17)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)

        self.verticalLayout_34.addWidget(self.label_22)


        self.verticalLayout_33.addWidget(self.widget_17)

        self.widget_74 = QWidget(self.widget_2)
        self.widget_74.setObjectName(u"widget_74")
        self.widget_74.setMinimumSize(QSize(0, 25))
        self.horizontalLayout_31 = QHBoxLayout(self.widget_74)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(12, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget_74)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(30, 30))
        self.pushButton_3.setMaximumSize(QSize(50, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/iCons/icons/coffee-cup (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon9)
        self.pushButton_3.setIconSize(QSize(40, 50))
        self.pushButton_3.setCheckable(True)

        self.horizontalLayout_31.addWidget(self.pushButton_3)

        self.label_8 = QLabel(self.widget_74)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)

        self.horizontalLayout_31.addWidget(self.label_8)


        self.verticalLayout_33.addWidget(self.widget_74)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.dashboard_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(170, 90))
        self.widget_3.setStyleSheet(u"background-color: #3B3B3B;\n"
"border-radius:10px;\n"
"")
        self.verticalLayout_35 = QVBoxLayout(self.widget_3)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, -1, 9)
        self.widget_18 = QWidget(self.widget_3)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 25))
        self.verticalLayout_36 = QVBoxLayout(self.widget_18)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, -1, -1, 0)
        self.label_23 = QLabel(self.widget_18)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font4)

        self.verticalLayout_36.addWidget(self.label_23)


        self.verticalLayout_35.addWidget(self.widget_18)

        self.widget_75 = QWidget(self.widget_3)
        self.widget_75.setObjectName(u"widget_75")
        self.widget_75.setMinimumSize(QSize(0, 25))
        self.horizontalLayout_32 = QHBoxLayout(self.widget_75)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(12, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget_75)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(30, 30))
        self.pushButton_4.setMaximumSize(QSize(50, 16777215))
        icon10 = QIcon()
        icon10.addFile(u":/iCons/icons/coffee-cup4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon10)
        self.pushButton_4.setIconSize(QSize(40, 50))
        self.pushButton_4.setCheckable(True)

        self.horizontalLayout_32.addWidget(self.pushButton_4)

        self.label_9 = QLabel(self.widget_75)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.horizontalLayout_32.addWidget(self.label_9)


        self.verticalLayout_35.addWidget(self.widget_75)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.widget_4 = QWidget(self.dashboard_page)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QSize(0, 360))
        self.widget_4.setStyleSheet(u"background-color: #3B3B3B;\n"
"border-radius:10px;\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setFamilies([u"Poppins SemiBold"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_6.setFont(font6)

        self.verticalLayout_7.addWidget(self.label_6)

        self.line = QFrame(self.widget_4)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: white;\n"
"")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.tableWidget = QTableWidget(self.widget_4)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 14):
            self.tableWidget.setRowCount(14)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem15)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    background-color: #1F1F1F;\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"}\n"
"\n"
"QTableWidget::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    text-align: center; /* Set text alignment to center */\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: white;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(50, 50, 50);\n"
"    text-align: center; /* Set text alignment to center */\n"
"    padding: 2px 4px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center; /* Set text alignment to center */\n"
"}\n"
"\n"
"QTableView::item:alternate {\n"
"    background-color: #272727; \n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #3B3B3B;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #606060;\n"
" "
                        "   min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:hover {\n"
"    opacity: 0.7;\n"
"}\n"
"")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.widget_4)


        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.dashboard_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(200, 0))
        self.widget_5.setMaximumSize(QSize(210, 16777215))
        self.widget_5.setStyleSheet(u"background-color: #3B3B3B;\n"
"border-radius:10px;\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_40 = QWidget(self.widget_5)
        self.widget_40.setObjectName(u"widget_40")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_40.sizePolicy().hasHeightForWidth())
        self.widget_40.setSizePolicy(sizePolicy2)
        self.verticalLayout_8 = QVBoxLayout(self.widget_40)
        self.verticalLayout_8.setSpacing(12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.widget_40)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(121, 31))
        self.label_4.setMaximumSize(QSize(121, 31))
        self.label_4.setFont(font6)

        self.verticalLayout_8.addWidget(self.label_4)

        self.bestSell1 = QWidget(self.widget_40)
        self.bestSell1.setObjectName(u"bestSell1")
        self.bestSell1.setMinimumSize(QSize(0, 45))
        self.bestSell1.setMaximumSize(QSize(16777215, 45))
        self.bestSell1.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.bestSell1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.widget_20 = QWidget(self.bestSell1)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(51, 0))
        self.widget_20.setStyleSheet(u"background-color: rgb(255, 140, 24);")
        self.verticalLayout_27 = QVBoxLayout(self.widget_20)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.toolButton = QToolButton(self.widget_20)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setIcon(icon10)
        self.toolButton.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.toolButton)


        self.horizontalLayout_5.addWidget(self.widget_20, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addWidget(self.bestSell1)

        self.widget_7 = QWidget(self.widget_40)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 45))
        self.widget_7.setMaximumSize(QSize(16777215, 45))
        self.widget_7.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, -1, 0)
        self.widget_21 = QWidget(self.widget_7)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(51, 0))
        self.widget_21.setStyleSheet(u"background-color: rgb(255, 140, 24);")
        self.gridLayout_10 = QGridLayout(self.widget_21)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.toolButton_3 = QToolButton(self.widget_21)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setIcon(icon10)
        self.toolButton_3.setIconSize(QSize(30, 30))

        self.gridLayout_10.addWidget(self.toolButton_3, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.widget_21, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_40)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 45))
        self.widget_8.setMaximumSize(QSize(16777215, 45))
        self.widget_8.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, -1, 0)
        self.widget_22 = QWidget(self.widget_8)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMinimumSize(QSize(51, 0))
        self.widget_22.setStyleSheet(u"background-color: rgb(255, 140, 24);")
        self.gridLayout_11 = QGridLayout(self.widget_22)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.toolButton_4 = QToolButton(self.widget_22)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setIcon(icon10)
        self.toolButton_4.setIconSize(QSize(30, 30))

        self.gridLayout_11.addWidget(self.toolButton_4, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.widget_22, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_40)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 45))
        self.widget_9.setMaximumSize(QSize(16777215, 45))
        self.widget_9.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, -1, 0)
        self.widget_23 = QWidget(self.widget_9)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(51, 0))
        self.widget_23.setStyleSheet(u"background-color: rgb(255, 140, 24);")
        self.gridLayout_21 = QGridLayout(self.widget_23)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.toolButton_5 = QToolButton(self.widget_23)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setIcon(icon10)
        self.toolButton_5.setIconSize(QSize(30, 30))

        self.gridLayout_21.addWidget(self.toolButton_5, 0, 0, 1, 1)


        self.horizontalLayout_13.addWidget(self.widget_23, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_40)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 45))
        self.widget_10.setMaximumSize(QSize(16777215, 45))
        self.widget_10.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, -1, 0)
        self.widget_24 = QWidget(self.widget_10)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(51, 0))
        self.widget_24.setStyleSheet(u"background-color: rgb(255, 140, 24);")
        self.gridLayout_22 = QGridLayout(self.widget_24)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.toolButton_6 = QToolButton(self.widget_24)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setIcon(icon10)
        self.toolButton_6.setIconSize(QSize(30, 30))

        self.gridLayout_22.addWidget(self.toolButton_6, 0, 0, 1, 1)


        self.horizontalLayout_16.addWidget(self.widget_24, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_40)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 45))
        self.widget_11.setMaximumSize(QSize(16777215, 45))
        self.widget_11.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, -1, 0)
        self.widget_25 = QWidget(self.widget_11)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(51, 0))
        self.widget_25.setStyleSheet(u"background-color: rgb(255, 140, 24);")
        self.gridLayout_23 = QGridLayout(self.widget_25)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.toolButton_7 = QToolButton(self.widget_25)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setIcon(icon10)
        self.toolButton_7.setIconSize(QSize(30, 30))

        self.gridLayout_23.addWidget(self.toolButton_7, 0, 0, 1, 1)


        self.horizontalLayout_17.addWidget(self.widget_25, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_40)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 45))
        self.widget_12.setMaximumSize(QSize(16777215, 45))
        self.widget_12.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, -1, 0)
        self.widget_26 = QWidget(self.widget_12)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(51, 0))
        self.widget_26.setStyleSheet(u"background-color: rgb(255, 140, 24);")
        self.gridLayout_24 = QGridLayout(self.widget_26)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.toolButton_8 = QToolButton(self.widget_26)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setIcon(icon10)
        self.toolButton_8.setIconSize(QSize(30, 30))

        self.gridLayout_24.addWidget(self.toolButton_8, 0, 0, 1, 1)


        self.horizontalLayout_18.addWidget(self.widget_26, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_40)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 45))
        self.widget_13.setMaximumSize(QSize(16777215, 45))
        self.widget_13.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, -1, 0)
        self.widget_71 = QWidget(self.widget_13)
        self.widget_71.setObjectName(u"widget_71")
        self.widget_71.setMinimumSize(QSize(51, 0))
        self.widget_71.setStyleSheet(u"background-color: rgb(255, 140, 24);")
        self.gridLayout_25 = QGridLayout(self.widget_71)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.toolButton_9 = QToolButton(self.widget_71)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setIcon(icon10)
        self.toolButton_9.setIconSize(QSize(30, 30))

        self.gridLayout_25.addWidget(self.toolButton_9, 0, 0, 1, 1)


        self.horizontalLayout_19.addWidget(self.widget_71, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_40)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 45))
        self.widget_14.setMaximumSize(QSize(16777215, 45))
        self.widget_14.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, -1, 0)
        self.widget_72 = QWidget(self.widget_14)
        self.widget_72.setObjectName(u"widget_72")
        self.widget_72.setMinimumSize(QSize(51, 0))
        self.widget_72.setStyleSheet(u"background-color: rgb(255, 140, 24);")
        self.gridLayout_26 = QGridLayout(self.widget_72)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.toolButton_10 = QToolButton(self.widget_72)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setIcon(icon10)
        self.toolButton_10.setIconSize(QSize(30, 30))

        self.gridLayout_26.addWidget(self.toolButton_10, 0, 0, 1, 1)


        self.horizontalLayout_20.addWidget(self.widget_72, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_8.addWidget(self.widget_14)


        self.verticalLayout_12.addWidget(self.widget_40, 0, Qt.AlignmentFlag.AlignTop)


        self.gridLayout_2.addWidget(self.widget_5, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.add_product = QWidget()
        self.add_product.setObjectName(u"add_product")
        self.gridLayout_18 = QGridLayout(self.add_product)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.widget_31 = QWidget(self.add_product)
        self.widget_31.setObjectName(u"widget_31")
        self.gridLayout = QGridLayout(self.widget_31)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 30)
        self.widget_32 = QWidget(self.widget_31)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 6)
        self.search_frame = QWidget(self.widget_32)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(200, 0))
        self.search_frame.setStyleSheet(u"#search_frame{\n"
"\n"
"	border-radius: 15px;\n"
"	background-color:#252525;\n"
"}\n"
"#search_frame QPushButton{\n"
"	\n"
"	padding: 5px 5px;\n"
"	border-radius:5px;\n"
"\n"
"	\n"
"}\n"
"#search_frame QLineEdit{\n"
"	border: none;\n"
"	color: white;\n"
"\n"
"}\n"
"\n"
"#seach_frame QPushButton::pressed {\n"
"\n"
"	padding-left:10px;\n"
"\n"
"}\n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.search_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, -1)
        self.pushButton_14 = QPushButton(self.search_frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(25, 25))
        self.pushButton_14.setMaximumSize(QSize(25, 25))
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.pushButton_14.setFont(font7)
        self.pushButton_14.setStyleSheet(u"background-color: none;\n"
"border-radius:15px;\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/iCons/icons/icons8-search-26.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon11)

        self.horizontalLayout_10.addWidget(self.pushButton_14)

        self.lineEdit_3 = QLineEdit(self.search_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(37, 37, 37);")

        self.horizontalLayout_10.addWidget(self.lineEdit_3)


        self.verticalLayout_14.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_6.addWidget(self.search_frame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer = QSpacerItem(418, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.add_prod_button = QPushButton(self.widget_32)
        self.add_prod_button.setObjectName(u"add_prod_button")
        self.add_prod_button.setMinimumSize(QSize(150, 30))
        self.add_prod_button.setMaximumSize(QSize(150, 25))
        self.add_prod_button.setFont(font7)
        self.add_prod_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_6.addWidget(self.add_prod_button)


        self.gridLayout.addWidget(self.widget_32, 0, 0, 1, 1)

        self.widget_35 = QWidget(self.widget_31)
        self.widget_35.setObjectName(u"widget_35")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_35.sizePolicy().hasHeightForWidth())
        self.widget_35.setSizePolicy(sizePolicy3)
        self.widget_35.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius:5px;\n"
"")
        self.verticalLayout_13 = QVBoxLayout(self.widget_35)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.product_table = QTableWidget(self.widget_35)
        if (self.product_table.columnCount() < 5):
            self.product_table.setColumnCount(5)
        font8 = QFont()
        font8.setFamilies([u"Inter SemiBold"])
        font8.setPointSize(10)
        font8.setBold(True)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font8);
        self.product_table.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font8);
        self.product_table.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font8);
        self.product_table.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font8);
        self.product_table.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font8);
        self.product_table.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        if (self.product_table.rowCount() < 16):
            self.product_table.setRowCount(16)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(7, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(8, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(9, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(10, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(11, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(12, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(13, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(14, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.product_table.setVerticalHeaderItem(15, __qtablewidgetitem36)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setForeground(brush);
        self.product_table.setItem(0, 0, __qtablewidgetitem37)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem38.setForeground(brush1);
        self.product_table.setItem(0, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.product_table.setItem(0, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.product_table.setItem(0, 3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.product_table.setItem(0, 4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.product_table.setItem(1, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.product_table.setItem(1, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.product_table.setItem(1, 2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.product_table.setItem(1, 3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.product_table.setItem(1, 4, __qtablewidgetitem46)
        self.product_table.setObjectName(u"product_table")
        sizePolicy1.setHeightForWidth(self.product_table.sizePolicy().hasHeightForWidth())
        self.product_table.setSizePolicy(sizePolicy1)
        font9 = QFont()
        font9.setFamilies([u"Inter Medium"])
        font9.setPointSize(9)
        font9.setBold(False)
        self.product_table.setFont(font9)
        self.product_table.setStyleSheet(u"QTableWidget {\n"
"    background-color: #1F1F1F;\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgb(50, 50, 50);\n"
" 	color: white;\n"
"\n"
"}\n"
"\n"
"QTableWidget::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    text-align: center; /* Set text alignment to center */\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: white;\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(70,70,70);\n"
"	\n"
"\n"
"    text-align: center; /* Set text alignment to center */\n"
"    padding: 2px 4px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center; /* Set text alignment to center */\n"
"}\n"
"\n"
"QTableView::item:alternate {\n"
"    background-color: #272727; \n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #454545; /* Background color when item is selected */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    backgr"
                        "ound: #3B3B3B;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #606060;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:hover {\n"
"    opacity: 0.7;\n"
"}")
        self.product_table.setDragEnabled(False)
        self.product_table.setAlternatingRowColors(True)
        self.product_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.product_table.setGridStyle(Qt.PenStyle.NoPen)
        self.product_table.setSortingEnabled(True)
        self.product_table.setWordWrap(True)
        self.product_table.horizontalHeader().setCascadingSectionResizes(True)
        self.product_table.horizontalHeader().setMinimumSectionSize(100)
        self.product_table.horizontalHeader().setDefaultSectionSize(150)
        self.product_table.horizontalHeader().setStretchLastSection(True)
        self.product_table.verticalHeader().setVisible(False)
        self.product_table.verticalHeader().setCascadingSectionResizes(False)
        self.product_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_13.addWidget(self.product_table)


        self.gridLayout.addWidget(self.widget_35, 1, 0, 1, 1)


        self.gridLayout_18.addWidget(self.widget_31, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.add_product)
        self.update_product = QWidget()
        self.update_product.setObjectName(u"update_product")
        self.gridLayout_14 = QGridLayout(self.update_product)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.widget_36 = QWidget(self.update_product)
        self.widget_36.setObjectName(u"widget_36")
        self.gridLayout_9 = QGridLayout(self.widget_36)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, -1, -1, 30)
        self.widget_38 = QWidget(self.widget_36)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 6)
        self.search_frame_2 = QWidget(self.widget_38)
        self.search_frame_2.setObjectName(u"search_frame_2")
        self.search_frame_2.setMinimumSize(QSize(200, 0))
        self.search_frame_2.setStyleSheet(u"#search_frame_2{\n"
"\n"
"	border-radius: 15px;\n"
"	background-color:#252525;\n"
"}\n"
"#search_frame_2 QPushButton{\n"
"	\n"
"	padding: 5px 5px;\n"
"	border-radius:5px;\n"
"\n"
"	\n"
"}\n"
"#search_frame_2 QLineEdit{\n"
"	border: none;\n"
"	color: white;\n"
"\n"
"}\n"
"\n"
"#seach_frame_2 QPushButton::pressed {\n"
"\n"
"	padding-left:10px;\n"
"\n"
"}\n"
"")
        self.verticalLayout_15 = QVBoxLayout(self.search_frame_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(2, 2, 2, -1)
        self.pushButton_16 = QPushButton(self.search_frame_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(25, 25))
        self.pushButton_16.setMaximumSize(QSize(25, 25))
        self.pushButton_16.setFont(font7)
        self.pushButton_16.setStyleSheet(u"background-color: none;\n"
"border-radius:15px;\n"
"")
        self.pushButton_16.setIcon(icon11)

        self.horizontalLayout_12.addWidget(self.pushButton_16)

        self.lineEdit_4 = QLineEdit(self.search_frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(37, 37, 37);")

        self.horizontalLayout_12.addWidget(self.lineEdit_4)


        self.verticalLayout_15.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_11.addWidget(self.search_frame_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_4 = QSpacerItem(418, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.update_prod_button = QPushButton(self.widget_38)
        self.update_prod_button.setObjectName(u"update_prod_button")
        self.update_prod_button.setMinimumSize(QSize(150, 30))
        self.update_prod_button.setMaximumSize(QSize(150, 25))
        self.update_prod_button.setFont(font7)
        self.update_prod_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_11.addWidget(self.update_prod_button)


        self.gridLayout_9.addWidget(self.widget_38, 0, 0, 1, 1)

        self.widget_39 = QWidget(self.widget_36)
        self.widget_39.setObjectName(u"widget_39")
        sizePolicy3.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy3)
        self.widget_39.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius:5px;\n"
"")
        self.gridLayout_27 = QGridLayout(self.widget_39)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.product_table_2 = QTableWidget(self.widget_39)
        if (self.product_table_2.columnCount() < 5):
            self.product_table_2.setColumnCount(5)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setFont(font8);
        self.product_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font8);
        self.product_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setFont(font8);
        self.product_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setFont(font8);
        self.product_table_2.setHorizontalHeaderItem(3, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setFont(font8);
        self.product_table_2.setHorizontalHeaderItem(4, __qtablewidgetitem51)
        if (self.product_table_2.rowCount() < 16):
            self.product_table_2.setRowCount(16)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(4, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(5, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(6, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(7, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(8, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(9, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(10, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(11, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(12, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(13, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(14, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.product_table_2.setVerticalHeaderItem(15, __qtablewidgetitem67)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.NoBrush)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setForeground(brush2);
        self.product_table_2.setItem(0, 0, __qtablewidgetitem68)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.NoBrush)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem69.setForeground(brush3);
        self.product_table_2.setItem(0, 1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.product_table_2.setItem(0, 2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.product_table_2.setItem(0, 3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.product_table_2.setItem(0, 4, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.product_table_2.setItem(1, 0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.product_table_2.setItem(1, 1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.product_table_2.setItem(1, 2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.product_table_2.setItem(1, 3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.product_table_2.setItem(1, 4, __qtablewidgetitem77)
        self.product_table_2.setObjectName(u"product_table_2")
        sizePolicy1.setHeightForWidth(self.product_table_2.sizePolicy().hasHeightForWidth())
        self.product_table_2.setSizePolicy(sizePolicy1)
        self.product_table_2.setFont(font9)
        self.product_table_2.setStyleSheet(u"QTableWidget {\n"
"    background-color: #1F1F1F;\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgb(50, 50, 50);\n"
" 	color: white;\n"
"\n"
"}\n"
"\n"
"QTableWidget::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    text-align: center; /* Set text alignment to center */\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: white;\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(70,70,70);\n"
"	\n"
"\n"
"    text-align: center; /* Set text alignment to center */\n"
"    padding: 2px 4px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center; /* Set text alignment to center */\n"
"}\n"
"\n"
"QTableView::item:alternate {\n"
"    background-color: #272727; \n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #454545; /* Background color when item is selected */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    backgr"
                        "ound: #3B3B3B;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #606060;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:hover {\n"
"    opacity: 0.7;\n"
"}")
        self.product_table_2.setDragEnabled(False)
        self.product_table_2.setAlternatingRowColors(True)
        self.product_table_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.product_table_2.setGridStyle(Qt.PenStyle.NoPen)
        self.product_table_2.setSortingEnabled(True)
        self.product_table_2.setWordWrap(True)
        self.product_table_2.horizontalHeader().setCascadingSectionResizes(True)
        self.product_table_2.horizontalHeader().setMinimumSectionSize(100)
        self.product_table_2.horizontalHeader().setDefaultSectionSize(150)
        self.product_table_2.horizontalHeader().setStretchLastSection(True)
        self.product_table_2.verticalHeader().setVisible(False)
        self.product_table_2.verticalHeader().setCascadingSectionResizes(False)
        self.product_table_2.verticalHeader().setStretchLastSection(False)

        self.gridLayout_27.addWidget(self.product_table_2, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_39, 1, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_36, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.update_product)
        self.delete_product = QWidget()
        self.delete_product.setObjectName(u"delete_product")
        self.gridLayout_16 = QGridLayout(self.delete_product)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.widget_42 = QWidget(self.delete_product)
        self.widget_42.setObjectName(u"widget_42")
        self.gridLayout_15 = QGridLayout(self.widget_42)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(-1, -1, -1, 30)
        self.widget_43 = QWidget(self.widget_42)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 6)
        self.search_frame_3 = QWidget(self.widget_43)
        self.search_frame_3.setObjectName(u"search_frame_3")
        self.search_frame_3.setMinimumSize(QSize(200, 0))
        self.search_frame_3.setStyleSheet(u"#search_frame_3{\n"
"\n"
"	border-radius: 15px;\n"
"	background-color:#252525;\n"
"}\n"
"#search_frame_3 QPushButton{\n"
"	\n"
"	padding: 5px 5px;\n"
"	border-radius:5px;\n"
"\n"
"	\n"
"}\n"
"#search_frame_3 QLineEdit{\n"
"	border: none;\n"
"	color: white;\n"
"\n"
"}\n"
"\n"
"#seach_frame_3 QPushButton::pressed {\n"
"\n"
"	padding-left:10px;\n"
"\n"
"}\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.search_frame_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(2, 2, 2, -1)
        self.pushButton_17 = QPushButton(self.search_frame_3)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(25, 25))
        self.pushButton_17.setMaximumSize(QSize(25, 25))
        self.pushButton_17.setFont(font7)
        self.pushButton_17.setStyleSheet(u"background-color: none;\n"
"border-radius:15px;\n"
"")
        self.pushButton_17.setIcon(icon11)

        self.horizontalLayout_15.addWidget(self.pushButton_17)

        self.lineEdit_5 = QLineEdit(self.search_frame_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(37, 37, 37);")

        self.horizontalLayout_15.addWidget(self.lineEdit_5)


        self.verticalLayout_17.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_14.addWidget(self.search_frame_3, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_5 = QSpacerItem(418, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)

        self.update_prod_button_2 = QPushButton(self.widget_43)
        self.update_prod_button_2.setObjectName(u"update_prod_button_2")
        self.update_prod_button_2.setMinimumSize(QSize(150, 30))
        self.update_prod_button_2.setMaximumSize(QSize(150, 25))
        self.update_prod_button_2.setFont(font7)
        self.update_prod_button_2.setStyleSheet(u"QPushButton {\n"
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
        self.update_prod_button_2.setCheckable(True)
        self.update_prod_button_2.setAutoExclusive(True)

        self.horizontalLayout_14.addWidget(self.update_prod_button_2)


        self.gridLayout_15.addWidget(self.widget_43, 0, 0, 1, 1)

        self.widget_45 = QWidget(self.widget_42)
        self.widget_45.setObjectName(u"widget_45")
        sizePolicy3.setHeightForWidth(self.widget_45.sizePolicy().hasHeightForWidth())
        self.widget_45.setSizePolicy(sizePolicy3)
        self.widget_45.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius:5px;\n"
"")
        self.gridLayout_28 = QGridLayout(self.widget_45)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.product_table_3 = QTableWidget(self.widget_45)
        if (self.product_table_3.columnCount() < 5):
            self.product_table_3.setColumnCount(5)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setFont(font8);
        self.product_table_3.setHorizontalHeaderItem(0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setFont(font8);
        self.product_table_3.setHorizontalHeaderItem(1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setFont(font8);
        self.product_table_3.setHorizontalHeaderItem(2, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setFont(font8);
        self.product_table_3.setHorizontalHeaderItem(3, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setFont(font8);
        self.product_table_3.setHorizontalHeaderItem(4, __qtablewidgetitem82)
        if (self.product_table_3.rowCount() < 16):
            self.product_table_3.setRowCount(16)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(1, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(2, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(3, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(4, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(5, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(6, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(7, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(8, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(9, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(10, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(11, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(12, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(13, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(14, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.product_table_3.setVerticalHeaderItem(15, __qtablewidgetitem98)
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.NoBrush)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setForeground(brush4);
        self.product_table_3.setItem(0, 0, __qtablewidgetitem99)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.NoBrush)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem100.setForeground(brush5);
        self.product_table_3.setItem(0, 1, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.product_table_3.setItem(0, 2, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.product_table_3.setItem(0, 3, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.product_table_3.setItem(0, 4, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.product_table_3.setItem(1, 0, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.product_table_3.setItem(1, 1, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.product_table_3.setItem(1, 2, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.product_table_3.setItem(1, 3, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.product_table_3.setItem(1, 4, __qtablewidgetitem108)
        self.product_table_3.setObjectName(u"product_table_3")
        sizePolicy1.setHeightForWidth(self.product_table_3.sizePolicy().hasHeightForWidth())
        self.product_table_3.setSizePolicy(sizePolicy1)
        self.product_table_3.setFont(font9)
        self.product_table_3.setStyleSheet(u"QTableWidget {\n"
"    background-color: #1F1F1F;\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgb(50, 50, 50);\n"
" 	color: white;\n"
"\n"
"}\n"
"\n"
"QTableWidget::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    text-align: center; /* Set text alignment to center */\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: white;\n"
"    border: none;\n"
"    border-bottom: 2px solid rgb(70,70,70);\n"
"	\n"
"\n"
"    text-align: center; /* Set text alignment to center */\n"
"    padding: 2px 4px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center; /* Set text alignment to center */\n"
"}\n"
"\n"
"QTableView::item:alternate {\n"
"    background-color: #272727; \n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #454545; /* Background color when item is selected */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    backgr"
                        "ound: #3B3B3B;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #606060;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:hover {\n"
"    opacity: 0.7;\n"
"}")
        self.product_table_3.setDragEnabled(False)
        self.product_table_3.setAlternatingRowColors(True)
        self.product_table_3.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.product_table_3.setGridStyle(Qt.PenStyle.NoPen)
        self.product_table_3.setSortingEnabled(True)
        self.product_table_3.setWordWrap(True)
        self.product_table_3.horizontalHeader().setCascadingSectionResizes(True)
        self.product_table_3.horizontalHeader().setMinimumSectionSize(100)
        self.product_table_3.horizontalHeader().setDefaultSectionSize(150)
        self.product_table_3.horizontalHeader().setStretchLastSection(True)
        self.product_table_3.verticalHeader().setVisible(False)
        self.product_table_3.verticalHeader().setCascadingSectionResizes(False)
        self.product_table_3.verticalHeader().setStretchLastSection(False)

        self.gridLayout_28.addWidget(self.product_table_3, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget_45, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_42, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.delete_product)
        self.sales_report = QWidget()
        self.sales_report.setObjectName(u"sales_report")
        self.gridLayout_3 = QGridLayout(self.sales_report)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 10, 30, 10)
        self.widget_27 = QWidget(self.sales_report)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(770, 131))
        self.widget_27.setMaximumSize(QSize(16777215, 131))
        self.widget_27.setStyleSheet(u"background-color: #1F1F1F;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.widget_27)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_29 = QWidget(self.widget_27)
        self.widget_29.setObjectName(u"widget_29")
        self.verticalLayout_11 = QVBoxLayout(self.widget_29)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_10 = QLabel(self.widget_29)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(50, 0))
        self.label_10.setMaximumSize(QSize(140, 16777215))
        font10 = QFont()
        font10.setFamilies([u"Poppins SemiBold"])
        font10.setPointSize(11)
        font10.setBold(True)
        self.label_10.setFont(font10)

        self.horizontalLayout_27.addWidget(self.label_10)

        self.label_11 = QLabel(self.widget_29)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font10)

        self.horizontalLayout_27.addWidget(self.label_11)


        self.verticalLayout_11.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_18 = QLabel(self.widget_29)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(130, 0))
        self.label_18.setMaximumSize(QSize(130, 16777215))
        self.label_18.setFont(font10)

        self.horizontalLayout_28.addWidget(self.label_18)

        self.label_21 = QLabel(self.widget_29)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font10)

        self.horizontalLayout_28.addWidget(self.label_21)


        self.verticalLayout_11.addLayout(self.horizontalLayout_28)


        self.verticalLayout_10.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_27)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_6 = QPushButton(self.widget_30)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 31))
        self.pushButton_6.setMaximumSize(QSize(16777215, 31))
        self.pushButton_6.setFont(font7)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
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
"QPushButton::checked {\n"
"    background-color: #B7B7B7;\n"
"    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.5) inset;\n"
"	color:black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFA54E; \n"
"}")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget_30)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 31))
        self.pushButton_7.setMaximumSize(QSize(16777215, 31))
        self.pushButton_7.setFont(font7)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
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
"QPushButton::checked {\n"
"    background-color: #B7B7B7;\n"
"    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.5) inset;\n"
"	color:black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFA54E; \n"
"}")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.widget_30)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 31))
        self.pushButton_8.setMaximumSize(QSize(16777215, 31))
        self.pushButton_8.setFont(font7)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
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
"QPushButton::checked {\n"
"    background-color: #B7B7B7;\n"
"    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.5) inset;\n"
"	color:black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFA54E; \n"
"}")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.widget_30)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 31))
        self.pushButton_9.setMaximumSize(QSize(16777215, 31))
        self.pushButton_9.setFont(font7)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
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
"QPushButton::checked {\n"
"    background-color: #B7B7B7;\n"
"    box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.5) inset;\n"
"	color:black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FFA54E; \n"
"}")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pushButton_9)


        self.verticalLayout_10.addWidget(self.widget_30)


        self.verticalLayout_9.addWidget(self.widget_27, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_28 = QWidget(self.sales_report)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy)
        self.widget_28.setMinimumSize(QSize(701, 315))
        self.widget_28.setMaximumSize(QSize(16777215, 16777215))
        self.widget_28.setStyleSheet(u"QWidget{\n"
"	background-color: #1F1F1F;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.gridLayout_4 = QGridLayout(self.widget_28)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(9, -1, -1, -1)
        self.tableWidget_2 = QTableWidget(self.widget_28)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        font11 = QFont()
        font11.setFamilies([u"Poppins SemiBold"])
        font11.setPointSize(10)
        font11.setBold(False)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setFont(font11);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setFont(font11);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem110)
        if (self.tableWidget_2.rowCount() < 18):
            self.tableWidget_2.setRowCount(18)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        __qtablewidgetitem129.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_2.setItem(6, 1, __qtablewidgetitem129)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy1.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy1)
        self.tableWidget_2.setStyleSheet(u"QTableWidget {\n"
"    background-color: #1F1F1F;\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"}\n"
"\n"
"QTableWidget::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    text-align: center; \n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: white;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgb(50, 50, 50);\n"
"    text-align: center; \n"
"    padding: 2px 4px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    color: white;\n"
"    padding: 5px;\n"
"    text-align: center; \n"
"}\n"
"\n"
"QTableView::item:alternate {\n"
"    background-color: #272727; \n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #3B3B3B;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #606060;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QSc"
                        "rollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:hover {\n"
"    opacity: 0.7;\n"
"}\n"
"")
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.gridLayout_4.addWidget(self.tableWidget_2, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_28)


        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.sales_report)
        self.Manage = QWidget()
        self.Manage.setObjectName(u"Manage")
        self.gridLayout_5 = QGridLayout(self.Manage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_37 = QWidget(self.Manage)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.verticalLayout_39 = QVBoxLayout(self.widget_37)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(70, 0, 90, 30)
        self.widget_66 = QWidget(self.widget_37)
        self.widget_66.setObjectName(u"widget_66")
        self.widget_66.setMinimumSize(QSize(0, 30))
        self.widget_66.setMaximumSize(QSize(16777215, 30))
        self.widget_66.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
"border-radius:10px;\n"
"")
        self.label_25 = QLabel(self.widget_66)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 0, 109, 27))
        self.label_25.setFont(font10)
        self.label_25.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.verticalLayout_39.addWidget(self.widget_66)

        self.widget_76 = QWidget(self.widget_37)
        self.widget_76.setObjectName(u"widget_76")
        self.widget_76.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius:10px;\n"
"")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_76)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.widget_77 = QWidget(self.widget_76)
        self.widget_77.setObjectName(u"widget_77")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_77.sizePolicy().hasHeightForWidth())
        self.widget_77.setSizePolicy(sizePolicy4)
        self.widget_77.setMinimumSize(QSize(180, 0))
        self.widget_77.setMaximumSize(QSize(160, 16777215))
        self.gridLayout_12 = QGridLayout(self.widget_77)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(20, -1, 0, -1)
        self.widget_78 = QWidget(self.widget_77)
        self.widget_78.setObjectName(u"widget_78")
        self.widget_78.setMinimumSize(QSize(0, 125))
        self.widget_78.setMaximumSize(QSize(140, 125))
        self.label_19 = QLabel(self.widget_78)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 0, 120, 120))
        sizePolicy4.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy4)
        self.label_19.setPixmap(QPixmap(u":/iCons/icons/administrator (1).png"))
        self.label_19.setScaledContents(True)

        self.gridLayout_12.addWidget(self.widget_78, 0, 0, 1, 1)


        self.horizontalLayout_21.addWidget(self.widget_77, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_79 = QWidget(self.widget_76)
        self.widget_79.setObjectName(u"widget_79")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_79.sizePolicy().hasHeightForWidth())
        self.widget_79.setSizePolicy(sizePolicy5)
        self.widget_79.setMinimumSize(QSize(270, 0))
        self.widget_79.setToolTipDuration(-1)
        self.verticalLayout_40 = QVBoxLayout(self.widget_79)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 40, -1, 40)
        self.widget_80 = QWidget(self.widget_79)
        self.widget_80.setObjectName(u"widget_80")
        self.widget_80.setMinimumSize(QSize(0, 40))
        self.widget_80.setMaximumSize(QSize(16777215, 15))
        self.verticalLayout_41 = QVBoxLayout(self.widget_80)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_49 = QLabel(self.widget_80)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 13))
        self.label_49.setMaximumSize(QSize(85, 13))
        self.label_49.setFont(font10)
        self.label_49.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_22.addWidget(self.label_49)

        self.label_50 = QLabel(self.widget_80)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 13))
        self.label_50.setFont(font10)
        self.label_50.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_22.addWidget(self.label_50)


        self.verticalLayout_41.addLayout(self.horizontalLayout_22)


        self.verticalLayout_40.addWidget(self.widget_80, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_81 = QWidget(self.widget_79)
        self.widget_81.setObjectName(u"widget_81")
        self.widget_81.setMinimumSize(QSize(0, 40))
        self.widget_81.setMaximumSize(QSize(16777215, 40))
        self.verticalLayout_42 = QVBoxLayout(self.widget_81)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(7)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_51 = QLabel(self.widget_81)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 13))
        self.label_51.setMaximumSize(QSize(85, 13))
        self.label_51.setFont(font10)
        self.label_51.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_23.addWidget(self.label_51)

        self.label_52 = QLabel(self.widget_81)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 13))
        self.label_52.setFont(font10)
        self.label_52.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_23.addWidget(self.label_52)


        self.verticalLayout_42.addLayout(self.horizontalLayout_23)


        self.verticalLayout_40.addWidget(self.widget_81, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_21.addWidget(self.widget_79, 0, Qt.AlignmentFlag.AlignVCenter)

        self.widget_82 = QWidget(self.widget_76)
        self.widget_82.setObjectName(u"widget_82")
        sizePolicy4.setHeightForWidth(self.widget_82.sizePolicy().hasHeightForWidth())
        self.widget_82.setSizePolicy(sizePolicy4)
        self.verticalLayout_43 = QVBoxLayout(self.widget_82)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(-1, -1, 25, -1)
        self.widget_83 = QWidget(self.widget_82)
        self.widget_83.setObjectName(u"widget_83")
        self.widget_83.setMinimumSize(QSize(150, 31))
        self.verticalLayout_44 = QVBoxLayout(self.widget_83)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.pushButton_21 = QPushButton(self.widget_83)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(0, 31))
        self.pushButton_21.setMaximumSize(QSize(16777215, 31))
        self.pushButton_21.setFont(font7)
        self.pushButton_21.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setAutoExclusive(True)

        self.verticalLayout_44.addWidget(self.pushButton_21)


        self.verticalLayout_43.addWidget(self.widget_83, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_21.addWidget(self.widget_82)


        self.verticalLayout_39.addWidget(self.widget_76)


        self.gridLayout_5.addWidget(self.widget_37, 0, 0, 1, 1)

        self.widget_84 = QWidget(self.Manage)
        self.widget_84.setObjectName(u"widget_84")
        self.widget_84.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.verticalLayout_45 = QVBoxLayout(self.widget_84)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(70, 0, 90, 30)
        self.widget_85 = QWidget(self.widget_84)
        self.widget_85.setObjectName(u"widget_85")
        self.widget_85.setMinimumSize(QSize(0, 30))
        self.widget_85.setMaximumSize(QSize(16777215, 30))
        self.widget_85.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
"border-radius:10px;\n"
"")
        self.label_26 = QLabel(self.widget_85)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 0, 109, 27))
        self.label_26.setFont(font10)
        self.label_26.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.verticalLayout_45.addWidget(self.widget_85)

        self.widget_86 = QWidget(self.widget_84)
        self.widget_86.setObjectName(u"widget_86")
        self.widget_86.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius:10px;\n"
"")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_86)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.widget_87 = QWidget(self.widget_86)
        self.widget_87.setObjectName(u"widget_87")
        sizePolicy4.setHeightForWidth(self.widget_87.sizePolicy().hasHeightForWidth())
        self.widget_87.setSizePolicy(sizePolicy4)
        self.widget_87.setMinimumSize(QSize(180, 0))
        self.widget_87.setMaximumSize(QSize(160, 16777215))
        self.gridLayout_13 = QGridLayout(self.widget_87)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(20, -1, 0, -1)
        self.widget_88 = QWidget(self.widget_87)
        self.widget_88.setObjectName(u"widget_88")
        self.widget_88.setMinimumSize(QSize(0, 125))
        self.widget_88.setMaximumSize(QSize(140, 125))
        self.label_20 = QLabel(self.widget_88)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 0, 120, 120))
        sizePolicy4.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy4)
        self.label_20.setPixmap(QPixmap(u":/iCons/icons/administrator (1).png"))
        self.label_20.setScaledContents(True)

        self.gridLayout_13.addWidget(self.widget_88, 0, 0, 1, 1)


        self.horizontalLayout_24.addWidget(self.widget_87, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_89 = QWidget(self.widget_86)
        self.widget_89.setObjectName(u"widget_89")
        sizePolicy5.setHeightForWidth(self.widget_89.sizePolicy().hasHeightForWidth())
        self.widget_89.setSizePolicy(sizePolicy5)
        self.widget_89.setMinimumSize(QSize(270, 0))
        self.widget_89.setToolTipDuration(-1)
        self.verticalLayout_46 = QVBoxLayout(self.widget_89)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 40, -1, 40)
        self.widget_90 = QWidget(self.widget_89)
        self.widget_90.setObjectName(u"widget_90")
        self.widget_90.setMinimumSize(QSize(0, 40))
        self.widget_90.setMaximumSize(QSize(16777215, 15))
        self.verticalLayout_47 = QVBoxLayout(self.widget_90)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_53 = QLabel(self.widget_90)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(0, 13))
        self.label_53.setMaximumSize(QSize(85, 13))
        self.label_53.setFont(font10)
        self.label_53.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_25.addWidget(self.label_53)

        self.label_54 = QLabel(self.widget_90)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(16777215, 13))
        self.label_54.setFont(font10)
        self.label_54.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_25.addWidget(self.label_54)


        self.verticalLayout_47.addLayout(self.horizontalLayout_25)


        self.verticalLayout_46.addWidget(self.widget_90, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget_91 = QWidget(self.widget_89)
        self.widget_91.setObjectName(u"widget_91")
        self.widget_91.setMinimumSize(QSize(0, 40))
        self.widget_91.setMaximumSize(QSize(16777215, 40))
        self.verticalLayout_48 = QVBoxLayout(self.widget_91)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(7)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_55 = QLabel(self.widget_91)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(0, 13))
        self.label_55.setMaximumSize(QSize(85, 13))
        self.label_55.setFont(font10)
        self.label_55.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_26.addWidget(self.label_55)

        self.label_56 = QLabel(self.widget_91)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(16777215, 13))
        self.label_56.setFont(font10)
        self.label_56.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_26.addWidget(self.label_56)


        self.verticalLayout_48.addLayout(self.horizontalLayout_26)


        self.verticalLayout_46.addWidget(self.widget_91, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_24.addWidget(self.widget_89, 0, Qt.AlignmentFlag.AlignVCenter)

        self.widget_92 = QWidget(self.widget_86)
        self.widget_92.setObjectName(u"widget_92")
        sizePolicy4.setHeightForWidth(self.widget_92.sizePolicy().hasHeightForWidth())
        self.widget_92.setSizePolicy(sizePolicy4)
        self.verticalLayout_49 = QVBoxLayout(self.widget_92)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(-1, -1, 25, -1)
        self.widget_93 = QWidget(self.widget_92)
        self.widget_93.setObjectName(u"widget_93")
        self.widget_93.setMinimumSize(QSize(150, 31))
        self.verticalLayout_50 = QVBoxLayout(self.widget_93)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.pushButton_22 = QPushButton(self.widget_93)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 31))
        self.pushButton_22.setMaximumSize(QSize(16777215, 31))
        self.pushButton_22.setFont(font7)
        self.pushButton_22.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setAutoExclusive(True)

        self.verticalLayout_50.addWidget(self.pushButton_22)


        self.verticalLayout_49.addWidget(self.widget_93, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_24.addWidget(self.widget_92)


        self.verticalLayout_45.addWidget(self.widget_86)


        self.gridLayout_5.addWidget(self.widget_84, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.Manage)
        self.addProdPage = QWidget()
        self.addProdPage.setObjectName(u"addProdPage")
        self.gridLayout_8 = QGridLayout(self.addProdPage)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_34 = QWidget(self.addProdPage)
        self.widget_34.setObjectName(u"widget_34")
        sizePolicy3.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy3)
        self.widget_34.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.widget_34)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_33 = QWidget(self.widget_34)
        self.widget_33.setObjectName(u"widget_33")
        sizePolicy.setHeightForWidth(self.widget_33.sizePolicy().hasHeightForWidth())
        self.widget_33.setSizePolicy(sizePolicy)
        self.verticalLayout_20 = QVBoxLayout(self.widget_33)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(15, 15, 15, 9)
        self.widget_55 = QWidget(self.widget_33)
        self.widget_55.setObjectName(u"widget_55")
        self.widget_55.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius: 10px;\n"
"")
        self.verticalLayout_21 = QVBoxLayout(self.widget_55)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_56 = QWidget(self.widget_55)
        self.widget_56.setObjectName(u"widget_56")
        self.widget_56.setMinimumSize(QSize(0, 50))
        self.verticalLayout_22 = QVBoxLayout(self.widget_56)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, -1, -1, 0)
        self.label_28 = QLabel(self.widget_56)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        font12 = QFont()
        font12.setFamilies([u"Poppins SemiBold"])
        font12.setPointSize(35)
        font12.setBold(True)
        self.label_28.setFont(font12)
        self.label_28.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.verticalLayout_22.addWidget(self.label_28, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_21.addWidget(self.widget_56, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_57 = QWidget(self.widget_55)
        self.widget_57.setObjectName(u"widget_57")
        sizePolicy.setHeightForWidth(self.widget_57.sizePolicy().hasHeightForWidth())
        self.widget_57.setSizePolicy(sizePolicy)
        self.verticalLayout_23 = QVBoxLayout(self.widget_57)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(50, 0, 50, -1)
        self.widget_58 = QWidget(self.widget_57)
        self.widget_58.setObjectName(u"widget_58")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_42.setSpacing(6)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 0, -1, -1)
        self.widget_94 = QWidget(self.widget_58)
        self.widget_94.setObjectName(u"widget_94")
        self.widget_94.setMinimumSize(QSize(360, 280))
        self.widget_94.setMaximumSize(QSize(360, 16777215))
        self.layoutWidget = QWidget(self.widget_94)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 343, 74))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.layoutWidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_29)

        self.label_30 = QLabel(self.layoutWidget)
        self.label_30.setObjectName(u"label_30")
        font13 = QFont()
        font13.setFamilies([u"Poppins Medium"])
        font13.setPointSize(14)
        font13.setBold(False)
        self.label_30.setFont(font13)
        self.label_30.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_30)

        self.horizontalSpacer_3 = QSpacerItem(171, 72, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_35 = QLabel(self.widget_94)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(10, 100, 145, 27))
        self.label_35.setFont(font3)
        self.label_35.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.lineEdit_2 = QLineEdit(self.widget_94)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(161, 95, 190, 35))
        sizePolicy4.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy4)
        self.lineEdit_2.setMinimumSize(QSize(185, 35))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 30))
        font14 = QFont()
        font14.setFamilies([u"Poppins Medium"])
        font14.setPointSize(11)
        self.lineEdit_2.setFont(font14)
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
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
        self.label_36 = QLabel(self.widget_94)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 177, 134, 27))
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.lineEdit_6 = QLineEdit(self.widget_94)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(150, 173, 200, 35))
        sizePolicy4.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy4)
        self.lineEdit_6.setMinimumSize(QSize(200, 35))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_6.setFont(font14)
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_42.addWidget(self.widget_94, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_95 = QWidget(self.widget_58)
        self.widget_95.setObjectName(u"widget_95")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_95.sizePolicy().hasHeightForWidth())
        self.widget_95.setSizePolicy(sizePolicy6)
        self.widget_95.setMinimumSize(QSize(270, 0))
        self.widget_95.setMaximumSize(QSize(250, 16777215))
        self.layoutWidget1 = QWidget(self.widget_95)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 251, 76))
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.layoutWidget1)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font3)
        self.label_31.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.verticalLayout_24.addWidget(self.label_31)

        self.comboBox = QComboBox(self.layoutWidget1)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font14)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
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

        self.verticalLayout_24.addWidget(self.comboBox)


        self.horizontalLayout_42.addWidget(self.widget_95, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_23.addWidget(self.widget_58)


        self.verticalLayout_21.addWidget(self.widget_57)


        self.verticalLayout_20.addWidget(self.widget_55)


        self.verticalLayout_19.addWidget(self.widget_33)

        self.widget_46 = QWidget(self.widget_34)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_43 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, -1, 12, -1)
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalSpacer_6 = QSpacerItem(538, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.pushButton_31 = QPushButton(self.widget_46)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(132, 31))
        self.pushButton_31.setMaximumSize(QSize(16777215, 31))
        self.pushButton_31.setFont(font7)
        self.pushButton_31.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_31.setCheckable(True)
        self.pushButton_31.setAutoExclusive(True)

        self.gridLayout_17.addWidget(self.pushButton_31, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_3, 1, 1, 1, 1)


        self.horizontalLayout_43.addLayout(self.gridLayout_17)


        self.verticalLayout_19.addWidget(self.widget_46, 0, Qt.AlignmentFlag.AlignBottom)


        self.gridLayout_8.addWidget(self.widget_34, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.addProdPage)
        self.updateProdPage = QWidget()
        self.updateProdPage.setObjectName(u"updateProdPage")
        self.gridLayout_20 = QGridLayout(self.updateProdPage)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.widget_96 = QWidget(self.updateProdPage)
        self.widget_96.setObjectName(u"widget_96")
        sizePolicy3.setHeightForWidth(self.widget_96.sizePolicy().hasHeightForWidth())
        self.widget_96.setSizePolicy(sizePolicy3)
        self.widget_96.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.widget_96)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_97 = QWidget(self.widget_96)
        self.widget_97.setObjectName(u"widget_97")
        sizePolicy.setHeightForWidth(self.widget_97.sizePolicy().hasHeightForWidth())
        self.widget_97.setSizePolicy(sizePolicy)
        self.verticalLayout_26 = QVBoxLayout(self.widget_97)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(15, 15, 15, 9)
        self.widget_98 = QWidget(self.widget_97)
        self.widget_98.setObjectName(u"widget_98")
        self.widget_98.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-radius: 10px;\n"
"")
        self.verticalLayout_51 = QVBoxLayout(self.widget_98)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.widget_99 = QWidget(self.widget_98)
        self.widget_99.setObjectName(u"widget_99")
        self.widget_99.setMinimumSize(QSize(0, 50))
        self.verticalLayout_52 = QVBoxLayout(self.widget_99)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(-1, -1, -1, 0)
        self.label_37 = QLabel(self.widget_99)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setFont(font12)
        self.label_37.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.verticalLayout_52.addWidget(self.label_37, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_51.addWidget(self.widget_99, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_100 = QWidget(self.widget_98)
        self.widget_100.setObjectName(u"widget_100")
        sizePolicy.setHeightForWidth(self.widget_100.sizePolicy().hasHeightForWidth())
        self.widget_100.setSizePolicy(sizePolicy)
        self.verticalLayout_53 = QVBoxLayout(self.widget_100)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(50, 0, 50, -1)
        self.widget_101 = QWidget(self.widget_100)
        self.widget_101.setObjectName(u"widget_101")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_101)
        self.horizontalLayout_44.setSpacing(6)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(-1, 0, -1, -1)
        self.widget_102 = QWidget(self.widget_101)
        self.widget_102.setObjectName(u"widget_102")
        self.widget_102.setMinimumSize(QSize(360, 280))
        self.widget_102.setMaximumSize(QSize(360, 16777215))
        self.layoutWidget_3 = QWidget(self.widget_102)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(9, 9, 343, 74))
        self.horizontalLayout_45 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.layoutWidget_3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_45.addWidget(self.label_38)

        self.label_39 = QLabel(self.layoutWidget_3)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font13)
        self.label_39.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_45.addWidget(self.label_39)

        self.horizontalSpacer_7 = QSpacerItem(171, 72, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_7)

        self.label_40 = QLabel(self.widget_102)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 100, 145, 27))
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.lineEdit_7 = QLineEdit(self.widget_102)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(161, 95, 190, 35))
        sizePolicy4.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy4)
        self.lineEdit_7.setMinimumSize(QSize(185, 35))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_7.setFont(font14)
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
        self.label_57 = QLabel(self.widget_102)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(10, 177, 134, 27))
        self.label_57.setFont(font3)
        self.label_57.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")
        self.lineEdit_8 = QLineEdit(self.widget_102)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(150, 173, 200, 35))
        sizePolicy4.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy4)
        self.lineEdit_8.setMinimumSize(QSize(200, 35))
        self.lineEdit_8.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_8.setFont(font14)
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

        self.horizontalLayout_44.addWidget(self.widget_102, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_103 = QWidget(self.widget_101)
        self.widget_103.setObjectName(u"widget_103")
        sizePolicy6.setHeightForWidth(self.widget_103.sizePolicy().hasHeightForWidth())
        self.widget_103.setSizePolicy(sizePolicy6)
        self.widget_103.setMinimumSize(QSize(270, 0))
        self.widget_103.setMaximumSize(QSize(250, 16777215))
        self.layoutWidget_4 = QWidget(self.widget_103)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 30, 251, 76))
        self.verticalLayout_54 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.layoutWidget_4)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font3)
        self.label_58.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.verticalLayout_54.addWidget(self.label_58)

        self.comboBox_2 = QComboBox(self.layoutWidget_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font14)
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

        self.verticalLayout_54.addWidget(self.comboBox_2)


        self.horizontalLayout_44.addWidget(self.widget_103)


        self.verticalLayout_53.addWidget(self.widget_101)


        self.verticalLayout_51.addWidget(self.widget_100)


        self.verticalLayout_26.addWidget(self.widget_98)


        self.verticalLayout_25.addWidget(self.widget_97)

        self.widget_104 = QWidget(self.widget_96)
        self.widget_104.setObjectName(u"widget_104")
        self.widget_104.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_46 = QHBoxLayout(self.widget_104)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(-1, -1, 12, -1)
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalSpacer_8 = QSpacerItem(538, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.pushButton_32 = QPushButton(self.widget_104)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(132, 31))
        self.pushButton_32.setMaximumSize(QSize(16777215, 31))
        self.pushButton_32.setFont(font7)
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

        self.gridLayout_19.addWidget(self.pushButton_32, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_19.addItem(self.verticalSpacer_4, 1, 1, 1, 1)


        self.horizontalLayout_46.addLayout(self.gridLayout_19)


        self.verticalLayout_25.addWidget(self.widget_104, 0, Qt.AlignmentFlag.AlignBottom)


        self.gridLayout_20.addWidget(self.widget_96, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.updateProdPage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_28 = QVBoxLayout(self.page)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(850, 584))
        self.label_12.setStyleSheet(u"border-radius:10px;")
        self.label_12.setPixmap(QPixmap(u":/mainIcons/minimal-wallpaper-46.jpg"))
        self.label_12.setScaledContents(True)

        self.verticalLayout_28.addWidget(self.label_12)

        self.stackedWidget.addWidget(self.page)
        self.manage_account = QWidget()
        self.manage_account.setObjectName(u"manage_account")
        self.gridLayout_6 = QGridLayout(self.manage_account)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stackedWidget.addWidget(self.manage_account)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout_7.addWidget(self.Main_menu, 0, 2, 1, 1)

        self.icon_only = QWidget(self.centralwidget)
        self.icon_only.setObjectName(u"icon_only")
        self.icon_only.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(49,49,49)\n"
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
        self.label.setPixmap(QPixmap(u":/iCons/CoffitoLogo (40 x 40 px).png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.dashboard1 = QPushButton(self.icon_only)
        self.dashboard1.setObjectName(u"dashboard1")
        self.dashboard1.setIcon(icon)
        self.dashboard1.setIconSize(QSize(25, 25))
        self.dashboard1.setCheckable(True)
        self.dashboard1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard1)

        self.add_item1 = QPushButton(self.icon_only)
        self.add_item1.setObjectName(u"add_item1")
        self.add_item1.setIcon(icon1)
        self.add_item1.setIconSize(QSize(20, 20))
        self.add_item1.setCheckable(True)
        self.add_item1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.add_item1)

        self.update_item1 = QPushButton(self.icon_only)
        self.update_item1.setObjectName(u"update_item1")
        self.update_item1.setIcon(icon2)
        self.update_item1.setIconSize(QSize(20, 20))
        self.update_item1.setCheckable(True)
        self.update_item1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_item1)

        self.delete_item1 = QPushButton(self.icon_only)
        self.delete_item1.setObjectName(u"delete_item1")
        self.delete_item1.setIcon(icon3)
        self.delete_item1.setIconSize(QSize(20, 20))
        self.delete_item1.setCheckable(True)
        self.delete_item1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.delete_item1)

        self.sales_report1 = QPushButton(self.icon_only)
        self.sales_report1.setObjectName(u"sales_report1")
        self.sales_report1.setIcon(icon4)
        self.sales_report1.setIconSize(QSize(20, 20))
        self.sales_report1.setCheckable(True)
        self.sales_report1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.sales_report1)

        self.mng_account1 = QPushButton(self.icon_only)
        self.mng_account1.setObjectName(u"mng_account1")
        self.mng_account1.setIcon(icon5)
        self.mng_account1.setIconSize(QSize(20, 20))
        self.mng_account1.setCheckable(True)
        self.mng_account1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.mng_account1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 182, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logout1 = QPushButton(self.icon_only)
        self.logout1.setObjectName(u"logout1")
        self.logout1.setIcon(icon6)
        self.logout1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.logout1)


        self.gridLayout_7.addWidget(self.icon_only, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_15.toggled.connect(self.icon_only.setHidden)
        self.pushButton_15.toggled.connect(self.word_iicon.setVisible)
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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Coffito", None))
        self.dashboard2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.add_item2.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.update_item2.setText(QCoreApplication.translate("MainWindow", u"Update Item", None))
        self.delete_item1_2.setText(QCoreApplication.translate("MainWindow", u"Delete Item", None))
        self.sales_report2.setText(QCoreApplication.translate("MainWindow", u"Sales Report", None))
        self.mng_account2.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.logout2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_15.setText("")
        self.dashboardTxt.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Total Sales", None))
        self.pushButton.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"48,760", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Total Item Sold", None))
        self.pushButton_3.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"48,760", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Total No. of Items", None))
        self.pushButton_4.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sales", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Sales", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Best Selling", None))
        self.toolButton.setText("")
        self.toolButton_3.setText("")
        self.toolButton_4.setText("")
        self.toolButton_5.setText("")
        self.toolButton_6.setText("")
        self.toolButton_7.setText("")
        self.toolButton_8.setText("")
        self.toolButton_9.setText("")
        self.toolButton_10.setText("")
        self.pushButton_14.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.add_prod_button.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        ___qtablewidgetitem2 = self.product_table.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Product ID", None));
        ___qtablewidgetitem3 = self.product_table.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem4 = self.product_table.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem5 = self.product_table.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem6 = self.product_table.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Created At", None));

        __sortingEnabled = self.product_table.isSortingEnabled()
        self.product_table.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.product_table.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"12312", None));
        ___qtablewidgetitem8 = self.product_table.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"sadasdas", None));
        ___qtablewidgetitem9 = self.product_table.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"40", None));
        ___qtablewidgetitem10 = self.product_table.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"cape", None));
        ___qtablewidgetitem11 = self.product_table.item(0, 4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"31212312", None));
        ___qtablewidgetitem12 = self.product_table.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2312312", None));
        ___qtablewidgetitem13 = self.product_table.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"sadasd", None));
        ___qtablewidgetitem14 = self.product_table.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"43", None));
        ___qtablewidgetitem15 = self.product_table.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"asdas", None));
        ___qtablewidgetitem16 = self.product_table.item(1, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"323232", None));
        self.product_table.setSortingEnabled(__sortingEnabled)

        self.pushButton_16.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.update_prod_button.setText(QCoreApplication.translate("MainWindow", u"Update Item", None))
        ___qtablewidgetitem17 = self.product_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Product ID", None));
        ___qtablewidgetitem18 = self.product_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem19 = self.product_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem20 = self.product_table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem21 = self.product_table_2.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Created At", None));

        __sortingEnabled1 = self.product_table_2.isSortingEnabled()
        self.product_table_2.setSortingEnabled(False)
        ___qtablewidgetitem22 = self.product_table_2.item(0, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"12312", None));
        ___qtablewidgetitem23 = self.product_table_2.item(0, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"sadasdas", None));
        ___qtablewidgetitem24 = self.product_table_2.item(0, 2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"40", None));
        ___qtablewidgetitem25 = self.product_table_2.item(0, 3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"cape", None));
        ___qtablewidgetitem26 = self.product_table_2.item(0, 4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"31212312", None));
        ___qtablewidgetitem27 = self.product_table_2.item(1, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"2312312", None));
        ___qtablewidgetitem28 = self.product_table_2.item(1, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"sadasd", None));
        ___qtablewidgetitem29 = self.product_table_2.item(1, 2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"43", None));
        ___qtablewidgetitem30 = self.product_table_2.item(1, 3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"asdas", None));
        ___qtablewidgetitem31 = self.product_table_2.item(1, 4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"323232", None));
        self.product_table_2.setSortingEnabled(__sortingEnabled1)

        self.pushButton_17.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.update_prod_button_2.setText(QCoreApplication.translate("MainWindow", u"Delete Item", None))
        ___qtablewidgetitem32 = self.product_table_3.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Product ID", None));
        ___qtablewidgetitem33 = self.product_table_3.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem34 = self.product_table_3.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem35 = self.product_table_3.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem36 = self.product_table_3.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Created At", None));

        __sortingEnabled2 = self.product_table_3.isSortingEnabled()
        self.product_table_3.setSortingEnabled(False)
        ___qtablewidgetitem37 = self.product_table_3.item(0, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"12312", None));
        ___qtablewidgetitem38 = self.product_table_3.item(0, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"sadasdas", None));
        ___qtablewidgetitem39 = self.product_table_3.item(0, 2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"40", None));
        ___qtablewidgetitem40 = self.product_table_3.item(0, 3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"cape", None));
        ___qtablewidgetitem41 = self.product_table_3.item(0, 4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"31212312", None));
        ___qtablewidgetitem42 = self.product_table_3.item(1, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"2312312", None));
        ___qtablewidgetitem43 = self.product_table_3.item(1, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"sadasd", None));
        ___qtablewidgetitem44 = self.product_table_3.item(1, 2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"43", None));
        ___qtablewidgetitem45 = self.product_table_3.item(1, 3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"asdas", None));
        ___qtablewidgetitem46 = self.product_table_3.item(1, 4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"323232", None));
        self.product_table_3.setSortingEnabled(__sortingEnabled2)

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Grand Total Sales: ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"447,000", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total Items Sold: ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"11,175", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Daily", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Monthly", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Yearly", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Item Sold", None))
        ___qtablewidgetitem47 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem48 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Total Sales", None));

        __sortingEnabled3 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled3)

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_19.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"AdminCoffito", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"CoffitoCafe", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_20.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"UserCoffito", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"CoffitoCafe", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Product ID: ", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"11234", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Product Name:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Product Price:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Select Category:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Coffee", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Non-Coffee", None))

        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Category", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Update Item", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Product ID: ", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"11234", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Product Name:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Product Price:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Select Category:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Coffee", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Non-Coffee", None))

        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Category", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"UPDATE", None))
        self.label_12.setText("")
        self.label.setText("")
        self.dashboard1.setText("")
        self.add_item1.setText("")
        self.update_item1.setText("")
        self.delete_item1.setText("")
        self.sales_report1.setText("")
        self.mng_account1.setText("")
        self.logout1.setText("")
    # retranslateUi

