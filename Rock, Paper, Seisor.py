import random

def winner(ch1, ch2):
    if ch2 == '0':
        exit()

    if ch1 == 1:             # 1 for Rock
        ch1 = 'R'
    elif ch1 == 2:           # 2 for Paper
        ch1 = 'P'
    else:                    # 3 for Seisor
        ch1 = 'S'

    print(f'You Select: {ch2}\nComputer Select: {ch1}\n')

    if ch1 == 'R' and ch2 == 'R' or ch1 == 'P' and ch2 == 'P' or ch1 == 'S' and ch2 == 'S':
        print('Draw')
    elif ch1 == 'R' and ch2 == 'P':
        print('You Win')
    elif ch1 == 'R' and ch2 == 'S':
        print('Computer Win')
    elif ch1 == 'P' and ch2 == 'R':
        print('Computer Win')
    elif ch1 == 'P' and ch2 == 'S':
        print('You Win')
    elif ch1 == 'S' and ch2 == 'P':
        print('Computer Win')
    elif ch1 == 'S' and ch2 == 'R':
        print('You Win')
    else:
        print('Enter a valid choice!')


while True:
    your_choice = input('\n"R" for Rock\n"P" for Paper\n"S" for Seisor\n"0" for exit\nInput your choice:')
    comp_choice = random.randint(1, 3)
    winner(comp_choice, your_choice)
