# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

from tkinter import simpledialog, messagebox, Tk
import math

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    radius = simpledialog.askinteger(title="Radius", prompt="Enter the radius")
    option = simpledialog.askstring(title="Area or Circumference?", prompt="Enter Area or Circumference")

    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius

    if option == "Area":
        messagebox.showinfo(title="Area", message="Area = " + str(area))
    elif option == "Circumference":
        messagebox.showinfo(title="Circumference", message="Circumference = " + str(circumference))
    else:
        messagebox.showerror(title="Error", message="Please enter Area or Circumference")