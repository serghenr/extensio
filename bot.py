import PySimpleGUI as sg
from uteis import metodos

class JanelaInterativa:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('EXTENSIO via Whatsapp:', size=(30, 0))],
            [sg.Multiline(size=(30, 10), key='mensagem')],
            [sg.Button('Enviar')],
            [sg.Output(size=(30, 10), key='output')],
        ]
        # Janela
        self.janela = sg.Window('Envio de mensagens via Whatsapp da Extensio para seus alunos').layout(layout)

    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()

            if self.button == sg.WIN_CLOSED:
                break

            mensagem = self.values['mensagem']

            # Carregar a lista de contatos
            lista_contatos = metodos.carregar_lista()
            for contato in lista_contatos:
                metodos.enviar_mensagem(mensagem)

tela = JanelaInterativa()
tela.iniciar()
