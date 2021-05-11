from tkinter import *

top = Tk()
playList = []

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs")
    LMain.grid(column = 2, row = 1)
    
    B1Main = Button(text = " Week One ", bg = "#719bb3", command = weekOne)
    B1Main.grid(column = 2, row = 3)
    
    B2Main = Button(text = " Week Two ", bg = "#719bb3", command = weekTwo)
    B2Main.grid(column = 2, row = 4)
    
    B3Main = Button(text = " Week Three ", bg = "#719bb3", command = weekThree)
    B3Main.grid(column = 2, row = 5)


def weekOne():
    
    def addToList():
        newItem = E1.get()
        playList.append(newItem)
        E1.delete(0, END)
    
    clearWindow()
    #This is a label widget
    L1 = Label(top, text = "Playlist")
    L1.grid(column = 0, row = 1)

    #This is an entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)


    #This is a button widget

    B1 = Button(text = "  Print ", bg = "#5defb5", command = results)
    B1.grid(column = 0, row = 3)

    B2 = Button(text = " + ", bg = "#5fe42b", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = " Export List ", bg = "#5defb5", command = exportList)
    B3.grid(column = 0, row = 4)

    BMenu = Button(text = "Main Menu", bg = "red", command = mainMenu)
    BMenu.grid(column = 1, row = 3)

def weekTwo():
    clearWindow()
    L1W2 = Label(top, text = "  Dice Roller Program  ")
    L1W2.grid(column = 1, row = 0)

    L2W2 = Label(top, text = "  How many sides?  ")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text = "  How many rolls?  ")
    L3W2.grid(column = 2, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 2, row = 3)

    B1W2 = Button(text = " Roll ", bg = "#5fe42b")
    B1W2.grid(column = 1, row = 5)

    B2W2 = Button(text = " Exit ", bg = "red")
    B2W2.grid(column = 1, row = 6)
    
def weekThree():
    clearWindow()

def results():
    results = E1.get()
    print(results)
    print(type(results))

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def exportList():
    with open('test.txt', 'w') as f:
        for item in playList:
            f.write("%s/n" % item)

if __name__ == "__main__":
    mainMenu()
    top.mainloop()
