import sys
import validadores
from constantes import TIEMPO_ESTANDAR, COORD_ESTANDAR


def normaliza(fichero, f1, f2):
    pass


def filtrar_telefono(fichero, telefono):
    telefono = telefono.strip()
    try:
        with open(fichero, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if validadores.validar_linea(linea) is None:
                    continue
                telefono_linea = linea.split(";")[0]
                if telefono_linea == telefono:
                    print(linea)
    except Exception:
        sys.exit(1)

def filtrar_nif(fichero, nif):
    nif = nif.strip()
    try:
        with open(fichero, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if validadores.validar_linea(linea) is None:
                    continue
                nif_linea = linea.split(";")[1]
                if nif_linea == nif:
                    print(linea)
    except Exception:
        sys.exit(1)


def filtrar_intervalo(fichero, desde, hasta):
    desde = validadores.validar_tiempo(desde)
    hasta = validadores.validar_tiempo(hasta)
    if desde is None or hasta is None:
        sys.exit(1)
    try:
        with open(fichero, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                linea_validada = validadores.validar_linea(linea)
                if linea_validada is None:
                    continue
                if desde < linea_validada[2] < hasta:
                    print(linea)
    except Exception:
        sys.exit(1)

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