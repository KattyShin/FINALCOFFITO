# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUserInterfaceXnIlyf.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

import resource1_rc
import main_resources
import resource1_rcc
import resourcesLatest
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1106, 576)
        MainWindow.setStyleSheet(u"background-color:#1F1F1F;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.OrderWidget = QWidget(self.centralwidget)
        self.OrderWidget.setObjectName(u"OrderWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OrderWidget.sizePolicy().hasHeightForWidth())
        self.OrderWidget.setSizePolicy(sizePolicy)
        self.OrderWidget.setMinimumSize(QSize(400, 0))
        self.OrderWidget.setMaximumSize(QSize(600, 16777215))
        self.OrderWidget.setStyleSheet(u"background-color: rgb(59,59,59)")
        self.verticalLayout_10 = QVBoxLayout(self.OrderWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.OrderWidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.orderListPage = QWidget()
        self.orderListPage.setObjectName(u"orderListPage")
        self.verticalLayout_12 = QVBoxLayout(self.orderListPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.orderListWidget = QWidget(self.orderListPage)
        self.orderListWidget.setObjectName(u"orderListWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.orderListWidget.sizePolicy().hasHeightForWidth())
        self.orderListWidget.setSizePolicy(sizePolicy1)
        self.gridLayout_5 = QGridLayout(self.orderListWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_33 = QLabel(self.orderListWidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(11)
        font.setBold(True)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_4.addWidget(self.label_33)

        self.totalPymtLbl = QLabel(self.orderListWidget)
        self.totalPymtLbl.setObjectName(u"totalPymtLbl")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.totalPymtLbl.sizePolicy().hasHeightForWidth())
        self.totalPymtLbl.setSizePolicy(sizePolicy2)
        self.totalPymtLbl.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Inter Medium"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.totalPymtLbl.setFont(font1)
        self.totalPymtLbl.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_4.addWidget(self.totalPymtLbl)

        self.removeProdOrder = QPushButton(self.orderListWidget)
        self.removeProdOrder.setObjectName(u"removeProdOrder")
        self.removeProdOrder.setMinimumSize(QSize(30, 30))
        self.removeProdOrder.setMaximumSize(QSize(30, 25))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.removeProdOrder.setFont(font2)
        self.removeProdOrder.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(u":/coffitoIcons/icons/icons8-delete-40.png", QSize(), QIcon.Normal, QIcon.Off)
        self.removeProdOrder.setIcon(icon)
        self.removeProdOrder.setCheckable(True)
        self.removeProdOrder.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.removeProdOrder)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.order_table = QTableWidget(self.orderListWidget)
        if (self.order_table.columnCount() < 3):
            self.order_table.setColumnCount(3)
        font3 = QFont()
        font3.setFamilies([u"Inter SemiBold"])
        font3.setPointSize(10)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.order_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.order_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.order_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.order_table.setObjectName(u"order_table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(50)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.order_table.sizePolicy().hasHeightForWidth())
        self.order_table.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Inter Medium"])
        font4.setPointSize(9)
        font4.setBold(False)
        self.order_table.setFont(font4)
        self.order_table.setStyleSheet(u"QTableWidget {\n"
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
        self.order_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.order_table.setDragEnabled(False)
        self.order_table.setAlternatingRowColors(True)
        self.order_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.order_table.setGridStyle(Qt.PenStyle.NoPen)
        self.order_table.setSortingEnabled(True)
        self.order_table.setWordWrap(True)
        self.order_table.horizontalHeader().setCascadingSectionResizes(True)
        self.order_table.horizontalHeader().setMinimumSectionSize(30)
        self.order_table.horizontalHeader().setDefaultSectionSize(100)
        self.order_table.horizontalHeader().setStretchLastSection(True)
        self.order_table.verticalHeader().setVisible(False)
        self.order_table.verticalHeader().setCascadingSectionResizes(False)
        self.order_table.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.order_table, 2, 0, 1, 1)

        self.label_30 = QLabel(self.orderListWidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setFamilies([u"Inter SemiBold"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"color: white;\n"
"")

        self.gridLayout_5.addWidget(self.label_30, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.orderListWidget)

        self.widget_21 = QWidget(self.orderListPage)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(0, 70))
        self.verticalLayout_11 = QVBoxLayout(self.widget_21)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.proceedBtn = QPushButton(self.widget_21)
        self.proceedBtn.setObjectName(u"proceedBtn")
        self.proceedBtn.setMinimumSize(QSize(150, 35))
        self.proceedBtn.setMaximumSize(QSize(100, 25))
        self.proceedBtn.setFont(font2)
        self.proceedBtn.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 14px;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    border-radius: 10px;\n"
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
        self.proceedBtn.setCheckable(True)
        self.proceedBtn.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.proceedBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_12.addWidget(self.widget_21)

        self.stackedWidget_2.addWidget(self.orderListPage)
        self.orderSummaryPage = QWidget()
        self.orderSummaryPage.setObjectName(u"orderSummaryPage")
        self.verticalLayout_14 = QVBoxLayout(self.orderSummaryPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.orderListWidget_2 = QWidget(self.orderSummaryPage)
        self.orderListWidget_2.setObjectName(u"orderListWidget_2")
        sizePolicy1.setHeightForWidth(self.orderListWidget_2.sizePolicy().hasHeightForWidth())
        self.orderListWidget_2.setSizePolicy(sizePolicy1)
        self.gridLayout_6 = QGridLayout(self.orderListWidget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, 9, -1)
        self.label_35 = QLabel(self.orderListWidget_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 0))
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"color: white;\n"
"")

        self.gridLayout_6.addWidget(self.label_35, 8, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_34 = QLabel(self.orderListWidget_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 0))
        self.label_34.setFont(font3)
        self.label_34.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_6.addWidget(self.label_34)

        self.totalPymtLbl_3 = QLabel(self.orderListWidget_2)
        self.totalPymtLbl_3.setObjectName(u"totalPymtLbl_3")
        sizePolicy2.setHeightForWidth(self.totalPymtLbl_3.sizePolicy().hasHeightForWidth())
        self.totalPymtLbl_3.setSizePolicy(sizePolicy2)
        self.totalPymtLbl_3.setMinimumSize(QSize(40, 30))
        self.totalPymtLbl_3.setMaximumSize(QSize(60, 16777215))
        self.totalPymtLbl_3.setFont(font1)
        self.totalPymtLbl_3.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_6.addWidget(self.totalPymtLbl_3)

        self.totalPymtLbl_2 = QLabel(self.orderListWidget_2)
        self.totalPymtLbl_2.setObjectName(u"totalPymtLbl_2")
        sizePolicy2.setHeightForWidth(self.totalPymtLbl_2.sizePolicy().hasHeightForWidth())
        self.totalPymtLbl_2.setSizePolicy(sizePolicy2)
        self.totalPymtLbl_2.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setFamilies([u"Inter Medium"])
        font6.setPointSize(10)
        font6.setBold(False)
        self.totalPymtLbl_2.setFont(font6)
        self.totalPymtLbl_2.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_6.addWidget(self.totalPymtLbl_2)


        self.gridLayout_6.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)

        self.order_table_2 = QTableWidget(self.orderListWidget_2)
        if (self.order_table_2.columnCount() < 3):
            self.order_table_2.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.order_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.order_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.order_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.order_table_2.setObjectName(u"order_table_2")
        sizePolicy3.setHeightForWidth(self.order_table_2.sizePolicy().hasHeightForWidth())
        self.order_table_2.setSizePolicy(sizePolicy3)
        self.order_table_2.setFont(font4)
        self.order_table_2.setStyleSheet(u"QTableWidget {\n"
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
        self.order_table_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.order_table_2.setDragEnabled(False)
        self.order_table_2.setAlternatingRowColors(True)
        self.order_table_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.order_table_2.setGridStyle(Qt.PenStyle.NoPen)
        self.order_table_2.setSortingEnabled(True)
        self.order_table_2.setWordWrap(True)
        self.order_table_2.horizontalHeader().setCascadingSectionResizes(True)
        self.order_table_2.horizontalHeader().setMinimumSectionSize(30)
        self.order_table_2.horizontalHeader().setDefaultSectionSize(100)
        self.order_table_2.horizontalHeader().setStretchLastSection(True)
        self.order_table_2.verticalHeader().setVisible(False)
        self.order_table_2.verticalHeader().setCascadingSectionResizes(False)
        self.order_table_2.verticalHeader().setStretchLastSection(False)

        self.gridLayout_6.addWidget(self.order_table_2, 5, 0, 1, 1)

        self.label_31 = QLabel(self.orderListWidget_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 0))
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"color: white;\n"
"")

        self.gridLayout_6.addWidget(self.label_31, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Amount_ContactNum = QLabel(self.orderListWidget_2)
        self.Amount_ContactNum.setObjectName(u"Amount_ContactNum")
        sizePolicy2.setHeightForWidth(self.Amount_ContactNum.sizePolicy().hasHeightForWidth())
        self.Amount_ContactNum.setSizePolicy(sizePolicy2)
        self.Amount_ContactNum.setMinimumSize(QSize(50, 30))
        self.Amount_ContactNum.setMaximumSize(QSize(120, 16777215))
        self.Amount_ContactNum.setFont(font6)
        self.Amount_ContactNum.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_10.addWidget(self.Amount_ContactNum)

        self.Amt_ContactNum_Val = QLineEdit(self.orderListWidget_2)
        self.Amt_ContactNum_Val.setObjectName(u"Amt_ContactNum_Val")
        self.Amt_ContactNum_Val.setMinimumSize(QSize(0, 30))
        font7 = QFont()
        font7.setFamilies([u"Inter Medium"])
        font7.setPointSize(10)
        self.Amt_ContactNum_Val.setFont(font7)
        self.Amt_ContactNum_Val.setStyleSheet(u"background-color: rgb(37, 37, 37);\n"
"color:white;\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.Amt_ContactNum_Val)


        self.gridLayout_6.addLayout(self.horizontalLayout_10, 12, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.backBtn = QPushButton(self.orderListWidget_2)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setMinimumSize(QSize(30, 30))
        self.backBtn.setMaximumSize(QSize(30, 30))
        self.backBtn.setFont(font2)
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 14px;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"    color: white;\n"
"    background: transparent;\n"
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
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/icons8-back-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backBtn.setIcon(icon1)
        self.backBtn.setIconSize(QSize(25, 25))
        self.backBtn.setCheckable(True)
        self.backBtn.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.backBtn, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(40, -1, 75, -1)
        self.label_38 = QLabel(self.orderListWidget_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(0, 0))
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_9.addWidget(self.label_38)

        self.cashSelectBtn = QRadioButton(self.orderListWidget_2)
        self.cashSelectBtn.setObjectName(u"cashSelectBtn")
        self.cashSelectBtn.setStyleSheet(u"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #7a7a7a;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #0d6efd;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #FF8C18;\n"
"    border: 2px solid #FF8C18;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    background-color: #FF8C18;\n"
"    border: 2px solid #0d6efd;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 16px;\n"
"    color: #333;\n"
"    padding: 5px;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.cashSelectBtn)


        self.gridLayout_6.addLayout(self.horizontalLayout_9, 10, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(40, -1, 75, -1)
        self.label_36 = QLabel(self.orderListWidget_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 0))
        self.label_36.setFont(font3)
        self.label_36.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_7.addWidget(self.label_36)

        self.gcashSelectRBtn = QRadioButton(self.orderListWidget_2)
        self.gcashSelectRBtn.setObjectName(u"gcashSelectRBtn")
        self.gcashSelectRBtn.setStyleSheet(u"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px;\n"
"    border: 2px solid #7a7a7a;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #0d6efd;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #FF8C18;\n"
"    border: 2px solid #FF8C18;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    background-color: #FF8C18;\n"
"    border: 2px solid #0d6efd;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    font-size: 16px;\n"
"    color: #333;\n"
"    padding: 5px;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.gcashSelectRBtn)


        self.gridLayout_6.addLayout(self.horizontalLayout_7, 9, 0, 1, 1)

        self.line = QFrame(self.orderListWidget_2)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(355, 0))
        self.line.setMaximumSize(QSize(310, 16777215))
        self.line.setStyleSheet(u"background-color: gray;\n"
"opacity: 0.5;\n"
"")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_6.addWidget(self.line, 7, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.widget_22 = QWidget(self.orderListWidget_2)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMinimumSize(QSize(0, 50))
        self.verticalLayout_13 = QVBoxLayout(self.widget_22)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.payButton = QPushButton(self.widget_22)
        self.payButton.setObjectName(u"payButton")
        self.payButton.setMinimumSize(QSize(150, 35))
        self.payButton.setMaximumSize(QSize(100, 25))
        self.payButton.setFont(font2)
        self.payButton.setStyleSheet(u"QPushButton {\n"
"    padding: 6px 14px;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    border-radius: 10px;\n"
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
        self.payButton.setCheckable(True)
        self.payButton.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.payButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_6.addWidget(self.widget_22, 14, 0, 1, 1)

        self.widget_2 = QWidget(self.orderListWidget_2)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_6.addWidget(self.widget_2, 11, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.changeLbl = QLabel(self.orderListWidget_2)
        self.changeLbl.setObjectName(u"changeLbl")
        sizePolicy2.setHeightForWidth(self.changeLbl.sizePolicy().hasHeightForWidth())
        self.changeLbl.setSizePolicy(sizePolicy2)
        self.changeLbl.setMinimumSize(QSize(50, 30))
        self.changeLbl.setMaximumSize(QSize(120, 16777215))
        self.changeLbl.setFont(font6)
        self.changeLbl.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_11.addWidget(self.changeLbl)

        self.changeAmount = QLabel(self.orderListWidget_2)
        self.changeAmount.setObjectName(u"changeAmount")
        sizePolicy2.setHeightForWidth(self.changeAmount.sizePolicy().hasHeightForWidth())
        self.changeAmount.setSizePolicy(sizePolicy2)
        self.changeAmount.setMinimumSize(QSize(40, 30))
        self.changeAmount.setMaximumSize(QSize(16777215, 16777215))
        self.changeAmount.setFont(font1)
        self.changeAmount.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_11.addWidget(self.changeAmount)


        self.gridLayout_6.addLayout(self.horizontalLayout_11, 13, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 2, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.orderListWidget_2)

        self.stackedWidget_2.addWidget(self.orderSummaryPage)

        self.verticalLayout_10.addWidget(self.stackedWidget_2)


        self.gridLayout.addWidget(self.OrderWidget, 0, 2, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.widget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 9, -1, 0)
        self.pushButton_16 = QPushButton(self.header_widget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"	\n"
"	border:none;\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/iCons/icons/icons8-menu-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/iCons/icons/icons8-menu-40-1.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_16.setIcon(icon2)
        self.pushButton_16.setIconSize(QSize(16, 16))
        self.pushButton_16.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_16)

        self.dashboardTxt_2 = QLabel(self.header_widget)
        self.dashboardTxt_2.setObjectName(u"dashboardTxt_2")
        font8 = QFont()
        font8.setFamilies([u"Inter SemiBold"])
        font8.setPointSize(14)
        font8.setBold(True)
        self.dashboardTxt_2.setFont(font8)
        self.dashboardTxt_2.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_5.addWidget(self.dashboardTxt_2)

        self.horizontalSpacer_3 = QSpacerItem(684, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.DateTimeLabel = QLabel(self.header_widget)
        self.DateTimeLabel.setObjectName(u"DateTimeLabel")
        self.DateTimeLabel.setMinimumSize(QSize(200, 0))
        self.DateTimeLabel.setFont(font3)
        self.DateTimeLabel.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_5.addWidget(self.DateTimeLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.Menu_SearchWidget = QWidget(self.widget)
        self.Menu_SearchWidget.setObjectName(u"Menu_SearchWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.Menu_SearchWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.Menu_SearchWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(250, 0))
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.search_frame_prod_2 = QWidget(self.Menu_SearchWidget)
        self.search_frame_prod_2.setObjectName(u"search_frame_prod_2")
        self.search_frame_prod_2.setMinimumSize(QSize(200, 0))
        self.search_frame_prod_2.setStyleSheet(u"#search_frame_prod_2{\n"
"\n"
"	border-radius: 15px;\n"
"	background-color:#252525;\n"
"}\n"
"#search_frame_prod_2 QPushButton{\n"
"	\n"
"	padding: 5px 5px;\n"
"	border-radius:5px;\n"
"\n"
"	\n"
"}\n"
"#search_frame_prod_2 QLineEdit{\n"
"	border: none;\n"
"	color: white;\n"
"\n"
"}\n"
"\n"
"#search_frame_prod_2 QPushButton::pressed {\n"
"\n"
"	padding-left:10px;\n"
"\n"
"}\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.search_frame_prod_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(2)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(2, 2, 2, -1)
        self.searchItemBtn = QPushButton(self.search_frame_prod_2)
        self.searchItemBtn.setObjectName(u"searchItemBtn")
        self.searchItemBtn.setMinimumSize(QSize(25, 25))
        self.searchItemBtn.setMaximumSize(QSize(25, 25))
        self.searchItemBtn.setFont(font2)
        self.searchItemBtn.setStyleSheet(u"background-color: none;\n"
"border-radius:15px;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/iCons/icons/icons8-search-26.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchItemBtn.setIcon(icon3)

        self.horizontalLayout_31.addWidget(self.searchItemBtn)

        self.searchMenuItem = QLineEdit(self.search_frame_prod_2)
        self.searchMenuItem.setObjectName(u"searchMenuItem")
        self.searchMenuItem.setStyleSheet(u"background-color: rgb(37, 37, 37);")

        self.horizontalLayout_31.addWidget(self.searchMenuItem)


        self.verticalLayout_17.addLayout(self.horizontalLayout_31)


        self.horizontalLayout_2.addWidget(self.search_frame_prod_2)


        self.verticalLayout_5.addWidget(self.Menu_SearchWidget)

        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	background-color:#1F1F1F;\n"
"}\n"
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
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 478, 462))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only = QWidget(self.widget_3)
        self.icon_only.setObjectName(u"icon_only")
        self.icon_only.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(59,59,59);\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/iCons/icons/icons8-coffee-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/iCons/icons/icons8-coffee0-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard1.setIcon(icon4)
        self.dashboard1.setIconSize(QSize(25, 25))
        self.dashboard1.setCheckable(True)
        self.dashboard1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 182, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logout1 = QPushButton(self.icon_only)
        self.logout1.setObjectName(u"logout1")
        icon5 = QIcon()
        icon5.addFile(u":/iCons/icons/icons8-logout-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/iCons/icons/icons8-logouto-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.logout1.setIcon(icon5)
        self.logout1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.logout1)


        self.horizontalLayout.addWidget(self.icon_only, 0, Qt.AlignmentFlag.AlignLeft)

        self.word_iicon = QWidget(self.widget_3)
        self.word_iicon.setObjectName(u"word_iicon")
        self.word_iicon.setMinimumSize(QSize(150, 0))
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
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.word_iicon)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(35, 35))
        self.label_2.setMaximumSize(QSize(35, 31))
        self.label_2.setPixmap(QPixmap(u":/iCons/CoffitoLogo (40 x 40 px).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.word_iicon)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 40))
        self.label_3.setMaximumSize(QSize(16777215, 40))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setWordWrap(True)

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
        self.dashboard2.setIcon(icon4)
        self.dashboard2.setIconSize(QSize(25, 25))
        self.dashboard2.setCheckable(True)
        self.dashboard2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 180, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.logout2 = QPushButton(self.word_iicon)
        self.logout2.setObjectName(u"logout2")
        font10 = QFont()
        font10.setFamilies([u"Poppins"])
        self.logout2.setFont(font10)
        self.logout2.setIcon(icon5)
        self.logout2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.logout2)


        self.horizontalLayout.addWidget(self.word_iicon, 0, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.dashboard1.toggled.connect(self.dashboard2.setChecked)
        self.pushButton_16.toggled.connect(self.word_iicon.setVisible)
        self.pushButton_16.toggled.connect(self.icon_only.setHidden)
        self.logout1.toggled.connect(MainWindow.close)
        self.logout2.toggled.connect(MainWindow.close)
        self.dashboard2.toggled.connect(self.dashboard1.setChecked)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.totalPymtLbl.setText("")
        self.removeProdOrder.setText("")
        ___qtablewidgetitem = self.order_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem1 = self.order_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem2 = self.order_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Order List", None))
        self.proceedBtn.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Mode of payment:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Total Amount:", None))
        self.totalPymtLbl_3.setText("")
        self.totalPymtLbl_2.setText("")
        ___qtablewidgetitem3 = self.order_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem4 = self.order_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem5 = self.order_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Order Summary", None))
        self.Amount_ContactNum.setText("")
        self.Amt_ContactNum_Val.setPlaceholderText("")
        self.backBtn.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Cash", None))
        self.cashSelectBtn.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"GCash", None))
        self.gcashSelectRBtn.setText("")
        self.payButton.setText(QCoreApplication.translate("MainWindow", u"Pay", None))
        self.changeLbl.setText("")
        self.changeAmount.setText("")
        self.pushButton_16.setText("")
        self.dashboardTxt_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to Coffito Cafe", None))
        self.DateTimeLabel.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Coffito Cafe Menu", None))
        self.searchItemBtn.setText("")
        self.searchMenuItem.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label.setText("")
        self.dashboard1.setText("")
        self.logout1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Coffito Cafe", None))
        self.dashboard2.setText(QCoreApplication.translate("MainWindow", u"Homepage", None))
        self.logout2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

