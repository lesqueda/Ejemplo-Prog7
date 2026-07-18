historial = []


def agregar_operacion(texto):
    historial.append(texto)


def mostrar_historial():
    if not historial:
        print("\nNo hay operaciones registradas.")
        return

    print("\n--- Historial de operaciones ---")

    for operacion in historial:
        print(operacion)