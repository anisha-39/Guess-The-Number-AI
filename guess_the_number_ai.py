import tkinter as tk
import random

def check_guess():
    user_guess = int(entry.get())
    if user_guess < number:
        result.set("Too low!")
    elif user_guess > number:
        result.set("Too high!")
    else:
        result.set("Correct! 🎉")

number = random.randint(1, 100)

window = tk.Tk()
window.title("Guess The Number Game")

tk.Label(window, text="Guess a number between 1 and 100").pack()
entry = tk.Entry(window)
entry.pack()
tk.Button(window, text="Submit", command=check_guess).pack()
result = tk.StringVar()
tk.Label(window, textvariable=result).pack()

window.mainloop()
