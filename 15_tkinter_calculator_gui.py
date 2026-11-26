# Tkinter Calculator GUI Program
import tkinter as tk

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operator.get()
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                output.config(text="Cannot divide by zero")
                return
            result = a / b
        else:
            output.config(text="Select a valid operator")
            return
        output.config(text="Result: " + str(result))
    except ValueError:
        output.config(text="Enter valid numbers")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")

tk.Label(root, text="First number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second number").pack()
entry2 = tk.Entry(root)
entry2.pack()

operator = tk.StringVar(value="+")
tk.OptionMenu(root, operator, "+", "-", "*", "/").pack()

tk.Button(root, text="Calculate", command=calculate).pack()

output = tk.Label(root, text="Result:")
output.pack()

root.mainloop()
