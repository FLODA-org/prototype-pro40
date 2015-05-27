__author__ = 'pschiffmann'

import pandas as pd
import numpy as np

class smartkitdata(object):
    def __init__(self):
        self._data = self.gen_data()

    def get_data(self):
        return pd.DataFrame(self._data)[-60:]

    def update_data(self):
        self._data = np.vstack([self._data, self.gen_data()])

    def gen_data(self):
        return np.random.random(4)


if __name__ == "__main__":
    data = smartkitdata()
    for i in range(10):
        print data.get_data()