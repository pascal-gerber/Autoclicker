from tkinter import *
import keyboard
import mouse
import threading
import time

clicking = 0
flicker = False

def startUp(sleepingTime, key):
    global clicking
    global flicker
    
    def clicker():
        while flicker == True:
            mouse.click("left")
            time.sleep(sleepingTime)
        
    def checkForClicks():
        while 1:
            global clicking
            global flicker
            del clicking
            keyboard.wait(str(key))
            flicker = not flicker
            clicking = threading.Thread(target = clicker)
            clicking.start()

    checker = threading.Thread(target = checkForClicks)
    checker.start()
    

def createWindow():
    window = Tk()

    empty = Label(window, height = 3, width = 15, bg = "Cyan")
    empty.grid(row = 0, column = 0)

    Title = Label(window, text="Autoclicker", font=("Calibri", 15), bg = "Cyan")
    Title.grid(row = 1, column = 1)

    empty = Label(window, height = 3, bg = "Cyan")
    empty.grid(row = 2, column = 0)

    informationOne = Label(window, text="Time betwem each click", bg = "Cyan")
    informationOne.grid(row = 3, column = 1)

    timeToSet = Entry(window)
    timeToSet.grid(row = 4, column = 1)
    timeToSet.insert('end', '0.1')

    empty = Label(window, height = 3, bg = "Cyan")
    empty.grid(row = 5, column = 0)

    informationTwo = Label(window, text="switch Key", bg = "Cyan")
    informationTwo.grid(row = 6, column = 1)
    
    letterPressed = Entry(window)
    letterPressed.grid(row = 7, column = 1)
    letterPressed.insert('end', 'q')

    empty = Label(window, height = 3, bg = "Cyan")
    empty.grid(row = 8, column = 0)

    confirm = Button(window, text="Confirm", bg="Lime", height = 4, width = 16,
                     command = lambda timeToSet = timeToSet, letterPressed = letterPressed:startUp(float(timeToSet.get()), letterPressed.get()))
    confirm.grid(row = 9, column = 1)

    window.configure(bg = "Cyan")
    window.geometry("500x500")
    window.mainloop()





createWindow()



#use this for games :b
#Enjoy!
