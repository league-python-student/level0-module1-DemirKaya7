import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    myTurtle = turtle.Turtle()
    myTurtle.goto(0,0)

    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="Shape", prompt="What shape would you like to draw?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "Triangle":
        for i in range(3):
            myTurtle.forward(100)
            myTurtle.left(120)

    elif shape == "Square":
        for i in range(4):
            myTurtle.forward(100)
            myTurtle.left(90)

    elif shape == "Pentagon":
        for i in range(5):
            myTurtle.forward(100)
            myTurtle.left(72)

    elif shape == "Hexagon":
        for i in range(6):
            myTurtle.forward(100)
            myTurtle.left(60)

    #Call the turtle .done() method
    turtle.done()
    
    window.mainloop()