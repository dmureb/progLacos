'''
 Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser
impressa no seguinte formato:
Considerando como exemplo o fornecimento do número 2
2 . 1 = 2
2 . 2 = 4
2 . 3 = 6
2 . 4 = 8
2 . 5 = 10
(...)
2 . 10 = 20
'''

num = int(input("Informe um número: "))

multiplicador = 1

while (multiplicador <= 10):
    print(f"{num} . {multiplicador} = {num * multiplicador}")
    multiplicador = multiplicador + 1