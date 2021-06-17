from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

width, height = 500, 400
class app(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setGeometry(200, 200, width, height)
        self.setWindowTitle("ass")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Weekly ToDo')
        self.label.move((width // 2) - self.label.width() // 4, 20)

def run():
    App = QApplication(sys.argv)
    win = app()
    win.show()
    sys.exit(App.exec_())
run()