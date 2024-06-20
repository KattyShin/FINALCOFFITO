import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton


class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(40)
        self.setObjectName("CustomTitleBar")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.title_label = QLabel("Modern Title Bar")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        self.close_button = QPushButton("X")
        self.close_button.setObjectName("CloseButton")
        self.close_button.clicked.connect(self.parentWidget().close)
        layout.addWidget(self.close_button)