import sys
from PySide6 import QtWidgets
from INF.GUI.main_window import Ui_FakeNews_window

app = QtWidgets.QApplication(sys.argv)
win = Ui_FakeNews_window()
win.show()
sys.exit(app.exec())
