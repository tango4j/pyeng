
import tkinter
from tkinter import *

top = tkinter.Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =10)

E1.pack(side = RIGHT)

top.mainloop()

print('The entry', E1)
