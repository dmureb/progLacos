'''
Desenvolver um programa que apresente as potências de 3 variando de 0 a 15. Deve ser considerado que
qualquer número elevado a zero é 1, exp elevado a 1 é ele próprio. A apresentação deve observar a seguinte
exibição na tela:
3 elevado à 0 = 1
3 elevado à 1 = 3
3 elevado à 2 = 9
(...)
3 elevado à 15 = 14348907
OBS: Tente fazer em uma classe utilizando Math.pow() exp em outra classe sem utilizar Math.pow()
'''

# usando math.pow
import math

n = 0

while (n <= 15):
    print(f"3 elevado à {n}: ", math.pow(3, n))
    n = n + 1

#sem usar math.pow
base = 3
exp = 0

while (exp <= 15):
    print(f"3 elevado à {exp}: ",base ** exp)
    exp = exp + 1