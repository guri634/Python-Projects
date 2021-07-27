from tkinter import *
from tkinter import ttk
from math import *
import parser

root = Tk()
root.title('Calculator')
root.geometry("700x300")
root.resizable(0, 0)
style = ttk.Style()
style.configure("TEntry", padding='10')
style.configure("TButton", font="Arial", padding='10', width='6', color='gray')
# style.configure("Label", font='Italic', Size=19)
root.configure(bg='dark gray')
# global base_string
base_string = ''
# global entire_string
entire_string = ''


def get_num(value):
    global base_string, entire_string
    base_string += value
    if display.get()[-1] == '+' or display.get()[-1] == '-' or display.get()[-1] == '*' or display.get()[-1] == '/':
        entire_string += base_string
        base_string = ''
    else:
        entire_string = base_string


def all_clear():
    display.delete(0, END)
    global base_string, entire_string
    base_string = ''
    entire_string = ''


def clear():
    string = display.get()
    all_clear()
    display.insert(0, string[:-1])


def calculation():
    # global entire_string, base_string
    # entire_string += base_string
    value = display.get()
    try:
        result = eval(parser.expr(value).compile())
        all_clear()
        display.insert(0, result)
    except Exception:
        all_clear()
        display.insert(0, "Error")


def display_bar(value):
    display.insert(END, value)


def insert_sign():
    string = display.get()
    if string[0] == '-':
        all_clear()
        display.insert(0, string[1:])
    else:
        all_clear()
        display.insert(0, '-')
        display.insert(1, string)


display = ttk.Entry(root, width=51)
display.grid(columnspan=4, pady=10)

button_AC = ttk.Button(root, text="AC", command=all_clear).grid(row='1', column='0')
button_clear = ttk.Button(root, text="◄─", command=clear).grid(row='1', column='1')
button_sign = ttk.Button(root, text="±", command=lambda: insert_sign()).grid(row='1', column='2')
button_add = ttk.Button(root, text="+", command=lambda: [display_bar('+'), get_num('+')]).grid(row='1', column='3')

button_1 = ttk.Button(root, text="1", command=lambda: [display_bar('1'), get_num('1')]).grid(row='2', column='0')
button_2 = ttk.Button(root, text="2", command=lambda: [display_bar('2'), get_num('2')]).grid(row='2', column='1')
button_3 = ttk.Button(root, text="3", command=lambda: [display_bar('3'), get_num('3')]).grid(row='2', column='2')
button_sub = ttk.Button(root, text="-", command=lambda: [display_bar('-'), get_num('-')]).grid(row='2', column='3')

button_4 = ttk.Button(root, text="4", command=lambda: [display_bar(4), get_num('4')]).grid(row='3', column='0')
button_5 = ttk.Button(root, text="5", command=lambda: [display_bar(5), get_num('5')]).grid(row='3', column='1')
button_6 = ttk.Button(root, text="6", command=lambda: [display_bar(6), get_num('6')]).grid(row='3', column='2')
button_mul = ttk.Button(root, text="*", command=lambda: [display_bar('*'), get_num('*')]).grid(row='3', column='3')

button_7 = ttk.Button(root, text="7", command=lambda: [display_bar(7), get_num('7')]).grid(row='4', column='0')
button_8 = ttk.Button(root, text="8", command=lambda: [display_bar(8), get_num('8')]).grid(row='4', column='1')
button_9 = ttk.Button(root, text="9", command=lambda: [display_bar(9), get_num('9')]).grid(row='4', column='2')
button_div = ttk.Button(root, text="/", command=lambda: [display_bar('/'), get_num('/')]).grid(row='4', column='3')

button_0 = ttk.Button(root, text="0", width='15', command=lambda: [display_bar('0'), get_num('0')]).grid(columnspan='2', row='5', column='0')
button_dot = ttk.Button(root, text=".", command=lambda: [display_bar('.'), get_num(".")]).grid(row='5', column='2')
button_eq = ttk.Button(root, text="=", command=calculation).grid(row=5, column=3)

Label(root, bg='dark gray', width=5).grid(row=1, column=4)
Label(root, text="Scientific Calculator", font="large").grid(columnspan=3, row=0, column=5)

button_sin = ttk.Button(root, text="sin", command=lambda: [display_bar('sin('), get_num('sin(')]).grid(row=1, column=5)
button_cos = ttk.Button(root, text="cos", command=lambda: [display_bar('cos('), get_num('sin(')]).grid(row=1, column=6)
button_tan = ttk.Button(root, text="tan", command=lambda: [display_bar('tan('), get_num('sin(')]).grid(row=1, column=7)

button_ln = ttk.Button(root, text="ln", command=lambda: [display_bar('log('), get_num('log(')]).grid(row=2, column=5)
button_log = ttk.Button(root, text="log", command=lambda: [display_bar('log10('), get_num('log10')]).grid(row=2, column=6)
button_fact = ttk.Button(root, text="x!", command=lambda: [display_bar('!'), ]).grid(row=2, column=7)

button_lp = ttk.Button(root, text="(", command=lambda: [display_bar('(')]).grid(row=3, column=5)
button_rp = ttk.Button(root, text=")", command=lambda: [display_bar(')')]).grid(row=3, column=6)
button_per = ttk.Button(root, text="%", command=lambda: [display_bar('/100'), calculation()]).grid(row=3, column=7)

button_under_root = ttk.Button(root, text='√', command=lambda: [display_bar('**(1/2)'),
                                                                calculation()]).grid(row=4, column=5)
button_recp = ttk.Button(root, text="1/x", command=lambda: [display_bar('1/')]).grid(row=4, column=6)
button_power = ttk.Button(root, text="x^y", command=lambda: [display_bar('^'), ]).grid(row=4, column=7)

button_pi = ttk.Button(root, text="π", command=lambda: [display_bar('π'), ]).grid(row=5, column=5)
button_e = ttk.Button(root, text="e", command=lambda: [display_bar('e'), get_num('e')]).grid(row=5, column=6)
button_inv = ttk.Button(root, text="inv").grid(row=5, column=6)

root.mainloop()

# print(degrees(asin(1)))
# print(tan(pi/2))
# print(-87+97)

button_cos_inv = ttk.Button(root, text="cos^(-1)", command=lambda: [display_bar('cos('),
                                                                    get_num('sin(')]).grid(row=1, column=6)
button_tan_inv = ttk.Button(root, text="tan^(-1)", command=lambda: [display_bar('tan('),
                                                                    get_num('sin(')]).grid(row=1, column=7)
button_square = ttk.Button(root, text="x²", command=lambda: [display_bar('**2'), calculation()]).grid(row=4,
                                                                                                      column=6)
button_ten_power = ttk.Button(root, text="10^x", command=lambda: [display_bar('10^'), ]).grid(row=5, column=7)