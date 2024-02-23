import datetime
from datetime import date
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import threading

d = datetime.date.today()

def greetings():
    def write_greeting(file_path):
        greetings = {
            0: "Good night",
            1: "Good morning",
            2: "Good afternoon",
            3: "Good evening"
        }

        while True:
            current_time = datetime.datetime.now()
            hour = current_time.hour

            if hour < 5:
                greeting = greetings[0]
            elif hour < 12:
                greeting = greetings[1]
            elif hour < 17:
                greeting = greetings[2]
            else:
                greeting = greetings[3]

            try:
                with open(file_path, 'a') as file:
                    file.write(f"{current_time}: {greeting}\n")
            except:
                print("hayda")

            print(f"Greeting written to '{file_path}'")

            time.sleep(5)  # Sleep for 3 minutes (180 seconds)

    window = tk.Tk()
    window.withdraw() #use to hide tkinter window
    def search_for_file_path ():
        currdir = os.getcwd()
        tempdir = filedialog.askopenfilename(parent=window, initialdir=currdir, title='Please select a directory')
        if len(tempdir) > 0:
            print ("You chose: %s" % tempdir)
        return tempdir
    # Provide the path to the file you want to create
    file_path = search_for_file_path()

    # Create a separate thread to run the greeting writing process
    thread = threading.Thread(target=write_greeting, args=(file_path,))
    thread.daemon = True  # Set the thread as a daemon so it terminates when the main program ends
    thread.start()

    # Keep the main program running
    while True:
        time.sleep(1)
