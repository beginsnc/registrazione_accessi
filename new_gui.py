from datetime import datetime

import PySimpleGUI as sg

from module.accessi import Accesso

# Scelgo il Tema grafico
# sg.theme_previewer()
sg.theme("LightGrey1")

# Creazione layout della GUI
layout = [
    [
        sg.Text(
            "Current Time: ",
            font=("Calibri", 20),
            justification="center",
            size=(30, 1),
            key="-TIME-",
        )
    ],
    [
        sg.Text("Azienda:", font=("Calibri", 15), size=(15, 1)),
        sg.InputText(font=("Calibri", 15), key="-AZIENDA-", size=(20, 1)),
    ],
    [
        sg.Text("Nominativo:", font=("Calibri", 15), size=(15, 1)),
        sg.InputText(font=("Calibri", 15), key="-NOMINATIVO-", size=(20, 1)),
    ],
    [
        sg.Button(
            "Invia registrazione",
            font=("Calibri", 20),
            size=(30, 2),
            bind_return_key=True,
            pad=(10, 10),
        )
    ],
    [
        sg.Text(
            "",
            font=("Calibri", 15),
            justification="center",
            size=(50, 1),
            key="-OUTPUT-",
        )
    ],
]

# Creazione finestra
window = sg.Window(
    "Registrazione Visitatori", layout, resizable=False, element_justification="c"
)

# Ciclo di eventi
while True:
    event, values = window.read(timeout=1000)

    # Uscita dal ciclo di eventi quando la finestra è chiusa
    if event == sg.WINDOW_CLOSED:
        break

    # Gestione evento del bottone
    if event == "Invia registrazione":
        # ottengo i valori delle text area
        azienda = values["-AZIENDA-"]
        nominativo = values["-NOMINATIVO-"]
        
        # Creare un'istanza della classe Accesso
        accessi = Accesso("accessi.xlsx")
        risultato = accessi.record_access(azienda, nominativo)
        output = f"{risultato} - {azienda}, {nominativo}"
        window["-OUTPUT-"].update(output)

    # Aggiornamento dell'orologio
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    window["-TIME-"].update(current_time)

# Chiusura finestra
window.close()
