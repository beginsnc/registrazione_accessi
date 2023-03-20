from datetime import datetime
import PySimpleGUI as sg
from module.accessi import Accesso


def set_theme():
    # Imposta il tema per la finestra PySimpleGUI
    sg.theme("LightGrey1")


def create_layout(lista_uscita_non_registrata):
    # Layout per il tab "Ingresso"
    layoutIN = [
        # Titolo
        [
            sg.Text(
                "Registrazione Ingresso",
                size=(20, 1),
                font="Calibri, 15",
                justification="left",
            )
        ],
        # Campo input per Azienda
        [
            sg.Text("Azienda:", font=("Calibri", 15), size=(15, 1)),
            sg.InputText(font=("Calibri", 15), key="-AZIENDA-", size=(20, 1)),
        ],
        # Campo input per Nominativo
        [
            sg.Text("Nominativo:", font=("Calibri", 15), size=(15, 1)),
            sg.InputText(font=("Calibri", 15), key="-NOMINATIVO-", size=(20, 1)),
        ],
        # Pulsante per inviare la registrazione
        [
            sg.Button(
                "Invia registrazione",
                font=("Calibri", 20),
                size=(30, 2),
                bind_return_key=True,
                pad=(10, 10),
            )
        ],
        # Campo di testo per mostrare il risultato dell'operazione di registrazione
        [
            sg.Text(
                "",
                font=("Calibri", 15),
                justification="center",
                size=(50, 1),
                key="-OUTPUTIN-",
            )
        ],
    ]

    # Layout per il tab "Uscita"
    layoutOUT = [
        # Titolo
        [
            sg.Text(
                "Registrazione Uscite",
                size=(20, 1),
                font="Calibri, 15",
                justification="left",
            )
        ],
        # ListBox per mostrare le uscite non registrate
        [
            sg.Listbox(
                values=lista_uscita_non_registrata,
                select_mode="extended",
                key="nominativo_list",
                size=(30, 6),
                font="Calibri, 15",
            ),
            sg.Button("Aggiorna", font="Calibri, 10"),
        ],
        # Pulsante per inviare l'uscita
        [
            sg.Button(
                "Invia Uscita",
                font=("Calibri", 20),
                size=(30, 2),
                bind_return_key=True,
                pad=(10, 10),
            )
        ],
        # Campo di testo per mostrare il risultato dell'operazione di registrazione dell'uscita
        [
            sg.Text(
                "",
                font=("Calibri", 15),
                justification="center",
                size=(50, 1),
                key="-OUTPUTOUT-",
            )
        ],
    ]

    # Creare il layout principale con il gruppo di tab e il clock
    tabgrp = [
        # Mostra l'ora corrente
        [
            sg.Text(
                "Current Time: ",
                font=("Calibri", 20),
                justification="center",
                size=(30, 1),
                key="-TIME-",
            )
        ],
        # Gruppo di tab per Ingresso e Uscita
        [
            sg.TabGroup(
                [
                    [
                        sg.Tab(
                                                    "Ingresso",
                            layoutIN,
                            title_color="Red",
                            tooltip="Registrazione Ingresso",
                            element_justification="center",
                        ),
                        sg.Tab(
                            "Uscita",
                            layoutOUT,
                            title_color="Blue",
                            tooltip="Registrazione Uscite",
                            element_justification="center",
                        ),
                    ]
                ],
                font=("Calibri", 15),
            )
        ],
    ]
    return tabgrp


def create_window(layout):
    # Crea la finestra PySimpleGUI con il layout dato
    return sg.Window(
        "Registrazione Visitatori", layout, resizable=False, element_justification="c"
    )


def update_clock(window):
    # Aggiorna l'orologio nella finestra PySimpleGUI
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    window["-TIME-"].update(current_time)

def aggionaLista(window, accessi):
    righe_uscita_non_registrata = accessi.get_unregistered_exits()
    lista_uscita_non_registrata = [
        f"{riga.value}" for riga in righe_uscita_non_registrata
    ]
    window["nominativo_list"].update(lista_uscita_non_registrata)


def main():
    accessi = Accesso("accessi.xlsx")
    # Ottenere le righe con l'uscita non registrata per oggi
    righe_uscita_non_registrata = accessi.get_unregistered_exits()

    # Creare una lista di stringhe dalle righe con l'uscita non registrata per oggi
    lista_uscita_non_registrata = [
        f"{riga.value}" for riga in righe_uscita_non_registrata
    ]
    set_theme()
    layout = create_layout(lista_uscita_non_registrata)
    window = create_window(layout)

    # Gestione degli eventi

    while True:
        event, values = window.read(timeout=1000)

        if event == sg.WINDOW_CLOSED:
            break

        if event == "Invia registrazione":
            azienda = values["-AZIENDA-"]
            nominativo = values["-NOMINATIVO-"]

            risultato = accessi.record_access(azienda, nominativo)
            output = f"{risultato} - {azienda}, {nominativo}"
            window["-OUTPUTIN-"].update(output)

        if event == "Invia Uscita":
            for val in values["nominativo_list"]:
                risultato = accessi.record_access("", val)
                messaggio = risultato + " " + val + ","
            window["-OUTPUTOUT-"].update(messaggio)
            
            aggionaLista(window,accessi)

        if event == "Aggiorna":
            righe_uscita_non_registrata = accessi.get_unregistered_exits()
            lista_uscita_non_registrata = [
                f"{riga.value}" for riga in righe_uscita_non_registrata
            ]
            window["nominativo_list"].update(lista_uscita_non_registrata)

        # Aggiorna l'orologio nella finestra
        update_clock(window)

    window.close()


if __name__ == "__main__":
    main()

