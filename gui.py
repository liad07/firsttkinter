from tkinter import *
import tkinter as tk
import socket
from win32api import GetSystemMetrics


hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)
print(hostname)
print(ip)
tkWindow = Tk()
tkWindow.configure(bg="white")

tkWindow.geometry(f"{GetSystemMetrics(0)}x{GetSystemMetrics(1)}")
tkWindow.title(hostname)
label=Label(tkWindow, text=ip, bg="red")
label.config(font=("arial", 40))
label.pack()


button = Button(tkWindow, text='Quit', bg='#ffb3fe',command=tkWindow.destroy)
button.config(font=("arial", 15))
button.pack()

tkWindow.mainloop()