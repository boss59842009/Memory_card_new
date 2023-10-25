from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

app = QApplication([])

from card_window import *

card_win.setWindowTitle("Memory card")
card_win.resize(600, 500)
card_win.show()

app.exec_()