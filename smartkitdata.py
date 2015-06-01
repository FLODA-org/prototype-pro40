__author__ = 'pschiffmann'

import pandas as pd
import numpy as np

from random import randint

class smartkitdata(object):
    def __init__(self):
        self._data = self.gen_data()

    def get_data(self, length=60):
        return pd.DataFrame(self._data)[-length:]

    def get_data_smooth(self, length=60, smooth=10):
        return pd.rolling_mean(pd.DataFrame(self._data[-(length+smooth):]), smooth)[-length:]

    def update_data(self):
        self._data = np.vstack([self._data, self.gen_data()])

    def gen_data(self):
        return np.array([randint(0,1023), randint(0,1023)])


if __name__ == "__main__":
    data = smartkitdata()
    for i in range(10):
        print data.get_data()