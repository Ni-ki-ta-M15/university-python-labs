import tkinter as tk
from tkinter import messagebox as mb


def add_digit(digit):
    value = calc.get()
    if value[0] =='0' and len(value) == 1:
        value = value[1:]

    calc.delete(0, tk.END)
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        mb.showinfo('Внимание', 'Мы считает, ТОЛЬКО цифры!')
        calc.insert(0, '0')
    except ZeroDivisionError:
        mb.showerror('Внимание', 'Невозможно выполнить данную операцию')
        calc.insert(0, '0')
def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')

def make_digit_button(digit):
    return tk.Button(text=digit, bd=6, bg='green', font=('Arial', 14), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=6, bg='yellow', font=('Arial', 14), command=lambda: add_operation(operation))

def make_culc_button(operation):
    return tk.Button(text=operation, bd=6, bg='red', font=('Arial', 14), command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation, bd=6, bg='red', font=('Arial', 14), command=clear)

def clear_one(operation):
    global formula

    if operation == 'del':
        formula = formula[0, -1]

def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '.':
        add_digit(event.char)






root = tk.Tk()
root.geometry('350x455')
root['bg'] = '#48ffe8'
root.title('Calculate')
root.bind('<Key>', press_key)


calc = tk.Entry(root, justify=tk.RIGHT, font=('Arial', 20,), width=20)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5)

make_digit_button('1').grid(row=4, column=0, stick='wens', padx=6, pady=6)
make_digit_button('2').grid(row=4, column=1, stick='wens', padx=6, pady=6)
make_digit_button('3').grid(row=4, column=2, stick='wens', padx=6, pady=6)
make_digit_button('4').grid(row=3, column=0, stick='wens', padx=6, pady=6)
make_digit_button('5').grid(row=3, column=1, stick='wens', padx=6, pady=6)
make_digit_button('6').grid(row=3, column=2, stick='wens', padx=6, pady=6)
make_digit_button('7').grid(row=2, column=0, stick='wens', padx=6, pady=6)
make_digit_button('8').grid(row=2, column=1, stick='wens', padx=6, pady=6)
make_digit_button('9').grid(row=2, column=2, stick='wens', padx=6, pady=6)
make_digit_button('0').grid(row=5, column=1, stick='wens', padx=6, pady=6)
make_digit_button('.').grid(row=5, column=2, stick='wens', padx=6, pady=6)
make_digit_button('+/-').grid(row=5, column=0, stick='wens', padx=6, pady=6)
make_digit_button('del').grid(row=1, column=1, stick='wens', padx=6, pady=6)
# make_digit_button(')').grid(row=1, column=2, stick='wens', padx=6, pady=6)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=6, pady=6)
make_operation_button('-').grid(row=2, column=3, sticky='wens', padx=6, pady=6)
make_operation_button('*').grid(row=3, column=3, sticky='wens', padx=6, pady=6)
make_operation_button('/').grid(row=4, column=3, sticky='wens', padx=6, pady=6)

make_culc_button('=').grid(row=5, column=3, sticky='wens', padx=6, pady=6)
make_clear_button('C').grid(row=1, column=0, sticky='wens', padx=6, pady=6)


root.grid_columnconfigure(0, minsize=85)
root.grid_columnconfigure(1, minsize=85)
root.grid_columnconfigure(2, minsize=85)
root.grid_columnconfigure(3, minsize=85)
root.grid_columnconfigure(4, minsize=85)
root.grid_columnconfigure(5, minsize=85)

root.grid_rowconfigure(1, minsize=85)
root.grid_rowconfigure(2, minsize=85)
root.grid_rowconfigure(3, minsize=85)
root.grid_rowconfigure(4, minsize=85)
root.grid_rowconfigure(5, minsize=85)
root.grid_rowconfigure(6, minsize=85)

root.mainloop()
