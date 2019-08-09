#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import pygame
from pygame import mixer

import PySimpleGUI as sg
import time
from datetime import datetime
import json


PYTOMATO_CONF_FILE = "PyTomato.json"
DEFAUT_CYCLE = 25 * 60
DEFAULT_MUSIC = "RainyMood.ogg"
DEFAULT_RUN_TIMES = 0
DEFAULT_PAUSE_TIMES = 0


def init_config(today):
    if not os.path.exists(PYTOMATO_CONF_FILE) or not os.path.isfile(PYTOMATO_CONF_FILE):
        return DEFAUT_CYCLE, DEFAULT_MUSIC, DEFAULT_RUN_TIMES, DEFAULT_PAUSE_TIMES

    with open(PYTOMATO_CONF_FILE, "r") as fp:
        content = json.load(fp)

    cycle = content.get("cycle", DEFAUT_CYCLE)
    music_file = content.get("music", DEFAULT_MUSIC)
    run_times, pause_times = DEFAULT_RUN_TIMES, DEFAULT_PAUSE_TIMES
    if today in content:
        run_times = content[today].get("Run", DEFAULT_RUN_TIMES)
        pause_times = content[today].get("Pause", DEFAULT_PAUSE_TIMES)

    return cycle, music_file, run_times, pause_times


def save_times(today, run_times, pause_times):
    with open(PYTOMATO_CONF_FILE, "r") as fp:
        content = json.load(fp)

    if today not in content:
        content[today] = dict()

    today_times = content[today]
    today_times["Run"] = run_times
    today_times["Pause"] = pause_times

    with open(PYTOMATO_CONF_FILE, "w") as fp:
        json.dump(content, fp, indent=2)


def main():
    today = datetime.today().strftime("%Y-%m-%d %a")

    default_time, music_file, run_times, pause_times = init_config(today)

    window = init_window(today, run_times, pause_times)

    init_music(music_file)
    current_time, start_time = default_time, 0
    while True:
        if window.FindElement("Play").GetText() == "Pause":
            event, values = window.Read(timeout=10)
            current_time = (start_time - end_time()) // 100
        else:
            event, values = window.Read()

        if event == 'Play':
            event = window.FindElement(event).GetText()

        if event in (None, 'Exit'):
            pause_times += 1 if window.FindElement("Play").GetText() == "Pause" else 0
            save_times(today, run_times, pause_times)
            break
        elif event == 'Pause':
            mixer.music.pause()
            window.FindElement('Play').Update(text='Run')

            pause_times += 1
            save_times(today, run_times, pause_times)
        elif event == 'Run':
            mixer.music.unpause()
            start_time = end_time() + default_time * 100
            window.FindElement('Play').Update(text='Pause')

            run_times += 1
            save_times(today, run_times, pause_times)

        window.FindElement("Times").Update(times_text(run_times, pause_times))

        current_text = '{:02d}:{:02d}'.format(current_time // 60, current_time % 60)
        window.FindElement('text').Update(current_text)

        if current_text == "00:00":
            current_time = default_time
            mixer.music.pause()
            window.FindElement('Play').Update(text='Run')
            window.FindElement('text').Update("25:00")


def init_window(today, run_times=0, pause_times=0):
    sg.SetOptions(element_padding=(0, 0))
    layout = init_layout(today, run_times, pause_times)
    window = sg.Window('PyTomato', auto_size_buttons=False).Layout(layout)
    return window


def init_layout(today, run_times, pause_times):
    layout = [[sg.Text('25:00', size=(8, 1), font=(None, 24), justification='center', key='text')],
              [sg.Button('Run', button_color=('#2E86C1', '#D6DBDF'), border_width=0, key='Play'),
               sg.Text(""),
               sg.Button('Exit', button_color=('#E74C3C', '#D6DBDF'), border_width=0, key='Exit')],
              [sg.Text(today, background_color="#fadbd8"),
               sg.Text(""),
               sg.Text(times_text(run_times, pause_times), auto_size_text=True, background_color="#f5b7b1", key="Times")]]
    return layout


def end_time():
    return int(round(time.time() * 100))


def times_text(run_times, pause_times):
    return "Run/Pause: {:0>3}/{:0>3}".format(run_times, pause_times)


def init_music(music_file):
    pygame.init()
    mixer.init()
    mixer.music.load(os.path.join(os.getcwd(), music_file))
    mixer.music.set_volume(1.0)
    mixer.music.play(-1)
    mixer.music.pause()


if __name__ == '__main__':
    main()
