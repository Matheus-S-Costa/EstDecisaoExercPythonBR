'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

import math
a = float(input('Insira o valor de a: '))
b = float(input('Insira o valor de b: '))
c = float(input('Insira o valor de c: '))
delta = (b*b) - 4*a * c
if delta<0:
    print('O delta da operacao é negativo e nao possui raizes.')
elif delta == 0:
    print('O delta é igual a zero e possui somente uma raiz!')
    x1 = (-b + (math.sqrt(delta))) / (2 * a)
    print('O valor da raiz é: ',x1)
elif delta > 0:
    x1 = (-b+(math.sqrt(delta)))/(2*a)
    x2 = (-b-(math.sqrt(delta)))/(2*a)
    print('O valor da primeira raiz real é %.2f e a segunda raíz real é %.2f'%(x1,x2))
else:
    print('Numeros invalidos, tente novamente!')
