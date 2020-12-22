# Write a Python program that asks the user for two numbers.
# Then ask the user if the would like to add, subtract, multiply, or divide.
# Use if-else statements to provide the desired math operation on the numbers and display the result.

from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    num1 = simpledialog.askinteger(title="Number 1", prompt="Enter a number")
    num2 = simpledialog.askinteger(title="Number 2", prompt="Enter another number")

    operation = simpledialog.askstring(title="Operation", prompt="Add, Subtract, Multiply, or Divide?")

    if operation == "Add":
        answer = num1 + num2
    elif operation == "Subtract":
        answer = num1 - num2
    elif operation == "Multiply":
        answer = num1 * num2
    elif operation == "Divide":
        answer = num1 / num2
    else:
        messagebox.showerror(title="Error", message="Please make sure the operation is spelled and capitalized correctly")

    messagebox.showinfo(title="Result", message=answer)