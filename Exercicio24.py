'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
-par ou ímpar;
-positivo ou negativo;
-inteiro ou decimal.
'''
n1 = float(input('Insira um numero: '))
n2 = float(input('Insira outro numero: '))
operacao = str(input('Qual operacao voce quer realizar (use verbos para digitar)? '))
if operacao=='somar':
    resultado = n1+n2
    print ('O resultado é: ',resultado)
    if (resultado % 2) == 0 and resultado>0 and resultado // 1 == resultado:
        print('O numero é par e positivo e inteiro')
    if (resultado % 2) == 0 and resultado<0 and resultado // 1 == resultado:
        print('O numero é par, negativo e inteiro')
    if (resultado % 2) == 0 and resultado < 0 and resultado // 1 != resultado:
        print('O numero negativo e decimal')
    if (resultado % 2) == 0 and resultado > 0 and resultado // 1 != resultado:
        print('O numero e positivo e decimal')
    if (resultado % 2) != 0 and resultado > 0 and resultado // 1 == resultado:
        print('O numero é impar e positivo e inteiro')
    if (resultado % 2) != 0 and resultado < 0 and resultado // 1 == resultado:
        print('O numero é impar e negativo e inteiro')
    if (resultado % 2) != 0 and resultado > 0 and resultado // 1 != resultado:
        print('O numero é positivo e decimal')
    if (resultado % 2) != 0 and resultado < 0 and resultado // 1 != resultado:
        print('O numero é negativo e decimal')
elif operacao=='subtrair':
    resultado = n1-n2
    print ('O resultado é: ',resultado)
    if (resultado % 2) == 0 and resultado>0 and resultado // 1 == resultado:
        print('O numero é par e positivo e inteiro')
    if (resultado % 2) == 0 and resultado<0 and resultado // 1 == resultado:
        print('O numero é par, negativo e inteiro')
    if (resultado % 2) == 0 and resultado < 0 and resultado // 1 != resultado:
        print('O numero negativo e decimal')
    if (resultado % 2) == 0 and resultado > 0 and resultado // 1 != resultado:
        print('O numero e positivo e decimal')
    if (resultado % 2) != 0 and resultado > 0 and resultado // 1 == resultado:
        print('O numero é impar e positivo e inteiro')
    if (resultado % 2) != 0 and resultado < 0 and resultado // 1 == resultado:
        print('O numero é impar e negativo e inteiro')
    if (resultado % 2) != 0 and resultado > 0 and resultado // 1 != resultado:
        print('O numero é positivo e decimal')
    if (resultado % 2) != 0 and resultado < 0 and resultado // 1 != resultado:
        print('O numero é negativo e decimal')
elif operacao=='multiplicar':
    resultado = n1*n2
    print ('O resultado é: ',resultado)
    if (resultado % 2) == 0 and resultado>0 and resultado // 1 == resultado:
        print('O numero é par e positivo e inteiro')
    if (resultado % 2) == 0 and resultado<0 and resultado // 1 == resultado:
        print('O numero é par, negativo e inteiro')
    if (resultado % 2) == 0 and resultado < 0 and resultado // 1 != resultado:
        print('O numero negativo e decimal')
    if (resultado % 2) == 0 and resultado > 0 and resultado // 1 != resultado:
        print('O numero e positivo e decimal')
    if (resultado % 2) != 0 and resultado > 0 and resultado // 1 == resultado:
        print('O numero é impar e positivo e inteiro')
    if (resultado % 2) != 0 and resultado < 0 and resultado // 1 == resultado:
        print('O numero é impar e negativo e inteiro')
    if (resultado % 2) != 0 and resultado > 0 and resultado // 1 != resultado:
        print('O numero é positivo e decimal')
    if (resultado % 2) != 0 and resultado < 0 and resultado // 1 != resultado:
        print('O numero é negativo e decimal')
elif operacao=='dividir':
    resultado = n1/n2
    print ('O resultado é: ',resultado)
    if (resultado % 2) == 0 and resultado>0 and resultado // 1 == resultado:
        print('O numero é par e positivo e inteiro')
    if (resultado % 2) == 0 and resultado<0 and resultado // 1 == resultado:
        print('O numero é par, negativo e inteiro')
    if (resultado % 2) == 0 and resultado < 0 and resultado // 1 != resultado:
        print('O numero negativo e decimal')
    if (resultado % 2) == 0 and resultado > 0 and resultado // 1 != resultado:
        print('O numero e positivo e decimal')
    if (resultado % 2) != 0 and resultado > 0 and resultado // 1 == resultado:
        print('O numero é impar e positivo e inteiro')
    if (resultado % 2) != 0 and resultado < 0 and resultado // 1 == resultado:
        print('O numero é impar e negativo e inteiro')
    if (resultado % 2) != 0 and resultado > 0 and resultado // 1 != resultado:
        print('O numero é positivo e decimal')
    if (resultado % 2) != 0 and resultado < 0 and resultado // 1 != resultado:
        print('O numero é negativo e decimal')
else:
    print('Numeros ou operacao invalido(s), tente de novo!')