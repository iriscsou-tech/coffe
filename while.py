numero = -1
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break

print("Você digitou:", numero)

#esse codigo possui limites, pois o "range" precisa ter um limitação

numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)

# o "while" é diferente, ele seria um loop infinto até o usuario estar correto