#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：socket_client.py

import socket  # 导入 socket 模块

def socket_receive(port=2222):
    s = socket.socket()  # 创建 socket 对象
    host = socket.gethostname()  # 获取本地主机名
    try:
        s.connect((host, port))
        content = s.recv(1024).decode("utf-8")
        s.close()
    except:
        s.close()
        return -1

    return content