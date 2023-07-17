from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("400x200")

def myfun():
    print("yo !sup peeps ;) ")
    tmsg.showinfo("myfun", "Romani is here :) ")

mymenue=Menu(root)
mymenue.add_command(label="option1", command=myfun)
mymenue.add_command(label="option2", command=quit)

root.config(menu=mymenue)
root.mainloop() 