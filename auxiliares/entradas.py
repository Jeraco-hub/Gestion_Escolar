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