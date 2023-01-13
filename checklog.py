import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()
root.configure(bg='#1D1F21')
root.state('zoomed')

style = ttk.Style()
style.theme_create("MyStyle", parent="alt", settings={
    "TFrame": {"configure": {"background": "#1D1F21"}},
    "TLabel": {"configure": {"foreground": "white", "background": "#1D1F21"}},
    "TButton": {"configure": {"foreground": "white", "background": "#1D1F21", "font": ("Helvetica", 20)}},
    "TCheckbutton": {"configure": {"background": "#1D1F21", "foreground":"white"}}
})
style.theme_use("MyStyle")

def open_file():
    os.system("python checkgaps.py")

open_file_button = ttk.Button(root, text="Click here to open a log file or drag and drop here", command=open_file)
open_file_button.place(relx=0.5, rely=0.5, anchor="center")
root.mainloop()
