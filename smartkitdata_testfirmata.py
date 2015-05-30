__author__ = 'pschiffmann'

import pandas as pd
import numpy as np

from PyMata.pymata import PyMata

ARDUINO_ADDRESS = "/dev/cu.usbmodem1411"

class smartkitdata(object):
    def __init__(self):
        self.board = PyMata(ARDUINO_ADDRESS)
        self.board.set_pin_mode(1, self.board.INPUT, self.board.ANALOG)
        self._data = self.gen_data()

    def get_data(self):
        return pd.DataFrame(self._data)[-60:]

    def update_data(self):
        self._data = np.vstack([self._data, self.gen_data()])

    def gen_data(self):
        return np.array(self.board.analog_read(1))


if __name__ == "__main__":
    data = smartkitdata()
    for i in range(10):
        print data.get_data()