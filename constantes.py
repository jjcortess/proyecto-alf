import re


FORMATOS_VALIDOS = [1, 2, 3]
TIEMPO_ESTANDAR = 2
COORD_ESTANDAR = 3

LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"
EQUIVALENCIA_NIE = {"X": "0", "Y": "1", "Z": "2"}


NUM_A_MES = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

MES_A_NUM = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}

DIAS_POR_MES = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]




# Expresiones regulares

ER_TLF = re.compile(r"\d{3}-\d{3}-\d{3}")
ER_LIMPIAR_TLF = re.compile(r"[- ]+")
ER_NIF = re.compile(r"(?P<cuerpo>[XYZ]\d{7}|\d{8})-(?P<letra>[TRWAGMYFPDXBNJZSQVHLCKE])")
ER_PRECIO = re.compile(r"(0|[1-9]\d*)(\.\d+)?[€$]")

ER_TIEMPO_F1 = re.compile(r"(?P<anio>\d{4})-(?P<mes>0[1-9]|1[0-2])-(?P<dia>0[1-9]|[12]\d|3[01]) +(?P<hora>[01]\d|2[0-3]):(?P<minuto>[0-5]\d)")
ER_TIEMPO_F2 = re.compile(r"((?i)?P<mes>January|February|March|April|May|June|July|August|September|October|November|December) +(?P<dia>[1-9]|[12]\d|3[01]), +(?P<anio>[1-9]\d{0,3}) +(?P<hora>[1-9]|1[0-2]):(?P<minuto>[0-5]\d) +(?P<ampm>am|pm)")
ER_TIEMPO_F3 = re.compile(r"(?P<hora>[01]\d|2[0-3]):(?P<minuto>[0-5]\d):(?P<segundo>[0-5]\d) +(?P<dia>0[1-9]|[12]\d|3[01])/(?P<mes>0[1-9]|1[0-2])/(?P<anio>\d{4})")

ER_COORD_F1 = re.compile(r"(?P<lat>[+-]?(0|[1-9]\d*)\.\d+) *, *(?P<lon>[+-]?(0|[1-9]\d*)\.\d+)")
ER_COORD_F2 = re.compile(r"(?P<lat_g>0|[1-9]\d?)° *(?P<lat_m>\d|[1-5]\d)' *(?P<lat_s>(\d|[1-5]\d)\.\d{4})\" *(?P<lat_dir>[NS]) *, *(?P<lon_g>0|[1-9]\d{0,2})° *(?P<lon_m>\d|[1-5]\d)' *(?P<lon_s>(\d|[1-5]\d)\.\d{4})\" *(?P<lon_dir>[EW])")
ER_COORD_F3 = re.compile(r"(?P<lat_g>\d{3})(?P<lat_m>[0-5]\d)(?P<lat_s>[0-5]\d\.\d{4})(?P<lat_dir>[NS])(?P<lon_g>\d{3})(?P<lon_m>[0-5]\d)(?P<lon_s>[0-5]\d\.\d{4})(?P<lon_dir>[EW])")