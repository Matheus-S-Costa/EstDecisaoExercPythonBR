#Este programa contem exercicios de Estrutura de Decisao do python Brasil!
#Exercicios no site: https://wiki.python.org.br/EstruturaDeDecisao
'''
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
  Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
  entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
print('Investigacao criminal, responda as perguntas a seguir (responda exatamente com sim ou nao): ')
print('--------------------------------------------------------------------------------')
a = str(input('Voce telefonou para a vitima? '))
b = str(input('Voce esteve no local do crime? '))
c = str(input('Voce mora perto da vitima? '))
d = str(input('Voce devia para a vitima? '))
e = str(input('Voce ja trabalhou com a vitima? '))
print('--------------------------------------------------------------------------------')
if a == b == c == d == e == 'sim':
    print('Voce e considerado assassino, contate seu advogado!')
elif a == b == c == d == e == 'nao' or \
     (a == 'sim' and b == c == d == e == 'nao') or\
     (b == 'sim' and a == c == d == e == 'nao') or\
     (c == 'sim' and a == b == d == e == 'nao') or\
     (d == 'sim' and a == b == c == e == 'nao') or\
     (e == 'sim' and a == b == c == d == 'nao'):
    print('Voce e considerado inocente!')
elif (a == b == 'sim' and c == d == e == 'nao') or (a == c == 'sim' and b == d == e == 'nao')  or (a == d == 'sim' and b == c == e == 'nao')\
    or (a == e == 'sim' and c == d == b == 'nao') or (b == c == 'sim'and a == d == e == 'nao') or (b == d == 'sim'and a == c == e == 'nao')\
    or (b == e == 'sim'and a == c == d == 'nao') or (c == d == 'sim'and b == a == e == 'nao') or (c == e == 'sim'and b == a == d == 'nao')\
    or (d == e == 'sim'and b == a == c == 'nao'):
    print('Voce e considerado suspeito, aguarde as investigacoes.')
else:
    print('Voce é considerado cumplice, contate seu advogado.')
print('Obrigado por participar!')