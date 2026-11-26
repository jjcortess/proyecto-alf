import sys
from constantes import TIEMPO_ESTANDAR, COORD_ESTANDAR


def normaliza(fichero, f1, f2):
    pass


def filtrar_telefono(fichero, telefono):
    pass


def filtrar_nif(fichero, nif):
    pass


def filtrar_intervalo(fichero, desde, hasta):
    pass


def main():
    if len(sys.argv) < 3:
        exit(1)

    opcion = sys.argv[1]
    fichero = sys.argv[2]

    if opcion == "-normaliza":
        if len(sys.argv) == 3:
            normaliza(fichero, TIEMPO_ESTANDAR, COORD_ESTANDAR)
        elif len(sys.argv) == 5:
            normaliza(fichero, sys.argv[3], sys.argv[4])
        else:
            exit(1)

    elif opcion == "-telefono" and len(sys.argv) == 4:
        filtrar_telefono(fichero, sys.argv[3])

    elif opcion == "-nif" and len(sys.argv) == 4:
        filtrar_nif(fichero, sys.argv[3])

    elif opcion == "-intervalo" and len(sys.argv) == 5:
        filtrar_intervalo(fichero, sys.argv[3], sys.argv[4])

    else:
        exit(1)


if __name__ == "__main__":
    main()