#creacion de objeto estudiante
class Estudiante:
    def __init__(self, nombre, carrera, promedio):
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Carrera: {self.carrera}, Promedio: {self.promedio}")

#lista que almacena los estudiantes
lista_estudinates = []
estudiante1 = Estudiante("ramses","ing sistemas",18)
estudiante2 = Estudiante("maria","ing sistemas",17)
estudiante3 = Estudiante("diana","derecho",15)
estudiante4 = Estudiante("rebeca","derecho",18)
lista_estudinates.append(estudiante1)
lista_estudinates.append(estudiante2)
lista_estudinates.append(estudiante3)
lista_estudinates.append(estudiante4)



def agregar_estudiante():

    print("INICIO DE REGISTRO!")
    
    #bucle si se introduce un error en el promedio repite todo el proceso
    bucle = 0
    #bucle de completar correctamente los campos requeridos
    while bucle !=1: 
        try: 
            valor = 0
            while valor != 1:
                nombre = (input("Ingrese nombre del estudiante: ")).lower()
                carrera = (input("Ingrese carrera del estudiante: ")).lower()
                #evalua si los campos estan vacios
                if nombre != "" and carrera != "":
                    promedio = int(input("Ingrese promedio: "))
                    if promedio <= 12 or promedio > 20:
                            print("INGRESE UN VALOR DE PROMEDIO MAYOR IGUAL A 12 O MENOR IGUAL DE 20!")
                    #al cumplir todas las condiciones finaliza el registro
                    else:
                        valor = 1
                #caso si nombre y carrera no se llenan
                else:
                    print("Debe llenar los datos de estudiante y carrera primero!")
        #error de dato en promedio
        except ValueError as e:
                print("Solo debes colocar numeros! ")
                print("Error: ",e)
        #si pasa el try, crea el objeto y se almacena en la lista
        else:    
                nuevo_alumno = Estudiante(nombre,carrera,promedio)
                lista_estudinates.append(nuevo_alumno)
                print(f"Estudiante: {nombre}, carrera:{carrera} se registro Exitosamente!")
                #finaliza el bucle 
                bucle= 1
            
def mostrar_estudiantes():
    print("Lista de Estudiantes:")
    #blucle lista numero y datos de los estudiantes
    for i, estudiante in enumerate(lista_estudinates):
        print(f"Estudiante {i+1})")
        estudiante.mostrar_info()

def buscar_estudiante():
    #ingresamos el nombre del estudiante
    print("BUSQUEDA DE ESTUDIANTE EN EL SISTEMA!")
    valor = (input("ingrese nombre del estudiante: ")).lower()

    #variable encuentra el estudiante en la lista
    estudiante_encontrado = None
    try:
        for estudiante in lista_estudinates:
            #si ecuentra el estudiante almacena los parametro del objeto
            if estudiante.nombre == valor:
                print(f"Estudiante: {valor} se encuentra en el registro!")
                estudiante_encontrado = estudiante
                #imprime los datos del estudiante   
                print(f"Datos de {valor}")
                estudiante_encontrado.mostrar_info()
                break
        #si no encuentra en el primer bucle se forza error 
        if estudiante_encontrado is None:
            raise ValueError("Estudiante no encontrado.")
    
    except ValueError as e:
        print(f"Error en la búsqueda: {e}")

    #se finaliza el proceso
    finally:
        print("Proceso de búsqueda terminado.")

def eliminar_estudiante():
    print("ELIMINACION DE ESTUDIANTES")
    #imprime lista de los nombres de los estudiantes
    for i in lista_estudinates:
         print(f"- {i.nombre}")

    #se ingresa el nombre 
    estudiante_eliminar = (input("Ingrese el nombre del estudiante a eliminar: ")).lower()    
    #se declara la variable al detectar la busqueda
    encontrado = None
    for estudiante in lista_estudinates:
         #si encuentra el nombre lo almacena en la variable
         if estudiante.nombre == estudiante_eliminar:
              encontrado = estudiante
              break
    
    #al haber un valor en la variable se procede a eliminar de la lista
    if encontrado:
         lista_estudinates.remove(encontrado)
         print(f"El estudiante: {estudiante_eliminar} fue eliminado de la lista!")
    #del caso no funcione finaliza la operacion que no existe el nombre
    else:
         print(f"No se encontro el estudiante: {estudiante_eliminar} en la lista!")

def actualizar_promedio():
    #se prueba buscando el nombre del alumno
    try:
        alumno = (input("ingrese nombre del estudiante: ")).lower()
        estudiante_encontrado = None
        valor = 0
        #del nombre se extrae de la lista si se encuentra
        for estudiante in lista_estudinates:
            if estudiante.nombre == alumno:
                estudiante_encontrado = estudiante
                #si se encuentra entra en bucle que debe colocar el nuevo promedio
                while valor != 1:
                    nuevo_promedio = int(input("Ingresa nuevo promedio para el estudiante: "))
                    #si cumple la condicion repite el bucle hasta que no lo cumpla
                    if nuevo_promedio <= 12 or nuevo_promedio > 20:
                        print("INGRESE UN VALOR DE PROMEDIO MAYOR IGUAL A 12 O MENOR IGUAL DE 20!")
                    #se actualiza los datos y finaliza el programa
                    else:
                        estudiante_encontrado.promedio = nuevo_promedio
                        valor = 1
                        print(f"Se actualizo el promedio del estudiante {alumno}")
                break
        #si no encuentra en el primer bucle se forza error 
        if estudiante_encontrado is None:
                raise ValueError("Estudiante no encontrado.")
    #si se inserta texto saldra la excepcion
    except ValueError as e:
        print(f"Error en la búsqueda: {e}")

    #se finaliza el proceso
    finally:
        print("Proceso de búsqueda terminado.")

def calcular_promedio_grupo():
    #aplica conceptos de compresion de lista
    suma_promedios = sum(estudiante.promedio for estudiante in lista_estudinates)
    promedio_total = round((suma_promedios / len(lista_estudinates)))
    print(f"Promedio de la lista de estudiantes: {promedio_total}")

def filtrar_por_carrera():
    #ingresamos el nombre del estudiante
    print("BUSQUEDA DE CARRERA EN EL SISTEMA!")
    valor = (input("ingrese nombre de la carrera: ")).lower()
    carrera_filtrada = []
    #proceso similar a buscar nombre de estudiante
    for estudiante in lista_estudinates:
        if estudiante.carrera.lower() == valor:
            carrera_filtrada.append(estudiante)
    if carrera_filtrada:
        
        for estudiante in carrera_filtrada:
            estudiante.mostrar_info()
    else:
        print("No se encontro ninguna carrera")
        


def mejor_estudiante():
    #creamos variable para asignar el promedio mas alto empezando desde el elemento 0
    mayor_promedio = lista_estudinates[0]

    #recorremos para obtener cada elemento
    for i in range(1, len(lista_estudinates)):
        estudiante = lista_estudinates[i]
        #en cada elemento se valua el parametro de promedio cual es mas alto
        if estudiante.promedio  > mayor_promedio.promedio :
            #se almacena en la variable y se vuelve a comparar hasta finalizar
            mayor_promedio=estudiante
    
    print("----------")
    print("estudiante con mejor promedio:")
    #se imprime el objeto.parametro mas alto qeu tiene la lista
    mayor_promedio.mostrar_info()


#inicio del programa
print("BIENVENIDO AL SISTEMA DE GESTION DE ESTUDIANTE")
print("TENDRAS LAS SIGUEINTES OPCIONES!")
valor = 0

#inicio del bucle del menu
while valor != 9:
    print("----------------------")
    print("1) AGREGRAR ESTUDIANTE")
    print("2) MOSTRAR LISTA")
    print("3) BUSCAR ESTUDIANTE")
    print("4) ELIMINAR ESTUDIANTE")
    print("5) ACTUALIZAR PROMEDIO")
    print("6) PROMEDIO DEL GRUPO")
    print("7) FILTRAR CARRERA")
    print("8) MAYOR PROMEDIO")
    print("9) SALIR")
    print("----------------------")
    #se prueba que todos los valores esten correctos
    try:
        valor = int(input("Ingrese el valor que salga disponible: "))
    except ValueError as e:
         print("Solo se acepta valor numerico!")
         print(f"Error: {e}")
    else:
    
        if valor == 1:
            agregar_estudiante()
        elif valor ==2:
            mostrar_estudiantes()
        elif valor ==3:
            buscar_estudiante()
        elif valor==4:
            eliminar_estudiante()
        elif valor == 5:
             actualizar_promedio()
        elif valor == 6:
             calcular_promedio_grupo()
        elif valor == 7:
             filtrar_por_carrera()
        elif valor == 8:
             mejor_estudiante()
        elif valor == 9:
             print("Finalizacion del programa!")
        else:
            print("DEBES COLOCAR UN VALOR DISPOIBLE EN LAS OPCIONES!")


    