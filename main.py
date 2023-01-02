import keyboard as key
import pynput 
import main
from time import sleep
from tkinter import Tk

# root = Tk()

# list = []
# listCounter = 0

# def on_scroll(x, y, dx, dy):
#     if dy > 0:
#         main.listCounter += 1
#     else: 
#         main.listCounter -= 1

#     print(list[listCounter])


# listener = pynput.mouse.Listener(
#     on_scroll=on_scroll)
# listener.start()


# while (key.is_pressed('ctrl+c') != True):
#     sleep(0.1)

# print("coppied!")
# root.withdraw()
# number = root.clipboard_get()
# print(number)


coppiedData = []
selectedItem = 0
toggleOn = False
root = Tk()

def on_scroll(x, y, dx, dy):
    if key.is_pressed("right arrow"):
        print('enter')
        main.toggleOn = False

    if main.toggleOn:
        if main.selectedItem == len(coppiedData)-1:
            if dy < 0:
                main.selectedItem -= 1
        elif main. selectedItem == 0:
            if dy > 0:
                main.selectedItem += 1
        else:
            main.selectedItem += dy
        key.write(coppiedData[selectedItem])
        for x in range(len(coppiedData[selectedItem])):
            key.press_and_release('shift+left arrow')
            print('current entry {0}, "{1}"'.format(
            selectedItem,
            coppiedData[selectedItem]))
        

listener = pynput.mouse.Listener(
    on_scroll=on_scroll)
listener.start()

while True:
    if key.is_pressed("ctrl+alt+v"):
        main.toggleOn = True
        print("activation")
        while key.is_pressed("ctrl"):
            sleep(0.1)
        key.write(coppiedData[0])
        for x in range(len(coppiedData[0])):
            key.press_and_release('shift+left arrow')
    elif key.is_pressed("right arrow"):
        main.toggleOn = False
        print('selected entry')
        selectedItem = 0
    elif key.is_pressed("ctrl+c"):
        root.withdraw()
        clipboard = root.clipboard_get()
        newArray = [clipboard]
        if len(coppiedData) == 0:
            coppiedData.append(clipboard)
        if clipboard != coppiedData[0]:
            newArray.extend(coppiedData)
            coppiedData = newArray
            print('coppied data')
    else:
        sleep(0.1)