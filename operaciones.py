import math

def multiplicacion(a,b):
    resultado = a * b
    return resultado

def division (a,b):
    resultado = a /b
    return resultado

def multiplicacion(a,b):
    resultado = a * b
    return resultado

def division (a,b):
    resultado = a /b
    return resultado

def potencia(base, exponente):
    """
    Retorna el resultado de elevar un número (base) a una potencia (exponente).
    """
    return math.pow(base, exponente)

def raiz_cuadrada(n):
    """
    Retorna la raíz cuadrada de un número 'n'.
    Valida que el número no sea negativo para evitar errores matemáticos.
    """
    if n < 0:
        raise ValueError("El número no puede ser negativo para calcular la raíz cuadrada.")
    
    return math.sqrt(n)

