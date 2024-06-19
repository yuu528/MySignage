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
        titleDom = soup.select_one('.title')
        if titleDom is None:
            return {}

        ret['title'] = titleDom.text.replace('の天気予報', '')

        # Today, Tomorrow
        for i in range(1, 3):
            sel = '.wTable__group:nth-child(' + str(i) + ') '
            rate_sel = sel + '.day2Table:last-child .day2Table__item:'

            iconDom = soup.select_one(sel + 'img')
            tempHDom = soup.select_one(sel + '.temp__h .text')
            tempLDom = soup.select_one(sel + '.temp__l .text')
            rate1Dom = soup.select_one(rate_sel + 'first-child .text')
            rate2Dom = soup.select_one(rate_sel + 'last-child .text')
            if iconDom is None or tempHDom is None or tempLDom is None or rate1Dom is None or rate2Dom is None:
                continue

            ret['days'].append({
                'temp_h': tempHDom.text,
                'temp_l': tempLDom.text,
                'rate1': rate1Dom.text,
                'rate2': rate2Dom.text,
                'icon': iconDom['src']
            })

            uf.download_tmp('https:' + icon)

        # 3, 4 days later
        for i in range(2, 4):
            week_sel = '.week .wTable__content .wTable__row:nth-child(' + str(i) + ') '

            iconDom = soup.select_one(sel + 'img')
            dateDom = soup.select_one(week_sel + '.day')
            tempDom = soup.select_one(week_sel + '.h')
            rateDom = soup.select_one(week_sel + '.r')
            if iconDom is None or dateDom is None or tempDom is None or rateDom is None:
                continue

            ret['days'].append({
                'date': soup.select_one(week_sel + '.day').text,
                'temp': soup.select_one(week_sel + '.h').text,
                'rate': soup.select_one(week_sel + '.r').text,
                'icon': iconDom['src']
            })

            uf.download_tmp('https:' + icon)

        return ret
