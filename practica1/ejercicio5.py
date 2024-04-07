# 5. Implementa un programa que solicite al usuario que ingrese una lista de numeros.
# Luego, imprime la lista pero deten la impresion si encuentras un numero negativo.
# Nota: utilice la sentencia break cuando haga falta.

lista = []

for i in range(5):
    lista.append(int(input("Ingresá tu númeroooo: ")))

for i in range(5):
    if (lista[i] >= 0):
        print(lista[i])
    else:
        break