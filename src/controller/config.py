from dialog.input import InputDialog

class ConfigController:
    def __init__(self, window, cu):
        self.window = window
        self.cu = cu

        self.sec_d = 'Date'
        self.sec_w = 'Weather'

        self.window.page3_page1_interval.setText(self.cu.get(self.sec_w, 'interval'))
        self.window.page3_page1_lat.setText(self.cu.get(self.sec_w, 'lat'))
        self.window.page3_page1_lon.setText(self.cu.get(self.sec_w, 'lon'))

        self.window.page3_page1_interval.clicked.connect(self.interval_change)
        self.window.page3_page1_lat.clicked.connect(self.lat_change)
        self.window.page3_page1_lon.clicked.connect(self.lon_change)

    def interval_change(self):
        dialog = InputDialog(
            self.window,
            self.window.page3_page1_interval_label.text(),
            'int',
            120
        )
        result = dialog.exec_()

        if result:
            self.cu.set(self.sec_w, 'interval', str(dialog.returnVal))
            self.window.page3_page1_interval.setText(str(dialog.returnVal))

    def lat_change(self):
        dialog = InputDialog(
            self.window,
            self.window.page3_page1_lat_label.text(),
            'float',
            153
        )
        result = dialog.exec_()

        if result:
            self.cu.set(self.sec_w, 'lat', str(dialog.returnVal))
            self.window.page3_page1_lat.setText(str(dialog.returnVal))

    def lon_change(self):
        dialog = InputDialog(
            self.window,
            self.window.page3_page1_lon_label.text(),
            'float',
            45
        )
        result = dialog.exec_()

        if result:
            self.cu.set(self.sec_w, 'lon', str(dialog.returnVal))
            self.window.page3_page1_lon.setText(str(dialog.returnVal))
