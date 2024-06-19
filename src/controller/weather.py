from PyQt5.QtGui import QPixmap

from provider.weather import WeatherProvider

import util.file as uf

class WeatherController:
    def __init__(self, ms):
        self.ms = ms
        self.wp = WeatherProvider()

    def update(self):
        sec_w = 'Weather'
        lat = self.ms.cu.get(sec_w, 'lat')
        lon = self.ms.cu.get(sec_w, 'lon')

        data = self.wp.get(lat, lon)

        if 'title' not in data or 'days' not in data or len(data['days']) < 4:
            return

        # Title
        self.ms.pc.set_status_label(1, data['title'])

        # Today
        self.ms.window.page2_today_temp1.setText(data['days'][0]['temp_h'])
        self.ms.window.page2_today_temp2.setText(data['days'][0]['temp_l'])
        self.ms.window.page2_today_rate1.setText(data['days'][0]['rate1'])
        self.ms.window.page2_today_rate2.setText(data['days'][0]['rate2'])
        self.ms.window.page2_today_icon.setPixmap(
            QPixmap(uf.get_tmp_path(data['days'][0]['icon']))
        )

        # Tomorrow
        self.ms.window.page2_tom_temp1.setText(data['days'][1]['temp_h'])
        self.ms.window.page2_tom_temp2.setText(data['days'][1]['temp_l'])
        self.ms.window.page2_tom_rate1.setText(data['days'][1]['rate1'])
        self.ms.window.page2_tom_rate2.setText(data['days'][1]['rate2'])
        self.ms.window.page2_tom_icon.setPixmap(
            QPixmap(uf.get_tmp_path(data['days'][1]['icon']))
        )

        # 3 days later
        self.ms.window.page2_day3.setText(data['days'][2]['date'])
        self.ms.window.page2_day3_temp.setText(data['days'][2]['temp'])
        self.ms.window.page2_day3_rate.setText(data['days'][2]['rate'])
        self.ms.window.page2_day3_icon.setPixmap(
            QPixmap(uf.get_tmp_path(data['days'][2]['icon']))
        )

        # 4 days later
        self.ms.window.page2_day4.setText(data['days'][3]['date'])
        self.ms.window.page2_day4_temp.setText(data['days'][3]['temp'])
        self.ms.window.page2_day4_rate.setText(data['days'][3]['rate'])
        self.ms.window.page2_day4_icon.setPixmap(
            QPixmap(uf.get_tmp_path(data['days'][3]['icon']))
        )
