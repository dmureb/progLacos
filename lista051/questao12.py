'''
Desenvolver um programa que peça ao usuário para digitar diversos números reais, exp ao final, exibir o maior exp o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, exp este número -1 não deve ser considerado nem
como maior, nem como menor, exp nem na contagem da média.
'''

num = float(input("Informe um número até que você insira o número -1: "))
maior = num
menor = num
total_respostas = 0
soma = 0

while (num != -1):
    soma = soma + num
    total_respostas = total_respostas + 1

    if (maior < num and num != -1):
        maior = num

    if (menor > num and num != -1):
        menor = num

    num = float(input("Informe um número até que você insira o número -1: "))


if (maior == -1):
    print("Você inseriu -1 na primeira resposta.\nPROGRAMA ENCERRADO!")
else:
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
    print(f"Média dos valores inseridos: {soma/total_respostas}")
    print("FIM DO PROGRAMA")
