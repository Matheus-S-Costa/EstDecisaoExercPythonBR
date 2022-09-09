'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
gasolina = 2.5
alcool = 1.9
combustivel = str(input('Qual combustivel voce deseja?(use letras minusculas sem acento) '))
quantidade = float(input('Insira a quantidade de litros: '))

if combustivel == 'alcool':
    if quantidade <= 20:
        desconto = quantidade*0.03
        valor_total = (alcool*quantidade)-desconto
        print('-------------------NOTA FISCAL-------------------------')
        print('Valor desconto:    R$', desconto)
        print('Valor a pagar:     R$', valor_total)
    if quantidade > 20:
        desconto = quantidade * 0.05
        valor_total = (2.5 * quantidade) - desconto
        print('-------------------NOTA FISCAL-------------------------')
        print('Valor desconto:    R$', desconto)
        print('Valor a pagar:     R$', valor_total)
if combustivel == 'gasolina':
    if quantidade <= 20:
        desconto = quantidade*0.04
        valor_total = (gasolina*quantidade)-desconto
        print('-------------------NOTA FISCAL-------------------------')
        print('Valor desconto:    R$', desconto)
        print('Valor a pagar:     R$', valor_total)
    if quantidade > 20:
        desconto = quantidade*0.06
        valor_total = (gasolina*quantidade)-desconto
        print('-------------------NOTA FISCAL-------------------------')
        print('Valor desconto:    R$', desconto)
        print('Valor a pagar:     R$', valor_total)
print('Valor do litro gasolina R$',gasolina)
print('Valor do litro alcool R$',alcool)
print('Combustivel escolhido: ',combustivel)
print('-------------------------------------------------------')