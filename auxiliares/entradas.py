from auxiliares.validaciones import validar_largo_string


def pedir_texto(etiqueta, largo, opcional=False):
    while True:
        ingresado = input(etiqueta).strip()
        if ingresado == '':
            if opcional:
                return ''
            print('Este dato es obligatorio, ingrese nuevamente...\n')
            continue
        valor, mensaje = validar_largo_string(ingresado, largo)
        if valor != '':
            return valor
        print(mensaje)


def pedir_entero(etiqueta, opcional=False, minimo=1):
    while True:
        entrada = input(etiqueta).strip()
        if entrada == '':
            if opcional:
                return None
            print('Este dato es obligatorio, ingrese nuevamente...\n')
            continue
        if entrada.isdecimal() and int(entrada) >= minimo:
            return int(entrada)
        print(f'Ingrese un número entero mayor o igual a {minimo}.\n')

def pedir_nota(etiqueta, opcional=False):
    while True:
        entrada = input(etiqueta).strip().replace(',', '.')
        if entrada == '':
            if opcional:
                return None
            print('Este dato es obligatorio, ingrese nuevamente...\n')
            continue
        try:
            nota = float(entrada)
        except ValueError:
            print('Ingrese un número válido (ej: 5.5).\n')
            continue
        if 1.0 <= nota <= 7.0:
            return round(nota, 1)
        print('La nota debe estar entre 1.0 y 7.0.\n')

from datetime import datetime


def pedir_fecha(etiqueta, opcional=False):
    while True:
        entrada = input(etiqueta).strip()
        if entrada == '':
            if opcional:
                return None
            print('Este dato es obligatorio, ingrese nuevamente...\n')
            continue
        try:
            return datetime.strptime(entrada, '%d-%m-%Y').date()
        except ValueError:
            print('Ingrese una fecha válida con formato DD-MM-AAAA (ej: 15-06-2026).\n')


def pedir_ponderacion(etiqueta, opcional=False):
    while True:
        entrada = input(etiqueta).strip().replace(',', '.')
        if entrada == '':
            if opcional:
                return None
            print('Este dato es obligatorio, ingrese nuevamente...\n')
            continue
        try:
            valor = float(entrada)
        except ValueError:
            print('Ingrese un número válido (ej: 30).\n')
            continue
        if 0 < valor <= 100:
            return round(valor, 1)
        print('La ponderación debe estar entre 1 y 100.\n')