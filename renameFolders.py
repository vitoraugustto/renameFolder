import PySimpleGUI as sg
import os

sg.theme('DarkGrey12')

layout = [
    [sg.Text("Digite a data:", size=(10, 0)), sg.Input(size=(14, 0), key="newDate")],
    [sg.Button("OK", size=(24, 1))]
]

window = sg.Window("Renomear", element_justification='center').layout(layout)

event, values = window.read()

newDate = values['newDate']

celulas = os.listdir('E:/Reprises - X-X (cópia exemplo)')

celula3  =  celulas[1]
celula4  =  celulas[2]
celula5  =  celulas[3]
celula6  =  celulas[4]
celula7  =  celulas[5]
celula8  =  celulas[6]
celula11 =  celulas[7]
celula12 =  celulas[8]


def renameFolder():

    os.rename(celula3,  'Reprises ' + newDate + ' - Célula 03')
    os.rename(celula4,  'Reprises ' + newDate + ' - Célula 04')
    os.rename(celula5,  'Reprises ' + newDate + ' - Célula 05')
    os.rename(celula6,  'Reprises ' + newDate + ' - Célula 06')
    os.rename(celula7,  'Reprises ' + newDate + ' - Célula 07')
    os.rename(celula8,  'Reprises ' + newDate + ' - Célula 08')
    os.rename(celula11, 'Reprises ' + newDate + ' - Célula 11')
    os.rename(celula12, 'Reprises ' + newDate + ' - Célula 12')
    
if event == 'OK':
    renameFolder()
