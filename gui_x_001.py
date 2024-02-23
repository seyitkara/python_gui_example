# importing  all the
# functions defined in py001.py
from calling_func import *
from tkinter import *
from tkinter import ttk
#from tag_Photo_001 import *
from delete_file_2 import *
from greetings import *
from dairy import *

from gui_x_002 import *
from backend_x_001 import *

def donothing():
   x = 0
   
def new_tab_01():
   x = 0

def calling_Gui():
#buraya tkinter icin gui yapilacak
   calling_func()
   root = Tk()
   ####################
   menubar = Menu(root)
   filemenu = Menu(menubar, tearoff=0)
   filemenu.add_command(label="New", command=new_tab_01)
   filemenu.add_command(label="Open", command=donothing)
   filemenu.add_command(label="Save", command=donothing)
   filemenu.add_separator()
   filemenu.add_command(label="Exit", command=root.quit)
   menubar.add_cascade(label="File", menu=filemenu)
   helpmenu = Menu(menubar, tearoff=0)
   helpmenu.add_command(label="Help Index", command=donothing)
   helpmenu.add_command(label="About...", command=donothing)
   menubar.add_cascade(label="Help", menu=helpmenu)
   root.config(menu=menubar)
   ###########################
   frm = ttk.Frame(root, padding=200)
   frm.grid()
   ttk.Label(frm, text="label2!").grid(column=0, row=0)
   ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
   ttk.Label(frm, text="dairy!").grid(column=0, row=7)
   ttk.Button(frm, text="dairy!", command=dfn).grid(column=1, row=7)
   ttk.Label(frm, text="delete!").grid(column=0, row=8)
   ttk.Button(frm, text="delete!", command=delete_2).grid(column=1, row=8)
   ttk.Label(frm, text="greetings!").grid(column=2, row=0)
   ttk.Button(frm, text="greetings!", command=greetings).grid(column=3, row=0)
   ttk.Label(frm, text="chatbot!").grid(column=2, row=1)
   ttk.Button(frm, text="chatbot!!!", command=main).grid(column=3, row=1)
   ttk.Label(frm, text="sayhello!").grid(column=2, row=2)
   ttk.Button(frm, text="sayhello!!!", command=say_hello).grid(column=3, row=3)

   root.mainloop()
