import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('User')], 
    [sg.Input(key='usuario')],
    [sg.Text('Password')], 
    [sg.Input(key='senha', password_char='*')],
    [sg.Input(key='Confirm your password', password_char='*')],
    [sg.Button('Cancel'), sg.Button('Register')],
]

#Janela
janela = sg.Window('Registration screen', layout)

#Ler os eventos
while True:
    eventos, valores = janela.read(),
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == '' and valores['senha'] == '':
         print ('Bem Vindo!')
