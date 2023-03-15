from module.accessi import Accesso

# Creare un'istanza della classe Accesso
accessi = Accesso("accessi.xlsx")

azienda = input("Inserisci l'azienda: ")
nominativo = input("Inserisci il nominativo: ")

risultato = accessi.record_access(azienda, nominativo)
print(risultato)
