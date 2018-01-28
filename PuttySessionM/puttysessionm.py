#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import os
import sys
import re
import functools

from subprocess import Popen

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (
    QPushButton, QApplication, QMessageBox,
    QLabel, QLineEdit, QGridLayout,
    QSystemTrayIcon, QAction, QMenu,
    QListWidget, QToolBar)

g_icon_name = {
    "software": "puttysessionm.png",
    "session_add": "add.png",
    "session_remove": "remove.png",
    "session_search": "search.png"
}

g_session_file_name="all_sessions.json"


class Sessions(object):
    def __init__(self):
        self.__all_sessions = {}
        if not os.path.exists(g_session_file_name):
            return

        with open(g_session_file_name, 'r') as session_fp:
            self.__all_sessions = json.load(session_fp)

    def get_session_names(self):
        return [session_name for session_name in self.__all_sessions]

    def get_session_attr(self, session_name):
        if session_name in self.__all_sessions:
            return self.__all_sessions[session_name]
        else:
            return []

    def is_new_session_name(self, session_name):
        return session_name not in self.__all_sessions

    def save_session(self, session_name, session_attr):
        if session_name not in self.__all_sessions:
            self.__all_sessions[session_name] = session_attr
        else:
            for attr in self.__all_sessions[session_name]:
                if attr in session_attr:
                    self.__all_sessions[session_name][attr] = session_attr[attr]
        with open(g_session_file_name, 'w') as session_fp:
            json.dump(
                self.__all_sessions, session_fp, indent=4, ensure_ascii=False
            )

    def remove_session(self, session_name):
        if session_name not in self.__all_sessions:
            return
        self.__all_sessions.pop(session_name)
        with open(g_session_file_name, 'w') as session_fp:
            json.dump(
                self.__all_sessions, session_fp, indent=4, ensure_ascii=False
            )


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
        self.setWindowIcon(QIcon(g_icon_name["software"]))

        self.setWindowFlags(
            Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint
        )
        self.sizeHint()
        self.setFixedSize(580, 160)

        self.close_confirm = False

    def init_tray(self):
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(g_icon_name["software"]))
        self.tray.activated.connect(self.tray_click)

        self.tray_restore = QAction(
            "Restore", self, triggered=self.showNormal
        )
        self.tray_quit = QAction(
            "Quit", self, triggered=self.close
        )

        self.tray_sessions = QMenu("Sessions", self)
        for session_name in self.session_names:
            session_name_action = QAction(session_name, self)
            session_name_action.triggered.connect(
                functools.partial(self.tray_session_open, session_name)
            )
            self.tray_sessions.addAction(session_name_action)

        self.tray_menu = QMenu(QApplication.desktop())
        self.tray_menu.addAction(self.tray_restore)
        self.tray_menu.addAction(self.tray_quit)
        self.tray_menu.addMenu(self.tray_sessions)

        self.tray.setContextMenu(self.tray_menu)
        self.tray.show()

    def init_slot(self):
        self.open_btn.clicked.connect(self.putty_open)
        self.save_open_btn.clicked.connect(self.putty_save_and_open)
        self.session_list.itemClicked.connect(self.session_show)
        self.session_list.itemDoubleClicked.connect(self.session_show_and_open)
        self.session_remove.triggered.connect(self.session_del)
        self.session_add.triggered.connect(self.session_save)
        self.save_edit.returnPressed.connect(self.session_save)
        self.session_search.triggered.connect(self.session_search_slot)
        self.session_search_edit.returnPressed.connect(self.session_search_slot)

    def init_layout(self):
        self.session_grid = QGridLayout()
        self.session_grid.addWidget(self.ip_label, 0, 4, 1, 1)
        self.session_grid.addWidget(self.ip_edit, 0, 5, 1, 2)
        self.session_grid.addWidget(self.port_label, 0, 7, 1, 1)
        self.session_grid.addWidget(self.port_edit, 0, 8, 1, 1)
        self.session_grid.addWidget(self.user_label, 1, 4, 1, 1)
        self.session_grid.addWidget(self.user_edit, 1, 5, 1, 2)
        self.session_grid.addWidget(self.pwd_label, 2, 4, 1, 1)
        self.session_grid.addWidget(self.pwd_edit, 2, 5, 1, 2)
        self.session_grid.addWidget(self.save_label, 3, 4, 1, 1)
        self.session_grid.addWidget(self.save_edit, 3, 5, 1, 2)

        self.session_grid.addWidget(self.session_list, 0, 0, 4, 4)
        self.session_grid.addWidget(self.session_toolbar, 4, 0, 1, 4)
        self.session_grid.addWidget(self.open_btn, 4, 5, 1, 1)
        self.session_grid.addWidget(self.save_open_btn, 4, 6, 1, 1)

        self.setLayout(self.session_grid)

    def init_element(self):
        self.ip_label = QLabel("Host  IP")
        self.ip_edit = QLineEdit()

        self.port_label = QLabel("Port")
        self.port_edit = QLineEdit()
        self.port_edit.setText("22")
        self.port_edit.setMaximumSize(QSize(40, 40))

        self.user_label = QLabel("Username")
        self.user_edit = QLineEdit()

        self.pwd_label = QLabel("Password")
        self.pwd_edit = QLineEdit()

        self.save_label = QLabel("Saved as")
        self.save_edit = QLineEdit()

        self.save_open_btn = QPushButton("&Save and Open")
        self.save_open_btn.minimumSizeHint()
        self.open_btn = QPushButton("&Open")
        self.open_btn.minimumSizeHint()

        self.session_add = QAction(
            QIcon(g_icon_name["session_add"]), "Add", self
        )
        self.session_remove = QAction(
            QIcon(g_icon_name["session_remove"]), "Remove", self
        )
        self.session_search = QAction(
            QIcon(g_icon_name["session_search"]), "Search", self
        )
        self.session_search_edit = QLineEdit()
        self.session_toolbar = QToolBar("SesionTool")
        self.session_toolbar.addAction(self.session_add)
        self.session_toolbar.addAction(self.session_remove)
        self.session_toolbar.addAction(self.session_search)
        self.session_toolbar.addWidget(self.session_search_edit)

        self.session_list = QListWidget()
        self.session_names = self.sessions.get_session_names()
        self.session_list.addItems(self.session_names)

    def tray_session_open(self, session_name):
        session_attr = self.sessions.get_session_attr(session_name)
        host = session_attr.get("host", "")
        port = session_attr.get("port", "")
        user = session_attr.get("username", "")
        pawd = session_attr.get("passwd", "")
        self.shell_open_putty(host, port, user, pawd)

    def session_search_slot(self):
        self.session_list.clear()

        self.session_names = self.sessions.get_session_names()
        search_text = self.session_search_edit.text()
        if not search_text:
            self.session_list.addItems(self.session_names)
            return

        match_sesion_names = []
        for session_name in self.session_names:
            if search_text in session_name:
                match_sesion_names.append(session_name)
        self.session_list.addItems(match_sesion_names)

    def session_save(self):
        if not self.check_input():
            return

        host = self.ip_edit.text()
        port = self.port_edit.text()
        user = self.user_edit.text()
        pawd = self.pwd_edit.text()
        session_name = self.save_edit.text()
        if not session_name:
            session_name = "{0}@{1}".format(user, host)
        session_attr = {
            "host": host,
            "port": port,
            "username": user,
            "passwd": pawd
        }
        if self.sessions.is_new_session_name(session_name):
            self.session_list.addItem(session_name)

            session_name_action = QAction(session_name, self)
            session_name_action.triggered.connect(
                functools.partial(self.tray_session_open, session_name)
            )
            self.tray_sessions.addAction(session_name_action)
        self.sessions.save_session(session_name, session_attr)


    def session_del(self):
        current_item = self.session_list.currentItem()
        if current_item is None:
            QMessageBox.information(
                self, "Message", "Please select a session!"
            )
            return
        session_name = current_item.text()
        reply = QMessageBox.question(
            self,
            "Message",
            "Are you sure to remove \"{0}\"?".format(session_name),
            QMessageBox.Yes|QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.No:
            return
        self.session_list.takeItem(self.session_list.currentRow())
        for action in self.tray_sessions.actions():
            if action.text() == session_name:
                self.tray_sessions.removeAction(action)
                break
        self.sessions.remove_session(session_name)

    def session_show_and_open(self):
        self.session_show()
        self.putty_open()

    def session_show(self):
        self.ip_edit.clear()
        self.port_edit.clear()
        self.user_edit.clear()
        self.pwd_edit.clear()
        self.save_edit.clear()

        session_name = self.session_list.currentItem().text()
        session_attr = self.sessions.get_session_attr(session_name)
        self.save_edit.setText(session_name)
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

    def putty_save_and_open(self):
        if not self.putty_open():
            return
        self.session_save()

    def putty_open(self):
        if not self.check_input():
            return False

        host_ip = self.ip_edit.text()
        host_port = self.port_edit.text()
        user_name = self.user_edit.text()
        passwd = self.pwd_edit.text()

        self.shell_open_putty(host_ip, host_port, user_name, passwd)
        return True

    def check_input(self):
        ip_text = self.ip_edit.text()
        if not ip_text or not self.check_ip_validity(ip_text):
            QMessageBox.information(
                self, "Information", "Please input right Host IP"
            )
            return False

        port_text = self.port_edit.text()
        if not port_text or not self.check_port_validity(port_text):
            QMessageBox.information(
                self, "Information", "Please input right Port"
            )
            return False
        return True

    def check_ip_validity(self, ip_text):
        compile_ip = re.compile(
            '^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
        )
        return compile_ip.match(ip_text)

    def check_port_validity(self, port_text):
        compile_port = re.compile('^([1-9]\d+|[1-9])$')
        return compile_port.match(port_text)

    def has_special_chars(self, str_text):
        special_chars = ";&\"\'"
        for one_special_char in special_chars:
            if one_special_char in str_text:
                return True
        return False

    def shell_open_putty(self, host_ip, host_port, user_name, passwd):
        if not host_ip or not host_port:
            QMessageBox.information(
                self, "Information", "Please input Host IP and Port"
            )
            return

        open_cmd = "putty -ssh -P {port}".format(port=host_port)
        if user_name and not self.has_special_chars(user_name):
            open_cmd = "{cmd} -l \"{user}\"".format(cmd=open_cmd, user=user_name)
        if passwd and not self.has_special_chars(passwd):
            open_cmd = "{cmd} -pw \"{pwd}\"".format(cmd=open_cmd, pwd=passwd)
        open_cmd = "{cmd} {ip}".format(cmd=open_cmd, ip=host_ip)
        print("Open putty:", open_cmd)
        Popen(open_cmd)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.hide()

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
