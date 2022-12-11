import pandas as pd  # Importa pandas y usa un alias para poder utilizar sus recursos

def main():
    # Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
    titulos_peliculas = pd.read_csv('imdb_titulos.csv')
  print("Cargando el archivo imdb_titulos.csv...")
    print(titulos_peliculas.head()) #head() devuelve los 5 primeros registros del dataframe
 # Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
    elenco = pd.read_csv('imdb_elenco.csv')
    print("Cargando el archivo imdb_elenco.csv...")
print(elenco.head()) #head() devuelve los 5 primeros registros del dataframe por defecto pero es modificable mediante el parámetro "n"
    print("\n")

    #Mostrar el número de registros del dataframe de titulos
    print("Mostrar el número de registros del dataframe de titulos: {}".format(len(titulos_peliculas)), "\n", ) #len() devuelve el número de registros del dataframe.


    #Mostrar el número de registros del dataframe de elenco
    print("Mostrar el número de registros del dataframe de elenco: {}.".format(len(elenco)), "\n") #len() devuelve el número de registros del dataframe.
 #Mostrar las 5 peliculas más antiguas del listado de titulos
    print("Mostrar las 5 peliculas más antiguas del listado de titulos", "\n")
    print(titulos_peliculas.sort_values(by='year').head()) #sort_values() ordena los registros del dataframe por el valor de la columna indicada en el parámetro "by"

    #Mostrar las peliculas que en el titulo tienen la palabra "Dracula". También mostrar el número total de peliculas que coincidan con este requisito
    print("Mostrar las peliculas que en el titulo tienen la palabra Dracula")
    print(titulos_peliculas[titulos_peliculas['title'].str.contains('Dracula')])  #str.contains() devuelve la subcadena indicada en el parámetro
print("Número de peliculas que coincidan con este requisito: {} coincidencias".format(len(titulos_peliculas[titulos_peliculas['title'].str.contains('Dracula')])), "\n")

    #Mostrar los 10 titulos más comunes (que más se repiten)
    print("Mostrar los 10 titulos más comunes")
    print(titulos_peliculas['title'].value_counts().head(10)) #value_counts() devuelve un dataframe con los valores de la columna indicada en el parámetro y la cantidad de veces que se repite cada uno
 #Mostrar cual fue la primer pelicula hecha titulada "Romeo and Juliet"
    print("Mostrar cual fue la primer pelicula hecha titulada 'Romeo and Juliet'")
    print(titulos_peliculas[titulos_peliculas['title'] == 'Romeo and Juliet'].sort_values(by='year').head(1)) #sort_values() ordena los registros del dataframe por el valor de la columna indicada en el parámetro "by"
  #Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
    print("Listar todas las peliculas que contengan la palabra 'Exorcist' ordenadas de la más vieja a la más reciente","\n",titulos_peliculas[titulos_peliculas['title'].str.contains('Exorcist')].sort_values(by='year')) #sort_values() ordena los registros del dataframe por el valor de la columna indicada en el parámetro "by"
 #Mostrar cuantas peliculas fueron hechas en el año 1950
    print("Mostrar cuantas peliculas fueron hechas en el año 1950: {} peliculas".format(len(titulos_peliculas[titulos_peliculas['year'] == 1950])),"\n") #len() devuelve el número de registros del dataframe.

    #Mostrar cuantas peliculas fueron hechas de 1950 a 1959
    print("Mostrar cuantas peliculas fueron hechas de 1950 a 1959: {} peliculas".format(len(titulos_peliculas[(titulos_peliculas['year'] >= 1950) & (titulos_peliculas['year'] <= 1959)])),"\n") #len() devuelve el número de registros del dataframe.


