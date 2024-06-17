# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginPageJaZQPq.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

import resource1_rc
import main_resources
import resource1_rcc
import psycopg2
from database_config import get_database_config  # Assuming you have a function to get database config
from AdminMain import Ui_MainWindow
from UserInterface import userInterface
from sidebar import mySideBar
from addItemUI import AddItemWindow
from ui_updateItemUI2 import UpdateItemWindow
from updateAdminModal import UpdateAdminWindow
from updateStaffModal import UpdateStaffWindow



class Login_MainWindow(QMainWindow):
    login_successful = Signal()

    def __init__(self):
        super().__init__()
        self.conn = None  # Initialize the connection attribute
        self.setupUi(self)
        self.userInterface = userInterface()


    def connect_to_database(self):
        try:
            config = get_database_config()
            conn = psycopg2.connect(**config)
            print("Database connection established successfully!")
            return conn
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)
            return None
   

    def check_login(self):
        print("Login check initiated.")
        admin_user_id = 9242
        staff_user_id = 9243

        username = self.lineEdit_7.text()  
        password = self.lineEdit_8.text()  

        

        try:
            if not self.conn:
                self.conn = self.connect_to_database()

            if not self.conn:
                return False

            cur = self.conn.cursor()

            query = "SELECT USER_ID, PASS_WORD FROM USERS WHERE USERNAME = %s AND PASS_WORD = %s"
            cur.execute(query, (username, password))

            user = cur.fetchone()
            cur.close()

            if user:
                user_id, _ = user  # Unpack fetched data

                if user_id == admin_user_id:
                    print("Login as admin!")

                    self.sidee = mySideBar()
                    self.mySideBar.show()
                    
                    self.addItemWindow = AddItemWindow()
                    self.updateItemWindow = UpdateItemWindow()
                    self.updateAdminWindow = UpdateAdminWindow()
                    self.UpdateStaffWindow = UpdateStaffWindow()
                    self.login_successful.emit()

                    self.lineEdit_7.setText("")  
                    self.lineEdit_8.setText("")  
                    return True

                elif user_id == staff_user_id:
                    print("Login as staff!")
                    self.userInterface.show()
                    self.lineEdit_7.setText("")  
                    self.lineEdit_8.setText("")  

                    return True

                else:
                    print("Login failed. Invalid username or password.")
                    return False

            else:
                print("Login failed. Invalid username or password.")
                return False

        except (Exception, psycopg2.Error) as error:
            print("Error while checking login credentials:", error)
            return False

    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 534)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color:#1F1F1F;\n"
"	\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 50, -1)
        self.rightWidget = QWidget(self.centralwidget)
        self.rightWidget.setObjectName(u"rightWidget")

        self.horizontalLayout.addWidget(self.rightWidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(500, 0))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u"CoffitoLogo (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(400, 400))

        self.verticalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(350, 494))
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QSize(300, 300))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(59,59,59);\n"
"	border-radius:10px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.dashboardTxt = QLabel(self.widget_3)
        self.dashboardTxt.setObjectName(u"dashboardTxt")
        font = QFont()
        font.setFamilies([u"Poppins SemiBold"])
        font.setPointSize(14)
        font.setBold(True)
        self.dashboardTxt.setFont(font)
        self.dashboardTxt.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"	text-align:center;\n"
"}")

        self.verticalLayout_3.addWidget(self.dashboardTxt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_7 = QLineEdit(self.widget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy1)
        self.lineEdit_7.setMinimumSize(QSize(185, 35))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Poppins Medium"])
        font1.setPointSize(11)
        self.lineEdit_7.setFont(font1)
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

        self.verticalLayout_2.addWidget(self.lineEdit_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_8 = QLineEdit(self.widget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy1.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy1)
        self.lineEdit_8.setMinimumSize(QSize(185, 35))
        self.lineEdit_8.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_8.setFont(font1)
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
        self.lineEdit_8.setEchoMode(QLineEdit.Password) ####
        self.verticalLayout_2.addWidget(self.lineEdit_8, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.loginButton_2 = QPushButton(self.widget_3)
        self.loginButton_2.setObjectName(u"loginButton_2")
        self.loginButton_2.setMinimumSize(QSize(185, 30))
        self.loginButton_2.setMaximumSize(QSize(150, 25))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.loginButton_2.setFont(font2)
        self.loginButton_2.setStyleSheet(u"QPushButton {\n"
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
        self.loginButton_2.setCheckable(True)
        self.loginButton_2.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.loginButton_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignRight)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")

        self.horizontalLayout.addWidget(self.widget_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.loginButton_2.clicked.connect(self.check_login)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.dashboardTxt.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginButton_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

