import tkinter as tk

def press(num):
    entry.insert(tk.END, num)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Graphical Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, command=calculate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t))
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text="C", width=5, height=2, command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

root.mainloop()