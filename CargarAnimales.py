
import os
os.system('cls')
#Metodos/Funciones

#Creo un procedimiento que me permita cargar animales y me entregue una lista de los animales cargados
def CargaDeAnimales():
    os.system('cls')
    print('Carga de fauna')
    #Variable de control, para que el usuario ingrese solo numeros en la cantidad de animales
    validarCantidad = False
    while validarCantidad == False: 
        #Intenta hacer el bloque de codigo, si no lo puede hacer, retorna la excepcion
        try:   
            #Guardo en una variable, la cantidad de animales que el usuario quiere cargar
            cantAnimales=int(input('Ingrese la cantidad de animales que desea cargar: '))
            validarCantidad = True
        except:
            #Da un aviso
            os.system('cls')
            print('Ingrese solo numeros')
    #Creo una lista vacia, la cual sera completada con la cantidad de animales que el usuario desea ingresar
    listaAnimales=[]
    os.system('cls')
    #Estructura de repeticion para cargar los animales
    for i in range(cantAnimales):
        #Solicitud de especie animal
        especie=input('Ingrese tipo de especie: ')
        #Variable de control, para que el usuario ingrese solo numeros en la cantidad de poblacion
        validar = False
        while validar == False: 
            #Intenta hacer el bloque de codigo, si no lo puede hacer, retorna la excepcion
            try:   
                #Solicitud de numero de poblacion
                poblacion=int(input(f'Ingrese la poblacion de {especie}: '))
                validar = True
            except:
                #Da un aviso
                print('Ingrese solo numeros')
        #Segun la cantidad ingresada el programa analizara el numero de la poblacion y establecera el estado de esta
        if (poblacion>=10000):
            poblacion='Fuera de peligro de extincion'
        elif (poblacion==0):
            poblacion='Extinto'
        else:
            poblacion='En vias de extincion'
        #Solicitud del habita de la especie
        ubicacion=input(f'Ingrese la region en que habita {especie}: ')
        #Creo un diccionario del animal con todos sus datos
        Animal={'Especie':especie,'Poblacion':poblacion,'Ubicacion':ubicacion}
        #Agrego a la lista el diccionario
        listaAnimales.append(Animal)
        os.system('cls')
    #Retorno la lista de animalees cargados
    return listaAnimales

#Creo un metodo que lista los animales que se encuentran guardados en la lista
def MostrarListaAnimales(lista):
    for aux in lista:
        listallaves = list(aux.keys())
        print(listallaves[0],':',aux.get(listallaves[0]))
        print(listallaves[1],':',aux.get(listallaves[1]))
        print(listallaves[2],':',aux.get(listallaves[2]))
        print('')
#Creo una funcion, donde el usuario puede elegir una de las opciones, esta retorna el numero ingresado por el usuario
def Menu():
    validar = False
    while validar ==False:
        print('##########   Menu   ##########')
        print('1- Crear lista de animales')
        print('2- Cargar nuevos animales a lista existente')
        print('3- Mostrar lista de animales')
        print('0- Salir')
        #Utilizo try, para que el usuario no pueda ingresar letras
        try:
            op=int(input('Seleccione una opcion: '))
            validar = True
        except:
            os.system('cls')
            print('Ingrese una opcion valida')
    return op

#Main
os.system('cls')
#Variable de control, que sirve para saber si el usuario ya cargo alguna vez un animal
listaCargada=False
#Variable de control, que permite decidir que opcion toma el usuario
control=Menu()
#Bucle de repeticion, para analizar el final del programa
while control!=0:
    #Opcion 1 (Crear lista de animales)
    if control == 1:
        #Llamo al metodo cargar animales
        Animales=CargaDeAnimales()
        #Cambio el estado de la variable de control para saber que ya se cargo algun animal en el programa
        listaCargada=True
        #Llamo al metodo Menu, para que el usuario elija la opcion que desea realizar
        control=Menu()
        os.system('cls')
    #Opcion 2 (Actualizar lista de animales)
    elif control == 2:
        #Analizo si el usuario ya cargo animales en el programa
        if listaCargada == True:
            #Suma de listas, sumo a la lista de animales ya cargada una nueva lista de animales
            Animales+=CargaDeAnimales()
            #Llamo al metodo Menu, para que el usuario elija la opcion que desea realizar
            control=Menu()
            os.system('cls')
        #Si el usuario no cargo un animal, se manda a la Opcion 1 para que cargue animales
        else:
            control=1
    #Opcion 3 (Listar Lista de animales)
    elif control == 3:
        #Analizo si el usuario ya cargo animales en el programa
        if listaCargada == True:
            #Llamo al metodo para mostrar la lista de animales
            MostrarListaAnimales(Animales)
        else:
            #Aviso al usuario que no se han cargado animales en el programa 
            print('No se han cargado animales.')
        #Llamo al metodo Menu, para que el usuario elija la opcion que desea realizar
        control=Menu()
        os.system('cls')
    #Si el usuario ingresa una opcion incorrecta, recibe un aviso y se le solicita nuevamente una opcion
    else:
        print('Ingrese una opcion valida.')
        control=Menu()
        os.system('cls')
#Mensaje de finalizacion de programa
print('Gracias por utilizar mi programa.')
