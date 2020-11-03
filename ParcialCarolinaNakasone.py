'''

Todos los ejercicios deberán contener las validaciones y excepciones
correspondientes.

1. Usted ha sido contratado para desarrollar una solución que le permita al dpto. De
RRHH obtener de manera ágil el estado de las vacaciones de sus empleados.
Por cuestiones organizativas la empresa tiene los datos de legajo separados de
los datos de vacaciones. El sistema deberá :

a. Tener un menú de acciones

b. Permitir la carga de datos y guardarlos en un archivo csv cuyo nombre
será dado por el usuario. Si el archivo ya existe deberá preguntar si se
desea modificar o sobreescribirlo. * sólo validar que legajo y total de
vacaciones sean números enteros.

c. Dado el número de legajo de un empleado calcular e informar en pantalla
los días que le quedan disponibles de vacaciones junto con el resto de sus
datos. Por ejemplo "Legajo 1 : Laura Estebanez, le restan 11 días de
vacaciones"
Tenga en cuenta que las acciones del menú no tienen un orden en particular

'''


import csv
import os.path

def menu_vacaciones():

    CAMPOS = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']
    ARCHIVODIAS = "dias.csv"
    archivolegajos = input("Ingrese el nombre del archivo: ")+".csv"

    while True:
        print("MENU:\n1.Cargar legajos.\n2.Leer/Recuper informacion.\n3.Salir. ")
        opcion = input("Ingrese una opcion: ")


        if opcion == "1":

            cargar(archivolegajos, CAMPOS)

        elif opcion == "2":

            leer(archivolegajos, ARCHIVODIAS)

        elif opcion == "3":
            exit()

        else:
            print("Ingrese una opcion valida.")




def entrada(campos):
        seguir = "si"
        lista_legajos = []
        while seguir =="si":
            trabajador = {}
            for campo in campos :

                if campo == "Legajo" or campo == "Total Vacaciones":

                    trabajador[campo] = input(f"Ingrese {campo} del trabajador: ")



                else:
                    trabajador[campo] = input(f"Ingrese {campo} del trabajador: ")

            lista_legajos.append(trabajador)
            seguir = input("Desea seguir? si/no: ").lower()
        return lista_legajos



def cargar(archivo1, campos):


    #el archivo tendra el formato dado por los campos: Legajo, Apellido, Nombre, Total Vacaciones



    try:
        archivo_existe = os.path.isfile(archivo1) #archivo existe o no

        if archivo_existe: #usuario selecciona si desea modificar o sobreescribir
            print("El archivo existe.")
            opcion = input("1.Modificar\n2.Sobreescribir\nIngrese opcion: ")

            if opcion =="1":
                modo = 'a'
                header = 'no'
            elif opcion == '2':
                modo = 'w'
                header = 'si'
            else:
                print("Ingrese una opcion valida.")
        else:

            modo = 'w'
            header = 'si'

        lista_legajos = entrada(campos)



        with open(archivo1, modo, newline='') as file:
            file_csv = csv.DictWriter(file, fieldnames = campos)

            if header == 'si':
                file_csv.writeheader()

            file_csv.writerows(lista_legajos)
            print("Se guardo correctamente.")
            return



    except IOError:
        print("Hubo un error con el archivo.")



#cargar("pruebaCarga.csv",  ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones'] )




def leer (archivolegajos, archivodias):
    legajo_buscado = input("Ingrese legajo: ")

    try:
        with open(archivolegajos, 'r') as legajos, open(archivodias, 'r') as dias:
            legajos_csv = csv.DictReader(legajos)
            dias_csv = csv.DictReader(dias)


            empleado = next(legajos_csv, None)
            dia_tomado = next(dias_csv, None)



            while empleado:


                while empleado and empleado['Legajo'] == legajo_buscado:
                    contador = 0

                    while dia_tomado:
                        while dia_tomado and dia_tomado['Legajo'] == legajo_buscado:


                            contador += 1

                            dia_tomado = next(dias_csv, None)

                        dia_tomado = next(dias_csv, None)

                    resto = int(empleado['Total Vacaciones']) - contador    #calculo cuantos dias le restan al empleado
                    print (f"El legajo {legajo_buscado}: {empleado['Nombre']} {empleado['Apellido']} le restan {resto} dias de sus vacaciones.")

                    empleado = next(legajos_csv, None)

                empleado = next(legajos_csv, None)





    except IOError:
        print("Hubo un error al abrir el archivo.")




#leer("pruebaCarga.csv", "dias.csv")
menu_vacaciones()
