from mainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setFixedSize(800, 600)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
