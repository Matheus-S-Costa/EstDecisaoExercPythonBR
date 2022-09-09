'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
valor = float(input('Insira quanto voce ganha por hora: '))
horas = float(input('Insira a quantidade de horas trabalhadas no mes: '))
sal_bruto = valor * horas
if sal_bruto <= 900:
    print('Você está isento dos descontos, seu salario liquido é R$' + str(sal_bruto))
if sal_bruto >= 901 and sal_bruto <= 1500:
    IR = sal_bruto * 0.05
    INSS = sal_bruto * 0.1
    FGTS = sal_bruto * 0.11
    total_descontos = IR + INSS
    sal_liquido = sal_bruto-total_descontos
    print('Salario bruto: R$' + str(sal_bruto))
    print('(-) IR (5%): R$' + str(IR))
    print('(-) INSS (10%): R$',INSS)
    print('FGTS (11%d): RS%',FGTS)
    print('Total de descontos: R$%.2f' % (total_descontos))
    print('Seu salario liquido é: R$'+str(sal_liquido))
if sal_bruto >= 1501 and sal_bruto <= 2500:
    IR = sal_bruto * 0.1
    INSS = sal_bruto * 0.1
    FGTS = sal_bruto * 0.11
    total_descontos = IR + INSS
    sal_liquido = sal_bruto - total_descontos
    print('Salario bruto: R$' + str(sal_bruto))
    print('(-) IR (5%): R$' + str(IR))
    print('(-) INSS (10%d): R$', INSS)
    print('FGTS (11%d): RS%', FGTS)
    print('Total de descontos: R$%.2f' %(total_descontos))
    print('Seu salario liquido é: R$' + str(sal_liquido))
if sal_bruto > 2500:
    IR = sal_bruto * 0.2
    INSS = sal_bruto * 0.1
    FGTS = sal_bruto * 0.11
    total_descontos = IR + INSS
    sal_liquido = sal_bruto - total_descontos
    print('Salario bruto: R$' + str(sal_bruto))
    print('(-) IR (5%): R$' + str(IR))
    print('(-) INSS (10%d): R$',INSS)
    print('FGTS (11%d): RS%',FGTS)
    print('Total de descontos: R$%.2f' % (total_descontos))
    print('Seu salario liquido é: R$'+str(sal_liquido))
