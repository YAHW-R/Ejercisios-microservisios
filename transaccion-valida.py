"""TRANSACCION VALIDA"""

def get_validate_key(digit_num:int = 16):
        _validate_key = input(f"Ingrese la clave de validacion de su respectivo metodo de pago (calve unicamente numerica de {digit_num} digitos): ")
        if _validate_key.isdigit():
            return _validate_key
        else:
            print("debe colocar unicamente numeros en la clave de validacion")
            get_validate_key(digit_num)

def verify_validate_key(validate_key:str, lenght:int = 16): 
    if len(validate_key) == lenght:
        print("transaccion valida")
    else:
        print("transaccion no valida")


def verify_transaction():
    __payment_method = input("Ingrese el metodo de pago que va a realizar: t/Tarjeta, p/Pago Movil. (Default Tarjeta): ")
    match __payment_method:
        case "t":
            __validate_key = get_validate_key()
            verify_validate_key(__validate_key)

        case "p":
            __validate_key = get_validate_key(8)
            verify_validate_key(__validate_key, 8)

        case _:
            __validate_key = get_validate_key()
            verify_validate_key(__validate_key)

        
verify_transaction()