def es_palindromo(palabra):
    # Convertimos la palabra a minúsculas para evitar problemas con mayúsculas
    palabra = palabra.lower()
    # Comprobamos si la palabra es igual a su reverso
    if palabra == palabra[::-1]:
        return True
    else:
        return False

# Solicitamos al usuario que escriba una palabra
palabra = input("Escriba la palabra: ")

# Determinamos si la palabra es un palíndromo y mostramos el mensaje correspondiente
if es_palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
