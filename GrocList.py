from tkinter import*
from tkinter.ttk import *
import tkinter.font as font
import sys
import os
from PIL import Image, ImageTk



def listPlace(grocery, item):
    iteration = -1
    for iter in range(len(grocery)):
        if grocery[iter][0] == item:
            iteration = iter
    return iteration

def quit(self):
    return self.quit(interface)

def restart():
    reset = sys.executable
    os.execl(reset, reset, * sys.argv)

def removeGrocery(grocery, iteration):
    del(grocery[iteration])
    

def addGrocery(grocery, item, iteration):
    if iteration == -1:
        grocery.append([item,1])
    else:
        grocery[iteration][1] = grocery[iteration][1] + quantity.get()
        

def groceryList(grocery):
    for item in grocery:
        someList.insert(END, item[0] + " | " + str(item[1]))



def addItems():
    iteration = listPlace(grocery, item.get())
    addGrocery(grocery, item.get(), iteration)
    if iteration >= 0:
        someList.delete(iteration)
        someList.insert(iteration,grocery[iteration][0] + " | " + str(grocery[iteration][1]))
    else:
        someList.insert(END, item.get() + " | " + str(quantity.get()))

def removeItems():
    iteration = someList.index(current)
    removeGrocery(grocery, iteration)
    someList.delete(iteration)


grocery = []

interface = Tk()
interface.geometry("350x300")

interface.title("Grocery List")
interface.configure()

someList = Listbox(interface, selectmode=BROWSE, bg='white', selectbackground='black')
someList.grid(row=2,column=1,sticky=N)
scroll = Scrollbar(interface, orient=VERTICAL)
scroll.grid(row=2, column=3, sticky='nsw')
someList.config(yscrollcommand=scroll.set)
scroll.config(command=someList.yview)

groceryList(grocery)
item=StringVar()
quantity=IntVar()

Button(interface, text="Add",  command=addItems).grid(row=5,column=1)
Label(interface, text="Click Remove to get rid of it").grid(row=2, column=0, sticky=S, pady=20)
Button(interface, text="Remove", command=removeItems).grid(row=5, column=0)
Label(interface,  text="Grocery Item:").grid(row=4, column=0, sticky=N)
Label(interface, text="Enter amount and item to add").grid(row=2,column=0, sticky=S)
Entry(interface, textvariable=item).grid(row=4,column=1,sticky=N)
Label(interface, text="Welcome to your grocery list!").grid(row=1,column=0, sticky=SW)
Label(interface, text="Amount:").grid(row=3,column=0, sticky=N)
Entry(interface, textvariable=quantity).grid(row=3,column=1, sticky=N)
Button(interface, text="Quit", command=interface.quit).grid(row=6,column=1,)
Button(interface, text="Restart", command=restart).grid(row=6, column=0)
image = Image.open("Logo.png")
image = image.resize((100,100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label = Label(interface, image=photo)
label.image=photo
label.grid(row=2, column=0, sticky=N)



interface.mainloop()
exit(0)




    
