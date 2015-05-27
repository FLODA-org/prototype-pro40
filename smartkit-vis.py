__author__ = 'pschiffmann'

import Tkinter as tk
import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class smartkitapp(object):
    """
    Visualisation tkinter app for the smartkit prototype
    """
    def __init__(self):
        """

        :return:
        """

        self.init_window()
        self.init_notebook()
        self.init_plot()
        tk.mainloop()

    def init_window(self):
        """
        Creates root root window and sets titlebars, size,..
        :return:
        """
        self.root = tk.Tk()
        self.root.geometry("800x600")

    def init_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

    def init_plot(self):
        self.fr_plot = tk.Frame()
        self.notebook.add(self.fr_plot, text="Plot")

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self.fr_plot)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    print "Starting smartkitapp"
    smartkitapp()
