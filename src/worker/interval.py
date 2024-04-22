import os
import datetime
import requests

from PyQt5 import QtCore

class IntervalWorker:
    def __init__(self, ms):
        self.ms = ms

        self.last_weather = datetime.datetime.min
        self.weather_status_label = ''

        self.timer = QtCore.QTimer(self.ms.window)
        self.timer.timeout.connect(self.update)
        self.timer.start(500)

    def update(self):
        dt = datetime.datetime.now()

        date_str = dt.strftime('%Y/%m/%d (%a)')
        time_str = dt.strftime('%H:%M')

        self.ms.pc.set_status_label(0, date_str)

        self.ms.window.page1_time.setText(time_str)
        self.ms.window.status_time.setText(time_str)

        sec_w = 'Weather'
        weather_interval = int(self.ms.cu.get(sec_w, 'interval'))
        if self.last_weather + datetime.timedelta(minutes=weather_interval) <= dt:
            # Update weather
            self.last_weather = dt

            self.ms.wc.update()
