# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_UI_v4UdXXlJ.ui'
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources
import resource1_rc
import main_resources
import resource1_rcc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1078, 536)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.icon_only = QWidget(self.widget_2)
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
        self.verticalLayout_6 = QVBoxLayout(self.icon_only)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, -1, 3, -1)
        self.label_4 = QLabel(self.icon_only)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setMaximumSize(QSize(40, 31))
        self.label_4.setPixmap(QPixmap(u":/iCons/icons/Green Simple Monoline Badge CK Letter Logo (3).png"))
        self.label_4.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.dashboard1_2 = QPushButton(self.icon_only)
        self.dashboard1_2.setObjectName(u"dashboard1_2")
        icon = QIcon()
        icon.addFile(u":/iCons/icons/icons8-coffee-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/iCons/icons/icons8-coffee0-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard1_2.setIcon(icon)
        self.dashboard1_2.setIconSize(QSize(25, 25))
        self.dashboard1_2.setCheckable(True)
        self.dashboard1_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.dashboard1_2)

        self.add_item1_2 = QPushButton(self.icon_only)
        self.add_item1_2.setObjectName(u"add_item1_2")
        icon1 = QIcon()
        icon1.addFile(u":/iCons/icons/icons8-add-folder-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/iCons/icons/icons8-add-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.add_item1_2.setIcon(icon1)
        self.add_item1_2.setIconSize(QSize(22, 22))
        self.add_item1_2.setCheckable(True)
        self.add_item1_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.add_item1_2)

        self.update_item1_2 = QPushButton(self.icon_only)
        self.update_item1_2.setObjectName(u"update_item1_2")
        icon2 = QIcon()
        icon2.addFile(u":/iCons/icons/icons8-edit-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/iCons/icons/icons8-edit-40 (1).png", QSize(), QIcon.Normal, QIcon.On)
        self.update_item1_2.setIcon(icon2)
        self.update_item1_2.setIconSize(QSize(22, 22))
        self.update_item1_2.setCheckable(True)
        self.update_item1_2.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.update_item1_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalSpacer_3 = QSpacerItem(20, 182, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.logout1_2 = QPushButton(self.icon_only)
        self.logout1_2.setObjectName(u"logout1_2")
        icon3 = QIcon()
        icon3.addFile(u":/iCons/icons/icons8-logout-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/iCons/icons/icons8-logouto-40.png", QSize(), QIcon.Normal, QIcon.On)
        self.logout1_2.setIcon(icon3)
        self.logout1_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.logout1_2)


        self.horizontalLayout_2.addWidget(self.icon_only, 0, Qt.AlignLeft)

        self.word_iicon = QWidget(self.widget_2)
        self.word_iicon.setObjectName(u"word_iicon")
        self.word_iicon.setMinimumSize(QSize(170, 0))
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
        self.verticalLayout_8 = QVBoxLayout(self.word_iicon)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 20, -1)
        self.label_5 = QLabel(self.word_iicon)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(40, 40))
        self.label_5.setMaximumSize(QSize(40, 31))
        self.label_5.setPixmap(QPixmap(u":/iCons/icons/Green Simple Monoline Badge CK Letter Logo (3).png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.word_iicon)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamilies([u"Poppins SemiBold"])
        font.setPointSize(14)
        font.setBold(False)
        self.label_6.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 20, -1, -1)
        self.dashboard2_2 = QPushButton(self.word_iicon)
        self.dashboard2_2.setObjectName(u"dashboard2_2")
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(11)
        self.dashboard2_2.setFont(font1)
        self.dashboard2_2.setIcon(icon)
        self.dashboard2_2.setIconSize(QSize(25, 25))
        self.dashboard2_2.setCheckable(True)
        self.dashboard2_2.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.dashboard2_2)

        self.add_item2_2 = QPushButton(self.word_iicon)
        self.add_item2_2.setObjectName(u"add_item2_2")
        self.add_item2_2.setFont(font1)
        self.add_item2_2.setIcon(icon1)
        self.add_item2_2.setIconSize(QSize(22, 22))
        self.add_item2_2.setCheckable(True)
        self.add_item2_2.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.add_item2_2)

        self.update_item2_2 = QPushButton(self.word_iicon)
        self.update_item2_2.setObjectName(u"update_item2_2")
        self.update_item2_2.setFont(font1)
        self.update_item2_2.setIcon(icon2)
        self.update_item2_2.setIconSize(QSize(22, 22))
        self.update_item2_2.setCheckable(True)
        self.update_item2_2.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.update_item2_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.verticalSpacer_4 = QSpacerItem(20, 180, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.logout2_2 = QPushButton(self.word_iicon)
        self.logout2_2.setObjectName(u"logout2_2")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        self.logout2_2.setFont(font2)
        self.logout2_2.setIcon(icon3)
        self.logout2_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.logout2_2)


        self.horizontalLayout_2.addWidget(self.word_iicon)


        self.horizontalLayout.addWidget(self.widget_2, 0, Qt.AlignLeft)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.widget_3)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_15 = QPushButton(self.widget_4)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(20, 16))
        self.pushButton_15.setMaximumSize(QSize(20, 16))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(31, 31, 31);\n"
"	border:none;\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/iCons/icons/icons8-menu-40.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/iCons/icons/icons8-menu-40-1.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_15.setIcon(icon4)
        self.pushButton_15.setIconSize(QSize(16, 16))
        self.pushButton_15.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pushButton_15)

        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setFamilies([u"Poppins SemiBold"])
        font3.setPointSize(14)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.search_frame = QWidget(self.widget_4)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(100, 0))
        self.search_frame.setMaximumSize(QSize(150, 16777215))
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
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.pushButton_14.setFont(font4)
        self.pushButton_14.setStyleSheet(u"background-color: none;\n"
"border-radius:15px;\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/iCons/icons/icons8-search-26.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon5)

        self.horizontalLayout_10.addWidget(self.pushButton_14)

        self.lineEdit_3 = QLineEdit(self.search_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(37, 37, 37);")

        self.horizontalLayout_10.addWidget(self.lineEdit_3)


        self.verticalLayout_14.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_5.addWidget(self.search_frame)


        self.verticalLayout_10.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.widget_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, -1, -1)
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.widget_7)
        self.label_8.setObjectName(u"label_8")
        font5 = QFont()
        font5.setFamilies([u"Poppins SemiBold"])
        font5.setPointSize(12)
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: white;\n"
"")

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout_11.addWidget(self.widget_7)

        self.scrollArea = QScrollArea(self.widget_5)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	border: none;\n"
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
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 535, 786))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 768))
        self.frame.setStyleSheet(u"background-color: rgb(31, 31, 31);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(120, 100))
        self.pushButton_5.setMaximumSize(QSize(120, 130))
        self.pushButton_5.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/iCons/icons/coffee-cup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(80, 80))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 0))
        self.pushButton_6.setMaximumSize(QSize(120, 40))
        font6 = QFont()
        font6.setFamilies([u"Poppins Medium"])
        font6.setPointSize(11)
        self.pushButton_6.setFont(font6)
        self.pushButton_6.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_6)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(120, 100))
        self.pushButton_3.setMaximumSize(QSize(120, 130))
        self.pushButton_3.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(80, 80))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 0))
        self.pushButton_4.setMaximumSize(QSize(120, 40))
        self.pushButton_4.setFont(font6)
        self.pushButton_4.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_61 = QPushButton(self.frame)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setMinimumSize(QSize(120, 100))
        self.pushButton_61.setMaximumSize(QSize(120, 130))
        self.pushButton_61.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_61.setIcon(icon6)
        self.pushButton_61.setIconSize(QSize(80, 80))
        self.pushButton_61.setCheckable(True)
        self.pushButton_61.setAutoExclusive(True)

        self.verticalLayout_38.addWidget(self.pushButton_61)

        self.pushButton_62 = QPushButton(self.frame)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setMinimumSize(QSize(0, 0))
        self.pushButton_62.setMaximumSize(QSize(120, 40))
        self.pushButton_62.setFont(font6)
        self.pushButton_62.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_62.setCheckable(True)
        self.pushButton_62.setAutoExclusive(True)

        self.verticalLayout_38.addWidget(self.pushButton_62)


        self.gridLayout_2.addLayout(self.verticalLayout_38, 2, 0, 1, 1)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_67 = QPushButton(self.frame)
        self.pushButton_67.setObjectName(u"pushButton_67")
        self.pushButton_67.setMinimumSize(QSize(120, 100))
        self.pushButton_67.setMaximumSize(QSize(120, 130))
        self.pushButton_67.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_67.setIcon(icon6)
        self.pushButton_67.setIconSize(QSize(80, 80))
        self.pushButton_67.setCheckable(True)
        self.pushButton_67.setAutoExclusive(True)

        self.verticalLayout_41.addWidget(self.pushButton_67)

        self.pushButton_68 = QPushButton(self.frame)
        self.pushButton_68.setObjectName(u"pushButton_68")
        self.pushButton_68.setMinimumSize(QSize(0, 0))
        self.pushButton_68.setMaximumSize(QSize(120, 40))
        self.pushButton_68.setFont(font6)
        self.pushButton_68.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_68.setCheckable(True)
        self.pushButton_68.setAutoExclusive(True)

        self.verticalLayout_41.addWidget(self.pushButton_68)


        self.gridLayout_2.addLayout(self.verticalLayout_41, 2, 3, 1, 1)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_69 = QPushButton(self.frame)
        self.pushButton_69.setObjectName(u"pushButton_69")
        self.pushButton_69.setMinimumSize(QSize(120, 100))
        self.pushButton_69.setMaximumSize(QSize(120, 130))
        self.pushButton_69.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_69.setIcon(icon6)
        self.pushButton_69.setIconSize(QSize(80, 80))
        self.pushButton_69.setCheckable(True)
        self.pushButton_69.setAutoExclusive(True)

        self.verticalLayout_42.addWidget(self.pushButton_69)

        self.pushButton_70 = QPushButton(self.frame)
        self.pushButton_70.setObjectName(u"pushButton_70")
        self.pushButton_70.setMinimumSize(QSize(0, 0))
        self.pushButton_70.setMaximumSize(QSize(120, 40))
        self.pushButton_70.setFont(font6)
        self.pushButton_70.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_70.setCheckable(True)
        self.pushButton_70.setAutoExclusive(True)

        self.verticalLayout_42.addWidget(self.pushButton_70)


        self.gridLayout_2.addLayout(self.verticalLayout_42, 3, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_13 = QPushButton(self.frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(120, 100))
        self.pushButton_13.setMaximumSize(QSize(120, 130))
        self.pushButton_13.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_13.setIcon(icon6)
        self.pushButton_13.setIconSize(QSize(80, 80))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.pushButton_13)

        self.pushButton_16 = QPushButton(self.frame)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 0))
        self.pushButton_16.setMaximumSize(QSize(120, 40))
        self.pushButton_16.setFont(font6)
        self.pushButton_16.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setAutoExclusive(True)

        self.verticalLayout_15.addWidget(self.pushButton_16)


        self.gridLayout_2.addLayout(self.verticalLayout_15, 0, 3, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 6)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 100))
        self.pushButton.setMaximumSize(QSize(120, 130))
        self.pushButton.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(80, 80))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setMaximumSize(QSize(120, 40))
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_21 = QPushButton(self.frame)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(120, 100))
        self.pushButton_21.setMaximumSize(QSize(120, 130))
        self.pushButton_21.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_21.setIcon(icon6)
        self.pushButton_21.setIconSize(QSize(80, 80))
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 0))
        self.pushButton_22.setMaximumSize(QSize(120, 40))
        self.pushButton_22.setFont(font6)
        self.pushButton_22.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setAutoExclusive(True)

        self.verticalLayout_18.addWidget(self.pushButton_22)


        self.gridLayout_2.addLayout(self.verticalLayout_18, 1, 0, 1, 1)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_65 = QPushButton(self.frame)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setMinimumSize(QSize(120, 100))
        self.pushButton_65.setMaximumSize(QSize(120, 130))
        self.pushButton_65.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_65.setIcon(icon6)
        self.pushButton_65.setIconSize(QSize(80, 80))
        self.pushButton_65.setCheckable(True)
        self.pushButton_65.setAutoExclusive(True)

        self.verticalLayout_40.addWidget(self.pushButton_65)

        self.pushButton_66 = QPushButton(self.frame)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setMinimumSize(QSize(0, 0))
        self.pushButton_66.setMaximumSize(QSize(120, 40))
        self.pushButton_66.setFont(font6)
        self.pushButton_66.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_66.setCheckable(True)
        self.pushButton_66.setAutoExclusive(True)

        self.verticalLayout_40.addWidget(self.pushButton_66)


        self.gridLayout_2.addLayout(self.verticalLayout_40, 2, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_17 = QPushButton(self.frame)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(120, 100))
        self.pushButton_17.setMaximumSize(QSize(120, 130))
        self.pushButton_17.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_17.setIcon(icon6)
        self.pushButton_17.setIconSize(QSize(80, 80))
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoExclusive(True)

        self.verticalLayout_16.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 0))
        self.pushButton_18.setMaximumSize(QSize(120, 40))
        self.pushButton_18.setFont(font6)
        self.pushButton_18.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoExclusive(True)

        self.verticalLayout_16.addWidget(self.pushButton_18)


        self.gridLayout_2.addLayout(self.verticalLayout_16, 1, 3, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_19 = QPushButton(self.frame)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(120, 100))
        self.pushButton_19.setMaximumSize(QSize(120, 130))
        self.pushButton_19.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_19.setIcon(icon6)
        self.pushButton_19.setIconSize(QSize(80, 80))
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.frame)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(0, 0))
        self.pushButton_20.setMaximumSize(QSize(120, 40))
        self.pushButton_20.setFont(font6)
        self.pushButton_20.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setAutoExclusive(True)

        self.verticalLayout_17.addWidget(self.pushButton_20)


        self.gridLayout_2.addLayout(self.verticalLayout_17, 1, 1, 1, 1)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_63 = QPushButton(self.frame)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setMinimumSize(QSize(120, 100))
        self.pushButton_63.setMaximumSize(QSize(120, 130))
        self.pushButton_63.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_63.setIcon(icon6)
        self.pushButton_63.setIconSize(QSize(80, 80))
        self.pushButton_63.setCheckable(True)
        self.pushButton_63.setAutoExclusive(True)

        self.verticalLayout_39.addWidget(self.pushButton_63)

        self.pushButton_64 = QPushButton(self.frame)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setMinimumSize(QSize(0, 0))
        self.pushButton_64.setMaximumSize(QSize(120, 40))
        self.pushButton_64.setFont(font6)
        self.pushButton_64.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_64.setCheckable(True)
        self.pushButton_64.setAutoExclusive(True)

        self.verticalLayout_39.addWidget(self.pushButton_64)


        self.gridLayout_2.addLayout(self.verticalLayout_39, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, 6)
        self.pushButton_23 = QPushButton(self.frame)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(120, 100))
        self.pushButton_23.setMaximumSize(QSize(120, 130))
        self.pushButton_23.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"\n"
"    border: none; \n"
"    border-top-right-radius: 8px;\n"
"    border-top-left-radius: 8px;  \n"
"    font-size: 12px; \n"
"    font-family: Arial, sans-serif; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_23.setIcon(icon6)
        self.pushButton_23.setIconSize(QSize(80, 80))
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setAutoExclusive(True)

        self.verticalLayout_19.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.frame)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(0, 0))
        self.pushButton_24.setMaximumSize(QSize(120, 40))
        self.pushButton_24.setFont(font6)
        self.pushButton_24.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #3B3B3B;\n"
"    color: white;\n"
"	text-align: bottom;\n"
"    padding-bottom: 15px;\n"
"    border: none; \n"
"    border-bottom-left-radius: 8px; \n"
"    border-bottom-right-radius: 8px; \n"
"    transition: background-color 0.3s, color 0.3s, box-shadow 0.3s; \n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5B5B5B; \n"
"    color: #FF8C18; \n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B2B2B; \n"
"    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3) inset; \n"
"}\n"
"")
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setAutoExclusive(True)

        self.verticalLayout_19.addWidget(self.pushButton_24)


        self.gridLayout_2.addLayout(self.verticalLayout_19, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)


        self.verticalLayout_10.addWidget(self.widget_5)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.widget_6.setMinimumSize(QSize(290, 0))
        self.widget_6.setMaximumSize(QSize(600, 16777215))
        self.widget_6.setStyleSheet(u"background-color:rgb(59,59,59);")

        self.horizontalLayout.addWidget(self.widget_6, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_15.toggled.connect(self.word_iicon.setVisible)
        self.pushButton_15.toggled.connect(self.icon_only.setHidden)
        self.dashboard1_2.toggled.connect(self.dashboard2_2.setChecked)
        self.dashboard2_2.toggled.connect(self.dashboard1_2.setChecked)
        self.add_item1_2.toggled.connect(self.add_item2_2.setChecked)
        self.add_item2_2.toggled.connect(self.add_item1_2.setChecked)
        self.update_item1_2.toggled.connect(self.update_item2_2.setChecked)
        self.update_item2_2.toggled.connect(self.update_item1_2.setChecked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard1_2.setText("")
        self.add_item1_2.setText("")
        self.update_item1_2.setText("")
        self.logout1_2.setText("")
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CoFFiTo", None))
        self.dashboard2_2.setText(QCoreApplication.translate("MainWindow", u"  Dashboard", None))
        self.add_item2_2.setText(QCoreApplication.translate("MainWindow", u"  Add Item", None))
        self.update_item2_2.setText(QCoreApplication.translate("MainWindow", u"  Update Item", None))
        self.logout2_2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_15.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Welcome to CoFFiTo Cafe", None))
        self.pushButton_14.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CoFFiTo Menu", None))
        self.pushButton_5.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"AMERICANO", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"MATCHA", None))
        self.pushButton_61.setText("")
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"AMERICAN VANILLA", None))
        self.pushButton_67.setText("")
        self.pushButton_68.setText(QCoreApplication.translate("MainWindow", u"LATTE", None))
        self.pushButton_69.setText("")
        self.pushButton_70.setText(QCoreApplication.translate("MainWindow", u"VANILLA", None))
        self.pushButton_13.setText("")
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"MOCHA", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"VIETNAMESE LATTE", None))
        self.pushButton_21.setText("")
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"SPANISH LATTE", None))
        self.pushButton_65.setText("")
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"MATCHA COFFEE", None))
        self.pushButton_17.setText("")
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"MATCHA", None))
        self.pushButton_19.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"ICED CHOCO", None))
        self.pushButton_63.setText("")
        self.pushButton_64.setText(QCoreApplication.translate("MainWindow", u"UBE LATTE", None))
        self.pushButton_23.setText("")
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"STRAWBERRY LATTE", None))
    # retranslateUi

