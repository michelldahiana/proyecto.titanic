# ============================================
# ANALISIS DEL DATASET TITANIC
# Guia paso a paso
# ============================================
import pandas as pd
pd.set_option('display.max_columns', None)  # Muestra TODAS las columnas al imprimir, sin cortar

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

# En su README.md, creen una seccion "Funciones investigadas" 
# y expliquen con sus propias palabra que hace cada una:
# - info()
# - isnull().sum()
# - shape
# - head()

# Tambien anoten:
# - Cuantas filas y columnas tiene el dataset
# - Que columnas tienen valores vacios y cuantos

# --------------------------------------------
# PASO 3: Limpieza basica (COMPLETEN USTEDES)
# --------------------------------------------
# Investiguen: la columna "Age" tiene varios valores vacios.
# Decidan como rellenarla (puede ser con el promedio de edad)
# Pista: usen .fillna()


# La columna "Cabin" tiene MUCHOS valores vacios (mas de la mitad).
# Investiguen: en estos casos, a veces es mejor ELIMINAR la 
# columna completa en vez de rellenarla. Investiguen drop()

# En su README, agreguen tambien: que hace fillna()? que hace drop()?

# --------------------------------------------
# PASO 4: Primer analisis simple
# --------------------------------------------
# Cuenten cuantos pasajeros sobrevivieron vs no sobrevivieron
# Pista: usen value_counts() sobre la columna "Survived"

# En su README: que hace value_counts()?

# Guardar el resultado limpio
df.to_csv("data/titanic_limpio.csv", index=False)