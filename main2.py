import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from UserInterface import userInterface
from PyQt6 import QtCore
from dotenv import load_dotenv



load_dotenv()
app = QApplication(sys.argv)

window = userInterface()

window.show()

app.exec()
