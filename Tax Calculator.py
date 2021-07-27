'''

age = float(input('Enter the age: '))
income = float(input('Enter the income: '))

if age < 60:
    if income <= 20000:
        print('No Tax have to pay')
    elif income <= 50000:
        tax = (10/100) * income
        print(f'Tax you have to pay is {tax} $')
    elif income <= 100000:
        tax = (20/100) * income
        print(f'Tax you have to pay is {tax} $')
    else:
        tax = (40/100) * income
        print(f'Tax you have to pay is {tax} $')
else:
    if income <= 20000:
        print('No Tax have to pay')
    elif income <= 50000:
        tax = (10/100) * income
        print(f'Tax you have to pay is {tax} $')
    elif income <= 100000:
        tax = (20/100) * income
        print(f'Tax you have to pay is {tax} $')
    else:
        tax = (30/100) * income
        print(f'Tax you have to pay is {tax} $')

'''

from tkinter import *
import tkinter.messagebox

root = Tk()
root.title('Tax Calculator')


def tax_calculator():
    newroot = Tk()
    ageis = int(age_entry.get())
    incomeis = int(income_entry.get())
    print(f'Age: {ageis} yrs')
    print(f'Income {incomeis} $')

    def tax_above_60():
        if incomeis <= 20000:
            tax_label = Label(newroot, text='No Tax you have to pay')
            tax_label.pack(side=TOP)
        elif incomeis <= 50000:
            tax = (10 / 100) * incomeis
            tax_label = Label(newroot, text=f'Tax you have to pay is {tax} $')
            tax_label.pack(side=TOP)
        elif incomeis <= 100000:
            tax = (20 / 100) * incomeis
            tax_label = Label(newroot, text=f'Tax you have to pay is {tax} $')
            tax_label.pack(side=TOP)
        else:
            tax = (30 / 100) * incomeis
            tax_label = Label(newroot, text=f'Tax you have to pay is {tax} $')
            tax_label.pack(side=TOP)

    ques = tkinter.messagebox.askquestion('Question', 'Are you a businessman?')
    if ques == 'yes':
        print('Businessman')
        if ageis < 60:
            if incomeis <= 20000:
                tax = (7.5 / 100) * incomeis
                tax_label = Label(newroot, text=f'Tax you have to pay is {tax} $')
                tax_label.pack(side=TOP)
            elif incomeis <= 50000:
                tax = (17.5 / 100) * incomeis
                tax_label = Label(newroot, text=f'Tax you have to pay is {tax} $')
                tax_label.pack(side=TOP)
            elif incomeis <= 100000:
                tax = (27.5 / 100) * incomeis
                tax_label = Label(newroot, text=f'Tax you have to pay is {tax} $')
                tax_label.pack(side=TOP)
            else:
                tax = (47.5 / 100) * incomeis
                tax_label = Label(newroot, text=f'Tax you have to pay is {tax} $')
                tax_label.pack(side=TOP)
        else:
            tax_above_60()
    else:
        if ageis < 60:
            if incomeis <= 20000:
                tax = 0
                tax_label = Label(newroot, text='No Tax you have to pay')
                tax_label.pack(side=TOP)
            elif incomeis <= 50000:
                tax = (10 / 100) * incomeis
                tax_label = Label(newroot, text=f'Tax you have to pay is {tax} $')
                tax_label.pack(side=TOP)
            elif incomeis <= 100000:
                tax = (20 / 100) * incomeis
                tax_label = Label(newroot, text=f'Tax you have to pay is {tax} $')
                tax_label.pack(side=TOP)
            else:
                tax = (40 / 100) * incomeis
                tax_label = Label(newroot, text=f'Tax you have to pay is {tax} $')
                tax_label.pack(side=TOP)
        else:
            tax_above_60()
    if tax:
        print(f'Tax: {tax} $\n')
    else:
        print('No Tax\n')

age = Label(root, text='Enter Age:')
age.grid(row=0, column=0)
age_entry = Entry(root)
age_entry.grid(row=0, column=1)
age_entry.focus_set()

income = Label(root, text='Enter Income:')
income.grid(row=1, column=0)
income_entry = Entry(root)
income_entry.grid(row=1, column=1)
income_entry.focus_set()

button1 = Button(root, text='Submit', command=tax_calculator)
button1.grid(row=2, column=0)

button2 = Button(root, text='Exit', command=exit)
button2.grid(row=2, column=1)

root.mainloop()
