'''
Desenvolver um programa que calcule o fatorial do número 5, ou seja, 5!. Desta forma, temos que 5! = 5 . 4 . 3 .
2 . 1 ou 5! = 1 . 2 . 3 . 4 . 5, equivalente a 120.
'''

fator = 5
mult = 1

while (fator > 1):
    fator = fator - 1
    mult = 5 * fator
    fator = fator - 1
    mult = mult * fator
    fator = fator - 1
    mult = mult * fator
    fator = fator - 1
    mult = mult * fator
print(f"O fatorial do número 5 é: {mult}")