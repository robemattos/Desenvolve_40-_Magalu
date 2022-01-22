from datetime import datetime
data_hora = datetime.now()
data_hora_texto = data_hora.strftime("%d/%m/%y %H:%M")

print(data_hora_texto)
