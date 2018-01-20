#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import os
import sys

from subprocess import Popen, PIPE

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (
    QPushButton, QApplication, QMessageBox,
    QDesktopWidget, QLabel, QLineEdit, QGridLayout,
    QSizePolicy, QSystemTrayIcon, QAction, QMenu,
    QHBoxLayout, QVBoxLayout, QListWidget)


g_icon_name="putty_session_m.png"
g_session_file_name="all_sessions.json"


class Sessions(object):
    def __init__(self):
        self.__all_sessions = {}
        if not os.path.exists(g_session_file_name):
            return

        with open(g_session_file_name, 'r') as session_fp:
            self.__all_sessions = json.load(session_fp)
        print(self.__all_sessions)

    def get_session_names(self):
        return [session_name for session_name in self.__all_sessions]

    def get_session_attr(self, session_name):
        if session_name in self.__all_sessions:
            return self.__all_sessions[session_name]
        else:
            return []


class PuttySessionM(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.sessions = Sessions()
        self.init_ui()

    def init_ui(self):
        self.init_element()
        self.init_layout()
        self.init_slot()
        self.init_tray()

        self.setWindowTitle("PuttySessionPanel")
        self.setWindowIcon(QIcon(g_icon_name))

        self.setWindowFlags(
            Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint
        )

        self.close_confirm = False

    def init_tray(self):
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(g_icon_name))
        self.tray.activated.connect(self.tray_click)

        self.tray_restore_action = QAction(
            "Restore", self, triggered=self.showNormal
        )
        self.tray_quit_action = QAction(
            "Quit", self, triggered=self.close
        )
        self.tray_menu = QMenu(QApplication.desktop())
        self.tray_menu.addAction(self.tray_restore_action)
        self.tray_menu.addAction(self.tray_quit_action)
        self.tray.setContextMenu(self.tray_menu)
        self.tray.show()

    def init_slot(self):
        self.open_btn.clicked.connect(self.putty_open)
        self.session_list.itemClicked.connect(self.session_show)

    def init_layout(self):
        self.session_attr_grid = QGridLayout()
        self.session_attr_grid.setSpacing(10)
        self.session_attr_grid.addWidget(self.ip_label, 1, 0)
        self.session_attr_grid.addWidget(self.ip_edit, 1, 1)
        self.session_attr_grid.addWidget(self.port_label, 1, 2)
        self.session_attr_grid.addWidget(self.port_edit, 1, 3)
        self.session_attr_grid.addWidget(self.user_label, 2, 0)
        self.session_attr_grid.addWidget(self.user_edit, 2, 1)
        self.session_attr_grid.addWidget(self.pwd_label, 3, 0)
        self.session_attr_grid.addWidget(self.pwd_edit, 3, 1)
        self.session_attr_grid.addWidget(self.save_label, 4, 0)
        self.session_attr_grid.addWidget(self.save_edit, 4, 1)

        self.button_grid = QHBoxLayout()
        self.button_grid.addWidget(self.open_btn)
        self.button_grid.addWidget(self.save_open_btn)

        self.session_grid = QHBoxLayout()
        self.session_grid.addWidget(self.session_list)
        self.session_grid.addLayout(self.session_attr_grid)

        self.gerneral_grid = QVBoxLayout()
        self.gerneral_grid.addLayout(self.session_grid)
        self.gerneral_grid.addLayout(self.button_grid)
        self.setLayout(self.gerneral_grid)

    def init_element(self):
        self.ip_label = QLabel("Host IP")
        self.ip_edit = QLineEdit()

        self.port_label = QLabel("Port")
        self.port_edit = QLineEdit()
        self.port_edit.setText("22")
        self.port_edit.setMaximumSize(QSize(40, 40))

        self.user_label = QLabel("Username")
        self.user_edit = QLineEdit()

        self.pwd_label = QLabel("Password")
        self.pwd_edit = QLineEdit()

        self.save_label = QLabel("Save as")
        self.save_edit = QLineEdit()

        self.save_open_btn = QPushButton("Save and Open")
        self.open_btn = QPushButton("Open")

        self.session_list = QListWidget()
        self.session_list.addItems(self.sessions.get_session_names())

    def session_show(self):
        self.ip_edit.clear()
        self.port_edit.clear()
        self.user_edit.clear()
        self.pwd_edit.clear()
        
        session_name = self.session_list.currentItem().text()
        session_attr = self.sessions.get_session_attr(session_name)
        if "host" in session_attr:
            self.ip_edit.setText(session_attr["host"])
        if "port" in session_attr:
            self.port_edit.setText(session_attr["port"])
        if "username" in session_attr:
            self.user_edit.setText(session_attr["username"])
        if "passwd" in session_attr:
            self.pwd_edit.setText(session_attr["passwd"])

    def tray_click(self, click_way):
        if click_way == QSystemTrayIcon.DoubleClick:
            self.showNormal()
            self.setWindowState(Qt.WindowActive)

    def putty_open(self):
        host_ip = self.ip_edit.text()
        if not host_ip:
            QMessageBox.information(
                self, "Information", "Please input right Host IP"
            )
            return
        host_port = self.port_edit.text()
        if not host_port:
            QMessageBox.information(
                self, "Information", "Please input right Port"
            )
            return
        user_name = self.user_edit.text()
        if not user_name:
            QMessageBox.information(
                self, "Information", "Please input your username"
            )
            return
        open_cmd = "putty -ssh -l {user} -P {port}".format(
            user=user_name, port=host_port
        )
        passwd = self.pwd_edit.text()
        if passwd:
            open_cmd = "{cmd} -pw {pwd} {ip}".format(
                cmd=open_cmd, pwd=passwd, ip=host_ip
            )
        else:
            open_cmd = "{cmd} {ip}".format(
                cmd=open_cmd, ip=host_ip
            )

        print("Open putty:", open_cmd)
        Popen(open_cmd)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def changeEvent(self, event):
        if self.isMinimized():
            self.hide()

    def closeEvent(self, event):
        if not self.close_confirm:
            return

        reply = QMessageBox.question(
            self, "Message", "Are you sure to quit?",
            QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = PuttySessionM()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
