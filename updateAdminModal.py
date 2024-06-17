# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manageUserAdminsxnZXl.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class UpdateAdminWindow(QMainWindow):
     def __init__(self):
        super().__init__()
        self.setupUi()

     def setupUi(self):
        self.setObjectName(u"MainWindow")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(470, 412)
        
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
        self.updateAdmin_Modal = QWidget(self.widget)
        self.updateAdmin_Modal.setObjectName(u"updateAdmin_Modal")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateAdmin_Modal.sizePolicy().hasHeightForWidth())
        self.updateAdmin_Modal.setSizePolicy(sizePolicy)
        self.updateAdmin_Modal.setMinimumSize(QSize(300, 300))
        self.updateAdmin_Modal.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(59,59,59);\n"
"	border-radius:10px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.updateAdmin_Modal)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.dashboardTxt = QLabel(self.updateAdmin_Modal)
        self.dashboardTxt.setObjectName(u"dashboardTxt")
        font = QFont()
        font.setFamilies([u"Inter ExtraBold"])
        font.setPointSize(24)
        font.setBold(True)
        self.dashboardTxt.setFont(font)
        self.dashboardTxt.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"	text-align:center;\n"
"}")

        self.verticalLayout_4.addWidget(self.dashboardTxt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.adminUsername = QLineEdit(self.updateAdmin_Modal)
        self.adminUsername.setObjectName(u"adminUsername")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.adminUsername.sizePolicy().hasHeightForWidth())
        self.adminUsername.setSizePolicy(sizePolicy1)
        self.adminUsername.setMinimumSize(QSize(200, 35))
        self.adminUsername.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Poppins Medium"])
        font1.setPointSize(11)
        self.adminUsername.setFont(font1)
        self.adminUsername.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_3.addWidget(self.adminUsername, 0, Qt.AlignmentFlag.AlignHCenter)

        self.admin_new_pass = QLineEdit(self.updateAdmin_Modal)
        self.admin_new_pass.setObjectName(u"admin_new_pass")
        sizePolicy1.setHeightForWidth(self.admin_new_pass.sizePolicy().hasHeightForWidth())
        self.admin_new_pass.setSizePolicy(sizePolicy1)
        self.admin_new_pass.setMinimumSize(QSize(200, 35))
        self.admin_new_pass.setMaximumSize(QSize(16777215, 30))
        self.admin_new_pass.setFont(font1)
        self.admin_new_pass.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_3.addWidget(self.admin_new_pass, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_6 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.widget_2 = QWidget(self.updateAdmin_Modal)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(70, -1, 70, -1)
        self.cancelBtn = QPushButton(self.widget_2)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(100, 30))
        self.cancelBtn.setMaximumSize(QSize(100, 25))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.cancelBtn.setFont(font2)
        self.cancelBtn.setStyleSheet(u"QPushButton {\n"
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
        self.cancelBtn.setCheckable(True)
        self.cancelBtn.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.cancelBtn)

        self.updateAdmin = QPushButton(self.widget_2)
        self.updateAdmin.setObjectName(u"updateAdmin")
        self.updateAdmin.setMinimumSize(QSize(100, 30))
        self.updateAdmin.setMaximumSize(QSize(100, 25))
        self.updateAdmin.setFont(font2)
        self.updateAdmin.setStyleSheet(u"QPushButton {\n"
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
        self.updateAdmin.setCheckable(True)
        self.updateAdmin.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.updateAdmin)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.verticalSpacer_7 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)


        self.verticalLayout_2.addWidget(self.updateAdmin_Modal)


        self.verticalLayout.addWidget(self.widget)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        self.cancelBtn.toggled.connect(self.close)

        QMetaObject.connectSlotsByName(self)
    # setupUi

     def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dashboardTxt.setText(QCoreApplication.translate("MainWindow", u"Manage Admin Account", None))
        self.adminUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.admin_new_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.cancelBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.updateAdmin.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi


