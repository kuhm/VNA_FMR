import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

import numpy as np

EntriesDict={
            "Effective magnetization":1000,
            "g-factor":2,
            "Start field":0.0,
            "End field":14000,
            "Field step":1000,
            "Field span":1000
            }

class KittelPlotter:
    
    def __init__(self,parent):
        self.tl = tk.Toplevel(parent)

        self.parent=parent
        
        self.dane=[]        

    # "Wyłącza" okno root. Nie można go kontrolować
        self.tl.grab_set()

        self.tl.wm_title("Window Kittel")
        # l = tk.Label(tl, text="This is window #%s" % self.counter)
        l = tk.Label(self.tl, text="Prepare measurement points")
        # l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        l.pack()

        containerLeft=tk.Frame(self.tl)
        containerLeft.pack(side="left")

        containerRight=tk.Frame(self.tl)
        containerRight.pack(side="left")

        PlotButton= tk.Button(containerLeft, text="Plot",
                            command=self.plotKittel)
        PlotButton.pack(side="top")

        # l1 = tk.Label(containerLeft, text="MagnEntry")
        # l1.pack(side="top", fill="both", expand=True)

        # self.MagnEntry=tk.Entry(containerLeft)   
        # self.MagnEntry.insert(0,"1000")    
        # self.MagnEntry.pack()
        
        # l2 = tk.Label(containerLeft, text="gEntry")
        # l2.pack(side="top", fill="both", expand=True)


        # self.gEntry=tk.Entry(containerLeft)
        # self.gEntry.insert(0,"2")       
        # self.gEntry.pack()
        self.labels={}
        self.entries={}
        for key,value in EntriesDict.items():
            l = tk.Label(containerLeft, text=key)
            l.pack(side="top", fill="both", expand=True)
            self.labels[key]=l

            ent=tk.Entry(containerLeft)   
            ent.insert(0,value)    
            ent.pack()
            self.entries[key]=ent



        self.fig = Figure(figsize=(5, 4), dpi=100)

        self.canvas = FigureCanvasTkAgg(self.fig, master=containerRight)  # A tk.DrawingArea.
        self.graph1 = self.fig.add_subplot(111)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(self.canvas, containerRight)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        
        # self.tl.protocol("WM_DELETE_WINDOW", self.close_window)


    # def close_window(self):
    #     self.parent.show()
    #     self.tl.destroy()


    def plotKittel(self):
        
        H = np.arange(float(self.entries["Start field"].get()),float(self.entries["End field"].get()),float(self.entries["Field step"].get()))
        f = float(self.entries["g-factor"].get()) * np.sqrt((H + 4 * np.pi * float(self.entries["Effective magnetization"].get())) + H )
        self.dane.append(H)
        self.dane.append(f)
        # print(self.MagnEntry.get())

        self.graph1.clear()
        self.graph1.scatter(H,f)
        
        self.canvas.draw()
        self.canvas.flush_events()
        