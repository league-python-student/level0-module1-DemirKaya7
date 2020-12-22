'''
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
'''

from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    numberCorrect = 0

    answer1 = simpledialog.askstring(title="Riddle 1", prompt="I am six letters. When you take one away I am twelve. What am I?")

    if answer1 == "A dozen":
        numberCorrect = numberCorrect + 1

    answer2 = simpledialog.askstring(title="Riddle 2", prompt="What has six faces, but does not wear makeup, has 21 eyes but cannot see?")

    if answer2 == "A die":
        numberCorrect = numberCorrect + 1

    answer3 = simpledialog.askstring(title="Riddle 3", prompt="Feed me and I will grow. Give me a drink and I will die. What am I?")

    if answer3 == "Fire":
        numberCorrect = numberCorrect + 1

    messagebox.showinfo(title="Score", message="You got " + str(numberCorrect) + " out of 3")