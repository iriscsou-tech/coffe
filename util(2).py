import os
import math

def titulo():
    print('ᑕᗩしᑕ⋃しᗩᗪ〇ᖇᗩ:\n')

def lista():
    print('1. 𝑀𝑒́𝑑𝑖𝑎​')
    print('2. 𝑇𝑎𝑏𝑢𝑎𝑑𝑎​')
    print('3. 𝐿𝑜𝑔​')
    print('4. 𝑀𝑀𝐶')
    print('5. 𝑅𝑎𝑖𝑧')
    print('6. 𝑆𝑎𝑖𝑟 𝑑𝑜 𝑠𝑖𝑠𝑡𝑒𝑚𝑎​​​​​\n')

def exibir(texto):
    os.system('cls')
    print()
    print(f'{texto}\n')


def calculadora_media():
    exibir('Ⲙᕮ́ↁᓮᗩ')

    numeros_str = input('𝐷𝑖𝑔𝑖𝑡𝑒 𝑜𝑠 𝑛𝑢́𝑚𝑒𝑟𝑜𝑠 𝑠𝑒𝑝𝑎𝑟𝑎𝑑𝑜𝑠 𝑝𝑜𝑟 𝑒𝑠𝑝𝑎𝑐̧𝑜𝑠 𝑑𝑎 𝑠𝑢𝑎 𝑚𝑒́𝑑𝑖𝑎:\n')
    numeros = numeros_str.split()

    numeros = [float(numero) for numero in numeros]

    if numeros:
        soma = sum(numeros)
        media = soma/ len(numeros)
        media = round(media, 3)
        print(f'\n𝐴 𝑚𝑒́𝑑𝑖𝑎 𝑒́ {media}')
    else:
        erro()
    voltar()

def tabuada():
    exibir('Ƭᗩᗷ⋃ᗩᗪᗩ')

    try:
        n = int(input('𝐸𝑠𝑐𝑟𝑒𝑣𝑎 𝑜 𝑛𝑢́𝑚𝑒𝑟𝑜 𝑞𝑢𝑒 𝑑𝑒𝑠𝑒𝑗𝑎​​​​​\n'))
        limite = int(input(f'𝐴𝑡𝑒́ 𝑞𝑢𝑎𝑙 𝑛𝑢́𝑚𝑒𝑟𝑜 𝑣𝑜𝑐𝑒̂ 𝑑𝑒𝑠𝑒𝑗𝑎 𝑚𝑢𝑙𝑡𝑖𝑝𝑙𝑖𝑐𝑎𝑟🇷​​​​​ {n} ？:\n'))
        
        for i in range(1, limite + 1):
            resultado = n * i
            print(f'{n} 𝑥 {i} ＝ {resultado}')
    except ValueError:
        erro()

    voltar()

def erro_log():
    exibir('ᖇᕮ⟆ᑭ〇⟆Ƭᗩ ᓰƝ⋎ᗩしᓮᗪᗩ​​​​​')
    error = input('\n𝐶𝑙𝑖𝑞𝑢𝑒 𝑞𝑢𝑎𝑙𝑞𝑢𝑒𝑟 𝑡𝑒𝑐𝑙𝑎 𝑝𝑎𝑟𝑎 𝑣𝑜𝑙𝑡𝑎𝑟 𝑎 𝑐𝑎𝑙𝑐𝑢𝑙𝑎𝑑𝑜𝑟𝑎 𝑑𝑒 𝐿𝑜𝑔\n')
    log()

def log():
    exibir('し〇ᎶᗩᖇᓮƬᓰⲘ〇')

    try:
        icog = float(input('𝐷𝑖𝑔𝑖𝑡𝑒 𝑜 𝑛𝑢́𝑚𝑒𝑟𝑜 𝑞𝑢𝑒 𝑑𝑒𝑠𝑒𝑗𝑎:\n'))
        base = float(input('\n𝐶𝑜𝑙𝑜𝑞𝑢𝑒 𝑎 𝑏𝑎𝑠𝑒 𝑑𝑜 𝐿𝑜𝑔:\n'))

        resu = math.log(icog, base)
        resu = round(resu, 3)
        print(f'\n𝑂 𝐿𝑜𝑔 𝑑𝑒 {icog} 𝑛𝑎 𝑏𝑎𝑠𝑒​​​​​ {base} ⁼ {resu}\n')
    except ValueError:
        erro_log()
    except ZeroDivisionError:
        erro_log()
    
    voltar()

def mmc():
    exibir('ⲘⲘᑕ')

    numeros_str = input("𝐷𝑖𝑔𝑖𝑡𝑒 𝑜𝑠 𝑛𝑢́𝑚𝑒𝑟𝑜𝑠 𝑠𝑒𝑝𝑎𝑟𝑎𝑑𝑜𝑠 𝑝𝑜𝑟 𝑣𝑖́𝑟𝑔𝑢𝑙𝑎 𝑑𝑜 𝑀𝑀𝐶: \n")
    numeros_str = numeros_str.replace(' ', ' ')
    numeros = numeros_str.split(',')

    numeros = [int(numero) for numero in numeros]

    if numeros:
        resultado = math.lcm(*numeros)
        print(f'\n𝑂 𝑟𝑒𝑠𝑢𝑙𝑡𝑎𝑑𝑜 𝑑𝑜 𝑀𝑀𝐶 𝑒́ {resultado}')
    else:
        erro()
    voltar()

def raiz():
    exibir('ᖇᗩᓮⲌ')

    try:
        z = float(input('𝐷𝑖𝑔𝑖𝑡𝑒 𝑜 𝑖́𝑛𝑑𝑖𝑐𝑒 𝑑𝑎 𝑟𝑎𝑖𝑧:\n'))
        x = float(input('\n𝐷𝑖𝑔𝑖𝑡𝑒 𝑜 𝑛𝑢́𝑚𝑒𝑟𝑜 𝑞𝑢𝑒 𝑑𝑒𝑠𝑒𝑗𝑎:\n'))

        result = x ** (1/z)
        result = round(result, 3)
        print(f'\n𝐴 𝑟𝑎𝑖𝑧🇿 {z} 𝑑𝑒​ {x} ＝ {result}\n')

    except ValueError:
        erro()

    voltar()

def sair():
    exibir('⟆ᗩᓮᖇ')
    pergunta = input('𝐶𝑎𝑠𝑜 𝑡𝑒𝑛ℎ𝑎 𝑐𝑒𝑟𝑡𝑒𝑧𝑎 𝑑𝑖𝑔𝑖𝑡𝑒 "𝑠𝑖𝑚" 𝑜𝑢 "𝑛𝑎̃𝑜" 𝑝𝑎𝑟𝑎 𝑣𝑜𝑙𝑡𝑎𝑟 𝑎𝑜 𝑚𝑒𝑛𝑢:​​​​​\n')

    try:
        if pergunta == 'sim':
            os.system('cls')
            print('𝑉𝑜𝑐𝑒̂ 𝑠𝑎𝑖𝑢 𝑑𝑜 𝑠𝑖𝑠𝑡𝑒𝑚𝑎​​​​​')
        elif pergunta == 'não':
            voltar()
        else:
            erro()
    except:
        erro()

def erro():
    exibir('ᕮᖇᖇ〇')
    print('𝑂𝑝𝑐̧𝑎̃𝑜 𝑖𝑛𝑣𝑎𝑙𝑖𝑑𝑎​​​​​')
    voltar()

def voltar():
    volta = input('\n𝐶𝑙𝑖𝑞𝑢𝑒 𝑞𝑢𝑎𝑙𝑞𝑢𝑒𝑟 𝑡𝑒𝑐𝑙𝑎 𝑒 "𝐸𝑛𝑡𝑒𝑟" 𝑝𝑎𝑟𝑎 𝑣𝑜𝑙𝑡𝑎𝑟:\n')
    print(volta)
    main()   
    
def interacao():
    m = input('𝐷𝑖𝑔𝑖𝑡𝑒 𝑜 𝑛𝑢́𝑚𝑒𝑟𝑜 𝑑𝑒 𝑞𝑢𝑎𝑙 𝑐𝑎𝑙𝑐𝑢𝑙𝑎𝑑𝑜𝑟𝑎 𝑑𝑒𝑠𝑒𝑗𝑎 𝑢𝑠𝑎𝑟:\n')

    try:

        if m == '1' or m.lower() == 'media':
            calculadora_media()
        elif m == '2' or m.lower() == 'tebuada':
            tabuada()
        elif m == '3' or m.lower() == 'log':
            log()
        elif m == '4' or m.lower() == 'mmc':
            mmc()
        elif m == '5' or m.lower() == 'raiz':
            raiz()
        elif m == '6' or m.lower() == 'sair':
            sair()
        else:
            erro()
    except:
        erro()


def main():
    os.system('cls')  
    titulo()
    lista()
    interacao()

if __name__ == '__main__':
    main()