"""BASE DE DATOS DSITRIBUIDA"""

def calc_parity(num:int):
    if num % 2 == 0:
        return "A"
    else:
        return "B"
    
try:
    print("Servidor "+calc_parity(int(input("enter id: ")))) # se realiza todo el programa en una sola linea
except ValueError:
    print("error: the data is incorrect")