from tkinter import *

windowWidth = 800
windowHeight = 800
root = Tk()

canvas = Canvas(root, width=windowWidth, height=windowHeight, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()
    
# this code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # draws a dark blue background
    canvas.create_rectangle(0, 0, windowWidth, windowHeight, fill="#000050")
    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y
    
    # this defines the x and y coordinated of all three points
    # of a triangle
    shipPoints = [x+100, y, x-100, y, x-100, y+250, x+100, y+250]
    outerFirePoints = [x+100, y+250, x+150, y+300, x-150, y+300, x-100, y+250]
    firePoints = [x+175, y+300, x+200, y+350, x-200, y+350, x-175, y+300]
    shipTop = [x+100, y, x-100, y, x, y-150]
    canvas.create_polygon(shipPoints, fill='gray', width=2) #draws triangle
    
    #1. Add details to your rocket to make it look better. You can look at rocket.png for inspiration.
    canvas.create_polygon(outerFirePoints, fill='orange', width=1)
    canvas.create_polygon(firePoints, fill='red', width=1)
    canvas.create_polygon(shipTop, fill = 'black', width=1)
    #2. Modify the locations of the shapes above so the rocket will be drawn where the mouse is clicked
    

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()