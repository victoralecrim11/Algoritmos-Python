from asyncio import events
from PySimpleGUI import PySimpleGUI as sg

# Primeiro criar o layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='Usuario',size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='Senha', password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar o login ?')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuario'] == 'Jhonatan' and valores['Senha'] == '123456':
            print('Bem vindo, você logou com sucesso! ')
        else:
            print("Nenhum valor foi inserido nos campos !")