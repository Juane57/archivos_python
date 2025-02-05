# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    with open ("stock.csv", "r") as csvfile:
        lista_stock = list(csv.DictReader(csvfile))
        tornillos_s = 0
        

        for k in lista_stock:

            tornillos_s += int(k["tornillos"])
        print(f"El stok de tornillos es {tornillos_s}")    
        return tornillos_s
            





def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    with open ('propiedades.csv',"r") as csvfile:
        departamentos = list(csv.DictReader(csvfile))
        d_ambientes = 0
        t_ambientes = 0

        for k in departamentos:
            try:
                if int(k["ambientes"]) == 2:
                    d_ambientes += 1
                    
                elif int(k["ambientes"]) == 3:
                    t_ambientes += 1
            except:
                continue
        print(f"Se registra {d_ambientes} departamentos dos ambientes")
        print(f"Se registra {t_ambientes} departamentos tres ambientes")    


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
