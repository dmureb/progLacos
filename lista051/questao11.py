'''
Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável base) elevada a um
expoente qualquer (Variável exp), ou seja, de be
. (Sem usar Math.pow();)
'''

b = int(input("Informe um número para servir de base: "))
e = int(input("Informe um número para servir de expoente: "))
cont = 1
potencia = b

while (cont < e):
    potencia = potencia * b
    cont += 1
print(f"O resultado da potência é igual a {potencia}")