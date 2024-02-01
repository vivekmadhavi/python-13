from tkinter import *


root = Tk()
root.title("app by me")
root.geometry("700x700+200+100")
f=("Arial",30,"bold")

def r():
	try:
		n=float(num.get())
		s = n * n
		sq= round(s,2)
		msg="square"+str(sq)
		ans.configure(text=msg)
	except ValueError:
		msg="u shud only enter integer"
		ans.configure(text=msg)
	

name=Label(root,text="Square Finder App",font=f)
number=Label(root,text="enter number",font=f)
num=Entry(root,font=f)
btn=Button(root,text="square",font=f,command=r)
ans=Label(root,font=f)

name.pack(pady=10)
number.place(x=20,y=200)
num.place(x=300,y=200)
btn.pack(pady=250)
ans.place(x=200,y=500)

root.mainloop()