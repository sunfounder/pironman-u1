from spc.spc import SPC

class PironmanU1(SPC):
    def __init__(self):
        super().__init__()

    def set_fan_mode(self, mode):
        self.write_fan_mode(mode)

