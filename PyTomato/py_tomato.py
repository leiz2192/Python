#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import pygame
from pygame import mixer

import PySimpleGUI as sg
import time


def main():
    sg.SetOptions(element_padding=(0, 0))
    layout = [[sg.Text('25:00', size=(8, 1), font=(None, 24), justification='center', key='text')],
              [sg.Button('Run', button_color=('#2E86C1', '#D6DBDF'), border_width=0, key='Play'),
               sg.Button('Exit', button_color=('#E74C3C', '#D6DBDF'), border_width=0, key='Exit')]]
    window = sg.Window('PyTomato', auto_size_buttons=False).Layout(layout)

    init_music()
    default_time = 25 * 60
    current_time, start_time = default_time, 0
    paused = True
    while True:
        if not paused:
            event, values = window.Read(timeout=10)
            current_time = (start_time - end_time()) // 100
        else:
            event, values = window.Read()

        if event == 'Play':
            event = window.FindElement(event).GetText()

        paused = (event == 'Pause')
        if event in (None, 'Exit'):
            break
        elif event == 'Pause':
            mixer.music.pause()
            window.FindElement('Play').Update(text='Run')
        elif event == 'Run':
            mixer.music.unpause()
            start_time = end_time() + default_time * 100
            window.FindElement('Play').Update(text='Pause')

        current_text = '{:02d}:{:02d}'.format(current_time // 60, current_time % 60)
        window.FindElement('text').Update(current_text)

        if current_text == "00:00":
            current_time = default_time
            paused = True
            mixer.music.pause()
            window.FindElement('Play').Update(text='Run')


def end_time():
    return int(round(time.time() * 100))


def init_music():
    pygame.init()
    mixer.init()
    mixer.music.load(os.path.join(os.getcwd(), "RainyMood.ogg"))
    mixer.music.set_volume(1.0)
    mixer.music.play(-1)
    mixer.music.pause()


if __name__ == '__main__':
    main()
