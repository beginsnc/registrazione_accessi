import tkinter as tk
from datetime import datetime

from module.accessi import Accesso


def print_input():
    azienda = input_azienda.get(1.0, "end-1c")
    nominativo = input_nominativo.get(1.0, "end-1c")

    # Creare un'istanza della classe Accesso
    accessi = Accesso("accessi.xlsx")
    risultato = accessi.record_access(azienda, nominativo)
    input_text = risultato + ": " + azienda + ", " + nominativo
    lbl.config(text=input_text)


def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=current_time)
    frame.after(1000, update_time)

# Ottenere data e ora
current_date = datetime.today().strftime("%Y-%m-%d")
current_time = datetime.today().strftime("%H:%M:%S")


# Creazione finestra principale
frame = tk.Tk()
frame.title("Registrazione Visitatori")
frame.geometry("350x250")
frame.resizable(False, False)
frame.grid_columnconfigure(0, weight=1)

# Visualizzazione data e ora correnti
time_label = tk.Label(
    frame,
    text=f"{current_date} - {current_time}",
    font=("Helvetica", 15),
)
time_label.grid(row=5, column=0, sticky="S", padx=20, pady=10, columnspan=2)

# Creazione campo di testo con label per azienda
azienda_label = tk.Label(
    frame,
    text="Azienda:",
    font=("Helvetica", 15),
)
azienda_label.grid(row=0, column=0, sticky="W", padx=20, pady=10)

input_azienda = tk.Text(frame, height=1, width=20)
input_azienda.grid(row=0, column=1, sticky="E", padx=20, pady=10)

# Creazione campo di testo con label per nominativo
nominativo_label = tk.Label(
    frame,
    text="Nominativo:",
    font=("Helvetica", 15),
)
nominativo_label.grid(row=2, column=0, sticky="W", padx=20, pady=10)

input_nominativo = tk.Text(frame, height=1, width=20)
input_nominativo.grid(row=2, column=1, sticky="E", padx=20, pady=10)

# Creazione bottone d'invio
button = tk.Button(frame, text="Invia registrazione", command=print_input, width=100)
button.grid(row=3, column=0, sticky="EW", padx=20, pady=10, columnspan=2)

# Creazione messaggio di conferma
lbl = tk.Label(frame, text="")
lbl.grid(row=4, column=0, sticky="N", padx=20, pady=10, columnspan=2)

update_time()
frame.mainloop()
