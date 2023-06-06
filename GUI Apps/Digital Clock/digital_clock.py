from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.minsize(450, 100)
root.maxsize(100, 100)

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=('digital-7', 80), background="black", foreground="white")
label.pack(anchor='center')
time()

mainloop()


