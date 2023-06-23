from tkinter import *
tk=Tk()
def fun():
	if(g.get()==1):
		u.set("male")
	if(g.get()==2):
		u.set("female")
	if(g.get()==3):
		u.set("others")
def fun1():
	if(c.get()==1):
		u1.set("cricket")
tk.geometry("1000x500")
u=StringVar()
u1=StringVar()
tk.title("new page")
tk.config(bg="blue")
b=Button(tk,bg="yellow",text="okay")
b.place(x=30,y=470)
g=IntVar()
c=IntVar()
c1=IntVar()
r1=Radiobutton(tk,text="male",value=1,variable=g,command=fun)
r1.place(x=50,y=170)
r2=Radiobutton(tk,text="female",value=2,variable=g,command=fun)
r2.place(x=50,y=200)
r3=Radiobutton(tk,text="other",value=3,variable=g,command=fun)
r3.place(x=50,y=230)
cb=Checkbutton(tk,text="cricket",onvalue=1,offvalue=0,variable=c,command=fun1)
cb.place(x=200,y=170)
cb1=Checkbutton(tk,text="volleyball",onvalue=1,offvalue=0,variable=c)
cb1.place(x=200,y=200)
e=Entry(tk,bg="white",width="50",textvariable=u)
e.place(x=30,y=90)
e1=Entry(tk,bg="white",width="50",textvariable=u1)
e1.place(x=30,y=130)
mainloop()
