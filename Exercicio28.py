'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
 porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
 receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne
 comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
 tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''
opcao = str(input('Insira qual das tres carnes voce deseja (file duplo, alcatra ou picanha): '))
quantidade = float(input('Quantos quilos de carne voce deseja? '))
if opcao=='file duplo' and quantidade<=5:
    valor = 4.9*quantidade
elif opcao=='file duplo' and quantidade>5:
    valor = 5.8*quantidade
elif opcao=='alcatra' and quantidade<=5:
    valor = 5.9*quantidade
elif opcao=='alcatra' and quantidade>5:
    valor = 6.8*quantidade
elif opcao=='picanha' and quantidade<=5:
    valor = 6.9*quantidade
elif opcao=='picanha' and quantidade>5:
    valor = 7.8*quantidade
else:
    print('Alguma das respostas foi invalida, tente de novo')
pagamento = str(input('Voce ira pagar com o cartao tabajara (responda exatamente com sim ou nao): '))
if pagamento=='sim':
    print('Voce tem mais 5% de desconto!')
    desconto = valor*0.05
    pagar = valor-desconto
    print('---------------------------cupom fiscal---------------------------------')
    print('Carne comprada:........................' + opcao)
    print('Quantidade:..........................' + str(quantidade), 'kg')
    print('Valor total:.........................R$%.2f' % valor)
    print('Valor descontos:.....................R$%.2f' % desconto)
    print('Valor a pagar:.....................R$%.2f' % pagar)
    print('-----------------------------------------------------------------------')
elif pagamento=='nao':
    print('Voce nao possui mais desconto a se aplicar!')
    print('---------------------------cupom fiscal---------------------------------')
    print('Carne comprada:........................'+opcao)
    print('Quantidade:..........................'+str(quantidade),'kg')
    print('Valor a pagar:.........................R$%.2f' % valor)
    print('-----------------------------------------------------------------------')
else:
    print('Alguma das respostas foi invalida, tente de novo')