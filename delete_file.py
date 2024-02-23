import os
from tkinter import filedialog
import tkinter

def delete():
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window
    def search_for_file_path ():
            currdir = os.getcwd()
            tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
            if len(tempdir) > 0:
                print ("You chose: %s" % tempdir)
            return tempdir

    def delete_file(file_path):
        try:
            # Check if the file exists
            if os.path.exists(file_path):
                # Confirm deletion
                confirm = input(f"Are you sure you want to delete '{file_path}'? (Y/N): ")
                if confirm.lower() == 'y':
                    # Delete the file
                    os.remove(file_path)
                    print(f"File '{file_path}' deleted successfully.")
                else:
                    print("Deletion cancelled.")
            else:
                print("File not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Provide the path to the file you want to delete
    file_path = search_for_file_path()
    delete_file(file_path)
    exit()