import requests
from bs4 import BeautifulSoup

import util.file as uf

class WeatherProvider:
    def __init__(self):
        pass

    def get(self, lat, lon):
        res = requests.get('https://weathernews.jp/onebox/' + lat + '/' + lon)
        soup = BeautifulSoup(res.text, 'html.parser')

        ret = {}
        ret['days'] = []

        # Title
        ret['title'] = soup.select_one('.index__tit').text.replace('の天気予報', '')

        # Today, Tomorrow
        for i in range(1, 3):
            sel = '.wTable__group:nth-child(' + str(i) + ') '
            rate_sel = sel + '.day2Table:last-child .day2Table__item:'

            icon = soup.select_one(sel + 'img')['src']

            ret['days'].append({
                'temp_h': soup.select_one(sel + '.temp__h .text').text,
                'temp_l': soup.select_one(sel + '.temp__l .text').text,
                'rate1': soup.select_one(rate_sel + 'first-child .text').text,
                'rate2': soup.select_one(rate_sel + 'last-child .text').text,
                'icon': icon
            })

            uf.download_tmp('https:' + icon)

        # 3, 4 days later
        for i in range(2, 4):
            week_sel = '.week .wTable__content .wTable__row:nth-child(' + str(i) + ') '

            icon = soup.select_one(week_sel + 'img')['src']

            ret['days'].append({
                'date': soup.select_one(week_sel + '.day').text,
                'temp': soup.select_one(week_sel + '.h').text,
                'rate': soup.select_one(week_sel + '.r').text,
                'icon': icon
            })

            uf.download_tmp('https:' + icon)

        return ret
