from tkinter import*
from tkinter.ttk import*
from time import strftime
import tkinter.font as font
import random

window = Tk()
window.geometry("500x250")
window.title("Personal Clock")

def time():
    pctime = strftime('%I:%M:%S %p %a %b')
    labl.config(text = pctime)
    labl.after(1000,time)

def colour():
    coloru = ["blue","red","green","orange"]
    labl.config(foreground = random.choice(coloru))
    labl.after(1000,colour)
    
    
labl = Label(window,text = "time",foreground = ("grey"),font =('Comic Sans MS',40,'bold'))
labl.pack(anchor = "center",pady = 50)


time()
colour()


window.mainloop()
