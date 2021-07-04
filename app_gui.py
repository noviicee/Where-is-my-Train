import requests
import PySimpleGUI as sg

def trainSchedule(number):
    train_number=input("Enter the train number")
    fetchData(train_number)

def fetchData(number): #edit the url's train_number with number
    url='http://indianrailapi.com/api/v2/TrainSchedule/apikey/<apikey>/TrainNumber/{}'.format(number)
    data=requests.get(url)
    data=data.json
    return(data)

sg.FlexForm("Check your train's route")

# Layout-1
layout = [[sg.Text("""How would you like to proceed?
        Enter 1 to check live train status.
        Enter 2 to check PNR.
        Enter 3 to check train schedule""")],
          
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Submit(), sg.Cancel()]
        ]

window = sg.Window('Check your train', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    else:
        #Layout-2
        layout = [[sg.Text("""Enter the train number""")],
                
                [sg.Input(key='-INPUT-')],
                [sg.Text(size=(40,1), key='-OUTPUT-')],
                [sg.Submit(), sg.Cancel()]
                ]

        window = sg.Window('Train Number', layout)

        while True:
            event, number = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                break
            else:
                if values['-INPUT-']=='1':
                    window['-OUTPUT-'].update("Live Status") 
                    
                elif values['-INPUT-']=='2':
                    window['-OUTPUT-'].update('PNR')
                else:
                    res=fetchData(number['-INPUT-'])
                    window['-OUTPUT-'].update(res)
                    window['-OUTPUT-'].update('Route: '+res)


        # Finish up by removing from the screen
        #Layout-2
        window.close()

# Finish up by removing from the screen
# Layout-1
window.close()
