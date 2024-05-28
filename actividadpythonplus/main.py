from collections import Counter
import csv

def my_function(file_name, n=10):
    with open(file_name, encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        artists = Counter(map(lambda x: x[0], reader))
        return artists.most_common(n)

try:
    my_songs = my_function('songs_normalize.csv')
except FileNotFoundError:
    print("Tenemos un problema!!")
finally:
    for song in my_songs:
        print(song)

"""
1_ El codigo tal cual esta intenta ejecutar my_function, la cual retorna el nombre de los 10 artistas o bandas mas 
comunes del archivo y su respectiva cantidad en una lista de tuplas. Si my_function no encuentra el archivo
de la ruta pasada como parametro se imprime "Tenemos un problema!!". Y por ultimo, ya pase lo que pase, recorre la
lista que devolvio my_function e imprime cada tupla de la lista. Tener en cuenta que si se ejecuto
el except esto ultimo no funcionaria.

b_ La funcion my_function se puede ejecutar con 1 solo parametro obligatorio, que seria la ruta del archivo a 
abrir. Y tambien se puede pasarle un parametro opcional el cual podes indicarle que top de artistas mas comunes
queres que te devuelva. Si no le pasas el parametro opcional devolvera el top 10 como la funcion original. Si al
parametro adicional le pasas 5, te devuelve el top 5 mas comun.

c_ Para que no se provoque una excepcion al ejecutar la funcion open el archivo debe estar ubicado en la misma 
carpeta donde se encuentra el codigo ejecutandose. Es decir en la misma carpeta deberiamos tener el archivo .csv
y el programa archivo .py.
    Si el archivo si se encuentra en la misma carpeta, el programa tampoco anda, esto es por que cuando abrimos el
archivo .csv este contiene caracteres que no pueden ser codificados con el codec que tenemos como predeterminado.
La solucion para esto que especificar como parametro en la funcion open el tipo de codec al abrir el archivo. En este
caso yo utilice "utf-8".

d_ Usaria en la function my_function un try para abrir el archivo y hacer lo que tiene que hacer, y le pondria un
except IOError: print('El formato del archivo no es correcto')

e_ La variable my_songs es de tipo lista.
    Como my_songs esta definida dentro del try, si ocurre una excepcion no se definiria esta variable, entonces
mas adelante en el codigo no estaria definida tampoco. En caso de que si se ejecute my_function, podremos acceder
a ella, si queremos recorrerla y acceder a su contenido podemos usar un for each, como en el codigo dado.
"""