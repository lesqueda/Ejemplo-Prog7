from operaciones import (
    suma,
    resta,
    multiplicacion,
    division,
    potencia,
    raiz_cuadrada
)

from historial import agregar_operacion, mostrar_historial
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

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Debe ingresar un número del 1 al 8.")
        continue

    if opcion == 1:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = suma(a, b)
        print("Resultado:", resultado)
        agregar_operacion(f"{a} + {b} = {resultado}")

    elif opcion == 2:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = resta(a, b)
        print("Resultado:", resultado)
        agregar_operacion(f"{a} - {b} = {resultado}")

    elif opcion == 3:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = multiplicacion(a, b)
        print("Resultado:", resultado)
        agregar_operacion(f"{a} * {b} = {resultado}")

    elif opcion == 4:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if b == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            resultado = division(a, b)
            print("Resultado:", resultado)
            agregar_operacion(f"{a} / {b} = {resultado}")

    elif opcion == 5:
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        resultado = potencia(base, exponente)
        print("Resultado:", resultado)
        agregar_operacion(f"{base}^{exponente} = {resultado}")
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

    elif opcion == 6:
        numero = float(input("Ingrese un número: "))

        try:
            resultado = raiz_cuadrada(numero)
            print("Resultado:", resultado)
            agregar_operacion(f"√{numero} = {resultado}")
        except ValueError as e:
            print(e)

    elif opcion == 7:
        mostrar_historial()

    elif opcion == 8:
        print("Gracias por usar la calculadora.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
