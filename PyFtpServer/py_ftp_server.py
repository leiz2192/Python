#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import socket
import time

import logging

import PySimpleGUI as sg
import threading
from threading import Thread, Lock

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer


class PyFtpServer(Thread):
    def __init__(self, path, user, pwd, port):
        super(PyFtpServer, self).__init__(name="PyFtpServer")
        self._stop_event = threading.Event()

        self._path = path
        self._user = user
        self._pwd = pwd
        self._port = port

        self._server = None

        self._lock = Lock()

    def run(self):
        with self._lock:
            # Instantiate a dummy authorizer for managing 'virtual' users
            authorizer = DummyAuthorizer()

            # Define a new user having full r/w permissions and a read-only anonymous user
            authorizer.add_user(self._user, self._pwd, self._path, perm='elradfmwMT')

            # Instantiate FTP handler class
            handler = FTPHandler
            handler.authorizer = authorizer

            # Define a customized banner (string returned when client connects)
            handler.banner = "pyftpdlib based ftpd ready."

            # Instantiate FTP server class and listen on 0.0.0.0:self._port
            address = ('0.0.0.0', int(self._port))
            try:
                self._server = ThreadedFTPServer(address, handler)
            except Exception as e:
                logging.error(f"Exception while start PyFtpServer: {e}")

        if self._server is not None:
            # set a limit for connections
            self._server.max_cons = 256
            self._server.max_cons_per_ip = 5

            # start ftp server
            self._server.serve_forever()

    def terminate(self):
        self._server.close_all()

    def success(self):
        with self._lock:
            return self._server is not None


def local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            ip, _ = s.getsockname()
    except Exception as e:
        logging.error("local_ip exception: {}".format(e))
        ip = socket.gethostbyname(socket.gethostname())

    return ip


def main():
    logging.basicConfig(filename=os.path.join(os.getcwd(), "pyftpd.log"),
                        level=logging.INFO,
                        format="%(levelname)s:%(asctime)s[%(process)d|%(thread)d]:%(name)s %(message)s")

    def_btn_color = ('#ff0000', '#D6DBDF')
    def_btn_size = (8, 1)
    def_text_size = (6, 1)

    ip = local_ip()

    sg.SetOptions(button_color=def_btn_color, border_width=0, text_justification="left", auto_size_text=False)
    layout = [
        [sg.Text("PATH:", size=def_text_size),
         sg.InputText(key="PATH", default_text=os.getcwd()),
         sg.FolderBrowse(size=def_btn_size, key="BROWSE")],
        [sg.Text("USER:", size=def_text_size),
         sg.Input(key="USER", default_text="ftpuser")],
        [sg.Text("PASS:", size=def_text_size),
         sg.Input(key="PASS", default_text="Changeme_123")],
        [sg.Text("PORT:", size=def_text_size),
         sg.Input(key="PORT", default_text=2121)],
        [sg.Button(button_text="Start", key="START_BTN",  size=def_btn_size),
         sg.Button(button_text="Stop", key="STOP_BTN", size=def_btn_size, disabled=True),
         sg.Button(button_text="Exit", key="EXIT_BTN", border_width=0, size=def_btn_size)],
        [sg.InputText(ftp_info(ip, "2121", "ftpuser", "Changeme_123"), key="ADDR", disabled=True)]]
    window = sg.Window("PyFtpServer", layout, use_default_focus=False)

    ftp_servers = []
    while True:
        event, values = window.Read()
        if event == "START_BTN":
            p = PyFtpServer(values["PATH"], values["USER"], values["PASS"], values["PORT"])
            p.start()
            if not p.success():
                sg.PopupOK("Cannot start ftp server. Maybe the port has been occupied.", title="ERROR")
                continue
            ftp_servers.append(p)

            window.FindElement("ADDR").Update(value=ftp_info(ip, values["PORT"], values["USER"], values["PASS"]))
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


def ftp_info(ip, port, user, pwd):
    return "ftp://{}:{} {}/{}".format(ip, port, user, pwd)


def terminate_server(ftp_servers):
    while ftp_servers:
        p = ftp_servers.pop()
        logging.info("{} {} {} terminate start".format(time.time(), p.ident, p.name))
        p.terminate()
        while p.is_alive():
            time.sleep(1)
            p.terminate()
        logging.info("{} {} {} terminate end".format(time.time(), p.ident, p.name))


if __name__ == '__main__':
    main()
