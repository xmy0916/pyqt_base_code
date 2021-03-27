# -*- coding: utf-8 -*-

from PyQt5 import QtCore,QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)

    def setupUi(self, UI_login):
        UI_login.setObjectName("UI_login")
        UI_login.resize(1172, 717)
        self.verticalLayoutWidget = QtWidgets.QWidget(UI_login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(480, 200, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_manage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_manage.setStyleSheet("font: 14pt \"宋体\";\n"
                                        "color: rgb(255, 255, 255);")
        self.label_manage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_manage.setObjectName("label_manage")
        self.verticalLayout.addWidget(self.label_manage)
        self.pushButton_manage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_manage.setObjectName("pushButton_manage")
        self.verticalLayout.addWidget(self.pushButton_manage)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(UI_login)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(770, 300, 170, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_carControl = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_carControl.setStyleSheet("font: 14pt \"宋体\";\n"
                                            "color: rgb(255, 255, 255);")
        self.label_carControl.setAlignment(QtCore.Qt.AlignCenter)
        self.label_carControl.setObjectName("label_carControl")
        self.verticalLayout_2.addWidget(self.label_carControl)
        self.pushButton_carControl = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_carControl.setObjectName("pushButton_carControl")
        self.verticalLayout_2.addWidget(self.pushButton_carControl)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(UI_login)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(830, 440, 160, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_camera = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_camera.setStyleSheet("font: 14pt \"宋体\";\n"
                                        "color: rgb(255, 255, 255);")
        self.label_camera.setAlignment(QtCore.Qt.AlignCenter)
        self.label_camera.setObjectName("label_camera")
        self.verticalLayout_3.addWidget(self.label_camera)
        self.pushButton_camera = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_camera.setObjectName("pushButton_camera")
        self.verticalLayout_3.addWidget(self.pushButton_camera)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(UI_login)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(630, 560, 160, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_traffic = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_traffic.setStyleSheet("font: 14pt \"宋体\";\n"
                                         "color: rgb(255, 255, 255);")
        self.label_traffic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_traffic.setObjectName("label_traffic")
        self.verticalLayout_4.addWidget(self.label_traffic)
        self.pushButton_traffic = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_traffic.setObjectName("pushButton_traffic")
        self.verticalLayout_4.addWidget(self.pushButton_traffic)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(UI_login)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(340, 560, 160, 80))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_vision = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_vision.setStyleSheet("font: 14pt \"宋体\";\n"
                                        "color: rgb(255, 255, 255);")
        self.label_vision.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vision.setObjectName("label_vision")
        self.verticalLayout_5.addWidget(self.label_vision)
        self.pushButton_vision = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_vision.setObjectName("pushButton_vision")
        self.verticalLayout_5.addWidget(self.pushButton_vision)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(UI_login)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(170, 440, 160, 80))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_guid = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_guid.setStyleSheet("font: 14pt \"宋体\";\n"
                                      "color: rgb(255, 255, 255);")
        self.label_guid.setAlignment(QtCore.Qt.AlignCenter)
        self.label_guid.setObjectName("label_guid")
        self.verticalLayout_6.addWidget(self.label_guid)
        self.pushButton_guid = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_guid.setObjectName("pushButton_guid")
        self.verticalLayout_6.addWidget(self.pushButton_guid)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(UI_login)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(220, 300, 160, 80))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_device = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_device.setStyleSheet("font: 14pt \"宋体\";\n"
                                        "color: rgb(255, 255, 255);")
        self.label_device.setAlignment(QtCore.Qt.AlignCenter)
        self.label_device.setObjectName("label_device")
        self.verticalLayout_7.addWidget(self.label_device)
        self.pushButton_device = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_device.setObjectName("pushButton_device")
        self.verticalLayout_7.addWidget(self.pushButton_device)
        self.label_manage_2 = QtWidgets.QLabel(UI_login)
        self.label_manage_2.setGeometry(QtCore.QRect(240, 20, 631, 111))
        self.label_manage_2.setStyleSheet("font: 44pt \"宋体\";\n"
                                          "color: rgb(255, 255, 255);")
        self.label_manage_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_manage_2.setObjectName("label_manage_2")

        self.retranslateUi(UI_login)
        QtCore.QMetaObject.connectSlotsByName(UI_login)

    def retranslateUi(self, UI_login):
        _translate = QtCore.QCoreApplication.translate
        UI_login.setWindowTitle(_translate("UI_login", "Dialog"))
        self.label_manage.setText(_translate("UI_login", "综合管理"))
        self.pushButton_manage.setText(_translate("UI_login", "综合管理"))
        self.label_carControl.setText(_translate("UI_login", "车辆管理系统"))
        self.pushButton_carControl.setText(_translate("UI_login", "车辆控制系统"))
        self.label_camera.setText(_translate("UI_login", "违章拍照系统"))
        self.pushButton_camera.setText(_translate("UI_login", "违章拍照系统"))
        self.label_traffic.setText(_translate("UI_login", "流量管理系统"))
        self.pushButton_traffic.setText(_translate("UI_login", "流量管理系统"))
        self.label_vision.setText(_translate("UI_login", "视觉定位系统"))
        self.pushButton_vision.setText(_translate("UI_login", "视觉定位系统"))
        self.label_guid.setText(_translate("UI_login", "导航系统"))
        self.pushButton_guid.setText(_translate("UI_login", "导航系统"))
        self.label_device.setText(_translate("UI_login", "设施管理系统"))
        self.pushButton_device.setText(_translate("UI_login", "设施管理系统"))
        self.label_manage_2.setText(_translate("UI_login", "沙盘管理系统"))

