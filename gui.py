import aiml
import PySimpleGUI as sg

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
sg.theme('LightBlue 1')
layout = [[sg.Text('You: '), sg.Text(size=(12,1), key='-mytext-')],
          [sg.Text('Csigusz Foxoup (bot): '), sg.Text(size=(12,1), key='-CSI-')],
          [sg.Input(key='-myinput-')],
          [sg.Button('Send message'), sg.Button('Bye!')]]

window = sg.Window('Csigusz Foxoup, your friend in a box (bot)', layout, [200,400])


while True:
    event = window.read()
    values = window.read()
    if event == sg.WIN_CLOSED or event == 'Bye!':
        break
    if event == 'Send message':
        # change the "output" element to be the value of "input" element
        input_text = (values)
        response = kernel.respond(input_text)
        window['-mytext-'].update(values['-myinput-'])
        print("Csigusz Foxoup(bot): "+response)

window.close()