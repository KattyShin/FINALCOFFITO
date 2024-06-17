import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from sidebar import mySideBar
from addItemUI import AddItemWindow
from ui_updateItemUI2 import UpdateItemWindow

app = QApplication(sys.argv)

window = mySideBar()
window.show()

addItemWindow = AddItemWindow()
updateItemWindow = UpdateItemWindow()

app.exec()
