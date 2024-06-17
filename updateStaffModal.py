# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manageUserStaffXwEgTz.ui'
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

class UpdateStaffWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName(u"MainWindow")
        self.resize(470, 412)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
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
        self.updateStaff_Modal = QWidget(self.widget)
        self.updateStaff_Modal.setObjectName(u"updateStaff_Modal")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updateStaff_Modal.sizePolicy().hasHeightForWidth())
        self.updateStaff_Modal.setSizePolicy(sizePolicy)
        self.updateStaff_Modal.setMinimumSize(QSize(300, 300))
        self.updateStaff_Modal.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(59,59,59);\n"
"	border-radius:10px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.updateStaff_Modal)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.staffAccount = QLabel(self.updateStaff_Modal)
        self.staffAccount.setObjectName(u"staffAccount")
        font = QFont()
        font.setFamilies([u"Inter ExtraBold"])
        font.setPointSize(24)
        font.setBold(True)
        self.staffAccount.setFont(font)
        self.staffAccount.setStyleSheet(u"QLabel{\n"
"	color:white;\n"
"	text-align:center;\n"
"}")

        self.verticalLayout_4.addWidget(self.staffAccount, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.staffUsername = QLineEdit(self.updateStaff_Modal)
        self.staffUsername.setObjectName(u"staffUsername")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.staffUsername.sizePolicy().hasHeightForWidth())
        self.staffUsername.setSizePolicy(sizePolicy1)
        self.staffUsername.setMinimumSize(QSize(200, 35))
        self.staffUsername.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Poppins Medium"])
        font1.setPointSize(11)
        self.staffUsername.setFont(font1)
        self.staffUsername.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_3.addWidget(self.staffUsername, 0, Qt.AlignmentFlag.AlignHCenter)

        self.staff_new_pass = QLineEdit(self.updateStaff_Modal)
        self.staff_new_pass.setObjectName(u"staff_new_pass")
        sizePolicy1.setHeightForWidth(self.staff_new_pass.sizePolicy().hasHeightForWidth())
        self.staff_new_pass.setSizePolicy(sizePolicy1)
        self.staff_new_pass.setMinimumSize(QSize(200, 35))
        self.staff_new_pass.setMaximumSize(QSize(16777215, 30))
        self.staff_new_pass.setFont(font1)
        self.staff_new_pass.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_3.addWidget(self.staff_new_pass, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalSpacer_6 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.widget_2 = QWidget(self.updateStaff_Modal)
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

        self.updateStaffBtn = QPushButton(self.widget_2)
        self.updateStaffBtn.setObjectName(u"updateStaffBtn")
        self.updateStaffBtn.setMinimumSize(QSize(100, 30))
        self.updateStaffBtn.setMaximumSize(QSize(100, 25))
        self.updateStaffBtn.setFont(font2)
        self.updateStaffBtn.setStyleSheet(u"QPushButton {\n"
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
        self.updateStaffBtn.setCheckable(True)
        self.updateStaffBtn.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.updateStaffBtn)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.verticalSpacer_7 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)


        self.verticalLayout_2.addWidget(self.updateStaff_Modal)


        self.verticalLayout.addWidget(self.widget)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        self.cancelBtn.toggled.connect(self.close)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.staffAccount.setText(QCoreApplication.translate("MainWindow", u"Manage Staff Account", None))
        self.staffUsername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.staff_new_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.cancelBtn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.updateStaffBtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

