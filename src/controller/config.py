from window.input import InputDialog

class ConfigController:
    def __init__(self, ms):
        self.ms = ms

        self.sec_d = 'Date'
        self.sec_w = 'Weather'

        self.ms.window.page3_page1_interval.setText(self.ms.cu.get(self.sec_w, 'interval'))
        self.ms.window.page3_page1_lat.setText(self.ms.cu.get(self.sec_w, 'lat'))
        self.ms.window.page3_page1_lon.setText(self.ms.cu.get(self.sec_w, 'lon'))

        self.ms.window.page3_page1_update.clicked.connect(self.ms.wc.update)
        self.ms.window.page3_page1_interval.clicked.connect(self.interval_change)
        self.ms.window.page3_page1_lat.clicked.connect(self.lat_change)
        self.ms.window.page3_page1_lon.clicked.connect(self.lon_change)

    def interval_change(self):
        dialog = InputDialog(
            self.ms.window,
            self.ms.window.page3_page1_interval_label.text(),
            'int',
            120
        )
        result = dialog.exec_()

        if result:
            self.ms.cu.set(self.sec_w, 'interval', str(dialog.returnVal))
            self.ms.window.page3_page1_interval.setText(str(dialog.returnVal))

    def lat_change(self):
        dialog = InputDialog(
            self.ms.window,
            self.ms.window.page3_page1_lat_label.text(),
            'float',
            153
        )
        result = dialog.exec_()

        if result:
            self.ms.cu.set(self.sec_w, 'lat', str(dialog.returnVal))
            self.ms.window.page3_page1_lat.setText(str(dialog.returnVal))

    def lon_change(self):
        dialog = InputDialog(
            self.ms.window,
            self.ms.window.page3_page1_lon_label.text(),
            'float',
            45
        )
        result = dialog.exec_()

        if result:
            self.ms.cu.set(self.sec_w, 'lon', str(dialog.returnVal))
            self.ms.window.page3_page1_lon.setText(str(dialog.returnVal))
