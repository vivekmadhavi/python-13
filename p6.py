from tkinter import *

root = Tk()
root.title("color me  - app by me")
root.geometry("700x600+200+100")
f=("Arial" , 40,"bold")

def r():
	root.configure(bg="red")
def g():
	root.configure(bg="green")
def b():
	root.configure(bg="blue")

btnred=Button(root, text="red",font=f,width=10,command=r)
btngreen=Button(root, text="green",font=f,width=10,command=g)
btnblue=Button(root, text="blue",font=f,width=10,command=b)

btnred.pack(pady=15)
btngreen.pack(pady=15)
btnblue.pack(pady=15)

root.mainloop()