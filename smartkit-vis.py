__author__ = 'pschiffmann'

import Tkinter as tk


class smartkitapp(object):
    """
    Visualisation tkinter app for the smartkit prototype
    """
    def __init__(self):
        """

        :return:
        """

        self.init_window()
        tk.mainloop()

    def init_window(self):
        """
        Creates root root window and sets titlebars, size,..
        :return:
        """
        self.root = tk.Tk()


if __name__ == "__main__":
    print "Starting smartkitapp"
    smartkitapp()
