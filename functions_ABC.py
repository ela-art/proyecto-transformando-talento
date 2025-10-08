
#importación de librerias necesarias para la manipulación del DF

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer  # Habilita IterativeImputer
from sklearn.impute import IterativeImputer

'''Lectura de archivo, enviar solo el nombre del fichero de esta manera:
    'fichero.csv'
'''
def leer_data(fichero):
    df = pd.read_csv(fichero,index_col=0)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    return df




def eda_(df):
    print("🔍 Primeras filas del DataFrame:")
    print(df.head(3))

    print("📐 Dimensiones:")
    print(df.shape , "\n")

    print("🧠 Información general:")
    print(df.info())

    print("📊 Tipos de datos por columna:")
    print(df.dtypes, "\n")

    print("📉 Descripción de columnas numéricas:")
    print(df.describe())

    print("🔤 Descripción de columnas categóricas:")
    print(df.describe(include=['O']))


    print("🚫 Valores nulos por columna:")
    print(df.isnull().sum())

    print("📎 Filas duplicadas:")
    dup_count = df.duplicated().sum()
    print(f"Duplicadas: {dup_count}")
    if dup_count > 0:
        print("Ejemplo de duplicados:")
        print(df[df.duplicated()].head(), "\n")
    else:
        print("No hay filas duplicadas.\n")


def transformation(df):

    df = df.copy()
    #Todas las casillas del archivo Jupyter va a ir dentro de esta función
    df[df['employeenumber'].duplicated(keep=False)]
    df = df.drop_duplicates()

    #Tratar columna age
    if 'datebirth' in df.columns:
        df['age'] = 2025 - df['datebirth']

    if 'businesstravel' in df.columns:
        df['businesstravel'] = df['businesstravel'].fillna('Unknown')

    #Dailyrate, se consideró eliminarlo
    df = df.drop('department', axis=1)

    #Distance from home, se rellena con la mediana para que no afecte en exceso
    df.loc[df['distancefromhome'] < 0, 'distancefromhome'] = np.nan
    df['distancefromhome'] = df['distancefromhome'].astype('Int64')
    df['distancefromhome'] = df['distancefromhome'].fillna(df['distancefromhome'].median())

    #educationrate: se aplica la moda.
    df['educationfield']= df['educationfield'].fillna(df['educationfield'].mode()[0])

    #No sirve para ID, se considera eliminar
    df = df.drop('employeecount', axis=1)

    # nvironmentSatisfaction
    # Verificar que los valores estén en el rango 1–4.
    # Corregir valores fuera de rango (ejemplo: 49).
    # Confirmar tipo int64.
    #Revisar duplicados (ok si se repiten)

    df["environmentsatisfaction"] = df["environmentsatisfaction"].astype(str).str[0].astype(int)

    #Columa Gender: unificar
    df["gender"] = df["gender"].astype(str).str.strip()
    gen = {'0': "M", '1': "F"}
    df['gender'] = df['gender'].map(gen)

    #Hourly Rate
    #Se considera eliminar
    df.drop("hourlyrate", axis=1, inplace=True)

    # Columa Jobrole, poner bonitos los datos a title
    df["jobrole"] = df["jobrole"].str.title()

    # JobSatisfaction
    #- Revisar que los valores estén en el rango 1–4. Ok
    #- Confirmar tipo int64. Ok

    # MaritalStatus
    #Normalizar texto con .str.title().
    #Alto % de nulos : nueva categoria: Unknown'
    df["maritalstatus"] = df["maritalstatus"].replace("Marreid", "Married")
    df["maritalstatus"] = df["maritalstatus"].replace(np.nan, "Unknown") #Habia varios tipos de nulos y tuve que eliminarlo de estas dos formas.
    df["maritalstatus"] = df["maritalstatus"].replace("nan", "Unknown")
    df["maritalstatus"] = df["maritalstatus"].str.title()

    #MonthlyIncome
    #Limpiar símbolos y comas, convertir a float
    #Rellenar nulos con media/mediana o estimación (Salary ÷ 12)
    df['monthlyincome'] = df['monthlyincome'].astype(str).str.replace("$", "")
    df["monthlyincome"] = df["monthlyincome"].astype(str).str.replace(",", ".").astype(float)
    df['monthlyincome'] = df['monthlyincome'].astype(float)


    #columnas 21-30
    df.rename(columns = {'numcompaniesworked':'numero_empresas_anteriores'}, inplace =True)
    ## columna over18 -> eliminar
    df.drop('over18', axis=1, inplace=True)
    ## columna 23
    #Elimnar 41% nulos------pasados a la categoria 'unknow'
    df.rename(columns = {'overtime': 'horas_extra'}, inplace =True)
    df['horas_extra'] = df['horas_extra'].fillna('Unknown')# si despues hacemos unique tiene que aparecer la nueva columna unknown


    df.rename(columns = {'percentsalaryhike':'incremento_salario'}, inplace =True)

    ## columna 25
    df.rename(columns = {'performancerating':'nivel_trabajo'}, inplace =True)

    #pasamos el dato a int64 para no tener problemas con los nulos
    df['nivel_trabajo']= df['nivel_trabajo'].astype(str).str.replace(',', '.', regex = False)
    df['nivel_trabajo'] = pd.to_numeric(df['nivel_trabajo'], errors='coerce')
    df['nivel_trabajo']= df['nivel_trabajo'].astype('Int64')
    # bajo % nulos, y categoria dominante 3, imputamos por la moda
    df['nivel_trabajo'] = df['nivel_trabajo'].fillna(df['nivel_trabajo'].mode()[0]) 

    ##columna 26
    df.rename(columns = {'relationshipsatisfaction':'satisfaccion_relaciones_interpersonales'}, inplace =True)

    ##columna 27
    df.rename(columns = {'standardhours':'clasificacion_jornada'}, inplace =True)

    #como son muchos nulos, creamos una nueva categoria
    df['clasificacion_jornada'] = df['clasificacion_jornada'].fillna('Unknown')# si despues hacemos unique tiene que aparecer la nueva columna unknown

    #columna28
    df.rename(columns = {'stockoptionlevel':'acciones_asignadas'}, inplace= True)
    #finalmente,vemos que la columna no aporta info util y la borramos
    df.drop('acciones_asignadas', axis=1, inplace=True)

    ##columna 29
    df.rename(columns = {'totalworkingyears':'años_experiencia'}, inplace =True)
    
    #pasamos el dato a int64 para no tener problema con los nulos
    df['años_experiencia']= df['años_experiencia'].astype(str).str.replace(',', '.', regex = False)
    df['años_experiencia'] = pd.to_numeric(df['años_experiencia'], errors='coerce')
    df['años_experiencia']= df['años_experiencia'].astype('Int64')

    #IterativeImputer
    #imputer_iter = IterativeImputer(max_iter = 100, random_state = 42)
    imputer_iter = IterativeImputer(max_iter = 100, random_state = 42)
    df['años_experiencia'] = imputer_iter.fit_transform(df[['años_experiencia']])
    df['años_experiencia'] = df['años_experiencia'].round(2)    

    ##columna 30
    df.rename(columns = {'trainingtimeslastyear':'cursos'}, inplace =True)


    #Conciliación
    df['worklifebalance'] = df['worklifebalance'].str.replace(',0','')
    dic = {'1':'Mal', '2':'Medio', '3':'Alto', '4':'Muy alto'}
    df['worklifebalance'] = df['worklifebalance'].map(dic).fillna("Unknown")

    #Columnas llenas de nulos, imposible tratar
    df = df.drop('yearsincurrentrole', axis = 1)
    df = df.drop('numberchildren', axis=1)
    df = df.drop('roledepartament', axis=1)

    #Salario anual
    #Imputación de nulos
    df['salary'] = df['salary'].str.replace('$', '')
    df['salary'] = df['salary'].str.replace(',', '.').astype(float)
    imputer_salary = IterativeImputer(max_iter = 100, random_state = 42)
    df['salary'] = imputer_salary.fit_transform(df[['salary']]).round(2)


    #remote 
    #Pide Yes o No
    #unificación con .map

    df['remotework'].value_counts()
    dic_yes = {'1':'Yes','True':'Yes','False':'No','0':'No','Yes':'Yes'}
    df['remotework'] = df['remotework'].map(dic_yes)

    #Se bora, alto nivel de nulos
    df = df.drop('sameasmonthlyincome', axis=1)
    df = df.drop('monthlyincome', axis=1)
    df = df.drop('monthlyrate', axis=1)
    df = df.drop('dailyrate', axis=1)
    df['salary_month'] = (df['salary'] / 12).round(2)
    df = df.drop('datebirth', axis=1)

    #Establecer un indice
    df = df.set_index("employeenumber")


    return df


import pandas as pd

def guardar_archivo_csv(df):
    print('entra en la creación')
    try:
        df.to_csv('hr_tratado.csv',  encoding='utf-8')
        print("Archivo 'hr_tratado.csv' creado con éxito.")
    # Creación del fichero con la limpieza y el tratamiento de nulos aplicado.
    except:
        print("No se ha podido crear el archivo")
    print('sale de la creación') 




