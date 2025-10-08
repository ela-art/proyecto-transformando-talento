from functions_ABC import leer_data, eda_, transformation, guardar_archivo_csv
from visualizaciones import edad, genero, nivel_estudios


# 1. Leer datos
df = leer_data("hr_raw_data.csv")

# 2. Ver EDA
eda_(df)

# 3. Transformar datos
df_tratado = transformation(df)

# 4. Guardar CSV
guardar_archivo_csv(df_tratado)






