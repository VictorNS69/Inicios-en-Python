#!/usr/bin/env python
# AUTOR: VICTOR NIEVES SANCHEZ
''' Programa para hacer una buscqueda de un archivo en un directorio. '''

import argparse
import os
import os.path
import sys

def parse():
    ''' parsear los elementos con los que se llama al programa. '''
    parser = argparse.ArgumentParser(description='Busca un archivo en el directorio.')
    parser.add_argument('Fichero', nargs='+', help='Nombre del fichero.')
    parser.add_argument('Ruta', nargs='?', default=os.getcwd(), help='Ruta donde buscar el archivo.')
    parser.add_argument('-r', nargs='?', default=None, help='Busqueda recursiva.')
    return parser.parse_args()


def recursivo(boolean):
    if boolean is None:
        print("Busqueda no recursiva.")
    print("Busqueda recursiva.")


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return 1

        
def main():
    '''Cuerpo main del programa'''
    userData = parse()
    archivoBuscar = str(userData.Fichero)
    rutaBuscar = os.path.join(userData.Ruta, archivoBuscar)
    #recursivo(userData.R)
    print(find(archivoBuscar,rutaBuscar))
    if find(archivoBuscar,rutaBuscar):
        print("Encontrado! en: %s" % rutaBuscar)
        sys.exit(0)
    print("No encontrado!")
    sys.exit(0)

    
if __name__ == "__main__":
    main()
