import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from UserInterface import userInterface


app = QApplication(sys.argv)

window = userInterface()

window.show()

app.exec()
