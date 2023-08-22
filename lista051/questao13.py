'''
Desenvolver um programa que imprima a tabuada de 3 a 6.
'''

num1 = 3
num2 = 4
num3 = 5
num4 = 6

multiplicador = 1

if (multiplicador <= 10):

    while (multiplicador <= 10):
        print(f"{num1} . {multiplicador} = {num1 * multiplicador}")
        multiplicador = multiplicador + 1

    multiplicador = 1

    while (multiplicador <= 10):
        print(f"{num2} . {multiplicador} = {num2 * multiplicador}")
        multiplicador = multiplicador + 1

    multiplicador = 1

    while (multiplicador <= 10):
        print(f"{num3} . {multiplicador} = {num3 * multiplicador}")
        multiplicador = multiplicador + 1

    multiplicador = 1

    while (multiplicador <= 10):
        print(f"{num4} . {multiplicador} = {num4 * multiplicador}")
        multiplicador = multiplicador + 1