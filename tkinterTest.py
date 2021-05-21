#MAKE SURE TO ADD TIME SLEEPS BEFORE SUBMITTING FINAL CODE!!!!!
from tkinter import *
import random

top = Tk()
playList = []
myRolls = []
myList = []
unique_list = []
numberOfRolls = 0
dieType = 0

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs")
    LMain.grid(column = 1, row = 0)
    L1K1 = Label(top, text = "       ")
    L1K1.grid(column = 0, row = 1)
    L1K2 = Label(top, text = "       ")
    L1K2.grid(column = 2, row = 1)

    
    B1Main = Button(text = " Week One ", bg = "#719bb3", command = weekOne)
    B1Main.grid(column = 1, row = 3)
    
    B2Main = Button(text = " Week Two ", bg = "#719bb3", command = weekTwo)
    B2Main.grid(column = 1, row = 4)
    
    B3Main = Button(text = " Week Three ", bg = "#719bb3", command = weekThree)
    B3Main.grid(column = 1, row = 5)


def weekOne():
    def addToList():
        newItem = E1.get()
        playList.append(newItem)
        E1.delete(0, END)

    def results():
        results = E1.get()
        print(results)
        print(type(results))
        
    def exportList():
        with open('test.txt', 'w') as f:
            for item in playList:
                f.write("%s/n" % item)
    
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

    BMenu = Button(text = "Return to Block 5 GUIs", bg = "red", command = mainMenu)
    BMenu.grid(column = 1, row = 3)

def weekTwo():
    def rollDice():
        #update variable data
        dieType = E1W2.get()
        numberOfRolls = E2W2.get()
        #clear window after pulling entry data
        clearWindow()
        #calculate dice rolls
        for x in range(0, int(numberOfRolls)):
                myRolls.append(random.randint(1, int(dieType)))
        #display dice rolls and present an exit button
        L4W2 = Label(top, text = "Here are your rolls!")
        L4W2.grid(column = 0, row = 1)
        L5W2 = Label(top, text = "{}".format(myRolls))
        L5W2.grid(column = 0, row = 3)
        B2W2 = Button(text = " Main Menu ", bg = "red", command = mainMenu)
        B2W2.grid(column = 1, row = 2)
    
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

    B1W2 = Button(text = " Roll ", bg = "#5fe42b", command = rollDice)
    B1W2.grid(column = 1, row = 5)
    BReturn2 = Button(text = "Return to Block 5 GUIs", bg = "#6aad92", command = mainMenu)
    BReturn2.grid(column = 0, row = 7)

    
def weekThree():
#FILL IN ALL GRID STATEMENTS
    def editMenu():
        clearWindow()
        L3W3 = Label(top, text = "     Edit Menu     ")
        L3W3.grid(column = 0, row = 0)

        B3W3 = Button(text = "  Add to List  ", bg = "#6aad92", command = addOne)
        B3W3.grid(column = 0, row = 2)
        B4W3 = Button(text = "  Clear List  ", bg = "#6aad92",  command = clearList)
        B4W3.grid(column = 0, row = 3)
        B5W3 = Button(text = "  Sort List  ", bg = "#6aad92", command = sortList)
        B5W3.grid(column = 0, row = 4)
        B1M = Button(text = "  Main Menu  ", bg = "#6aad92", command = weekThree)
        B1M.grid(column = 0, row = 5)
        
    def searchMenu():
        clearWindow()
        L4W3 = Label(top, text = "     Search Menu     ")
        L4W3.grid(column = 0, row = 0)

        B6W3 = Button(text = "  Search List  ", bg = "#6aad92", command = linearSearch)
        B6W3.grid(column = 0, row = 2)
        B7W3 = Button(text = "  Generate a Random Number  ", bg = "#6aad92", command = generateRandom)
        B7W3.grid(column = 0, row = 3)
        B8W3 = Button(text = "  Read Index Position  ", bg = "#6aad92", command = indexValues)
        B8W3.grid(column = 0, row = 4)
        B10W3 = Button(text = "  Print List  ", bg = "#6aad92", command = printList)
        B10W3.grid(column = 0, row = 5)
        B2M = Button(text = "  Main Menu  ", bg = "#6aad92", command = weekThree)
        B2M.grid(column = 0, row = 6)
    def clearList():
        clearWindow()
        myList.clear()
        L7W3 = Label(top, text = "  List Cleared  ")
        L7W3.grid(column = 0, row = 0)
        B3M = Button(text = "  Main Menu  ", bg = "#6aad92", command = weekThree)
        B3M.grid(column = 0, row = 1)

    def sortList():
        clearWindow()
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        unique_list.sort()
        L8W3 = Label(top, text = "  List Sorted  ")
        L8W3.grid(column = 0, row = 0)
        B4M = Button(text = "  Main Menu  ", bg = "#6aad92", command = weekThree)
        B4M.grid(column = 0, row = 1)
    def linearSearch():
        clearWindow()
        L9W3 = Label(top, text = "What number would you like to find?")
        L9W3.grid(column = 0, row = 0)
        E1W3 = Entry(top, bd = 5)
        E1W3.grid(column = 0, row = 2)
        for x in range(len(myList)):
            if myList[x] == int(E1W3.get):
                indexCount = indexCount + 1
                L10W3 = Label(top, text = "  Your item is at index {}  ".format(x)) 
        B5M = Button(text = "  Main Menu  ", bg = "#6aad92", command = weekThree)
        B5M.grid(column = 0, row = 3)

    def generateRandom():
        clearWindow()
        print("  Your number is {}  ".format(myList[random.randint(0, len(myList)-1)]))
        B6M = Button(text = "  Main Menu  ", bg = "#6aad92", command = weekThree)
        B6M.grid(column = 0, row = 1)
    def indexValues():
        def printIndex():
            indexPos = E2W3.get()

            clearWindow()
            print("Here you go! Your number is {}".format(myList[int(indexPos)]))
        clearWindow()
        L12W3 = Label(top, text = "What index position would you like to check?")
        L12W3.grid(column = 0, row = 0)
        E2W3 = Entry(top, bd = 5)
        E2W3.grid(column = 0, row = 2)
        B7M = Button(text = "  Main Menu  ", bg = "#6aad92", command = weekThree)
        B7M.grid(column = 0, row = 3)
        BPlus = Button(text = "  Enter  ", bg = "#6aad92", command = printIndex)
        BPlus.grid(column = 1, row = 2)

    
        
    def printList():
        clearWindow()
        L14W3 = Label(top, text = myList)
        L14W3.grid(column = 0, row = 0)
        B8M = Button(text = "  Main Menu  ", bg = "#6aad92", command = weekThree)
        B8M.grid(column = 0, row = 1)

    def addOne():
        clearWindow()
        def makeList():
            thatItem = E3W3.get()
            myList.append(thatItem)
            E3W3.delete(0, END)
        #This is a label widget
        L14W3 = Label(top, text = "Add One to List")
        L14W3.grid(column = 0, row = 1)

        #This is an entry widget
        E3W3 = Entry(top, bd = 5)
        E3W3.grid(column = 0, row = 2)


        #This is a button widget

        B13W3 = Button(text = "  Print ", bg = "#5defb5", command = printList)
        B13W3.grid(column = 0, row = 3)

        B14W3 = Button(text = " + ", bg = "#5fe42b", command = makeList)
        B14W3.grid(column = 1, row = 2)

        B15W3 = Button(text = " Print List ", bg = "#5defb5", command = printList)
        B15W3.grid(column = 1, row = 3)

        BMenuW3 = Button(text = "Main Menu", bg = "red", command = weekThree)
        BMenuW3.grid(column = 0, row = 3)

    clearWindow()
    L1W3 = Label(top, text = " Let's Make a List ")
    L1W3.grid(column = 0, row = 0)
    L2W3 = Label(top, text = "     Main Menu     ")
    L2W3.grid(column = 0, row = 1)
    L1S1 = Label(top, text = "       ")
    L1S1.grid(column = 0, row = 2)

    B1W3 = Button(text = " Edit Menu ", bg = "#6aad92", command = editMenu)
    B1W3.grid(column = 0, row = 3)
    B2W3 = Button(text = " Search Menu ", bg = "#6aad92", command = searchMenu)
    B2W3.grid(column = 0, row = 4)

    BReturn3 = Button(text = "Return to Block 5 GUIs", bg = "#6aad92", command = mainMenu)
    BReturn3.grid(column = 0, row = 6)


def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()



if __name__ == "__main__":
    mainMenu()
    top.mainloop()
