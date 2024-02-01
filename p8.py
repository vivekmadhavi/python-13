from tkinter import *
from random import *


root = Tk()
root.title("color me  - app by me")
root.geometry("700x600+200+100")
f=("Arial" , 40,"bold")

def c():
	colors=["red","yellow","green","blue","salmon"]
	co=choice(colors)
	root.configure(bg=co)
	root.after(10000,c)
c()
	
root.mainloop()         