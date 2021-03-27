from PyQt5.QtWidgets import QMainWindow
from UI.UI_carControl import Ui_CarControl

class MainCode_CarControl(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.mainUI = Ui_CarControl()
        self.mainUI.MainWindow.show()
        self.mainUI.MainWindow.setStyleSheet("#UI_carControl{border-image:url(./source/background.png);}")
        self.button_init()
        self.port = 'COM17'
        self.baudrate = 115200

    def button_init(self):
        # radioButton_1_f_h :
        # 1 -> 从左往右第几排
        # f -> forward缩写表示向前，b -> back缩写表示退后
        # h -> high缩写表示高速，l -> low缩写表示低速
        # [0xAA, 0xFB, 0x00, 0x6F, 0x01]指令格式参考马学长
        self.mainUI.radioButton_1_f_h.clicked.connect(lambda: self.send_command([0xAA, 0xFB, 0x00, 0x6F, 0x01]))
        self.mainUI.radioButton_1_f_l.clicked.connect(lambda: self.send_command([0xAA, 0xFB, 0x00, 0x6F, 0x02]))
        # TODO:实现其他radio按钮，这里radiobutton考虑换成pushbutton？不然还得写互斥




    def send_command(self,command):
        print("send command:{}".format(str(command)))
        # TODO:底下先注释了不知道这代码串口发送能不能用
        # ser = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=0)
        # ser.write(bytes(command))


