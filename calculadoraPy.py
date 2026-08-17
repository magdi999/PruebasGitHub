def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b == 0:
        raise ZeroDivisionError("no existe la division por cero")
    return a/b

def potencia(a,b):
    return a**b
