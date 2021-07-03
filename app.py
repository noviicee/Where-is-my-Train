import requests
import PySimpleGUI as sg

sg.FlexForm('Check your train')

def trainSchedule(self):
        train_number=input("Enter the train number")
        self.fetchData(train_number)

def fetchData(self,url):
    data=requests.get(url)

    data=data.json

    print(data)


# Define the window's contents
layout = [[sg.Text("""How would you like to proceed?
        Enter 1 to check live train status.
        Enter 2 to check PNR.
        Enter 3 to check train schedule""")],
          
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Submit(), sg.Cancel()]
        ]

# Create the window
window = sg.Window('Check your train', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    # Output a message to the window
    else:
        # print(values)
        if values['-INPUT-']=='1':
            window['-OUTPUT-'].update("Live Status") 
        elif values['-INPUT-']=='2':
            window['-OUTPUT-'].update('PNR')
        else:
            trainSchedule()

# Finish up by removing from the screen
window.close()
