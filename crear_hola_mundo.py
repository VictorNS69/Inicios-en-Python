#!/usr/bin/env python
# AUTOR: VICTOR NIEVES SANCHEZ
''' Programa que crea un archivo con "Hola Mundo" si este no existe. '''

import argparse
import os
import os.path
import sys

def parse():
    ''' parsear los elementos con los que se llama al programa. '''
    parser = argparse.ArgumentParser(description='Crea un archivo "Hola Mundo" en la ruta deseada o por defecto en la actual.')
    parser.add_argument('ruta', nargs='?', default=os.getcwd(), help='Ruta donde crear el archivo')
    return parser.parse_args()


def imprimirRuta(ruta): 
    ''' Imprime la ruta en la cual se guardara el archivo.'''
    print("Creando el fichero en la ruta: %s " % ruta)


def main():
    '''Se buscara el fichero "Hola_Mundo.txt" si esta no hara nada, en caso contrario lo creara de cero.'''
    userData = parse()
    nuevoFichero = os.path.join(userData.ruta,"Hola_Mundo.txt")
    imprimirRuta(nuevoFichero)
    if not os.path.exists(nuevoFichero):
        with open(nuevoFichero, 'w') as fichero:
            fichero.write('Hola Mundo!\n')
            #fichero.close() no hace falta pq el entorno cierra el fichero solo
        sys.exit(0)

        
if __name__ == "__main__":
    main()
