import re
import sys
import constantes as const


def validar_telefono(campo):

    if const.ER_TLF.fullmatch(campo) is None:
        return None
    limpio = const.ER_LIMPIAR_TLF.sub("", campo)
    return "+34" + limpio


def letra_dni(num):
    return const.LETRAS_DNI[num%23]

def validar_nif(campo):

    coincidencia = const.ER_NIF.fullmatch(campo)

    if coincidencia != None:
        cuerpo = coincidencia.group("cuerpo")
        letra = coincidencia.group("letra")
    else: 
        return None

    if cuerpo[0] in const.EQUIVALENCIA_NIE:
        cuerpo = const.EQUIVALENCIA_NIE[cuerpo[0]] + cuerpo[1:]

    if letra_dni(int(cuerpo)) == letra:
        return campo
    else:
        return None


def es_bisiesto(anio):
    return (anio%4 == 0 and anio%100 != 0) or (anio%400 == 0)

def fecha_valida(anio, mes, dia):

    if anio < 1 or anio > 9999:
        return False

    max_dias = const.DIAS_POR_MES[mes]
    if mes == 2 and es_bisiesto(anio):
        max_dias = 29

    if dia < 1 or dia > max_dias:
        return False

    return True


def validar_tiempo(campo):
    coincidencia = const.ER_TIEMPO_F1.fullmatch(campo)
    if coincidencia is not None:
        anio = int(coincidencia.group("anio"))
        mes = int(coincidencia.group("mes"))
        dia = int(coincidencia.group("dia"))
        hora = int(coincidencia.group("hora"))
        minuto = int(coincidencia.group("minuto"))
        segundo = 0
    else:
        coincidencia = const.ER_TIEMPO_F2.fullmatch(campo)
        if coincidencia is not None:
            anio = int(coincidencia.group("anio"))
            mes = const.MES_A_NUM[coincidencia.group("mes").lower()]
            dia = int(coincidencia.group("dia"))
            hora = int(coincidencia.group("hora"))
            minuto = int(coincidencia.group("minuto"))
            segundo = 0
            ampm = coincidencia.group("ampm").lower()

            if ampm == "am" and hora == 12:
                hora = 0
            elif ampm == "pm" and hora != 12:
                hora = hora + 12
        else:
            coincidencia = const.ER_TIEMPO_F3.fullmatch(campo)
            if coincidencia is None:
                return None
            anio = int(coincidencia.group("anio"))
            mes = int(coincidencia.group("mes"))
            dia = int(coincidencia.group("dia"))
            hora = int(coincidencia.group("hora"))
            minuto = int(coincidencia.group("minuto"))
            segundo = int(coincidencia.group("segundo"))
        
    if not fecha_valida(anio, mes, dia):
        return None

    return [anio,mes,dia,hora,minuto,segundo]

def gms_decimal(grados, minutos, segundos, direccion):
    res = grados+minutos/60 + segundos/3600
    if direccion=="S" or direccion=="W":
        res = -res
    return res

def validar_coordenadas(campo):
    coincidencia =const.ER_COORD_F1.fullmatch(campo)
    if coincidencia is not None:
        lat = float(coincidencia.group("lat"))
        lon = float(coincidencia.group("lon"))
    else:
        coincidencia = const.ER_COORD_F2.fullmatch(campo)
        if coincidencia is None:
            coincidencia = const.ER_COORD_F3.fullmatch(campo)
        if coincidencia is None:
            return None

        lat = gms_decimal(
            int(coincidencia.group("lat_g")),
            int(coincidencia.group("lat_m")),
            float(coincidencia.group("lat_s")),
            coincidencia.group("lat_dir")
        )
        lon = gms_decimal(
            int(coincidencia.group("lon_g")),
            int(coincidencia.group("lon_m")),
            float(coincidencia.group("lon_s")),
            coincidencia.group("lon_dir")
        )

    if lat < -90 or lat > 90 or lon < -180 or lon > 180:
        return None

    return [lat, lon]

def validar_precio(campo):
    if const.ER_PRECIO.fullmatch(campo) is None:
        return None
    return campo

def validar_linea(linea):

    linea_limpia = linea.strip()
    if not linea_limpia:
        return None

    campos_bruto = linea_limpia.split(';')
    if len(campos_bruto) != 6:
        return None

    campos = []
    for c in campos_bruto:
        campos.append(c.strip())

    #campos = [tlf, nif o nie, tiempo, coord, prod, precio]

    tlf = validar_telefono(campos[0])
    if tlf is None:
        return None

    nif = validar_nif(campos[1])
    if nif is None:
        return None

    tiempo = validar_tiempo(campos[2])
    if tiempo is None:
        return None

    coord = validar_coordenadas(campos[3])
    if coord is None:
        return None

    prod = campos[4]

    precio = validar_precio(campos[5])
    if precio is None:
        return None

    return [tlf, nif, tiempo, coord, prod, precio]
