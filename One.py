import tkinter as tk
from math import sqrt

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.title("Advanced Calculator")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=10, insertwidth=4, width=14, borderwidth=4)
screen.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '√', '**', '%'
]

row = 1
col = 0
for button in buttons:
    b = tk.Button(root, text=button, font="Arial 18", padx=20, pady=20)
    b.grid(row=row, column=col)
    b.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
