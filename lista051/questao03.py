'''
Desenvolver um programa que apresente os quadrados dos números inteiros de 15 a 200.
'''
import math

contador = 15
while (contador <=200):
    print("a potência desses números é: ", math.pow(contador,2))
    contador = contador + 1