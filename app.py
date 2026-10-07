from presentacion import cargar_menu
from datos.repositorios.repo_direccion import listado_direcciones
from prettytable import PrettyTable

def main():
    cargar_menu()

    # Probar que el repositorio y la BD funcionan con PrettyTable
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Calle", "Número", "Comuna", "Ciudad"]

    direcciones = listado_direcciones()
    if direcciones:
        for d in direcciones:
            tabla.add_row([d.id_direccion, d.calle, d.numero, d.comuna, d.ciudad])
        print("\n--- Direcciones Registradas ---")
        print(tabla)
    else:
        print("\nNo hay direcciones registradas o no se pudo conectar.")

if __name__ == '__main__':
    main()