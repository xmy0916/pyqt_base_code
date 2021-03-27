from PyQt5.QtWidgets import QMainWindow,QMessageBox,QWidget
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import Qt
from UI.UI_carView import Ui_CarView
from utils.socket_client import socket_receive
from utils.util import img_resize
import threading
import cv2

class MainCode_CarView(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.mainUI = Ui_CarView()
        self.mainUI.MainWindow.show()
        self.listen_flag = True
        self.picture_init()
        self.button_init()

    def loop_get_position(self):
        self.cnt = 0
        print("loop listen!")
        while self.listen_flag:
            msg = socket_receive()
            if msg == -1:
                self.mainUI.label_background.setText("socket链接断开")
                break
            self.cnt += 1
            if self.cnt % 100 == 0:
                print(msg)
                # TODO：还要写拿到msg怎么处理

    def button_init(self):
        self.mainUI.pushButton_start.clicked.connect(self.start)
        self.mainUI.pushButton_stop.clicked.connect(self.stop)

    def start(self):
        if socket_receive() == -1:
            QMessageBox.warning(self.mainUI.MainWindow, '警告', 'socket链接失败！socket端口号默认2222！')
            return
        self.picture_init()
        self.listen_flag = True
        get_position_thread = threading.Thread(target=self.loop_get_position)
        get_position_thread.start()

    def stop(self):
        self.listen_flag = False

    def picture_init(self):
        # 页面背景
        self.mainUI.MainWindow.setStyleSheet("#UI_carView{border-image:url(./source/background.png);}")
        img = cv2.imread("./source/sand_table_background.png")
        res = img_resize(img, self.mainUI.label_background)
        img2 = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
        _image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        pixmap = QPixmap(_image)
        self.mainUI.label_background.setPixmap(pixmap)
        self.mainUI.label_background.setAlignment(Qt.AlignCenter)






