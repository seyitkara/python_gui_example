# importing  all the
# functions defined in py001.py
from calling_func import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from urllib import request
import pandas as pd
from multiprocessing.pool import ThreadPool
import pypyodbc


connection = pypyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=database01;')
cursor = connection.cursor()
cursor.execute("SELECT * FROM Table1")
sonuc = cursor.fetchall()
for i in sonuc:
    print(i)


def sql01():
    master = Tk()
    master.geometry("200x200")
    label = Label(master,text ="This is the main window")
    label.pack(pady = 10)

    mainloop()
