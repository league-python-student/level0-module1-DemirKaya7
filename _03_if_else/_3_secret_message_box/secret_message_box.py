from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    password = "eee"

    secretMessage = simpledialog.askstring(title="Enter a secret message", prompt="Secret message = ")

    guess = simpledialog.askstring(title="Guess the password", prompt="Passowrd = ")

    if guess == password:
        messagebox.showinfo(title="Secret Message", message=secretMessage)
    else:
        messagebox.showwarning(title="INTRUDER", message="INTRUDER")