import pandas as pd
from pathlib import  Path

file_route = Path('lagos_arg.csv')
df_lakes = pd.read_csv(file_route)

top_rating = df_lakes.Ubicación.value_counts().tail(3)

title = "Super listado"
print(f"{title.capitalize():-^40}")
print(top_rating)



"""
• (a) Mostrá la ejecución del código y explicá qué hace. ¿De qué tipo es top_rating?¿Qué
contiene?
    a_ top_rating es una lista de tuplas, debido a que hace my_data.items(). Por cada tupla de la lista contiene la provincia 
    y la cantidad de apariencias de esa provincia en el dataset.

• (b) Escribí una solución alternativa usando pandas. Mostrá la ejecución de tu versión y
explicá en detalle qué hace. En esta versión,¿es necesario abrir el archivo con la función
open? ¿Por qué?
    b_ No es necesario hacer el open ya que pd.read_csv(file_route) se encarga de abrir y cerar el archivo internamente.

– (c) Mostrá en tu código algún objeto de tipo dataframe y otro de tipo Series
"""

print(f"Este objeto es de tipo dataframe {type(df_lakes)}")
print(df_lakes)

nombres = df_lakes.Nombre
print(f"Este objeto es de tipo Series {type(nombres)}")
print(nombres)

"""
– (d) ¿De qué manera (usando pandas) podemos obtener la cantidad de filas y columnas
del dataset? Ejemplificá con los objetos mostrados en el inciso anterior.
    d_ Para obtener la cantidad de filas y columnas del dataset, debemos leerlo usando df_lakes = pd.read_csv(file_route)
    y usar la funcion .shape().
"""
print(f"La cantidad de filas del dataset (de tipo dataframe) es {df_lakes.shape[0]} y la cantidad de columnas es {df_lakes.shape[1]}.")

print(f"La cantidad de filas del objeto Series es {nombres.shape[0]}. Tienen una sola columna los objetos Series.")

"""
- (e) En base a tu versión en pandas del código dado, describí al menos dos ventajas del
uso de esta librería sobre el manejo de archivos csv. Si considerás que no las hay, indicá
en qué te basás.

    Una primera ventaja puede ser que no necesitamos hacer uso de la funcion open(), ya que cuando usamos las funciones de read 
    de pandas lo hace implicitamente.
    Una segunda ventaja que le veo es que no tenemos que recorrer fila por fila para filtrar u obtener los datos que necesitamos
    analizar.
    Tambien esta bueno por que tenemos funciones como .describe que  permite obtener los valores de algunos cálculos estadísticos
    básicos, sobre las columnas con datos numéricos. Todo eso en una sola linea de codigo. O tambien dtypes que nos dice el tipo
    de dato que almacena cada columna.
    Con pandas tenemos muchisimas funciones que nos brinda informacion util de los datasets y que nos abstraen de recorrerlos 
    manualmente.

"""

