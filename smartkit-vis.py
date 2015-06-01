__author__ = 'pschiffmann'

import Tkinter as tk
import ttk

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Switch between random data and arduino as data source
import smartkitdata
#import smartkitdata_testfirmata as smartkitdata


matplotlib.use("TkAgg")

class smartkitapp(object):
    """
    Visualisation tkinter app for the smartkit prototype
    """
    def __init__(self):
        """

        :return:
        """
        self.cur_tab = 0
        self.nr_tabs = 2

        self.init_data()
        self.init_window()
        self.init_notebook()
        self.init_plot()
        self.init_plot_smooth()
        self.init_bar()
        self.init_stats()

        self.update_loop()
        tk.mainloop()

    def leftKey(self, event):
        new_tab = self.cur_tab -1 if self.cur_tab > 0 else self.nr_tabs
        self.cur_tab = new_tab
        self.notebook.select(new_tab)

    def rightKey(self, event):
        new_tab = self.cur_tab +1 if self.cur_tab < self.nr_tabs else 0
        self.cur_tab = new_tab
        self.notebook.select(new_tab)


    def init_data(self):
        """
        Initialises connection to data object
        :return:
        """
        self.data = smartkitdata.smartkitdata()

    def init_window(self):
        """
        Creates root root window and sets titlebars, size,..
        :return:
        """
        self.root = tk.Tk()
        self.root.geometry("800x600")

        self.root.bind('<Left>', self.leftKey)
        self.root.bind('<Right>', self.rightKey)

    def init_notebook(self):
        """
        Initialises notebook
        :return:
        """
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

    def init_plot(self):
        """
        Initialises plot
        :return:
        """
        self.fr_plot = tk.Frame()
        self.notebook.add(self.fr_plot, text="Plot")

        self.fig = Figure()
        self.plot = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, self.fr_plot)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def init_plot_smooth(self):
        """
        Initialises plot
        :return:
        """
        self.fr_plot_smooth = tk.Frame()
        self.notebook.add(self.fr_plot_smooth, text="Smooth Plot")

        self.fig_smooth = Figure()
        self.plot_smooth = self.fig_smooth.add_subplot(111)

        self.canvas_smooth = FigureCanvasTkAgg(self.fig_smooth, self.fr_plot_smooth)
        self.canvas_smooth.show()
        self.canvas_smooth.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def init_bar(self):
        """
        Initialises plot
        :return:
        """
        self.fr_bar = tk.Frame()
        self.notebook.add(self.fr_bar, text="Barplot")

        self.fig_bar = Figure()
        self.plot_bar = self.fig_bar.add_subplot(111)

        self.canvas_bar = FigureCanvasTkAgg(self.fig_bar, self.fr_bar)
        self.canvas_bar.show()
        self.canvas_bar.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def init_stats(self):
        """
        Initialises statistics tab
        :return:
        """

        self.fr_stats = tk.Frame(bd=1)
        self.notebook.add(self.fr_stats, text="Statistics")

        tk.Label(self.fr_stats, text="Statistics").grid(row=1, column=1, columnspan=8, sticky="WE")

        self.stringvars = list()
        for i in range(4):
            self.stringvars.append(list())
            for j in range(5):
                self.stringvars[i].append(tk.StringVar())
                tk.Label(self.fr_stats, textvariable=self.stringvars[i][j], width=10).grid(row=j+3, column=2*i+2)
            tk.Label(self.fr_stats, text="Sensor %d" % i).grid(row=2, column=2*i+1, columnspan=2)
            tk.Label(self.fr_stats, text="Mean").grid(row=3, column=2*i+1)
            tk.Label(self.fr_stats, text="StDev").grid(row=4, column=2*i+1)
            tk.Label(self.fr_stats, text="Min").grid(row=5, column=2*i+1)
            tk.Label(self.fr_stats, text="Max").grid(row=6, column=2*i+1)

    def update_data(self):
        """
        Gets new data into data object
        :return:
        """
        self.data.update_data()

    def update_loop(self):
        """
        Updates all notebook tabs
        :return:
        """
        self.update_data()
        self.update_plot()
        self.update_plot_smooth()
        self.update_bar()
        self.update_stats()

        self.root.after(0, self.update_loop)

    def update_plot(self):
        """
        Updates plot tab
        :return:
        """
        self.plot.clear()
        self.data.get_data().plot(ax=self.plot)
        self.canvas.show()

    def update_plot_smooth(self):
        """
        Updates plot tab
        :return:
        """
        self.plot_smooth.clear()
        self.data.get_data_smooth().plot(ax=self.plot_smooth)
        self.canvas_smooth.show()

    def update_bar(self):
        """
        Updates barplot
        :return:
        """
        self.plot_bar.clear()
        self.data.get_data().plot(ax=self.plot_bar, kind="bar")
        self.canvas_bar.show()


    def update_stats(self):
        """
        Updates statistics tab
        :return:
        """
        data = self.data.get_data()
        for i in range(data.shape[1]):
            self.stringvars[i][0].set("{0:.2f}".format(data.ix[:,i].mean()))
            self.stringvars[i][1].set("{0:.2f}".format(data.ix[:,i].std()))
            self.stringvars[i][2].set("{0:.2f}".format(data.ix[:,i].min()))
            self.stringvars[i][3].set("{0:.2f}".format(data.ix[:,i].max()))


if __name__ == "__main__":
    print "Starting smartkitapp"
    smartkitapp()
