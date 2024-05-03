#--------------------------------------------------------------------------------------------
#Printing Labek------------------------------------------------------------------------------

from tkinter import *

root = Tk()
label1 = Label(root, text="Hello world")
label1.pack()
root.mainloop()

#--------------------------------------------------------------------------------------------
#Creating Frames and Buttons-----------------------------------------------------------------
from tkinter import *

root = Tk()
frm1 = Frame(root)
frm1.pack(side=TOP)

frm2 = Frame(root)
frm2.pack(side=BOTTOM)

b1 = Button(frm1, text="Click Here", fg="RED")
b2 = Button(frm2, text="Press on this", fg="BLUE")

b1.pack()
b2.pack()

root.mainloop()

#--------------------------------------------------------------------------------------------
#Using Grid Layout---------------------------------------------------------------------------
from tkinter import *

root = Tk()

l1 = Label(root, text="First Name")
l2 = Label(root, text="Last Name")
entry1 = Entry(root)
entry2 = Entry(root)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()

#--------------------------------------------------------------------------------------------
#Self Adjusting Labels-----------------------------------------------------------------------
from tkinter import *

root = Tk()

label1 = Label(root, text='First Name', bg='YELLOW', fg='RED')
label1.pack(side=TOP, fill=X)

label2 = Label(root, text='Second Name', fg='BLUE', bg='GREEN')
label2.pack(side=LEFT, fill=Y)

root.mainloop()

#--------------------------------------------------------------------------------------------
#Handling Button Clicks----------------------------------------------------------------------
from tkinter import *

root = Tk()

def function1():
    print("Hello You just clicked here")

b1 = Button(root, text="click", command=function1)
b1.pack()

root.mainloop()

#--------------------------------------------------------------------------------------------
#Why OOP Here--------------------------------------------------------------------------------
from tkinter import *

root = Tk()

class MyButton:
    def __init__(self, root):
        frm = Frame(root)
        frm.pack()

        self.butt1 = Button(frm, text="click", fg="RED", command=self.print_data)
        self.butt1.pack(side=TOP)

        self.butt2 = Button(frm, text="Exit", command=frm.quit)
        self.butt2.pack()

    def print_data(self):
        print("Hello How r You?")

b = MyButton(root)
root.mainloop()

#--------------------------------------------------------------------------------------------
#Create Dropdown menu------------------------------------------------------------------------
from tkinter import *

root = Tk()

def fun1():
    print("You just clicked menu")

def fun2():
    print("Hi")

mymenu = Menu(root)
submenu = Menu(mymenu)
root.config(menu=mymenu)

mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="NewNotebook", command=fun1)
submenu.add_command(label="open", command=fun2)
submenu.add_separator()
submenu.add_command(label="save", command=fun2)

newmenu = Menu(mymenu)
mymenu.add_cascade(label="edit", menu=newmenu)
newmenu.add_command(label="Undo", command=fun1)

root.mainloop()

#--------------------------------------------------------------------------------------------
#Create toolbar------------------------------------------------------------------------------

from tkinter import *

root = Tk()

def fun1():
    print("You just clicked menu")

def fun2():
    print("Hi")

toolbar1 = Frame(root, bg="RED")
butt1 = Button(toolbar1, text="print", command=fun1)
butt1.pack(side=LEFT, padx=2, pady=2)

butt2 = Button(toolbar1, text="##", command=fun2)
butt2.pack(side=LEFT, padx=3, pady=3)

butt3 = Button(toolbar1, text="++", command=fun2)
butt3.pack(side=LEFT, padx=3, pady=3)

toolbar1.pack(side=TOP, fill=X)

root.mainloop()


#--------------------------------------------------------------------------------------------
#Status Bar----------------------------------------------------------------------------------
from tkinter import *

root = Tk()

statusbar1 = Label(root, text="Hi This is status", anchor=W, bd=1, relief=SUNKEN)
statusbar1.pack(side=BOTTOM, fill=X)

root.mainloop()

#--------------------------------------------------------------------------------------------
#Message Box---------------------------------------------------------------------------------
from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("title", "Don't Fall for her Again")

res = tkinter.messagebox.askquestion("Que.1", "Is She the One!")
if res == 'yes':
    print("Here is tea")
else:
    print("Ok")

root.mainloop()

#--------------------------------------------------------------------------------------------
#Canvas--------------------------------------------------------------------------------------
from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

root.mainloop()
