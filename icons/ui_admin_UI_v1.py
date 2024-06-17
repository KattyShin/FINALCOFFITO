# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_UI_v1XDMvao.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource1_rc
import resource1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1054, 562)
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
        self.label.setPixmap(QPixmap(u":/iCons/icons/Green Simple Monoline Badge CK Letter Logo (3).png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.dashboard1 = QPushButton(self.icon_only)
        self.dashboard1.setObjectName(u"dashboard1")
        icon = QIcon()
        icon.addFile(u":/iCons/icons/icons8-coffee-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/iCons/icons/icons8-coffee0-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard1.setIcon(icon)
        self.dashboard1.setIconSize(QSize(25, 25))
        self.dashboard1.setCheckable(True)
        self.dashboard1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard1)

        self.add_item1 = QPushButton(self.icon_only)
        self.add_item1.setObjectName(u"add_item1")
        icon1 = QIcon()
        icon1.addFile(u":/iCons/icons/icons8-add-folder-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/iCons/icons/icons8-add-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.add_item1.setIcon(icon1)
        self.add_item1.setIconSize(QSize(20, 20))
        self.add_item1.setCheckable(True)
        self.add_item1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.add_item1)

        self.update_item1 = QPushButton(self.icon_only)
        self.update_item1.setObjectName(u"update_item1")
        icon2 = QIcon()
        icon2.addFile(u":/iCons/icons/icons8-edit-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/iCons/icons/icons8-edit-40 (1).png", QSize(), QIcon.Normal, QIcon.On)
        self.update_item1.setIcon(icon2)
        self.update_item1.setIconSize(QSize(20, 20))
        self.update_item1.setCheckable(True)
        self.update_item1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.update_item1)

        self.delete_item1 = QPushButton(self.icon_only)
        self.delete_item1.setObjectName(u"delete_item1")
        icon3 = QIcon()
        icon3.addFile(u":/iCons/icons/icons8-delete-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/iCons/icons/icons8-delete-40(1).png", QSize(), QIcon.Normal, QIcon.On)
        self.delete_item1.setIcon(icon3)
        self.delete_item1.setIconSize(QSize(20, 20))
        self.delete_item1.setCheckable(True)
        self.delete_item1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.delete_item1)

        self.sales_report1 = QPushButton(self.icon_only)
        self.sales_report1.setObjectName(u"sales_report1")
        icon4 = QIcon()
        icon4.addFile(u":/iCons/icons/icons8-sales-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/iCons/icons/icons8-sales-40(1).png", QSize(), QIcon.Normal, QIcon.On)
        self.sales_report1.setIcon(icon4)
        self.sales_report1.setIconSize(QSize(20, 20))
        self.sales_report1.setCheckable(True)
        self.sales_report1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.sales_report1)

        self.mng_account1 = QPushButton(self.icon_only)
        self.mng_account1.setObjectName(u"mng_account1")
        icon5 = QIcon()
        icon5.addFile(u":/iCons/icons/personalization.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mng_account1.setIcon(icon5)
        self.mng_account1.setIconSize(QSize(20, 20))
        self.mng_account1.setCheckable(True)
        self.mng_account1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.mng_account1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 182, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logout1 = QPushButton(self.icon_only)
        self.logout1.setObjectName(u"logout1")
        icon6 = QIcon()
        icon6.addFile(u":/iCons/icons/icons8-logout-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/iCons/icons/icons8-logouto-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.logout1.setIcon(icon6)
        self.logout1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.logout1)


        self.gridLayout.addWidget(self.icon_only, 0, 0, 1, 1)

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

        self.label_12 = QLabel(self.header_widget)
        self.label_12.setObjectName(u"label_12")
        font = QFont()
        font.setFamilies([u"Poppins SemiBold"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.horizontalSpacer_2 = QSpacerItem(684, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.header_widget, 0, Qt.AlignTop)

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
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 101, 31))
        font1 = QFont()
        font1.setFamilies([u"Poppins SemiBold"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 40, 141, 31))
        font2 = QFont()
        font2.setFamilies([u"Poppins Black"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.label_15.setFont(font2)

        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.dashboard_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(170, 90))
        self.widget_2.setStyleSheet(u"background-color: #3B3B3B;\n"
"border-radius:10px;\n"
"")
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 10, 111, 31))
        self.label_13.setFont(font1)
        self.label_16 = QLabel(self.widget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 40, 141, 31))
        self.label_16.setFont(font2)

        self.horizontalLayout.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.dashboard_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(170, 90))
        self.widget_3.setStyleSheet(u"background-color: #3B3B3B;\n"
"border-radius:10px;\n"
"")
        self.label_14 = QLabel(self.widget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 10, 121, 31))
        self.label_14.setFont(font1)
        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 40, 141, 31))
        self.label_17.setFont(font2)

        self.horizontalLayout.addWidget(self.widget_3, 0, Qt.AlignTop)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.widget_4 = QWidget(self.dashboard_page)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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
        font3 = QFont()
        font3.setFamilies([u"Poppins SemiBold"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_6.setFont(font3)

        self.verticalLayout_7.addWidget(self.label_6)

        self.line = QFrame(self.widget_4)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: white;\n"
"")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.tableWidget = QTableWidget(self.widget_4)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
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
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: #3B3B3B;\n"
"	border-radius:3px;\n"
"	border:1px solid rgb(50,50,50);\n"
"}\n"
"QTableWidget::section{\n"
"\n"
"	border: none;\n"
"	border-bottom: 1px solid #d0c6ff;\n"
"	text-align: left;\n"
"	padding: 3px 5px;\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(50,50,50);\n"
"	color: white;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(50,50,50);\n"
"	text-align: left;\n"
"	padding: 2px 4px;\n"
"	min-width: 20px;\n"
"}\n"
"QTableView::item{\n"
"	color: white;\n"
"	padding:2px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #3B3B3B;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #606060;\n"
"    min-height: 20px; \n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    bac"
                        "kground: none;\n"
"}\n"
"QScrollBar:hover {\n"
"    opacity: 0.7;\n"
"}\n"
"")

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
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 121, 31))
        self.label_4.setFont(font3)
        self.widget1 = QWidget(self.widget_5)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 50, 161, 411))
        self.verticalLayout_8 = QVBoxLayout(self.widget1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget1)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 45))
        self.widget_6.setMaximumSize(QSize(16777215, 45))
        self.widget_6.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(140, 40, 161, 45))
        self.widget_7.setMinimumSize(QSize(0, 45))
        self.widget_7.setMaximumSize(QSize(16777215, 45))
        self.widget_7.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7;\n"
"")
        self.widget_20 = QWidget(self.widget_6)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setGeometry(QRect(0, 0, 51, 45))
        self.widget_20.setStyleSheet(u"background-color: rgb(255, 140, 24);")

        self.verticalLayout_8.addWidget(self.widget_6)

        self.widget_8 = QWidget(self.widget1)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 45))
        self.widget_8.setMaximumSize(QSize(16777215, 45))
        self.widget_8.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(140, 40, 161, 45))
        self.widget_9.setMinimumSize(QSize(0, 45))
        self.widget_9.setMaximumSize(QSize(16777215, 45))
        self.widget_9.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7;\n"
"")
        self.widget_21 = QWidget(self.widget_8)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setGeometry(QRect(0, 0, 51, 45))
        self.widget_21.setStyleSheet(u"background-color: rgb(255, 140, 24);")

        self.verticalLayout_8.addWidget(self.widget_8)

        self.widget_10 = QWidget(self.widget1)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 45))
        self.widget_10.setMaximumSize(QSize(16777215, 45))
        self.widget_10.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(140, 40, 161, 45))
        self.widget_11.setMinimumSize(QSize(0, 45))
        self.widget_11.setMaximumSize(QSize(16777215, 45))
        self.widget_11.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7;\n"
"")
        self.widget_22 = QWidget(self.widget_10)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setGeometry(QRect(0, 0, 51, 45))
        self.widget_22.setStyleSheet(u"background-color: rgb(255, 140, 24);")

        self.verticalLayout_8.addWidget(self.widget_10)

        self.widget_12 = QWidget(self.widget1)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 45))
        self.widget_12.setMaximumSize(QSize(16777215, 45))
        self.widget_12.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setGeometry(QRect(140, 40, 161, 45))
        self.widget_13.setMinimumSize(QSize(0, 45))
        self.widget_13.setMaximumSize(QSize(16777215, 45))
        self.widget_13.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7;\n"
"")
        self.widget_23 = QWidget(self.widget_12)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setGeometry(QRect(0, 0, 51, 45))
        self.widget_23.setStyleSheet(u"background-color: rgb(255, 140, 24);")

        self.verticalLayout_8.addWidget(self.widget_12)

        self.widget_14 = QWidget(self.widget1)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 45))
        self.widget_14.setMaximumSize(QSize(16777215, 45))
        self.widget_14.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setGeometry(QRect(140, 40, 161, 45))
        self.widget_15.setMinimumSize(QSize(0, 45))
        self.widget_15.setMaximumSize(QSize(16777215, 45))
        self.widget_15.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7;\n"
"")
        self.widget_24 = QWidget(self.widget_14)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setGeometry(QRect(0, 0, 51, 45))
        self.widget_24.setStyleSheet(u"background-color: rgb(255, 140, 24);")

        self.verticalLayout_8.addWidget(self.widget_14)

        self.widget_16 = QWidget(self.widget1)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 45))
        self.widget_16.setMaximumSize(QSize(16777215, 45))
        self.widget_16.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setGeometry(QRect(140, 40, 161, 45))
        self.widget_17.setMinimumSize(QSize(0, 45))
        self.widget_17.setMaximumSize(QSize(16777215, 45))
        self.widget_17.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7;\n"
"")
        self.widget_25 = QWidget(self.widget_16)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setGeometry(QRect(0, 0, 51, 45))
        self.widget_25.setStyleSheet(u"background-color: rgb(255, 140, 24);")

        self.verticalLayout_8.addWidget(self.widget_16)

        self.widget_18 = QWidget(self.widget1)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 45))
        self.widget_18.setMaximumSize(QSize(16777215, 45))
        self.widget_18.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7px;\n"
"")
        self.widget_19 = QWidget(self.widget_18)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setGeometry(QRect(140, 40, 161, 45))
        self.widget_19.setMinimumSize(QSize(0, 45))
        self.widget_19.setMaximumSize(QSize(16777215, 45))
        self.widget_19.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius:7;\n"
"")
        self.widget_26 = QWidget(self.widget_18)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setGeometry(QRect(0, 0, 51, 45))
        self.widget_26.setStyleSheet(u"background-color: rgb(255, 140, 24);")

        self.verticalLayout_8.addWidget(self.widget_18)


        self.gridLayout_2.addWidget(self.widget_5, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.update_product = QWidget()
        self.update_product.setObjectName(u"update_product")
        self.label_8 = QLabel(self.update_product)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 190, 281, 41))
        font4 = QFont()
        font4.setPointSize(20)
        self.label_8.setFont(font4)
        self.stackedWidget.addWidget(self.update_product)
        self.delete_product = QWidget()
        self.delete_product.setObjectName(u"delete_product")
        self.label_9 = QLabel(self.delete_product)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(230, 190, 261, 41))
        self.label_9.setFont(font4)
        self.pushButton_5 = QPushButton(self.delete_product)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(370, 280, 178, 31))
        self.pushButton_5.setMinimumSize(QSize(0, 31))
        self.pushButton_5.setMaximumSize(QSize(16777215, 31))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 14px;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: black;\n"
"    background: #CCCCCC;\n"
"    box-shadow: 0px 0.5px 1.5px rgba(54, 122, 246, 0.25), inset 0px 0.8px 0px -0.25px rgba(255, 255, 255, 0.2);\n"
"    user-select: none;\n"
"    -webkit-user-select: none;\n"
"    touch-action: manipulation;\n"
"}\n"
"")
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
        self.label_10 = QLabel(self.widget_29)
        self.label_10.setObjectName(u"label_10")
        font5 = QFont()
        font5.setFamilies([u"Poppins SemiBold"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.label_10.setFont(font5)

        self.verticalLayout_11.addWidget(self.label_10)

        self.label_18 = QLabel(self.widget_29)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)

        self.verticalLayout_11.addWidget(self.label_18)


        self.verticalLayout_10.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_27)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_6 = QPushButton(self.widget_30)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 31))
        self.pushButton_6.setMaximumSize(QSize(16777215, 31))
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.pushButton_6.setFont(font6)
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 14px;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: black;\n"
"    background: #CCCCCC;\n"
"    box-shadow: 0px 0.5px 1.5px rgba(54, 122, 246, 0.25), inset 0px 0.8px 0px -0.25px rgba(255, 255, 255, 0.2);\n"
"    user-select: none;\n"
"    -webkit-user-select: none;\n"
"    touch-action: manipulation;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget_30)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 31))
        self.pushButton_7.setMaximumSize(QSize(16777215, 31))
        self.pushButton_7.setFont(font6)
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 14px;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: black;\n"
"    background: #CCCCCC;\n"
"    box-shadow: 0px 0.5px 1.5px rgba(54, 122, 246, 0.25), inset 0px 0.8px 0px -0.25px rgba(255, 255, 255, 0.2);\n"
"    user-select: none;\n"
"    -webkit-user-select: none;\n"
"    touch-action: manipulation;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.widget_30)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 31))
        self.pushButton_8.setMaximumSize(QSize(16777215, 31))
        self.pushButton_8.setFont(font6)
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 14px;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: black;\n"
"    background: #CCCCCC;\n"
"    box-shadow: 0px 0.5px 1.5px rgba(54, 122, 246, 0.25), inset 0px 0.8px 0px -0.25px rgba(255, 255, 255, 0.2);\n"
"    user-select: none;\n"
"    -webkit-user-select: none;\n"
"    touch-action: manipulation;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.widget_30)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 31))
        self.pushButton_9.setMaximumSize(QSize(16777215, 31))
        self.pushButton_9.setFont(font6)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 14px;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    border-radius: 6px;\n"
"    border: none;\n"
"    color: black;\n"
"    background: #CCCCCC;\n"
"    box-shadow: 0px 0.5px 1.5px rgba(54, 122, 246, 0.25), inset 0px 0.8px 0px -0.25px rgba(255, 255, 255, 0.2);\n"
"    user-select: none;\n"
"    -webkit-user-select: none;\n"
"    touch-action: manipulation;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.pushButton_9)


        self.verticalLayout_10.addWidget(self.widget_30)


        self.verticalLayout_9.addWidget(self.widget_27, 0, Qt.AlignTop)

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
        font7 = QFont()
        font7.setFamilies([u"Poppins SemiBold"])
        font7.setPointSize(10)
        font7.setBold(False)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font7);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font7);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy1.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy1)
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	background-color: #1F1F1F;\n"
"	border-radius:3px;\n"
"	border:1px solid rgb(50,50,50);\n"
"}\n"
"QTableWidget::section{\n"
"\n"
"	border: none;\n"
"	border-bottom: 1px solid #d0c6ff;\n"
"	text-align: left;\n"
"	padding: 3px 5px;\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(50,50,50);\n"
"	color: white;\n"
"	border: none;\n"
"	border-bottom: 1px solid rgb(50,50,50);\n"
"	text-align: left;\n"
"	padding: 2px 4px;\n"
"	min-width: 0; \n"
"    width: auto;\n"
"}\n"
"QTableView::item{\n"
"	color: white;\n"
"	padding:2px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #3B3B3B;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #606060;\n"
"    min-height: 20px; \n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:ver"
                        "tical {\n"
"    background: none;\n"
"}\n"
"QScrollBar:hover {\n"
"    opacity: 0.7;\n"
"}\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.tableWidget_2, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.widget_28)


        self.gridLayout_3.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.sales_report)
        self.manage_account = QWidget()
        self.manage_account.setObjectName(u"manage_account")
        self.label_11 = QLabel(self.manage_account)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(220, 190, 311, 41))
        self.label_11.setFont(font4)
        self.stackedWidget.addWidget(self.manage_account)
        self.add_product = QWidget()
        self.add_product.setObjectName(u"add_product")
        self.label_7 = QLabel(self.add_product)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 200, 221, 41))
        self.label_7.setFont(font4)
        self.stackedWidget.addWidget(self.add_product)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.Main_menu, 0, 2, 1, 1)

        self.word_iicon = QWidget(self.centralwidget)
        self.word_iicon.setObjectName(u"word_iicon")
        self.word_iicon.setStyleSheet(u"QWidget{\n"
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
        self.label_2.setPixmap(QPixmap(u":/iCons/icons/Green Simple Monoline Badge CK Letter Logo (3).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.word_iicon)
        self.label_3.setObjectName(u"label_3")
        font8 = QFont()
        font8.setFamilies([u"Poppins"])
        font8.setPointSize(12)
        font8.setBold(True)
        self.label_3.setFont(font8)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.dashboard2 = QPushButton(self.word_iicon)
        self.dashboard2.setObjectName(u"dashboard2")
        font9 = QFont()
        font9.setFamilies([u"Poppins"])
        font9.setPointSize(10)
        self.dashboard2.setFont(font9)
        self.dashboard2.setIcon(icon)
        self.dashboard2.setIconSize(QSize(20, 20))
        self.dashboard2.setCheckable(True)
        self.dashboard2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard2)

        self.add_item2 = QPushButton(self.word_iicon)
        self.add_item2.setObjectName(u"add_item2")
        self.add_item2.setFont(font9)
        self.add_item2.setIcon(icon1)
        self.add_item2.setIconSize(QSize(20, 20))
        self.add_item2.setCheckable(True)
        self.add_item2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.add_item2)

        self.update_item2 = QPushButton(self.word_iicon)
        self.update_item2.setObjectName(u"update_item2")
        self.update_item2.setFont(font9)
        self.update_item2.setIcon(icon2)
        self.update_item2.setIconSize(QSize(20, 20))
        self.update_item2.setCheckable(True)
        self.update_item2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_item2)

        self.delete_item1_2 = QPushButton(self.word_iicon)
        self.delete_item1_2.setObjectName(u"delete_item1_2")
        self.delete_item1_2.setFont(font9)
        self.delete_item1_2.setIcon(icon3)
        self.delete_item1_2.setIconSize(QSize(20, 20))
        self.delete_item1_2.setCheckable(True)
        self.delete_item1_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.delete_item1_2)

        self.sales_report2 = QPushButton(self.word_iicon)
        self.sales_report2.setObjectName(u"sales_report2")
        self.sales_report2.setFont(font9)
        self.sales_report2.setIcon(icon4)
        self.sales_report2.setIconSize(QSize(20, 20))
        self.sales_report2.setCheckable(True)
        self.sales_report2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.sales_report2)

        self.mng_account2 = QPushButton(self.word_iicon)
        self.mng_account2.setObjectName(u"mng_account2")
        self.mng_account2.setFont(font9)
        self.mng_account2.setIcon(icon5)
        self.mng_account2.setIconSize(QSize(20, 20))
        self.mng_account2.setCheckable(True)
        self.mng_account2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.mng_account2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 180, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.logout2 = QPushButton(self.word_iicon)
        self.logout2.setObjectName(u"logout2")
        font10 = QFont()
        font10.setFamilies([u"Poppins"])
        self.logout2.setFont(font10)
        self.logout2.setIcon(icon6)
        self.logout2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.logout2)


        self.gridLayout.addWidget(self.word_iicon, 0, 1, 1, 1)

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

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.dashboard1.setText("")
        self.add_item1.setText("")
        self.update_item1.setText("")
        self.delete_item1.setText("")
        self.sales_report1.setText("")
        self.mng_account1.setText("")
        self.logout1.setText("")
        self.pushButton_15.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total Sales", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"$ 48, 000", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Total Items Sold", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"1,175", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Total No. of Items", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sales", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Sales", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Best Selling", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Update-Product Page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Delete-Product Page", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Grand Total Sales: 447,000", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total Items Sold: 11,175", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Daily", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Monthly", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Yearly", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Item Sold", None))
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Total Sales", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Manage-Accounts Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Add-Product Page", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CoFFiTo", None))
        self.dashboard2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.add_item2.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.update_item2.setText(QCoreApplication.translate("MainWindow", u"Update Item", None))
        self.delete_item1_2.setText(QCoreApplication.translate("MainWindow", u"Delete Item", None))
        self.sales_report2.setText(QCoreApplication.translate("MainWindow", u"Sales Report", None))
        self.mng_account2.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.logout2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

