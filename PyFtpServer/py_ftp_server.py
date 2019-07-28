#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time

import PySimpleGUI as sg
from multiprocessing import Process

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class PyFtpServer(Process):
    def __init__(self, path, user, pwd, port):
        super(PyFtpServer, self).__init__()
        self._path = path
        self._user = user
        self._pwd = pwd
        self._port = port

    def run(self):
        print(self._path, self._user, self._pwd, self._port)

        # Instantiate a dummy authorizer for managing 'virtual' users
        authorizer = DummyAuthorizer()

        # Define a new user having full r/w permissions and a read-only anonymous user
        authorizer.add_user(self._user, self._pwd, self._path, perm='elradfmwMT')

        # Instantiate FTP handler class
        handler = FTPHandler
        handler.authorizer = authorizer

        # Define a customized banner (string returned when client connects)
        handler.banner = "pyftpdlib based ftpd ready."

        # Instantiate FTP server class and listen on 0.0.0.0:2121
        address = ('0.0.0.0', int(self._port))
        server = FTPServer(address, handler)

        # set a limit for connections
        server.max_cons = 256
        server.max_cons_per_ip = 5

        # start ftp server
        server.serve_forever()


def main():
    def_btn_color = ('#ff0000', '#ffffff')
    def_btn_size = (8, 1)

    layout = [
        [sg.Text("Path:"),
         sg.Input(key="__PATH__", default_text=os.getcwd()),
         sg.FolderBrowse(button_color=def_btn_color, size=def_btn_size)],
        [sg.Text("User:"),
         sg.Input(key="__USER__", default_text="ftpuser"),
         sg.Button(button_text="Start", key="START_BTN", button_color=def_btn_color, size=def_btn_size)],
        [sg.Text("Pass:"),
         sg.Input(key="__PASS__", default_text="Changeme_123"),
         sg.Button(button_text="Stop", key="STOP_BTN", button_color=def_btn_color, size=def_btn_size, disabled=True)],
        [sg.Text("Port:"),
         sg.Input(key="__PORT__", default_text=2121),
         sg.Button(button_text="Exit", key="EXIT_BTN", button_color=def_btn_color, size=def_btn_size)]
    ]
    window = sg.Window("PyFtpServer", layout)

    ftp_servers = []
    while True:
        event, values = window.Read()
        if event == "START_BTN":
            p = PyFtpServer(values["__PATH__"], values["__USER__"], values["__PASS__"], values["__PORT__"])
            ftp_servers.append(p)
            p.start()
            window.FindElement("START_BTN").Update(disabled=True)
            window.FindElement("STOP_BTN").Update(disabled=False)
        elif event == "STOP_BTN":
            terminate_server(ftp_servers)
            window.FindElement("START_BTN").Update(disabled=False)
            window.FindElement("STOP_BTN").Update(disabled=True)
        elif event == "EXIT_BTN" or event is None:
            terminate_server(ftp_servers)
            break

    window.Close()


def terminate_server(ftp_servers):
    while ftp_servers:
        p = ftp_servers.pop()
        p.terminate()
        print("{} {} {} terminated".format(time.time(), p.pid, p.name))
        while p.is_alive():
            time.sleep(1)
        print("{} {} {} not alive".format(time.time(), p.pid, p.name))


if __name__ == '__main__':
    main()
