from multiprocessing.sharedctypes import Value
from optparse import Values
from tokenize import Number
import PySimpleGUI as sg

#Layout

def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('User')], 
        [sg.Input(key='usuario')],
        [sg.Text('Password')], 
        [sg.Input(key='senha',password_char='*')],
        [sg.Checkbox('Save the password')],
        [sg.Button('Login'), sg.Button('Cancel'),sg.Button('Register')],   
    ]
    return sg.Window('login', layout=layout,finalize=True)

def janela_register():
    sg.theme('Reddit')
    layout = [
        [sg.Text('User')],
        [sg.Input(key='usuario')],
        [sg.Text('Passoword')],
        [sg.Input(key='senha',password_char='*')],
        [sg.Text('Email')],
        [sg.Input(key='email')],
        [sg.Text('Full address')],
        [sg.Input(key='endereço completo')],
        [sg.Text('City')],
        [sg.Input(key='cidade')],
        [sg.Text('State')],
        [sg.Input(key='estado')],
        [sg.Button('Register'), sg.Button('Cancel')]
    ]
    return sg.Window('Register', layout=layout,finalize=True)

#Janelas
janela1, janela2 = janela_login(), None

#Eventos
while True:
    window, eventos, valores = sg.read_all_windows()
    
    #Evento Fechamento
    if window == janela1 and eventos == sg.WINDOW_CLOSED:
        break
    if window == janela1 and eventos == 'Cancel':
        break
    if window == janela2 and eventos == sg.WINDOW_CLOSED:
        break
    
    #Evento Voltar Pagina
    if window == janela1 and eventos == 'Register':
        janela2 = janela_register()
    if window == janela2 and eventos == 'Cancel':
        janela2.hide()
        janela1.un_hide()
        
    #Evento Cadastrado
    if window == janela2 and eventos == 'Register':
        if Values['Register'] == True: 
            sg.popup('Cadastro efetuado com sucesso!'),

