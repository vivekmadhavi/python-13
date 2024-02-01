from tkinter import *


root = Tk()
root.title("app by me")
root.geometry("1000x1000+200+100")
f=("Arial",30,"bold")


def show():
	n=num.get()
	choice=""
	if c.get()==1:
		choice="job"
	elif c.get()==2:
		choice="ms"
	elif c.get()==3:
		choice="mba"
	msg="name ="+ n+" " +"choice ="+choice	
	ans.configure(text=msg)

name=Label(root,text="What next??",font=f)
number=Label(root,text="enter name",font=f)
num=Entry(root,font=f)
sel=Label(root,text="select",font=f)
btn=Button(root,text="submit",font=f,command=show)
ans=Label(root,font=f)

c=IntVar()
c.set(1)
job=Radiobutton(root,text="job",font=f,value=1,variable=c)
ms=Radiobutton(root,text="ms",font=f,value=2,variable=c)
mba=Radiobutton(root,text="mba",font=f,value=3,variable=c)

name.pack(pady=10)
number.place(x=20,y=200)
num.place(x=300,y=200)
sel.place(x=20,y=300)
btn.place(x=300,y=500)
ans.place(x=200,y=600)
job.place(x=300,y=290)
ms.place(x=300,y=340)
mba.place(x=300,y=390)
root.mainloop()