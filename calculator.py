from tkinter import *
from PIL import Image , ImageTk

def close():
    print("Ru sure u want to exit? ")

def minimize():
    print("Ru sure u want to minimize? ")

def help():
    print("Need help ? ")

root=Tk()

root.geometry("500x400")
root.title("My GUI")

root.minsize(200,100)

f1=Frame(bg="orange", padx=40 ,pady=40 , borderwidth=3,relief=SUNKEN)
f1.pack(side='left', fill=Y, pady=10,padx=10)

l=Label(f1,text="Hi there! Aur bhai ,keda phir? :)" ,fg="white" , bg="orange" , font="lucid 13 bold", )
l.pack()

greet=Label(text="ready", bg="brown" , fg= "white", padx=100, pady=10, font="Times 15 bold italic" , borderwidth=4, relief=GROOVE)
greet.pack(side="bottom" , fill=X , padx=10, pady=10)

f2=Frame(bg="red", padx=10, pady=10, relief=RAISED, borderwidth=10 )
f2.pack(pady=2 ,padx=2)

l2=Button(text="X", fg="white", bg="red", command=close)
l2.pack(side=RIGHT, anchor="ne", padx=2 , pady=1)

f3=Frame(bg="green", padx=10, pady=10, relief=RAISED, borderwidth=10 )
f3.pack(pady=2 ,padx=2)

l3=Button(text="o", fg="white", bg="green", command=help)
l3.pack(side=RIGHT, anchor="ne", padx=5)

f4=Frame(bg="black", padx=10, pady=10, relief=RAISED, borderwidth=10 )
f4.pack(pady=2 ,padx=2)

l4=Button(text="-", fg="white", bg="black", command=minimize)
l4.pack(side=RIGHT, anchor="ne", padx=4)



# pic=PhotoImage(file="sunnyDay.JPG")
# image=Image.open("pinkLaptop.gif")
# pic= ImageTk.PhotoImage(image)
#
# pic_label=Label(image=pic)

root.mainloop()

