"""DATASETS DE SENSORES"""

farenheit_list = [0.12, 0.20, 200, 120, 360, 40]

celsius_list = [(f* (9/5) + 32) for f in farenheit_list] # se realizo el programa de la manera avanzada que recomienda la guia.

print(celsius_list)

