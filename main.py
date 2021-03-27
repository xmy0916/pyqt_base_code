import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap

root = os.getcwd()
sys.path.append(root)

from UI.UI_main import Ui_MainWindow
from car_control import MainCode_CarControl
from car_view import MainCode_CarView

class MainCode_UI1(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.mainUI = Ui_MainWindow()
        self.mainUI.MainWindow.show()
        self.picture_init()
        self.UI = {"main":self.mainUI,"car_control":None,"car_view":None}
        self.button_init()

    def picture_init(self):
        # 页面背景
        self.mainUI.MainWindow.setStyleSheet("#UI_login{border-image:url(./source/background.png);}")
        pixmap = QPixmap('./source/camera.png')
        self.mainUI.label_camera.setPixmap(pixmap)
        self.mainUI.label_manage.setPixmap(pixmap)
        self.mainUI.label_traffic.setPixmap(pixmap)
        self.mainUI.label_guid.setPixmap(pixmap)
        self.mainUI.label_device.setPixmap(pixmap)
        self.mainUI.label_carControl.setPixmap(pixmap)
        self.mainUI.label_manage_2.setPixmap(pixmap)
        self.mainUI.label_vision.setPixmap(pixmap)
        # TODO：等陈总发主页的ICON，加上一些空间的背景图

    def button_init(self):
        self.mainUI.pushButton_carControl.clicked.connect(lambda: self.open_UI("car_control",MainCode_CarControl))
        self.mainUI.pushButton_vision.clicked.connect(lambda: self.open_UI("car_view", MainCode_CarView))
        # TODO：其他按钮事件

    def open_UI(self, name, ui):
        # 这个字典可以存所有UI的对象这样方便主页操作其他对象，不知道用不用得上
        self.UI[name] = ui()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode_UI1()
    sys.exit(app.exec_())