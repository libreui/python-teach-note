import sys
import _thread
from PyQt5.QtGui import QColor, QMovie
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QTextEdit, QFileDialog, QMessageBox
import os
from mainWindow import *
from transformWindow import *
from tools import common, word_to_pdf


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(100, 100, 1024, 600)
        self.setWindowTitle("Word 助手")
        self.setFixedSize(1024, 600)


class TransformWindow(QMainWindow, Ui_transformWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showLoading.setScaledContents(True)
        self.showLoading.setText("")
        self.showLoading.setMinimumWidth(100)
        self.gif = QMovie("image/loading.gif")

        self.file_list = []

        # 绑定源按钮点击槽函数
        self.sourcebrowseButton.clicked.connect(self.source_browse_button_clicked)
        # 绑定目标按钮点击槽函数
        self.targetbrowseButton.clicked.connect(self.target_browse_button_clicked)
        # 绑定批量转换电机槽函数
        self.multipeExecute.clicked.connect(self.multiple_execute_click)

    def open(self):
        self.__init__()
        self.show()

    def source_browse_button_clicked(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择源文件目录",
                                                    r"/Users/libre1/Desktop")
        if dir_path == "":
            return

        self.sourcepath.setText(dir_path)
        self.listword.clear()
        self.file_list = common.git_file_names(dir_path)
        self.listword.addItems(self.file_list)


    def target_browse_button_clicked(self):
        dir_path = QFileDialog.getExistingDirectory(self, "请选择目标文件目录",
                                                    r"/Users/libre1/Desktop")
        self.targetpath.setText(dir_path)


    def multiple_execute_click(self):
        # 判断是否选择了源文件，如果没有选择，弹出提示框
        if self.listword.count() == 0:
            QMessageBox.warning(self, "警告", "请选择源文件目录")
            return
        target_path = self.targetpath.text()
        # 判断是否选择了目标文件，如果没有选择，弹出提示框
        if not os.path.exists(target_path):
            QMessageBox.warning(self, "警告", "请选择目标文件目录")
            return
        # 清空结果列表
        self.listpdf.clear()
        self.showLoading.setMovie(self.gif)
        self.gif.start()
        # 开启线程进行转换
        _thread.start_new_thread(self.execute, ())

    def execute(self):
        target_path = self.targetpath.text()
        # 实现word批量转换为PDF
        value_list = word_to_pdf.word_to_pdf(self.file_list, target_path)
        if value_list:
            self.showLoading.clear()
            self.showLoading.setText("转换完成")
            self.listpdf.addItems(value_list)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()

    # 连接菜单中word转pdf的槽函数
    transformWindow = TransformWindow()
    myWin.actionWord_PDF.triggered.connect(transformWindow.open)
    sys.exit(app.exec_())
