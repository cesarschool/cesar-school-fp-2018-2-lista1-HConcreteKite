import math

quantidade = int(input("Quantos cigarros voce fumou por dia:\n"))
tempo_anos = int(input("Quantos anos:\n"))

total_de_cigaros = quantidade * (tempo_anos*360)
tempo_perdido = (total_de_cigaros * 10) / 1440

print("Voce perdeu:",math.floor(tempo_perdido),"dias de sua vida")x