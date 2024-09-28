# vetores
semana = (1, 2, 3, 4, 5, 6, 7)
dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

# exemplo segunda feira
dias = 1

# condição de imprimir dias e numeração dos dias da semana
if dias in semana:
    for número, nome_dias in zip (semana, dias_semana):
        print (f"{número} - {nome_dias}")
