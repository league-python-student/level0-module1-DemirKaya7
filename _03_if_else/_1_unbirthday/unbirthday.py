from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    birthday = simpledialog.askstring(title="Birth date", prompt="Enter your birthday (mm/dd)")

    if birthday == "12/21":
        messagebox.showinfo(title="Happy Birthday", message="It is your birthday")
    else:
        messagebox.showinfo(title="Happy Unbirthday", message="It is not you bithrday")