# importing  all the
# functions defined in py001.py
from gui_x_001 import *
from tkinter import *
from tkinter import ttk

def donothing():
   x = 0
   
def new_tab_01():
   x = 0

root = Tk()
frm = ttk.Frame(root, padding=200)
frm.grid()
ttk.Label(frm, text="label2!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Label(frm, text="calling_Gui!").grid(column=0, row=1)
ttk.Button(frm, text="calling_Gui", command=calling_Gui).grid(column=1, row=1)
root.mainloop()

#def init():
# calling functions
#    calling_Gui()
#    browser01()
#    speech()
    
if __name__ == "__main__":
    print("Hello, World!")
    #init()
