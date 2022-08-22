#Crea la funcion fizzbuzz, donde n es el valor a imprimir mas adelante
def fizzBuzz(n):
    #Bucle donde i comienza en 1 hasta el valor de n+1 para que haga el
    #ultimo ciclo y no lo termine antes
    for i in range(1, n+1):
        #Si se cumplen las condiciones se imprimen los valores
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
            #Si no se cumplen las condiciones imprime el valor guardado en i
        else:
            print(i)
            #Aqui se llama a la funcion para que se imprima con un valor n
print(fizzBuzz(69))
