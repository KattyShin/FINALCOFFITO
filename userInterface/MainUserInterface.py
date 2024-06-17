# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUserInterfaceBschfd.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

import resource1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1064, 529)
        MainWindow.setStyleSheet(u"background-color:#1F1F1F;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 182, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logout1 = QPushButton(self.icon_only)
        self.logout1.setObjectName(u"logout1")
        icon4 = QIcon()
        icon4.addFile(u":/iCons/icons/icons8-logout-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/iCons/icons/icons8-logouto-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.logout1.setIcon(icon4)
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
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(11)
        font.setBold(True)
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
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(10)
        self.dashboard2.setFont(font1)
        self.dashboard2.setIcon(icon)
        self.dashboard2.setIconSize(QSize(25, 25))
        self.dashboard2.setCheckable(True)
        self.dashboard2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard2)

        self.add_item2 = QPushButton(self.word_iicon)
        self.add_item2.setObjectName(u"add_item2")
        self.add_item2.setFont(font1)
        self.add_item2.setIcon(icon1)
        self.add_item2.setIconSize(QSize(20, 20))
        self.add_item2.setCheckable(True)
        self.add_item2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.add_item2)

        self.update_item2 = QPushButton(self.word_iicon)
        self.update_item2.setObjectName(u"update_item2")
        self.update_item2.setFont(font1)
        self.update_item2.setIcon(icon2)
        self.update_item2.setIconSize(QSize(20, 20))
        self.update_item2.setCheckable(True)
        self.update_item2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.update_item2)

        self.delete_item1_2 = QPushButton(self.word_iicon)
        self.delete_item1_2.setObjectName(u"delete_item1_2")
        self.delete_item1_2.setFont(font1)
        self.delete_item1_2.setIcon(icon3)
        self.delete_item1_2.setIconSize(QSize(20, 20))
        self.delete_item1_2.setCheckable(True)
        self.delete_item1_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.delete_item1_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 180, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.logout2 = QPushButton(self.word_iicon)
        self.logout2.setObjectName(u"logout2")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        self.logout2.setFont(font2)
        self.logout2.setIcon(icon4)
        self.logout2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.logout2)


        self.horizontalLayout.addWidget(self.word_iicon, 0, Qt.AlignmentFlag.AlignLeft)


        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

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
        icon5 = QIcon()
        icon5.addFile(u":/iCons/icons/icons8-menu-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/iCons/icons/icons8-menu-40-1.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_16.setIcon(icon5)
        self.pushButton_16.setIconSize(QSize(16, 16))
        self.pushButton_16.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_16)

        self.dashboardTxt_2 = QLabel(self.header_widget)
        self.dashboardTxt_2.setObjectName(u"dashboardTxt_2")
        font3 = QFont()
        font3.setFamilies([u"Inter SemiBold"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.dashboardTxt_2.setFont(font3)
        self.dashboardTxt_2.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"}")

        self.horizontalLayout_5.addWidget(self.dashboardTxt_2)

        self.horizontalSpacer_3 = QSpacerItem(684, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.DateTimeLabel = QLabel(self.header_widget)
        self.DateTimeLabel.setObjectName(u"DateTimeLabel")
        self.DateTimeLabel.setMinimumSize(QSize(150, 0))
        font4 = QFont()
        font4.setFamilies([u"Inter SemiBold"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.DateTimeLabel.setFont(font4)
        self.DateTimeLabel.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_5.addWidget(self.DateTimeLabel)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(250, 0))
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.search_frame_prod_2 = QWidget(self.widget_4)
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
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.searchItemBtn.setFont(font5)
        self.searchItemBtn.setStyleSheet(u"background-color: none;\n"
"border-radius:15px;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/iCons/icons/icons8-search-26.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchItemBtn.setIcon(icon6)

        self.horizontalLayout_31.addWidget(self.searchItemBtn)

        self.searchMenuItem = QLineEdit(self.search_frame_prod_2)
        self.searchMenuItem.setObjectName(u"searchMenuItem")
        self.searchMenuItem.setStyleSheet(u"background-color: rgb(37, 37, 37);")

        self.horizontalLayout_31.addWidget(self.searchMenuItem)


        self.verticalLayout_17.addLayout(self.horizontalLayout_31)


        self.horizontalLayout_2.addWidget(self.search_frame_prod_2)


        self.verticalLayout_5.addWidget(self.widget_4)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 526, 676))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_19 = QWidget(self.scrollAreaWidgetContents)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(120, 160))
        self.widget_19.setMaximumSize(QSize(120, 160))
        self.widget_19.setSizeIncrement(QSize(40, 0))
        self.widget_19.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_28 = QVBoxLayout(self.widget_19)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, -1)
        self.pushButton_24 = QPushButton(self.widget_19)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/iCons/icons/coffee-cup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon7)
        self.pushButton_24.setIconSize(QSize(70, 120))
        self.pushButton_24.setCheckable(True)

        self.verticalLayout_28.addWidget(self.pushButton_24)

        self.label_24 = QLabel(self.widget_19)
        self.label_24.setObjectName(u"label_24")
        font6 = QFont()
        font6.setFamilies([u"Inter SemiBold"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_24.setFont(font6)
        self.label_24.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_24.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.label_24)


        self.gridLayout_3.addWidget(self.widget_19, 2, 0, 1, 1)

        self.widget_20 = QWidget(self.scrollAreaWidgetContents)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(120, 160))
        self.widget_20.setMaximumSize(QSize(120, 160))
        self.widget_20.setSizeIncrement(QSize(40, 0))
        self.widget_20.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_29 = QVBoxLayout(self.widget_20)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, -1)
        self.pushButton_25 = QPushButton(self.widget_20)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_25.setIcon(icon7)
        self.pushButton_25.setIconSize(QSize(70, 120))
        self.pushButton_25.setCheckable(True)

        self.verticalLayout_29.addWidget(self.pushButton_25)

        self.label_25 = QLabel(self.widget_20)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font6)
        self.label_25.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_25.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_25)


        self.gridLayout_3.addWidget(self.widget_20, 2, 2, 1, 1)

        self.widget_18 = QWidget(self.scrollAreaWidgetContents)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(120, 160))
        self.widget_18.setMaximumSize(QSize(120, 160))
        self.widget_18.setSizeIncrement(QSize(40, 0))
        self.widget_18.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_27 = QVBoxLayout(self.widget_18)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, -1)
        self.pushButton_23 = QPushButton(self.widget_18)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_23.setIcon(icon7)
        self.pushButton_23.setIconSize(QSize(70, 120))
        self.pushButton_23.setCheckable(True)

        self.verticalLayout_27.addWidget(self.pushButton_23)

        self.label_23 = QLabel(self.widget_18)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font6)
        self.label_23.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_23.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.label_23)


        self.gridLayout_3.addWidget(self.widget_18, 2, 1, 1, 1)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(120, 160))
        self.widget_7.setMaximumSize(QSize(120, 160))
        self.widget_7.setSizeIncrement(QSize(40, 0))
        self.widget_7.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_8 = QVBoxLayout(self.widget_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.pushButton_3 = QPushButton(self.widget_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QSize(70, 120))
        self.pushButton_3.setCheckable(True)

        self.verticalLayout_8.addWidget(self.pushButton_3)

        self.label_6 = QLabel(self.widget_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_6)


        self.gridLayout_3.addWidget(self.widget_7, 0, 2, 1, 1)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(120, 160))
        self.widget_5.setMaximumSize(QSize(120, 160))
        self.widget_5.setSizeIncrement(QSize(40, 0))
        self.widget_5.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton.setIcon(icon7)
        self.pushButton.setIconSize(QSize(70, 120))
        self.pushButton.setCheckable(True)

        self.verticalLayout_6.addWidget(self.pushButton)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_4)


        self.gridLayout_3.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_15 = QWidget(self.scrollAreaWidgetContents)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(120, 160))
        self.widget_15.setMaximumSize(QSize(120, 160))
        self.widget_15.setSizeIncrement(QSize(40, 0))
        self.widget_15.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_19 = QVBoxLayout(self.widget_15)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, -1)
        self.pushButton_11 = QPushButton(self.widget_15)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_11.setIcon(icon7)
        self.pushButton_11.setIconSize(QSize(70, 120))
        self.pushButton_11.setCheckable(True)

        self.verticalLayout_19.addWidget(self.pushButton_11)

        self.label_15 = QLabel(self.widget_15)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font6)
        self.label_15.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_15)


        self.gridLayout_3.addWidget(self.widget_15, 1, 1, 1, 1)

        self.widget_13 = QWidget(self.scrollAreaWidgetContents)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(120, 160))
        self.widget_13.setMaximumSize(QSize(120, 160))
        self.widget_13.setSizeIncrement(QSize(40, 0))
        self.widget_13.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_15 = QVBoxLayout(self.widget_13)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, -1)
        self.pushButton_9 = QPushButton(self.widget_13)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QSize(70, 120))
        self.pushButton_9.setCheckable(True)

        self.verticalLayout_15.addWidget(self.pushButton_9)

        self.label_13 = QLabel(self.widget_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_13)


        self.gridLayout_3.addWidget(self.widget_13, 1, 3, 1, 1)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(120, 160))
        self.widget_6.setMaximumSize(QSize(120, 160))
        self.widget_6.setSizeIncrement(QSize(40, 0))
        self.widget_6.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.pushButton_2 = QPushButton(self.widget_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QSize(70, 120))
        self.pushButton_2.setCheckable(True)

        self.verticalLayout_7.addWidget(self.pushButton_2)

        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_5)


        self.gridLayout_3.addWidget(self.widget_6, 0, 1, 1, 1)

        self.widget_16 = QWidget(self.scrollAreaWidgetContents)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(120, 160))
        self.widget_16.setMaximumSize(QSize(120, 160))
        self.widget_16.setSizeIncrement(QSize(40, 0))
        self.widget_16.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_20 = QVBoxLayout(self.widget_16)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, -1)
        self.pushButton_12 = QPushButton(self.widget_16)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_12.setIcon(icon7)
        self.pushButton_12.setIconSize(QSize(70, 120))
        self.pushButton_12.setCheckable(True)

        self.verticalLayout_20.addWidget(self.pushButton_12)

        self.label_16 = QLabel(self.widget_16)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font6)
        self.label_16.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_16.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_16)


        self.gridLayout_3.addWidget(self.widget_16, 1, 2, 1, 1)

        self.widget_14 = QWidget(self.scrollAreaWidgetContents)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(120, 160))
        self.widget_14.setMaximumSize(QSize(120, 160))
        self.widget_14.setSizeIncrement(QSize(40, 0))
        self.widget_14.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_18 = QVBoxLayout(self.widget_14)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, -1)
        self.pushButton_10 = QPushButton(self.widget_14)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_10.setIcon(icon7)
        self.pushButton_10.setIconSize(QSize(70, 120))
        self.pushButton_10.setCheckable(True)

        self.verticalLayout_18.addWidget(self.pushButton_10)

        self.label_14 = QLabel(self.widget_14)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font6)
        self.label_14.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_14)


        self.gridLayout_3.addWidget(self.widget_14, 1, 0, 1, 1)

        self.widget_17 = QWidget(self.scrollAreaWidgetContents)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(120, 160))
        self.widget_17.setMaximumSize(QSize(120, 160))
        self.widget_17.setSizeIncrement(QSize(40, 0))
        self.widget_17.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_26 = QVBoxLayout(self.widget_17)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, -1)
        self.pushButton_22 = QPushButton(self.widget_17)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_22.setIcon(icon7)
        self.pushButton_22.setIconSize(QSize(70, 120))
        self.pushButton_22.setCheckable(True)

        self.verticalLayout_26.addWidget(self.pushButton_22)

        self.label_22 = QLabel(self.widget_17)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font6)
        self.label_22.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_22.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.label_22)


        self.gridLayout_3.addWidget(self.widget_17, 2, 3, 1, 1)

        self.widget_23 = QWidget(self.scrollAreaWidgetContents)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(120, 160))
        self.widget_23.setMaximumSize(QSize(120, 160))
        self.widget_23.setSizeIncrement(QSize(40, 0))
        self.widget_23.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_36 = QVBoxLayout(self.widget_23)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, -1)
        self.pushButton_32 = QPushButton(self.widget_23)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_32.setIcon(icon7)
        self.pushButton_32.setIconSize(QSize(70, 120))
        self.pushButton_32.setCheckable(True)

        self.verticalLayout_36.addWidget(self.pushButton_32)

        self.label_32 = QLabel(self.widget_23)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font6)
        self.label_32.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_32.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.label_32)


        self.gridLayout_3.addWidget(self.widget_23, 3, 0, 1, 1)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(120, 160))
        self.widget_8.setMaximumSize(QSize(120, 160))
        self.widget_8.setSizeIncrement(QSize(40, 0))
        self.widget_8.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_9 = QVBoxLayout(self.widget_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, -1)
        self.pushButton_4 = QPushButton(self.widget_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QSize(70, 120))
        self.pushButton_4.setCheckable(True)

        self.verticalLayout_9.addWidget(self.pushButton_4)

        self.label_7 = QLabel(self.widget_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)
        self.label_7.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_7)


        self.gridLayout_3.addWidget(self.widget_8, 0, 3, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.OrderWidget = QWidget(self.centralwidget)
        self.OrderWidget.setObjectName(u"OrderWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OrderWidget.sizePolicy().hasHeightForWidth())
        self.OrderWidget.setSizePolicy(sizePolicy)
        self.OrderWidget.setMinimumSize(QSize(300, 0))
        self.OrderWidget.setMaximumSize(QSize(600, 16777215))
        self.OrderWidget.setStyleSheet(u"background-color: rgb(59,59,59)")
        self.verticalLayout_10 = QVBoxLayout(self.OrderWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_22 = QWidget(self.OrderWidget)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_30 = QLabel(self.widget_22)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 0))
        self.label_30.setFont(font4)
        self.label_30.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_6.addWidget(self.label_30, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_10.addWidget(self.widget_22, 0, Qt.AlignmentFlag.AlignTop)

        self.orderListWidget = QWidget(self.OrderWidget)
        self.orderListWidget.setObjectName(u"orderListWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.orderListWidget.sizePolicy().hasHeightForWidth())
        self.orderListWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.orderListWidget)

        self.widget_21 = QWidget(self.OrderWidget)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(0, 50))
        self.label_33 = QLabel(self.widget_21)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 10, 51, 31))
        self.label_33.setMinimumSize(QSize(0, 0))
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"color: white;\n"
"")
        self.totalPymtLbl = QLabel(self.widget_21)
        self.totalPymtLbl.setObjectName(u"totalPymtLbl")
        self.totalPymtLbl.setGeometry(QRect(60, 10, 91, 31))
        self.totalPymtLbl.setMinimumSize(QSize(0, 0))
        font7 = QFont()
        font7.setFamilies([u"Inter Medium"])
        font7.setPointSize(11)
        font7.setBold(False)
        self.totalPymtLbl.setFont(font7)
        self.totalPymtLbl.setStyleSheet(u"color: white;\n"
"")
        self.update_prod_button_2 = QPushButton(self.widget_21)
        self.update_prod_button_2.setObjectName(u"update_prod_button_2")
        self.update_prod_button_2.setGeometry(QRect(170, 10, 100, 30))
        self.update_prod_button_2.setMinimumSize(QSize(100, 30))
        self.update_prod_button_2.setMaximumSize(QSize(100, 25))
        self.update_prod_button_2.setFont(font5)
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

        self.verticalLayout_10.addWidget(self.widget_21)


        self.gridLayout.addWidget(self.OrderWidget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_16.toggled.connect(self.icon_only.setHidden)
        self.pushButton_16.toggled.connect(self.word_iicon.setVisible)
        self.dashboard2.toggled.connect(self.dashboard1.setChecked)
        self.dashboard1.toggled.connect(self.dashboard2.setChecked)
        self.add_item1.toggled.connect(self.add_item2.setChecked)
        self.add_item2.toggled.connect(self.add_item1.setChecked)
        self.update_item2.toggled.connect(self.update_item1.setChecked)
        self.update_item1.toggled.connect(self.update_item2.setChecked)
        self.delete_item1.toggled.connect(self.delete_item1_2.setChecked)
        self.delete_item1_2.toggled.connect(self.delete_item1.setChecked)
        self.logout2.toggled.connect(MainWindow.close)
        self.logout1.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.dashboard1.setText("")
        self.add_item1.setText("")
        self.update_item1.setText("")
        self.delete_item1.setText("")
        self.logout1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Coffito Cafe", None))
        self.dashboard2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.add_item2.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.update_item2.setText(QCoreApplication.translate("MainWindow", u"Update Item", None))
        self.delete_item1_2.setText(QCoreApplication.translate("MainWindow", u"Delete Item", None))
        self.logout2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_16.setText("")
        self.dashboardTxt_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to Coffito Cafe", None))
        self.DateTimeLabel.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Coffito Cafe Menu", None))
        self.searchItemBtn.setText("")
        self.searchMenuItem.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_24.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"AMERICAN VANILLA", None))
        self.pushButton_25.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"STRAWBERRY LATTE", None))
        self.pushButton_23.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"VIETNAMESE LATTE", None))
        self.pushButton_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"LATTE", None))
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"AMERICANO", None))
        self.pushButton_11.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MATCHA", None))
        self.pushButton_9.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"SPANISH LATTE", None))
        self.pushButton_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CARAMEL", None))
        self.pushButton_12.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ICED CHOCO", None))
        self.pushButton_10.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"MOCHA", None))
        self.pushButton_22.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"MATCHA COFFEE", None))
        self.pushButton_32.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"UBE LATTE", None))
        self.pushButton_4.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"VANILLA", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Order List", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.totalPymtLbl.setText("")
        self.update_prod_button_2.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
    # retranslateUi

