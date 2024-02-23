import datetime
from datetime import date
import tkinter
from tkinter import filedialog
import os

d = datetime.date.today()

def dfn():
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window

    def search_for_file_path ():
        currdir = os.getcwd()
        tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
        if len(tempdir) > 0:
            print ("You chose: %s" % tempdir)
        return tempdir

    def search_for_output_path ():
        curredir = os.getcwd()
        tdir = filedialog.askdirectory(parent=root, initialdir=curredir, title='Please select a directory')
        if len(tdir) > 0:
            print ("You chose: %s" % tdir)
        return tdir

    # Get the current date
    current_date = datetime.datetime.now()
    #current_hour = datetime.time.hour()
    #datetime.combine(current_date, current_hour)
    tarih = d.strftime("%Y.%m.%d")
    # Create a file and write the date inside it
    file_path = search_for_output_path()+"/"+tarih+".txt"
    with open(file_path, 'a') as file:
        file.write(str(current_date))
        file.write(str("\n"))
    dairy = input("Please add write dairy: ")
    with open(file_path, 'a') as file:
        file.write(f"Sevgili Günlük,\n{dairy}\n\n")
        file.write(str(current_date))
    print(f"File '{file_path}' created with the current date.")
    #quit()
    exit()
