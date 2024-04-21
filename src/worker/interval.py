import os
import datetime
import requests

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

from bs4 import BeautifulSoup

from provider.weather import WeatherProvider

import util.file as uf

class IntervalWorker:
    def __init__(self, window, cu):
        self.window = window
        self.cu = cu
        self.wp = WeatherProvider()

        self.last_weather = datetime.datetime.min
        self.weather_status_label = ''

        self.timer = QtCore.QTimer(self.window)
        self.timer.timeout.connect(self.update)
        self.timer.start(500)

    def update(self):
        dt = datetime.datetime.now()

        date_str = dt.strftime('%Y/%m/%d (%a)')
        time_str = dt.strftime('%H:%M')

        idx = self.window.stacked_widget.currentIndex()
        if idx == 0:
            # Date/Time
            self.window.status_label.setText(date_str)
        elif idx == 1:
            # Weather
            self.window.status_label.setText(self.weather_status_label)

        self.window.page1_time.setText(time_str)
        self.window.status_time.setText(time_str)

        sec_w = 'Weather'
        weather_interval = int(self.cu.get(sec_w, 'interval'))
        if self.last_weather + datetime.timedelta(minutes=weather_interval) <= dt:
            # Update weather
            self.last_weather = dt

            lat = self.cu.get(sec_w, 'lat')
            lon = self.cu.get(sec_w, 'lon')

            data = self.wp.get(lat, lon)

            # Title
            self.weather_status_label = data['title']

            # Today
            self.window.page2_today_temp1.setText(data['days'][0]['temp_h'])
            self.window.page2_today_temp2.setText(data['days'][0]['temp_l'])
            self.window.page2_today_rate1.setText(data['days'][0]['rate1'])
            self.window.page2_today_rate2.setText(data['days'][0]['rate2'])
            self.window.page2_today_icon.setPixmap(
                QPixmap(uf.get_tmp_path(data['days'][0]['icon']))
            )

            # Tomorrow
            self.window.page2_tom_temp1.setText(data['days'][1]['temp_h'])
            self.window.page2_tom_temp2.setText(data['days'][1]['temp_l'])
            self.window.page2_tom_rate1.setText(data['days'][1]['rate1'])
            self.window.page2_tom_rate2.setText(data['days'][1]['rate2'])
            self.window.page2_tom_icon.setPixmap(
                QPixmap(uf.get_tmp_path(data['days'][1]['icon']))
            )

            # 3 days later
            self.window.page2_day3.setText(data['days'][2]['date'])
            self.window.page2_day3_temp.setText(data['days'][2]['temp'])
            self.window.page2_day3_rate.setText(data['days'][2]['rate'])
            self.window.page2_day3_icon.setPixmap(
                QPixmap(uf.get_tmp_path(data['days'][2]['icon']))
            )

            # 4 days later
            self.window.page2_day4.setText(data['days'][3]['date'])
            self.window.page2_day4_temp.setText(data['days'][3]['temp'])
            self.window.page2_day4_rate.setText(data['days'][3]['rate'])
            self.window.page2_day4_icon.setPixmap(
                QPixmap(uf.get_tmp_path(data['days'][3]['icon']))
            )
