'''CALCULO DE GANANCIA'''

sale_price = 0
manu_cost = 0

try:
    sale_price = float(input("Ingrese su precion de venta: "))
    manu_cost = float(input("Igrese el costo de fabricacion: "))

except ValueError: 
    print("ingrese un valor numerico")

print("Su ganamcia neta es: "  + str(sale_price - manu_cost))