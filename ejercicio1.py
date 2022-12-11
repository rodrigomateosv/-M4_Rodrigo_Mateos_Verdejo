import pandas as pd  # Importa pandas y usa un alias para poder utilizar sus recursos

def main():
    
    titulos_peliculas = pd.read_csv('imdb_titulos.csv')
  print("Cargando el archivo imdb_titulos.csv...")
    print(titulos_peliculas.head()) 
    elenco = pd.read_csv('imdb_elenco.csv')
    print("Cargando el archivo imdb_elenco.csv...")
print(elenco.head()) 
    print("\n")

    
    print("Mostrar el número de registros del dataframe de titulos: {}".format(len(titulos_peliculas)), "\n", ) 


    print("Mostrar el número de registros del dataframe de elenco: {}.".format(len(elenco)), "\n") 
    print("Mostrar las 5 peliculas más antiguas del listado de titulos", "\n")
    print(titulos_peliculas.sort_values(by='year').head()) 
    print("Mostrar las peliculas que en el titulo tienen la palabra Dracula")
    print(titulos_peliculas[titulos_peliculas['title'].str.contains('Dracula')])  
print("Número de peliculas que coincidan con este requisito: {} coincidencias".format(len(titulos_peliculas[titulos_peliculas['title'].str.contains('Dracula')])), "\n")

   
    print("Mostrar los 10 titulos más comunes")
    print(titulos_peliculas['title'].value_counts().head(10)) 
    print("Mostrar cual fue la primer pelicula hecha titulada 'Romeo and Juliet'")
    print(titulos_peliculas[titulos_peliculas['title'] == 'Romeo and Juliet'].sort_values(by='year').head(1)) 
    print("Listar todas las peliculas que contengan la palabra 'Exorcist' ordenadas de la más vieja a la más reciente","\n",titulos_peliculas[titulos_peliculas['title'].str.contains('Exorcist')].sort_values(by='year')) 
    print("Mostrar cuantas peliculas fueron hechas en el año 1950: {} peliculas".format(len(titulos_peliculas[titulos_peliculas['year'] == 1950])),"\n") 

    
    print("Mostrar cuantas peliculas fueron hechas de 1950 a 1959: {} peliculas".format(len(titulos_peliculas[(titulos_peliculas['year'] >= 1950) & (titulos_peliculas['year'] <= 1959)])),"\n") .
 
    print("Mostrar todos los roles o papeles que hubo en la pelicula 'The Godfather'","\n",elenco[elenco['title'] == 'The Godfather'], "\n") 
    print("Número de coincidencias: {} coincidencias".format(len(elenco[elenco['title'] == 'The Godfather'])), "\n") 
    print("Mostrar el elenco completo ordenado por la clasificacion 'n' de la pelicula 'Dracula' de 1958","\n",elenco[(elenco['title'] == 'Dracula') & (elenco['year'] == 1958)].sort_values(by='year'), "\n") 
    print("Mostrar cuantos papeles de 'Bruce Wayne' han sido hechos en la historia de las peliculas: {} papeles".format(len(elenco[elenco['character'] == 'Bruce Wayne'])), "\n") 
    print("Mostrar cuantos papeles ha hecho 'Robert De Niro' en su carrera: {} papeles".format(len(elenco[elenco['name'] == 'Robert De Niro'])), "\n") 
    print("Listado de papeles como protagonista (n=1) que tuvo el actor 'Charlton Heston' en la década de los 60's, ordenado por año de forma descendente","\n",elenco[(elenco['name'] == 'Charlton Heston') & (elenco['n'] == 1) & (elenco['year'] >= 1960) & (elenco['year'] <= 1969)].sort_values(by='year', ascending=False), "\n") 
    print("Mostrar cuantos papeles para actores hubo en la década de los 50's: {} papeles".format(len(elenco[(elenco['type'] == 'actor') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)])),"\n") 
    print("Mostrar cuantos papeles para actrices hubo en la década de los 50's: {} papeles.".format(len(elenco[(elenco['type'] == 'actress') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)])),"\n") 
    return None

if _name_ == '_main_':
    main()
