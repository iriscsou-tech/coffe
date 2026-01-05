numero= int(input('escreva um numero e direi se ele é par ou impar:'))

if numero % 2 == 0:
    print('seu numero é par')
else:
    print('seu numero é impar')

idade = int(input('qual a sua idade?:'))

if 0 <= idade <= 12:
    print('vc é uma criança')
elif 13 <= idade <= 18:
    print('vc é um adolecente')
else:
    print('vc é um adulto')

nome = 'irr8ss'
senha = '1234'

x = input('qual seu nome de logim? :')
y = input('qual sua senha? :')

if x == nome and y == senha:
    print('esta correto')
else:
    print('esta incorreto')