
from operaciones import suma
from operaciones import resta
from operaciones import multiplicacion
from operaciones import division
from operaciones import potencia
from operaciones import raiz_cuadrada
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

    a = int(input("Agregar valor 1"))

    b = int(input("agregar valor 2"))

    if opcion == "1":
        suma(a,b)

    elif opcion == "2":
        resta(a,b)

    elif opcion == "3":
        multiplicacion(a,b)

    elif opcion == "4":
        division(a,b)

    elif opcion == "5":
        potencia(a,b)

    elif opcion == "6":
        raiz_cuadrada(a)

    elif opcion == "7":
        ver_historial()

    elif opcion == "8":
        print("Gracias por usar la calculadora.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

print("Hello World - Equipo")
