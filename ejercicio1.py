import pandas as pd  # Importa pandas y usa un alias para poder utilizar sus recursos

def main():
    # Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
    titulos_peliculas = pd.read_csv('imdb_titulos.csv')
  print("Cargando el archivo imdb_titulos.csv...")
    print(titulos_peliculas.head()) #head() devuelve los 5 primeros registros del dataframe
 # Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
    elenco = pd.read_csv('imdb_elenco.csv')
    print("Cargando el archivo imdb_elenco.csv...")

