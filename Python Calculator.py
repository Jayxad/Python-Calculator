import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(expression))
            entry_var.set(result)
            expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            entry_var.set("")
    elif text == "C":
        expression = ""
        entry_var.set("")
    else:
        expression += text
        entry_var.set(expression)

# Create the main window
root = tk.Tk()
root.title("Classic Calculator")
root.geometry("400x600")

# Background color
root.configure(bg='#ffffff')

expression = ""
entry_var = tk.StringVar()

# Entry frame with a simple background
entry_frame = tk.Frame(root, bg='#cccccc', bd=10)
entry_frame.grid(row=0, column=0, columnspan=4, pady=10)

entry = tk.Entry(entry_frame, textvar=entry_var, font="Arial 20 bold", justify='right', bd=5, bg='#ffffff', relief=tk.SUNKEN)
entry.grid(row=0, column=0, ipadx=8, sticky='nsew')

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', 'C', '=', '+'
]

# Button colors (two colors only)
button_colors = {
    '0': '#4d4d4d', '1': '#4d4d4d', '2': '#4d4d4d', '3': '#4d4d4d', 
    '4': '#4d4d4d', '5': '#4d4d4d', '6': '#4d4d4d', '7': '#4d4d4d', 
    '8': '#4d4d4d', '9': '#4d4d4d', 'C': '#ff3333', '=': '#3366ff', 
    '/': '#4d4d4d', '*': '#4d4d4d', '-': '#4d4d4d', '+': '#4d4d4d'
}

row = 1
col = 0

for button in buttons:
    btn = tk.Button(root, text=button, font="Arial 15 bold", relief=tk.RAISED, border=5, 
                    bg=button_colors[button], fg='white', activebackground='#666666')
    btn.grid(row=row, column=col, ipadx=20, ipady=20, padx=5, pady=5, sticky='nsew')
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make grid cells expand proportionally
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
