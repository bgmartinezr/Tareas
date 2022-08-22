#Crea la funcion contador de palabras donde como entrada se espera una cadena
def contador_palabras(str):
    #Se declaran 2 variables
    #numero es un diccionario porque va albergando los valores de palabra en cada ciclo
    #oracion se declara como la operacion que divide la oracion en una lista de palabras
    numero = dict()
    oracion = str.split()
    
    #Ciclo donde palabra se va a repetir el numero de palabras en la lista oracion.
    #Tomando palabra el valor de cada palabra que va recorriendo en la lista
    for palabra in oracion:
        #Condicion donde palabra se va albergando en el diccionario numero
        #Al mismo tiempo (despues del primer ciclo) va comprobando si ese valor ya existe
        #para agregarle 1 a la cuenta
        if palabra in numero:
            numero[palabra] += 1
        else:
            numero[palabra] = 1
    #Regresa los valores guardados en el diccionario numero
    return numero
#Imprime la funcion con la cadena de entrada
#Como nota, en el primer ciclo if todos los valores se guardan como 1 ya que siempre
#entra el else, ya en el segundo ciclo "del trabalenguas" es cuando va agregando +1
#ya que los valores fueron encontrados en el diccionario
print( contador_palabras('pepe pecas pica papas con un pico con un pico pepe pecas pica papas'))
