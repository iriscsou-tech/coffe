numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Maria', 'josé', 'Fulano', 'Ciclano']
anos= [2009,2025]

for numero in numeros:
    print(numero)

for nome in nomes:
    print(nome)

for ano in anos:
    print(ano)

impares = 0

#Essa linha é como um "para cada" número ímpar de 1 a 10, o 2 faz pular ele de dois em dois
for i in range(1, 11, 2):
    impares += i
print(impares)

for i in range(10, 0, -1):
    print(i)

n = int(input('escreva um numero: '))
for i in range(1, 11):
    resultado = n * i
    print(f'{n} x {i} = {resultado}')

lista = [17, 3, 4, 6, 9]
soma = 0

try:
    for nu in lista:
        soma += nu
    print(f'a soma dos numeros é: {soma}')
except Exception as e:
    print(f'Ocorreu um erro em: {e}')

l = [10, 9, 3, 8]
s = 0

try:
    for num in l:
        s += num
    media = s/ len(l)
    print(f'a media dos valores é: {media}')
except ZeroDivisionError:
    print('a lista esta vazia')
except Exception as e:
    print(f'Ocorreu um erro em {e}')