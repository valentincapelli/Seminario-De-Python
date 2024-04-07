# 6. Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una
# con los número pares y otras con los que son impares. Imprima las listas al terminar de
# procesarlas.

lista = range(20)
lista_pares = []
lista_impares = []

for i in lista:
    if (i % 2 == 0):
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print('La lista de numeros pares es la siguiente')
for i in lista_pares:
    print(i)
    
print('--------------------------------------------')

print('La lista de numeros impares es la siguiente')
for i in lista_impares:
    print(i)