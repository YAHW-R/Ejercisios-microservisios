'''BACKEND LOGISTICO DINAMICO'''

from datetime import datetime

distance = 0.0
car_type = input("select the type p (Pickup: $6.00), g (Grandola: $7.00), m (Mudanza: $10.00): ")
try:
    distance = float(input("set de distance in km: numbers: "))
except ValueError: 
    print("the distance must be a number")
    quit()

mont = 0.0

match car_type:
    case "p": 
        mont = 6.00
    case "g":
        mont = 7.00
    case "m":
        mont = 10.00
    case _: 
        print("error: the car type selected does not exist")

print(f'''
------ FACTURA ---------
day: {str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))}

selected car charge: {mont}$
distance charge: {distance * 1.5}$

total charge:  {mont + (distance * 1.5)}$

-------------------------
''')