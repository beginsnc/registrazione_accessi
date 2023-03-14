import openpyxl
from datetime import datetime

# aprire il file excel
workbook = openpyxl.load_workbook('accessi.xlsx')

# selezionare il foglio di lavoro
worksheet = workbook.active

# ottenere i dati di input
data = datetime.today().strftime('%Y-%m-%d')
ora = datetime.today().strftime('%H:%M:%S')
nome_societa = input("Inserisci il nome della società: ")
nominativo = input("Inserisci il nominativo: ")

for row in worksheet.iter_rows(min_row=2, min_col=1, max_col=3):
    if row[0].value == data and row[2].value == nominativo:
       # Inserisci il nominativo nella quinta casella della stessa riga
        for cell in worksheet[row[0].row]:
            if cell.column == 3:
                cell.value = nominativo
                worksheet.cell(row=cell.row, column=5, value=ora)
    else:
        # aggiungere i dati all'ultima riga del foglio di lavoro
        last_row = worksheet.max_row + 1
        worksheet.cell(row=last_row, column=1).value = data
        worksheet.cell(row=last_row, column=4).value = ora
        worksheet.cell(row=last_row, column=2).value = nome_societa
        worksheet.cell(row=last_row, column=3).value = nominativo

# Salvataggio delle modifiche al file Excel
workbook.save('accessi.xlsx')