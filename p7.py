from tkinter import *
from random import *

root = Tk()
root.title("color me  - app by me")
root.geometry("700x600+200+100")
f=("Arial" , 40,"bold")

def r():
	colors=["red","yellow","green","blue","salmon"]
	co = choice(colors)
	root.configure(bg=co)

btnred=Button(root, text="color",font=f,width=10,command=r)

btnred.pack(pady=15)
root.mainloop()