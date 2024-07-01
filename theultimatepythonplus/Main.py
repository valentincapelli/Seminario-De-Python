def double(x):
    return x*2

numbers = [1, 2, 3, 4]
print("Usando def")
for elem in numbers:    
    print(double(elem), end=" ")
    
print('\n')
# ------------------ Usando lamba para este caso no es la mejor opcion ---------------------------------- #

duplicated_numbers = map(lambda x: x*2, numbers)
print("Usando lambda")
for elem in duplicated_numbers:
    print(elem, end=" ")

print('\n')
# -----------------Mejor usarlo de esta manera ----------------------------------- #

doubles = [2*x for x in numbers]
#doubles = map(lambda x: 2*x, numbers)
print("Sin usar def ni lambda")
for elem in doubles:
    print(elem, end=" ")
