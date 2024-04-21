import os
import configparser

class ConfigUtil:
    DEFAULT = {
        'Date': {
            '24h': '1'
        },
        'Weather': {
            'interval': '30',
            'lat': '35.689500',
            'lon': '139.691722'
        }
    }

    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.ini')

        self.config = configparser.ConfigParser()

        if not os.path.isfile(self.path):
            # Generate config
            sec_d = 'Date'
            self.config.add_section(sec_d)

            sec_w = 'Weather'
            self.config.add_section(sec_w)
            self.config.set(sec_w, 'interval', self.DEFAULT[sec_w]['interval'])
            self.config.set(sec_w, 'lat', self.DEFAULT[sec_w]['lat'])
            self.config.set(sec_w, 'lon', self.DEFAULT[sec_w]['lon'])

            with open(self.path, 'w') as file:
                self.config.write(file)
        else:
            self.config.read(self.path)

    def get(self, sec, opt):
        if not self.config.has_section(sec):
            self.config.add_section(sec)

        if not self.config.has_option(sec, opt):
            self.set(sec, opt, self.DEFAULT[sec][opt])

        return self.config[sec][opt]

    def set(self, sec, opt, val):
        self.config.set(sec, opt, val)

        with open(self.path, 'w') as file:
            self.config.write(file)
