"""CRIPTOGRAFIA"""

import math

num = 0

try:
    num = int(input("Ingrese un numero entero: "))
    num = abs(num)

except ValueError:
    print("el valor de entrada debe ser numerico")
    quit()

def verify_perfect_num(n:int):
    # Ningun numero impar es perfecto
    if n % 2 != 0: return False

    # Relacion de primos de eculides 2^(p-1)(2^p - 1) = N (despejado (1 + sqrt(1 + 8N))/2 = 2^p)
    dis = 1 + (8 * n)

    # La raiz del discriminante debe ser exacta
    sqrt_dis = int(math.isqrt(dis))
    if sqrt_dis ** 2 != dis: return False

    # Debe ser potencia de dos
    power2 = sqrt_dis + 1
    if not(power2 & (power2 - 1) == 0) and (power2 != 0): return False # x & (x - 1) == 0 es una exprecion para verificar si un numero no tiene unos en bianrio

    ## logaritmo base para el despeje
    p = power2.bit_length() - 1

    ## verificamos si 2^p - 1 es primo con el truco de lucas-lehmer
    if p < 2: return False
    if p == 2: return True # caso del 6

    s = 4
    m = 2 ** p - 1
    for _ in range(p-2):
        s = (s ** 2 - 2) % m

    return s == 0

print(verify_perfect_num(num))







