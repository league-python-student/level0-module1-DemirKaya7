# Write a Python program that asks the user for two numbers. 
# Then display the sum of the two numbers

from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    num1 = simpledialog.askinteger(title="Number 1", prompt="Enter a number")
    num2 = simpledialog.askinteger(title="Number 2", prompt="Enter another number")

    sum = num1 + num2

    messagebox.showinfo(title="Sum", message=sum)