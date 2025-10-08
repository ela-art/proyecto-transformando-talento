import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer  # Habilita IterativeImputer
from sklearn.impute import IterativeImputer
from sklearn.utils import resample




def correlacion(df):
    """
    Genera un mapa de calor que muestra la correlación entre las variables numéricas del DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos.
    
    Retorna:
    None: Muestra un mapa de calor de correlación.
    """
    corr = df.select_dtypes(include=['number']).corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    plt.figure(figsize=(5, 5))  # Tamaño de la figura
    sns.heatmap(corr, cmap='OrRd', linewidths=0.5, mask = mask) #grosor linea
    # Título
    plt.title("")
    # Mostrar la gráfica
    plt.show()

def edad(df):
    """
    Genera un histograma que muestra la distribución de la variable 'edad' en el DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos.
    
    Retorna:
    None: Muestra un histograma de la variable 'edad'.
    
    """
    plt.figure(figsize=(5, 5))  # Tamaño de la figura
    sns.histplot(df['edad'], bins=10, kde=True, color='blue')  # Histograma con línea KDE
    plt.title('Distribución de Edad')  # Título del gráfico
    plt.xlabel('Edad')  # Etiqueta del eje x
    plt.ylabel('Frecuencia')  # Etiqueta del eje y
    plt.show()  # Mostrar la gráfica    


    df_yes = df[df['attrition']=="Yes"]
    df_no = df[df['attrition']=="No"]


    
    plt.hist(df_yes['age'], bins=12, color="lightblue", edgecolor='black')
    plt.axvline(round(df_yes['age'].mean()), color='red', linestyle='--', label=f"Media: {round(df_yes['age'].mean())}")
    plt.grid(True)
    plt.show();


def genero(df):
    """
    Genera un gráfico de barras que muestra la distribución de la variable 'genero' en el DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos.
    
    Retorna:
    None: Muestra un gráfico de barras de la variable 'genero'.
    
    """
    df_yes = df[df['attrition']=="Yes"]
    plt.figure(figsize=(5, 5))  # Tamaño de la figura
    sns.countplot(x='genero', data=df_yes, palette='pastel')  # Gráfico de barras
    plt.title('Distribución de Género')  # Título del gráfico
    plt.xlabel('Género')  # Etiqueta del eje x
    plt.ylabel('Frecuencia')  # Etiqueta del eje y
    plt.show()  # Mostrar la gráficaº


def nivel_estudios(df):
    """
    Genera un gráfico de barras que muestra la distribución de la variable 'nivel_estudios' en el DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos.
    
    Retorna:
    None: Muestra un gráfico de barras de la variable 'nivel_estudios'.
    
    """
    df_yes = df[df['attrition']=="Yes"]
    valores = df_yes['education'].value_counts()
    categorias = valores.index
    plt.pie(valores, labels=categorias, autopct='%1.0f%%',colors=['c', 'lightblue', 'skyblue'])
    plt.title("Distribución del Nivel de Educación")
    plt.show()


def estado_civil(df):   
    """
    Genera un gráfico de barras que muestra la distribución de la variable 'estado_civil' en el DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos.
    
    Retorna:
    None: Muestra un gráfico de barras de la variable 'estado_civil'.
    
    """
    df_yes = df[df['attrition']=="Yes"]
    valores = df_yes['marital_status'].value_counts()
    colores_ocre = ['#C19A6B', '#D2B48C', '#DEB887', '#F5DEB3', '#EED8AE']
    categorias = valores.index
    plt.pie(valores, labels=categorias, autopct='%1.0f%%',colors=colores_ocre, wedgeprops={'edgecolor': 'white'})
    plt.title("Distribución estado")
    plt.show()



def remote(df):   
    """
    Genera un gráfico de barras que muestra la distribución de la variable 'remote_work' en el DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos.
    
    Retorna:
    None: Muestra un gráfico de barras de la variable 'remote_work'.
    
    """
    df_yes = df[df['attrition']=="Yes"]
    valores = df_yes['remote_work'].value_counts()
    colores_azul = ['#ADD8E6', '#87CEEB', '#4682B4', '#5F9EA0', '#B0C4DE']
    categorias = valores.index
    plt.pie(valores, labels=categorias, autopct='%1.0f%%',colors=colores_azul, wedgeprops={'edgecolor': 'white'})
    plt.title("Distribución remote work")
    plt.show()   

    
def distancia(df):   
    """
    Genera un histograma que muestra la distribución de la variable 'distancia' en el DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos.
    
    Retorna:
    None: Muestra un histograma de la variable 'distancia'.
    
    """
    df_yes = df[df['attrition']=="Yes"]
    plt.hist(df_yes['distancefromhome'], bins=12, color="#C19A6B", edgecolor='black')
    plt.title("Distancia desde casa empleados que se ahn ido", fontsize=14, fontweight='bold')
    plt.xlabel("Distancia")
    plt.ylabel("Frecuencia")
    plt.show()

    plt.hist(df['distancefromhome'], bins=12, color="#C19A6B", edgecolor='black')
    plt.title("Distancia desde casa trabajadores", fontsize=14, fontweight='bold')
    plt.xlabel("Distancia")
    plt.ylabel("Frecuencia")
    plt.show()

def jobrole(df):
    """
    Genera un gráfico de barras que muestra la distribución de la variable 'jobrole' en el DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos.
    
    Retorna:
    None: Muestra un gráfico de barras de la variable 'jobrole'.
    
    """
    df_yes = df[df['attrition']=="Yes"]
    valores = df_yes['jobrole'].value_counts()
    categorias = valores.index
    plt.figure(figsize=(10, 6))  # Tamaño de la figura
    plt.pie(valores, labels=categorias, autopct='%1.0f%%',colors=["#EBDD72", "#CDA75B", "#E18D18", "#E47A1D", "#E8CE66"])
    plt.title("Distribución de jobrole")
    plt.show()


def joblevel(df):
    """
    Genera un gráfico de barras que muestra la distribución de la variable 'joblevel' en el DataFrame.
    
    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos.
    
    Retorna:
    None: Muestra un gráfico de barras de la variable 'joblevel'.
    
    """
    df_yes = df[df['attrition']=="Yes"]
    valores = df_yes['joblevel'].value_counts()
    categorias = valores.index
    plt.figure(figsize=(8, 5))  # Tamaño de la figura
    plt.pie(valores, labels=categorias, autopct='%1.0f%%',colors=["#EBDD72", "#CDA75B", "#E18D18", "#E47A1D", "#E8CE66"])
    plt.title("Distribución de joblevel")
    plt.show()

def antiguedad(df):
    df_yes = df[df['attrition']=="Yes"]
    valores = df_yes['joblevel'].value_counts()
    plt.hist(df_yes['yearsatcompany'], bins=12, color="salmon", edgecolor='black')
    plt.axvline(round(df_yes['yearsatcompany'].mean()), color='red', linestyle='--', label=f"Media: {round(df_yes['yearsatcompany'].mean())}")
    plt.grid(True)
    plt.show();    
    
    
def BoxPlotSalaryAttrition(df):
    """
    Genera un boxplot que compara la columna 'salary_month' según la columna 'attrition'.

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'attrition' y 'salary_month'.

    Retorna:
    None
    """
    sns.boxplot(data=df, x="attrition", y="salary_month")
    plt.title("Salario mensual según Attrition")
    plt.show()
    
def BoxPlotAgeYearsAttrition(df):
    """
    Genera dos boxplots que comparan las columnas 'age' y 'yearsatcompany' según la columna 'attrition'.

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'attrition', 'age' y 'yearsatcompany'.

    Retorna:
    None
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    sns.boxplot(data=df, x="attrition", y="age", ax=axes[0])
    axes[0].set_title("Edad según Attrition")

    sns.boxplot(data=df, x="attrition", y="yearsatcompany", ax=axes[1])
    axes[1].set_title("Años en la compañía según Attrition")

    plt.tight_layout()
    plt.show()

def BarPlotSalaryAttrition(df):
    """
    Genera un gráfico de barras que compara la columna 'salary' según la columna 'attrition'.

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'attrition' y 'salary'.

    Retorna:
    None
    """
    df_melt = df.melt(
        id_vars="attrition",
        value_vars=["salary"],
        var_name="Variable",
        value_name="Valor"
    )

    sns.barplot(data=df_melt, x="Variable", y="Valor", hue="attrition", ci=None)
    plt.title("Promedios por Attrition")
    plt.show()

def ScatterYearsPromotionAttrition(df):
    """
    Genera un diagrama de dispersión que compara 'yearsatcompany' con 
    'yearssincelastpromotion' según la columna 'attrition'.

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'yearsatcompany', 'yearssincelastpromotion' y 'attrition'.

    Retorna:
    None
    """
    sns.scatterplot(
        data=df,
        x="yearsatcompany",
        y="yearssincelastpromotion",
        hue="attrition",
        alpha=0.6
    )
    plt.title("Años en la compañía vs. Años desde última promoción según Attrition")
    plt.show()


def BarPlotJobLevelSalaryAttrition(df):
    """
    Genera un gráfico de barras que muestra el salario promedio por nivel de puesto ('joblevel')
    según la columna 'attrition'.

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'joblevel', 'salary' y 'attrition'.

    Retorna:
    None
    """
    sns.barplot(data=df, x="joblevel", y="salary", hue="attrition", ci=None)
    plt.title("Salario promedio por nivel de puesto y Attrition")
    plt.show()

def BarPlotJobLevelSalaryMonthAttrition(df):
    """
    Genera un gráfico de barras que muestra el salario mensual promedio por nivel de puesto ('joblevel')
    según la columna 'attrition'.

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'joblevel', 'salary_month' y 'attrition'.

    Retorna:
    None
    """
    sns.barplot(data=df, x="joblevel", y="salary_month", hue="attrition", ci=None, palette="Set2")
    plt.title("Salario mensual promedio por nivel de puesto y Attrition")
    plt.show()

def PointPlotJobLevelExperienceAttrition(df):
    """
    Genera un gráfico de puntos que muestra los años de experiencia por nivel de puesto ('joblevel')
    según la columna 'attrition'.

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'joblevel', 'años_experiencia' y 'attrition'.

    Retorna:
    None
    """
    sns.pointplot(
        data=df,
        x="joblevel",
        y="años_experiencia",
        hue="attrition",
        dodge=True,
        markers=["o", "s"],
        ci=None,
        palette="Dark2"
    )
    plt.title("Años de experiencia por nivel de puesto y Attrition")
    plt.show()

def StripPlotJobLevelYearsAttrition(df):
    """
    Genera un gráfico de dispersión tipo stripplot que muestra los años en la compañía ('yearsatcompany')
    por nivel de puesto ('joblevel') según la columna 'attrition'.

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'joblevel', 'yearsatcompany' y 'attrition'.

    Retorna:
    None
    """
    sns.stripplot(
        data=df,
        x="joblevel",
        y="yearsatcompany",
        hue="attrition",
        dodge=True,
        alpha=0.6,
        palette="Set2"
    )
    plt.title("Años en la compañía por nivel de puesto y Attrition")
    plt.show()

def LinePlotJobLevelAgeAttrition(df):
    """
    Genera un gráfico de líneas que muestra la edad promedio por nivel de puesto ('joblevel')
    según la columna 'attrition'.

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'joblevel', 'age' y 'attrition'.

    Retorna:
    None
    """
    sns.lineplot(
        data=df,
        x="joblevel",
        y="age",
        hue="attrition",
        marker="o",
        palette="Set1"
    )
    plt.title("Edad promedio por nivel de puesto y Attrition")
    plt.show()

def BarPlotAttritionJobRole(df):
    """
    Genera un gráfico de barras que muestra el porcentaje de attrition por cada rol de trabajo ('jobrole').

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'jobrole' y 'attrition_flag' (0 = se queda, 1 = se va).

    Retorna:
    None
    """
    (df.groupby("jobrole")["attrition_flag"].mean() * 100).plot(
        kind="bar",
        figsize=(10, 5),
        color="tomato"
    )
    plt.title("Attrition (%) por Job Role")
    plt.ylabel("% empleados que se van")
    plt.show()

def BarPlotAttritionWorkLifeBalance(df):
    """
    Genera un gráfico de barras que muestra el porcentaje de attrition por nivel de balance vida-trabajo ('worklifebalance').

    Parámetros:
    df (pd.DataFrame): DataFrame con las columnas 'worklifebalance' y 'attrition_flag' (0 = se queda, 1 = se va).

    Retorna:
    None
    """
    (df.groupby("worklifebalance")["attrition_flag"].mean() * 100).plot(
        kind="bar",
        figsize=(6, 4),
        color=sns.color_palette("coolwarm", 6)
    )
    plt.title("Attrition (%) por Work-Life Balance")
    plt.ylabel("% empleados que se van")
    plt.show()
