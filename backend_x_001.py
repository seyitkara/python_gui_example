import tkinter as tk
import subprocess

def say_hello():
   subprocess.run(["./hello_cpp"])

root = tk.Tk()
root.title("Hello World GUI")

label = tk.Label(root, text="Hello, World!")
label.pack(padx=20, pady=20)

button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack(pady=10)

root.mainloop()
