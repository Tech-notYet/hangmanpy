from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.OK(), sg.Cancel()]]

guessed_layout = [
    [
        sg.Text(text='Previous Guesses:', justification=sg.TEXT_LOCATION_LEFT)
    ],
    [
        sg.Text(text='', size=(20, 5), justification=sg.TEXT_LOCATION_CENTER, pad=(
            (5, 5), (0, 5)), key='GUESSEDTEXT', border_width=2, relief=sg.RELIEF_GROOVE)
    ]
]

guess_input_layout = [
    [
        sg.InputText(pad=((2, 2), (15, 5)), key='GUESSINPUT')
    ],
    [
        sg.Ok(button_text='Guess', pad=(5, 5), key='GUESSBUTTON'),
        sg.Cancel(button_text='Retry', pad=(5, 5), key='RETRYBUTTON')
    ]
]

layout = [
    [
        sg.Canvas(background_color='white', size=(400, 400), pad=(5, 5)),
        sg.Frame('', layout=[
            *guessed_layout,
            [
                sg.Frame('', guess_input_layout, pad=(10, 10),
                         key='INPUTFRAME', element_justification='right')
            ]
        ]
        , element_justification='center')
    ]
]

# Create the Window
window = sg.Window('PyHangman', layout)
# Event Loop to process "events"
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break

window.close()
