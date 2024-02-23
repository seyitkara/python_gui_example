import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

def delete_2():
    def delete_file(file_path):
        try:
            # Check if the file exists
            if os.path.exists(file_path):
                # Show confirmation dialog
                confirm = messagebox.askquestion("Confirmation", f"Are you sure you want to delete '{file_path}'?")
                if confirm == 'yes':
                    # Delete the file
                    os.remove(file_path)
                    messagebox.showinfo("Success", f"File '{file_path}' deleted successfully.")
                else:
                    messagebox.showinfo("Cancelled", "Deletion cancelled.")
            else:
                messagebox.showerror("File Not Found", "File not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # Create the main application window
    window = tk.Tk()
    window.title("Delete File")

    # Create an entry widget to input the file path
    def search_for_file_path ():
            currdir = os.getcwd()
            tempdir = filedialog.askopenfilename(parent=window, initialdir=currdir, title='Please select a directory')
            if len(tempdir) > 0:
                print ("You chose: %s" % tempdir)
            return tempdir
    
    # Function to handle button click event
    def delete_button_click():
        # Get the file path from the entry widget
        file_path = search_for_file_path()
        delete_file(file_path)
    
    # Create a delete button
    delete_button = tk.Button(window, text="Delete", command=delete_button_click)
    delete_button.pack(pady=5)
    quit_button = tk.Button(window, text="Quit", command=window.destroy)
    quit_button.pack(pady=25)

    # Start the main event loop
    window.mainloop()
    exit()
