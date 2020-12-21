from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    name = simpledialog.askstring(title="Enter a name", prompt="(Mike, Jon, or Chris)")
    if name == "Mike":
        messagebox.showinfo(title="Mike", message="intelligent")
    elif name == "Jon":
        messagebox.showinfo(title="Jon", message="athletic")
    elif name == "Chris":
        messagebox.showinfo(title="Chris", message="dedicated")
    else:
        messagebox.showinfo(title="Student is not in class", message="Enter a different name")
