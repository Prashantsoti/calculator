import tkinter as tk

def press(key):
    entry_var.set(entry_var.get() + str(key))

def clear():
    entry_var.set("")

def backspace():
    entry_var.set(entry_var.get()[:-1])

def calculate(event=None):  # event=None so Enter key works too
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def key_handler(event):
    if event.keysym in "0123456789":
        press(event.char)
    elif event.char in "+-*/.":
        press(event.char)
    elif event.keysym == "Return":  # Enter key
        calculate()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()

# Create main window
root = tk.Tk()
root.title("Perfect Calculator")
root.state('zoomed')   # Maximized window

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 30), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, sticky="nsew")

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('⌫', 5, 1)  # Clear and Backspace
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=clear)
    elif text == "⌫":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=backspace)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda t=text: press(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Make grid expand
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Bind keyboard keys
root.bind("<Key>", key_handler)

# Run the application
root.mainloop()

