# importing  all the
# functions defined in py001.py
from calling_func import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def new_window02():
    master = Tk()
    master.geometry("200x200")
    def openNewWindow():        
        newWindow = Toplevel(master)
        newWindow.title("New Window")
        newWindow.geometry("200x200")
        Label(newWindow,text ="This is a new window").pack()
        #canvas = Canvas(newWindow, width = 100, height = 100)      
        #canvas.pack()
        #img = PhotoImage(file="res\danger.png")      
        #canvas.create_image(50,50, anchor=NW, image=img)
    def openNewWindow2():   
        newWindow02 = Toplevel(master)
        image = Image.open('./res/danger.png')
        python_image = ImageTk.PhotoImage(image)
        #Label(newWindow2, image=python_image).pack()
        label1 = Label(image=python_image)
        label1.image = python_image
        label1.place(x=10,y=10)
        Button(newWindow02, text="Quit", command=master.destroy).grid(column=0, row=6)
    label = Label(master,text ="This is the main window")
    label.pack(pady = 10)
    btn = Button(master,text ="Click to open a new window",command = openNewWindow)
    btn.pack(pady = 10)
    btn2 = Button(master,text ="Click to open figure",command = openNewWindow2)
    btn2.pack(pady = 10)


    mainloop()

#burada ise calling_func ile func cagirilacak
