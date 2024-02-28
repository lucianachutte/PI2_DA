import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

def verificar_tipo_datos(df):
    '''
    Realiza un análisis de los tipos de datos y la presencia de valores nulos en un DataFrame.

    Esta función toma un DataFrame como entrada y devuelve un resumen que incluye información sobre
    los tipos de datos en cada columna, el porcentaje de valores no nulos y nulos, así como la
    cantidad de valores nulos por columna.

    Parameters:
        df (pandas.DataFrame): El DataFrame que se va a analizar.

    Returns:
        pandas.DataFrame: Un DataFrame que contiene el resumen de cada columna, incluyendo:
        - 'nombre': Nombre de cada columna.
        - 'tipo_datos': Tipos de datos únicos presentes en cada columna.
        - 'porcentaje_no_nulos': Porcentaje de valores no nulos en cada columna.
        - 'porcentaje_nulos': Porcentaje de valores nulos en cada columna.
        - 'nulos': Cantidad de valores nulos en cada columna.
    '''

    mi_dict = {"nombre": [], "tipo_datos": [], "porcentaje_no_nulos": [], "porcentaje_nulos": [], "nulos": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        mi_dict["nombre"].append(columna)
        mi_dict["tipo_datos"].append(df[columna].apply(type).unique())
        mi_dict["porcentaje_no_nulos"].append(round(porcentaje_no_nulos, 2))
        mi_dict["porcentaje_nulos"].append(round(100-porcentaje_no_nulos, 2))
        mi_dict["nulos"].append(df[columna].isnull().sum())

    df_info = pd.DataFrame(mi_dict)
        
    return df_info


def filas_duplicadas(dataframe):
    """
    Verifica si hay filas duplicadas en un DataFrame de Pandas.

    Parameters:
    - dataframe (pd.DataFrame): El DataFrame que se va a verificar.

    Returns:
    - bool: True si hay al menos una fila duplicada, False si no hay filas duplicadas.
    """
    
    dataframe = dataframe.applymap(lambda x: tuple(x) if isinstance(x, list) else x)
    
   
    duplicados = dataframe.duplicated()
    
    return any(duplicados)

def duplicados_por_columna(df, columna):
    
    """
    Encuentra y muestra las filas duplicadas en un DataFrame de Pandas basándose en una columna específica.

    Parameters:
    - df (pd.DataFrame): El DataFrame en el que buscar filas duplicadas.
    - columna (str): El nombre de la columna sobre la cual basar la búsqueda de duplicados.

    Returns:
    - pd.DataFrame o str: Si hay filas duplicadas, devuelve un DataFrame ordenado que contiene esas filas.
      Si no hay duplicados, devuelve el mensaje "No hay duplicados".
    """
   
    # Se filtran las filas duplicadas
    duplicacion_de_filas = df[df.duplicated(subset=columna, keep=False)]
    if duplicacion_de_filas.empty:
        return "No hay duplicados"
    
    # Se ordenan dichas filas y se comparan
    filas_duplicadas_ordenadas = duplicacion_de_filas.sort_values(by=columna)
    return filas_duplicadas_ordenadas

def convertir_a_time(x):
    if isinstance(x, str):
        try:
            return datetime.strptime(x, "%H:%M:%S").time()
        except ValueError:
            return None
    elif isinstance(x, datetime):
        return x.time()
    return x


def imputa_valor_frecuente(df, columna):
    '''
    Imputa los valores faltantes en una columna de un DataFrame con el valor más frecuente.

    Esta función reemplaza los valores "SD" con NaN en la columna especificada,
    luego calcula el valor más frecuente en esa columna y utiliza ese valor
    para imputar los valores faltantes (NaN).

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene la columna a ser imputada.
        columna (str): El nombre de la columna en la que se realizará la imputación.

    Returns:
        None
    '''
    # Se reemplaza "SD" con NaN en la columna
    df[columna] = df[columna].replace('SD', pd.NA)

    # Se calcula el valor más frecuente en la columna
    valor_mas_frecuente = df[columna].mode().iloc[0]
    print(f'El valor mas frecuente es: {valor_mas_frecuente}')

    # Se imputan los valores NaN con el valor más frecuente
    df[columna].fillna(valor_mas_frecuente, inplace=True)

def imputa_edad_media_segun_sexo(df):
    '''
    Imputa valores faltantes en la columna 'Edad' utilizando la edad promedio según el género.

    Esta función reemplaza los valores "SD" con NaN en la columna 'Edad', calcula la edad promedio
    para cada grupo de género (Femenino y Masculino), imprime los promedios calculados y
    luego llena los valores faltantes en la columna 'Edad' utilizando el promedio correspondiente
    al género al que pertenece cada fila en el DataFrame.

    Parameters:
        df (pandas.DataFrame): El DataFrame que contiene la columna 'Edad' a ser imputada.

    Returns:
        None
    '''
    
    # Se reemplaza "SD" con NaN en la columna 'edad'
    df['EDAD'] = df['EDAD'].replace('SD', pd.NA)

    # Se calcula el promedio de edad para cada grupo de género
    promedio_por_genero = df.groupby('SEXO')['EDAD'].mean()
    print(f'La edad promedio de Femenino es {round(promedio_por_genero["FEMENINO"])} y de Masculino es {round(promedio_por_genero["MASCULINO"])}')

    # Se llenan los valores NaN en la columna 'edad' utilizando el promedio correspondiente al género
    df['EDAD'] = df.apply(lambda row: promedio_por_genero[row['SEXO']] if pd.isna(row['EDAD']) else row['EDAD'], axis=1)

    # Se convierte a tipo float para manejar NaN e infinitos
    df['EDAD'] = df['EDAD'].astype(float)

    # Se redondean los valores finitos a tipo entero