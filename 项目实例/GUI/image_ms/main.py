import os
import subprocess

from PIL import Image, ImageFont, ImageDraw, ImageEnhance

from mainWindow import *
from markWindow import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QFontMetrics, QFontInfo
import sys



class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setFixedSize(800, 600)


class MyMarkWindow(QMainWindow, Ui_MarkWindow):
    def __init__(self, parent=None):
        super(MyMarkWindow, self).__init__(parent)
        # 设置不能拉伸，只有关闭按钮
        self.setFixedSize(654, 600)
        self.setWindowTitle("设置水印")
        self.setupUi(self)

        # 选中图片文件夹路径
        self.images_path = ""

        # 选中的字体
        self.font = ""
        self.font_size: QFontMetrics = None
        self.font_info: QFontInfo = None

        # 水印图片
        self.image_mark = ""

        # 打完水印后保存位置
        self.save_path = ""

        # 水印类型
        self.mark_type = ""
        # 水印位置
        self.mark_position = ""
        # 水印透明度
        self.mark_alpha = 0.5

        # 初始化UI
        self.init_ui()
        # 初始化连接
        self.set_connect()

    def init_ui(self):
        self.rb_word_mark.setChecked(True)


    def set_connect(self):

        # 添加图片加载槽函数
        self.btn_load_image.clicked.connect(self.load_images)
        # 绑定listWidget的点击事件
        self.listWidget.itemDoubleClicked.connect(self.item_click)
        # 添加字体按钮槽函数
        self.btn_font.clicked.connect(self.set_font)
        # 添加水印图片按钮槽函数
        self.btn_image_path.clicked.connect(self.set_image)
        # 添加保存路径按钮槽函数
        self.btn_save_path.clicked.connect(self.set_save_path)
        # 添加应用按钮槽函数
        self.btn_apply.clicked.connect(self.apply)

    def load_images(self):
        # 打开文件对话框，选择图片文件
        self.images_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹", os.getcwd())
        image_list = os.listdir(self.images_path)
        num = 0
        for image in image_list:
            if image.endswith(".jpg") or image.endswith(".png") or image.endswith(".jpeg"):
                num += 1
            self.listWidget.addItem(image)
        self.statusbar.showMessage(f"共选择了{num}张图片")


    def item_click(self, item):
        # 获取选中的图片文件名
        try:
            file_name = f"{self.images_path}/{item.text()}"
            # Windows打开
            # os.startfile(file_name)
            # mac 打开文件
            subprocess.run(["open", file_name], check=True)
        except Exception as e:
            print(f"打开图片失败：{e}")


    def set_font(self):
        self.font, ok = QtWidgets.QFontDialog.getFont()
        if ok:
            self.le_word.setFont(self.font)
            self.font_size = QFontMetrics(self.font)
            self.font_info = QFontInfo(self.font)

    def set_image(self):
        try:
            self.image_mark = QFileDialog.getOpenFileName(
                None, "选择水印图片", os.getcwd(),
                "图片文件(*.jpg *.png *.jpeg *.bmp)")
            self.le_image_path.setText(self.image_mark[0])
        except Exception as e:
            print(f"打开图片失败：{e}")


    def set_save_path(self):
        try:
            self.save_path = QFileDialog.getExistingDirectory(
                None, "选择保存路径", os.getcwd())
            self.le_save_path.setText(self.save_path)
        except Exception as e:
            print(f"打开路径失败：{e}")

    def apply(self):
        # 获取选中列表中的图片地址
        image = f"{self.images_path}/{self.listWidget.currentItem().text()}"
        print(image)
        # 获取水印类型
        if self.rb_word_mark.isChecked():
            self.apply_text_mark(image, self.save_path)
        elif self.rb_image_mark.isChecked():
            self.mark_type = "图片"

    def apply_text_mark(self, img, save_path):
        try:
            # 获取水印文本
            im = Image.open(img).convert('RGBA')
            new_image = Image.new('RGBA', im.size, (255, 255, 255, 0))
            # 字体
            font = ImageFont.truetype("SimSong", self.font_info.pointSize())
            # 创建绘制对象
            image_draw = ImageDraw.Draw(new_image)
            # 图片的宽高
            img_w, img_h = im.size
            # 文字的宽高
            text_w = self.font_size.maxWidth() * len(self.le_word.text())
            text_h = self.font_size.height()
            # 设置水印文字位置
            if self.cbx_postion.currentText() == "左上角":
                position = (0, 0)
            elif self.cbx_postion.currentText() == "左下角":
                position = (0, img_h - text_h)
            elif self.cbx_postion.currentText() == "右上角":
                position = (img_w - text_w, 0)
            elif self.cbx_postion.currentText() == "右下角":
                position = (img_w - text_w, img_h - text_h)
            else:
                position = (img_w // 2 - text_w // 2, img_h // 2 - text_h // 2)
            # 设置文本颜色
            image_draw.text(position, self.le_word.text(), fill="#FCA454", font=font)
            # 设置透明度
            alpha = new_image.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(self.sld_alphe.value()/10)
            new_image.putalpha(alpha)
            Image.alpha_composite(im, new_image).save(save_path)
        except Exception as e:
            QMessageBox.warning(self, "警告", f"打水印失败：{e}")


    def open(self):
        self.__init__()
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()

    # 实例化mark窗口
    markWindow = MyMarkWindow()

    # 连接按钮的点击事件到mark窗口的open方法
    mainWindow.actionMark.triggered.connect(markWindow.open)


    mainWindow.show()
    sys.exit(app.exec_())
