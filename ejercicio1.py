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

