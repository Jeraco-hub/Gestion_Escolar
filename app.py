from presentacion import cargar_menu
from presentacion.presentacion_login import iniciar_sesion

if __name__ == '__main__':
    usuario = iniciar_sesion()
    if usuario:
        cargar_menu()