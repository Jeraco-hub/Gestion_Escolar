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