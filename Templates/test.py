import PySimpleGUI as sg

layout = [
    [sg.VPush()],
    [sg.Text("Search: "), sg.Input(key='INPUT')], 
    [sg.Ok()],
    [sg.Text("", size=(0, 1), key='OUTPUT'),  ],
    [sg.VPush()],
]

window = sg.Window("Tweets Database", layout, size=(1200, 600), element_justification='c',background_color="pink")

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Ok':
        name = values['INPUT']
        tokenized_query = name.split(" ")
        doc_scores = bm25.get_scores(tokenized_query)
        window['OUTPUT'].update(value=bm25.get_top_n(tokenized_query, corpus, n=1))

window.close()