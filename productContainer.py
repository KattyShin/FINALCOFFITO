# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prodContainereWbuEc.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(120, 160)
        Form.setMinimumSize(QSize(120, 160))
        Form.setMaximumSize(QSize(168, 178))
        Form.setStyleSheet(u"background-color: transparent;\n"
"")
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.productWidget = QWidget(Form)
        self.productWidget.setObjectName(u"productWidget")
        self.productWidget.setMinimumSize(QSize(120, 160))
        self.productWidget.setMaximumSize(QSize(120, 160))
        self.productWidget.setSizeIncrement(QSize(40, 0))
        self.productWidget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(59, 59, 59);\n"
"	border-radius: 5px;\n"
"}\n"
"QWidget:hover {\n"
"	background-color: rgb(79, 79, 79);\n"
" }         ")
        self.verticalLayout_9 = QVBoxLayout(self.productWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, -1)
        self.productBtn = QPushButton(self.productWidget)
        self.productBtn.setObjectName(u"productBtn")
        self.productBtn.setStyleSheet(u"QPushButton{\n"
"	border: none\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(79, 79, 79);\n"
"}\n"
"QPushButton:pressed {\n"
"     background-color: rgb(99, 99, 99);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/iCons/icons/coffee-cup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.productBtn.setIcon(icon)
        self.productBtn.setIconSize(QSize(70, 120))
        self.productBtn.setCheckable(True)

        self.verticalLayout_9.addWidget(self.productBtn)

        self.prodNameLabel = QLabel(self.productWidget)
        self.prodNameLabel.setObjectName(u"prodNameLabel")
        font = QFont()
        font.setFamilies([u"Inter SemiBold"])
        font.setPointSize(10)
        font.setBold(True)
        self.prodNameLabel.setFont(font)
        self.prodNameLabel.setStyleSheet(u"color:white;\n"
"text-align: center;\n"
"background-color: none;\n"
"\n"
"")
        self.prodNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.prodNameLabel.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.prodNameLabel)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.productWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.productBtn.setText("")
        self.prodNameLabel.setText(QCoreApplication.translate("Form", u"VANILLA", None))
    # retranslateUi

