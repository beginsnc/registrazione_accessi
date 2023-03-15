import tkinter as tk
from datetime import datetime

# ottenere data e ora
data = datetime.today().strftime("%Y-%m-%d")
ora = datetime.today().strftime("%H:%M:%S")

frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry("350x250")
frame.resizable(False, False)
frame.grid_columnconfigure(0, weight=1)


# Funzione all'push del bottone
def printInput():
    inp = input_Azienda.get(1.0, "end-1c")
    lbl.config(text="Provided Input: " + inp)


def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=current_time)
    frame.after(1000, update_time)


# Visualizzo data e ora correnti
time_label = tk.Label(
    frame,
    text=data + " - " + ora,
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

input_Azienda = tk.Text(frame, height=1, width=20)
input_Azienda.grid(row=0, column=1, sticky="E", padx=20, pady=10)


# Creazione campo di testo con label per nominativo
nominativo_label = tk.Label(
    frame,
    text="Nominativo:",
    font=("Helvetica", 15),
)
nominativo_label.grid(row=2, column=0, sticky="W", padx=20, pady=10)

input_Nominativo = tk.Text(frame, height=1, width=20)
input_Nominativo.grid(row=2, column=1, sticky="E", padx=20, pady=10)

# Creazione bottone d'invio
Button = tk.Button(frame, text="Invia registrazione", command=printInput, width=100)
Button.grid(row=3, column=0, sticky="EW", padx=20, pady=10, columnspan=2)


# Creazione messaggio di conferma
lbl = tk.Label(frame, text="")
lbl.grid(row=4, column=0, sticky="N", padx=20, pady=10)

update_time()
frame.mainloop()
