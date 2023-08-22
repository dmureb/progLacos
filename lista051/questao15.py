'''
Desenvolver um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é
formada pela sequência 1,1,2,3,5,8,13,21,34, ... etc. Ela se caracteriza pela soma de um termo posterior com seu
anterior subsequente.
'''

ultimo = 1
penultimo = 1
cont = 3

while (cont <= 15):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    cont += 1
    print(termo)


















