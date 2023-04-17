import keyboard
import mouse
import threading
import time

flicker = False
clicking = 0

def clicker():
    while flicker == True:
        mouse.click("left")
        time.sleep(0.1)

while 1:
    del clicking #deletes to not overload the PC overtime
    keyboard.wait("q") #change key for autoclicker change
    flicker = not flicker
    clicking = threading.Thread(target = clicker)
    clicking.start()

#use this for games :b
#Enjoy!
