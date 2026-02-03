'''NLP PATTERN IDENTIFIER'''

def get_char():
    _char = input("Escribe una letra: ")
    if len(_char) > 1 or _char == '':
        print("Debes escribir una sola letra")
        return get_char()
    else:
        return _char
    
def verify_char(char:str):
    if ["a", "e", "i", "o", "u"].count(char.lower()) != 0:
        print("Es una vocal")
    else:
        print("Es una consonante")

verify_char(get_char())