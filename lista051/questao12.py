'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, exp ao final, exibir o maior exp o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, exp este número -1 não deve ser considerado nem
como maior, nem como menor, exp nem na contagem da média.
'''

cont = int(input("Informe um número até que você insira o número -1: "))
maior = cont
menor = cont
acumulador = cont
media = 1

while (cont != -1):
    cont = int(input("Informe um número até que você insira o número -1: "))
    if (cont != -1):
        acumulador = acumulador + cont
        media = media + 1
    if (maior < cont and cont != -1):
        maior = cont
    elif (menor > cont and cont != -1):
        menor = cont

print(f"A média desses números é: {acumulador / media}")
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

