import os

restaurante = [{'nome': 'Coco bambu', 'categoria': 'frutos do mar', 'ativo': False},
               {'nome': 'Belas artes', 'categoria': 'padaria', 'ativo': True},
               {'nome': 'Outback', 'categoria': 'carne', 'ativo': False}]

def exibir_nome():
    print(f'{'✿ ⼕龱千千㠪 ✿'.center(20)}\n')

def opcoes():
    print('𝟭. 𝗖𝗮𝗱𝗮𝘀𝘁𝗿𝗮𝗿 𝗿𝗲𝘀𝘁𝗮𝘂𝗿𝗮𝗻𝘁𝗲')
    print('𝟮. 𝗟𝗶𝘀𝘁𝗮𝗿 𝗿𝗲𝘀𝘁𝗮𝘂𝗿𝗮𝗻𝘁𝗲𝘀')
    print('𝟯. 𝗔𝗹𝘁𝗲𝗿𝗻𝗮𝗿 𝗲𝘀𝘁𝗮𝗱𝗼 𝗱𝗼 𝗿𝗲𝘀𝘁𝗮𝘂𝗿𝗮𝗻𝘁𝗲')
    print('𝟰. 𝗦𝗮𝗶𝗿\n')


def voltar_ao_menu():
    ''' Ussado no final de cada interação, ela volta ao inicio'''
    input('\n𝙳𝚒𝚐𝚒𝚝𝚎 𝚞𝚖𝚊 𝚝𝚎𝚌𝚕𝚊 𝚙𝚊𝚛𝚊 𝚟𝚘𝚕𝚝𝚊𝚛 𝚊𝚘 𝚖𝚎𝚗𝚞: \n')
    main()

def exibir_titulo(texto):
    '''Essa exibe o subtitulo de todas as opções'''
    os.system('cls')
    linha = '~' * (len(texto))
    print(f'{linha}\n')
    print(texto)
    print(f'\n{linha}')
    print()    

def sair():
    ''' Essa função é a opção 4, com opção de sim ou não'''
    exibir_titulo(f'{'𝐒𝐚𝐢𝐫?'.center(20)}')
    pergunta = input('𝙲𝚊𝚜𝚘 𝚝𝚎𝚗𝚑𝚊 𝚌𝚎𝚛𝚝𝚎𝚣𝚊 𝚍𝚒𝚐𝚒𝚝𝚎 "𝚜𝚒𝚖" 𝚘𝚞 "𝚗𝚊̃𝚘" 𝚙𝚊𝚛𝚊 voltar ao menu:\n')

    try:
        if pergunta == 'sim':
            os.system('cls')
            print('𝚅𝚘𝚌𝚎̂ 𝚜𝚊𝚒𝚞 𝚍𝚘 𝚜𝚒𝚜𝚝𝚎𝚖a')
        elif pergunta == 'não':
            voltar_ao_menu()
        else:
            erro()
    except:
        erro()

def erro():
    '''aparece sempre que alguem digita algo que não tem resultado, assim faz voltar ao inicio'''
    print('𝙾𝚙𝚌̧𝚊̃𝚘 𝚒𝚗𝚟𝚊𝚕𝚒𝚍𝚊')
    voltar_ao_menu()

def cadastrando_restaurante():
    ''' Essa função faz um novo cadastro, opção 1'''
    exibir_titulo('𝐂𝐀𝐃𝐀𝐃𝐓𝐑𝐎 𝐃𝐄 𝐍𝐎𝐕𝐎 𝐑𝐄𝐒𝐓𝐀𝐔𝐑𝐀𝐍𝐓𝐄')
    novo_restaurante = input('𝙳𝚒𝚐𝚒𝚝𝚎 𝚘 𝚗𝚘𝚖𝚎 𝚍𝚘 𝚛𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝𝚎 𝚚𝚞𝚎 𝚍𝚎𝚜𝚎𝚓𝚊 𝚌𝚊𝚍𝚊𝚜𝚝𝚛𝚊:\n')
    categoria_nova = input(f'𝚍𝚒𝚐𝚒𝚝𝚎 𝚊 𝚌𝚊𝚝𝚎𝚐𝚘𝚛𝚒𝚊 𝚍𝚘 𝚛𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝𝚎 {novo_restaurante}:\n')
    dados = {'nome': novo_restaurante, 'categoria': categoria_nova, 'ativo': False}
    restaurante.append(dados)
    print(f'𝚘 𝚛𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝𝚎 {novo_restaurante} 𝚏𝚘𝚒 𝚌𝚊𝚍𝚊𝚜𝚝𝚛𝚊𝚍𝚘')
    voltar_ao_menu()

def listar_restaurantes():
    ''' Essa opção é a 2, listar restaurante'''
    exibir_titulo('𝐋𝐈𝐒𝐓𝐀𝐍𝐃𝐎 𝐓𝐎𝐃𝐎𝐒 𝐎𝐒 𝐑𝐄𝐒𝐓𝐀𝐔𝐑𝐀𝐍𝐓𝐄𝐒')

    
    rotulos = f'{'𝖭𝖮𝖬𝖤'.center(21)} | {'𝖢𝖠𝖳𝖤𝖦𝖮𝖱𝖨𝖠'.center(20)} | {'𝖲𝖳𝖠𝖳𝖴𝖲'.center(10)} |'
    print(rotulos)

    linhas = '~' * len(rotulos)
    print(linhas)
    for novo_restaurante in restaurante:
        nome_novo = novo_restaurante['nome']
        categoria = novo_restaurante['categoria']
        atividade = 'ativado' if novo_restaurante['ativo'] else 'desativado'
        print(f'-{nome_novo. ljust(20)} | {categoria.ljust(20)} | {atividade.ljust(10)} |' )
    print(linhas)
    voltar_ao_menu()

def mudar_estado():
    ''' Muda o estado de ativo e desativado do restaurate que deseja'''
    exibir_titulo('𝐌𝐔𝐃𝐀𝐑 𝐎 𝐄𝐒𝐓𝐀𝐃𝐎 𝐃𝐎 𝐑𝐄𝐒𝐓𝐀𝐔𝐑𝐀𝐍𝐓𝐄')
    mudado = input('𝙳𝚒𝚐𝚒𝚝𝚎 𝚘 𝚗𝚘𝚖𝚎 𝚍𝚘 𝚛𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝𝚎 𝚚𝚞𝚎 𝚍𝚎𝚜𝚎𝚓𝚊 𝚖𝚞𝚍𝚊𝚛 𝚘 𝚎𝚜𝚝𝚊𝚍𝚘:\n')
    encontrado = False

    for restaurantes in restaurante:
        if mudado == restaurantes['nome']:
            encontrado = True
            restaurantes['ativo'] = not restaurantes['ativo']
            mensagem = f'𝐎 𝚛𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝𝚎 {mudado} 𝚏𝚘𝚒 𝚊𝚝𝚒𝚟𝚊𝚍𝚘 𝚌𝚘𝚖 𝚜𝚞𝚌𝚎𝚜𝚜𝚘\n' if restaurantes['ativo'] else f'𝙾 𝚛𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝𝚎 {mudado} 𝚏𝚘𝚒 𝚍𝚎𝚜𝚊𝚝𝚒𝚟𝚊𝚍𝚘 𝚌𝚘𝚖 𝚜𝚞𝚌𝚎𝚜𝚜𝚘\n'
            print(mensagem)
    if not encontrado:
        print ('𝚁𝚎𝚜𝚝𝚊𝚞𝚛𝚊𝚗𝚝𝚎 𝚗𝚊̃𝚘 𝚏𝚘𝚒 𝚎𝚗𝚌𝚘𝚗𝚝𝚛𝚊𝚍𝚘\n')
    
    voltar_ao_menu()

def interação():
    ''' As escolhas de qual opção quer'''
    try:
        escolha = input('𝗘𝘀𝗰𝗼𝗹𝗵𝗮 𝘂𝗺𝗮 𝗼𝗽𝗰̧𝗮̃𝗼:\n')
        escolha = int(escolha)
            
        if escolha == 1:
            cadastrando_restaurante()
        elif escolha == 2:
            listar_restaurantes()
        elif escolha == 3:
            mudar_estado()
        elif escolha == 4:
            sair()
        else:
            erro()
    except:
        erro()
        

def main():
    ''' reinicia o sistema inteiro, com as mudanças das interações'''
    os.system('cls')
    exibir_nome()
    opcoes()
    interação()

if __name__ == '__main__':
     main()