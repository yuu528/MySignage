class ConfigController:
    def __init__(self, window, cu):
        self.window = window
        self.cu = cu

        self.sec_d = 'Date'
        self.sec_w = 'Weather'

        self.window.page3_page1_interval.setValue(int(self.cu.get(self.sec_w, 'interval')))
        self.window.page3_page1_lat.setValue(float(self.cu.get(self.sec_w, 'lat')))
        self.window.page3_page1_lon.setValue(float(self.cu.get(self.sec_w, 'lon')))

        self.window.page3_page1_interval.valueChanged.connect(self.interval_changed)
        self.window.page3_page1_lat.valueChanged.connect(self.lat_changed)
        self.window.page3_page1_lon.valueChanged.connect(self.lon_changed)

    def interval_changed(self):
        self.cu.set(self.sec_w, 'interval', str(self.window.page3_page1_interval.value()))

    def lat_changed(self):
        self.cu.set(self.sec_w, 'lat', str(self.window.page3_page1_lat.value()))

    def lon_changed(self):
        self.cu.set(self.sec_w, 'lon', str(self.window.page3_page1_lon.value()))
