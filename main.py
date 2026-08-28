# ============================================
# TITANIC - Exploracion, Limpieza y Analisis
# ============================================
import pandas as pd
import matplotlib.pyplot as plt
import os
pd.set_option('display.max_columns', None)

# Crea la carpeta resultados si no existe
os.makedirs("resultados", exist_ok=True)

# --------------------------------------------
# PASO 1: Leer el archivo
# --------------------------------------------
df = pd.read_csv("data/titanic.csv")
print(df.head(5))

# --------------------------------------------
# PASO 2: Exploracion basica
# --------------------------------------------
print(df.info())
print(df.isnull().sum())
print(df.shape)

# En su README.md, seccion "Funciones investigadas" (si ya la 
# tienen de la sesion pasada, NO la repitan): 
# expliquen info(), isnull().sum(), shape, head()

# --------------------------------------------
# PASO 3: Cuantos sobrevivieron?
# --------------------------------------------
print(df['Survived'].value_counts())

# En su README (si no la tienen ya de antes): que hace value_counts()?

# ============================================
# CONTENIDO NUEVO DE HOY (a partir de aqui)
# ============================================

# --------------------------------------------
# PASO 4: Limpieza
# --------------------------------------------
promedio_edad = df['Age'].mean()
df['Age'] = df['Age'].fillna(promedio_edad)
df = df.drop('Cabin', axis=1)

print("Limpieza completa")
df.to_csv("data/titanic_limpio.csv", index=False)

# En su README: que hace fillna()? que hace drop()?

# --------------------------------------------
# PASO 5: Reflexionen antes de analizar
# --------------------------------------------
# El Titanic tenia la politica "mujeres y ninos primero" en los 
# botes salvavidas. Van a comprobarlo con los numeros.

# --------------------------------------------
# PASO 6: EJEMPLO RESUELTO - Supervivencia por clase
# --------------------------------------------
supervivencia_clase = df.groupby('Pclass')['Survived'].mean()
print(supervivencia_clase)

supervivencia_clase.plot(kind='bar', title='Supervivencia por Clase')
plt.ylabel('Proporcion de sobrevivientes')
plt.savefig("resultados/supervivencia_clase.png")
plt.show()

# --------------------------------------------
# PASO 7: AHORA USTEDES - Supervivencia por genero
# --------------------------------------------
# Repitan el mismo patron del Paso 6, pero agrupando por "Sex" 
# en vez de "Pclass". Guarden como resultados/supervivencia_genero.png


# En su README: 
# - Que hace fillna()? Que hace drop()?
# - Cual clase tuvo mas supervivencia? Y cual genero?
# - Responda la pregunta del Paso 5 con los numeros reales
