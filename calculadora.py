#funciones de operaciones de calculo
def sumar(a,b):
    resultado = a + b
    print(resultado)

def restar(a,b):
    resultado = a-b
    print(resultado)

def dividir(a,b):
    #comprobacion si es divisible
    try:
        resultado = a/ b
    except ZeroDivisionError as e:
        print("No puedes dividir entre cero!")
        print("Error: ",e)
    else:
        print(resultado)

def multiplicar(a,b):
    resultado = a*b
    print(resultado)

def potencia(a,b):
    resultado =  a**b 
    print(resultado)

#llamada de funcion 
def calcular(operador,a,b):
    if operador == 1:
        sumar(a,b)
        return
    elif operador ==2:
        restar(a,b)
    elif operador == 3:
        dividir(a,b)
    elif operador == 4:
        multiplicar(a,b)
    elif operador == 5:
        potencia(a,b)
    #salir del bucle
    elif operador == 6:
        print("Operacion Finalizada!")
    else:
        print("Debe seleccionar los que estan disponible")


#inicio del programa
print("ingresa dos valores para calcular:")
print(" ")
#comprobacion numerica de entrada
try: 

    valor1=int(input("valor 1: ")) 
    valor2=int(input("valor 2: ")) 
except ValueError as e:
    print("Solo debes colocar numeros! ")
    print("Error: ",e)
else:

#inicio del bucle 
    seleccion =  0
    while seleccion != 6:

        print("Ingrese el operador que desea calcular:")
        operadores = ["1)suma","2)resta","3)dividir","4)multiplicar","5)potenciar","6)salir"]
        print(operadores)
        print(" ")
        #comprobacion numerica de la entrada
        try:
            seleccion = int(input("Seleccion el operador: ")) #ValueError
        except ValueError as e:
            print("Solo se debe ingresar un valor numero que indica las opciones!")
            print("Error: ",e)
        else:
            #ejecucion del calculo
            calcular(seleccion,valor1,valor2)







