import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtCore import *

root = os.getcwd()
sys.path.append(root)
sys.path.append(os.path.join(root, "UI"))
from UI.UI_1 import Ui_MainWindow


class MainCode(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.mainUI = Ui_MainWindow()
        self.mainUI.MainWindow.show()


    def getDir(self):
        _dir = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        if len(_dir) != 0:
            if self.is_chinese(_dir):
                print("有中文")
                QMessageBox.warning(self, '警告', '暂不支持含有中文的路径')
                return
            else:
                self.dir_lineedit.setText(_dir)

    def is_chinese(self, string):
        """
        检查整个字符串是否包含中文
        :param string: 需要检查的字符串
        :return: bool
        """
        for ch in string:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    sys.exit(app.exec_())