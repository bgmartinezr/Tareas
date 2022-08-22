#Establece la oracion a evaluar
oracion = 'somos o no somos'
#Crea la funcion palindromo
def palindrome(pal):
    #La cadena ingresada primero se transforma en minusculas
    #enseguida remplaza por espacios por no espacios
    pal = pal.lower().replace(' ', '')
    #Regresa un valor True o False por la comparacion de la cadena sin espacios
    #por si misma pero invertida
    return pal == pal[::-1]
#Imprime y llama la funcion con la oracion ingresada
print(palindrome(oracion))