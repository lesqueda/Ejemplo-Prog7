
from suma import sumar
from resta import restar
from multiplicacion import multiplicar
from division import dividir
from potencia import potencia
from raiz import raiz_cuadrada
from historial import agregar_operacion, ver_historial

while True:
    print("\n===== CALCULADORA =====")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Ver historial")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        sumar()

    elif opcion == "2":
        restar()

    elif opcion == "3":
        multiplicar()

    elif opcion == "4":
        dividir()

    elif opcion == "5":
        potencia()

    elif opcion == "6":
        raiz_cuadrada()

    elif opcion == "7":
        ver_historial()

    elif opcion == "8":
        print("Gracias por usar la calculadora.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

