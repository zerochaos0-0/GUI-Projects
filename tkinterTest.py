from tkinter import *

top = Tk()
groceryList = []

def results():
    results = E1.get()
    print(results)
    print(type(results))

def addToList():
    newItem = E1.get()
    groceryList.append(newItem)

def clearList():
    groceryList.clear()
    

#This is a label widget
L1 = Label(top, text = "Grocery List")
L1.grid(column = 0, row = 1)

#This is an entry widget
E1 = Entry(top, bd = 5)
E1.grid(column = 0, row = 2)


#This is a button widget
B1 = Button(text = "    Print Your List    ", bg = "light blue", command = results)
B1.grid(column = 1, row = 3)
B2 = Button(text = "    Add to List    ", bg = "light blue", command = addToList)
B2.grid(column = 1, row = 2)
B3 = Button(text = "    Clear List    ", bg = "light blue", command = clearList)
B3.grid(column = 0, row = 3)

top.mainloop()

