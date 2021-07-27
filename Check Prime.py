number = float(input('Enter a number you want to check weather it is prime or not :- '))
global i
if number < 0:
    number = number * -1
    for i in range(2, int(number) + 1):
        if number % i == 0:
            break
    number = number * -1

if number == 1:
    print('1 is not a prime number')
    exit()

for i in range(2, int(number) + 1):
    if number % i == 0:
        break

if i == number:
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')
