import pywhatkit
from datetime import datetime
from time import sleep
from pynput.keyboard import Controller, Key

def fechar_guia():
    """Gera um comando de 'CTRL' + 'W' para fechar a guia do navegador."""
    teclado = Controller()
    teclado.press(Key.ctrl)
    teclado.press('w')
    teclado.release(Key.ctrl)
    teclado.release('w')

def carregar_lista():
    """Carrega lista de contatos no array 'lista'."""
    try:
        lista = list()
        with open('contatos.txt', 'r') as arq:
            for valor in arq:
                if '+55' in valor:
                    lista.append(valor.replace('\n', ''))
                else:
                    print(f'O número {valor} não foi adicionado.')
    except FileNotFoundError:
        print('Erro ao localizar o arquivo!')
        lista = []
    return lista

def enviar_mensagem(msg='Olá aluno(a), esta é uma mensagem automática te lembrando que a data de vencimento é __/__/__ e te enviaremos a chave pix nesse dia.\nObrigado, att.: equipe Extensio.'):
    """Realiza o envio de mensagem para os contatos."""
    lista = carregar_lista()
    cont = 0
    sucesso = list()
    falhando = list()

    while cont < len(lista):
        try:
            print(f'Enviando para: {lista[cont]}')
            pywhatkit.sendwhatmsg(lista[cont], msg, datetime.today().hour, datetime.today().minute + 1, wait_time=10)
        except Exception as e:
            print(f'Falha ao enviar para: {lista[cont]} - {e}')
            falhando.append(lista[cont])  # caso falhe - falhando
            cont += 1
        else:
            sucesso.append(lista[cont])  # caso envie
            sleep(5)
            fechar_guia()

            # Caso seja o último item da lista não precisará contar até 60s
            if cont == len(lista) - 1:
                print('\n\n-> Mensagens enviadas!')
                print(f'Envios realizados com sucesso: {sucesso}')
                print(f'Falha no envio: {falhando}')

            sleep(60)
            cont += 1
