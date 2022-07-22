import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('User')], [sg.Input(key='usuario')]
    [sg.Text('password')], [sg.Input(key='senha',password_char='*')]
    [sg.Checkbox('Save the password')]
    [sg.Button('Login')]
]

#Janela
janela =sg.Window('Login screen', layout=layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == '' and valores['senha'] == '':
            print ('Bem Vindo')
            