import tkinter
import random

size = 50
color = ["red", "blue", "green", "yellow", "pink"]


# functions
def stamp(event = None):
    x = event.x
    y = event.y
    pad.create_oval(x - (size / 2), y - (size / 2), x + (size / 2), y + (size / 2), fill=random.choice(color))

def stamp2(event = None):
    size2 = random.randint(10,100)
    x = event.x
    y = event.y
    pad.create_rectangle(x - (size2 / 2), y - (size2 / 2), x + (size2 / 2), y + (size2 / 2), fill=random.choice(color))


# window setup
window = tkinter.Tk()
window.title("stamp.py")

# canvas setup
pad = tkinter.Canvas(window, height=600, width=600, bg="#2a2a2a")
pad.pack()
pad.bind("<Button-1>", stamp)
pad.bind("<Button-2>", stamp2)

window.mainloop()
