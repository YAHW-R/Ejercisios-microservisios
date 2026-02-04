'''NLP PATTERN IDENTIFIER'''

def get_char():
    _char = input("Escribe una letra: ")
    if len(_char) > 1 or _char == '': # se verifica si el caracter es mas de uno y si este caracter es nulo
        print("Debes escribir una sola letra")
        return get_char() # si es asi se vuelve a llamar a la funcion y se reterna el valor obtenido (funcion recursiva)
    else:
        return _char
    
def verify_char(char:str):
    if ["a", "e", "i", "o", "u"].count(char.lower()) != 0: # en vez de la recomendacion de la guia se usa el metodo count de las listas.
        print("Es una vocal")
    else:
        print("Es una consonante")

verify_char(get_char())