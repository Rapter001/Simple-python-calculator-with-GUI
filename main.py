import tkinter as tk

# Create a window
window = tk.Tk()
window.title("Calculator")

# Define a function for each operation
def add():
    result = float(num1.get()) + float(num2.get())
    output.config(text=result)

def subtract():
    result = float(num1.get()) - float(num2.get())
    output.config(text=result)

def multiply():
    result = float(num1.get()) * float(num2.get())
    output.config(text=result)

def divide():
    result = float(num1.get()) / float(num2.get())
    output.config(text=result)

# Create input fields for the numbers
num1_label = tk.Label(window, text="Enter first number:")
num1_label.pack()
num1 = tk.Entry(window)
num1.pack()

num2_label = tk.Label(window, text="Enter second number:")
num2_label.pack()
num2 = tk.Entry(window)
num2.pack()

# Create buttons for each operation
add_button = tk.Button(window, text="+", command=add)
add_button.pack()

subtract_button = tk.Button(window, text="-", command=subtract)
subtract_button.pack()

multiply_button = tk.Button(window, text="*", command=multiply)
multiply_button.pack()

divide_button = tk.Button(window, text="/", command=divide)
divide_button.pack()

# Create a label to display the result
output_label = tk.Label(window, text="Result:")
output_label.pack()
output = tk.Label(window, text="")
output.pack()

# Run the window
window.mainloop()
