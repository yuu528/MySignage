class ParentController:
    def __init__(self, ms):
        self.ms = ms
        self.window = ms.window
        self.cu = ms.cu

        self.set_page(0)

        self.window.ctrl_next.clicked.connect(self.next_page)
        self.window.ctrl_prev.clicked.connect(self.prev_page)
        self.window.ctrl_conf.clicked.connect(self.toggle_config)

    def toggle_config(self):
        idx = self.window.stacked_widget.currentIndex()
        cnt = self.window.stacked_widget.count()

        if idx == cnt - 1:
            self.set_page(0)
        else:
            self.set_page(self.window.stacked_widget.count() - 1)

    def next_page(self):
        idx = self.window.stacked_widget.currentIndex() + 1
        self.set_page(idx, True)

    def prev_page(self):
        idx = self.window.stacked_widget.currentIndex() - 1
        self.set_page(idx, True)

    def set_page(self, idx, disable_last=False):
        cnt = self.window.stacked_widget.count()

        if disable_last:
            cnt -= 1

        if idx < 0:
            idx = cnt - 1
        elif idx >= cnt:
            idx = 0

        if idx == 0:
            # Date/Time page
            self.window.status_time.setHidden(True)
            self.window.status_label.setHidden(False)
        elif idx == 1:
            # Weather page
            self.window.status_time.setHidden(False)
            self.window.status_label.setHidden(False)
        elif idx == cnt - 1:
            # Config page
            self.window.status_time.setHidden(False)
            self.window.status_label.setHidden(True)

        self.window.stacked_widget.setCurrentIndex(idx)
