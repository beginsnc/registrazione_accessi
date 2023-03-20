from module.accessi import Accesso

# Creare un'istanza della classe Accesso
accessi = Accesso("accessi.xlsx")

# azienda = input("Inserisci l'azienda: ")
# nominativo = input("Inserisci il nominativo: ")

# risultato = accessi.record_access(azienda, nominativo)
# print(risultato)

    

# Chiamare la funzione get_unregistered_exits per ottenere le righe con l'uscita non registrata per oggi
righe_uscita_non_registrata = accessi.get_unregistered_exits()

# Stampare le righe con l'uscita non registrata
print("Righe con l'uscita non registrata per oggi:")
for riga in righe_uscita_non_registrata:
    print(riga.value)

