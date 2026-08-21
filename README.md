# Análisis del Dataset Titanic

## Descripción del proyecto

Este proyecto tiene como objetivo realizar una exploración y limpieza básica de un conjunto de datos relacionado con los pasajeros del Titanic.

Para realizar el análisis se utiliza la librería **Pandas** de Python y el archivo `Titanic.Dataset.csv`, ubicado dentro de la carpeta `data/`.

Durante el proyecto se exploran los datos para conocer su estructura, identificar valores vacíos, observar los primeros registros y realizar una limpieza básica de algunas columnas. Finalmente, se realiza un primer análisis sobre la cantidad de pasajeros que sobrevivieron y los que no sobrevivieron.

## Funciones investigadas

### `head()`

La función `head()` permite visualizar los primeros registros de un DataFrame. Por defecto muestra las primeras 5 filas, aunque también se puede indicar una cantidad diferente.

En este proyecto se utiliza para observar cómo están organizados los primeros datos del dataset.

```python
df.head(5)
```

### `info()`

La función `info()` muestra información general del DataFrame. Permite conocer la cantidad de filas, las columnas, los tipos de datos y la cantidad de valores que no están vacíos.

En este proyecto se utiliza para conocer la estructura general del dataset.

```python
df.info()
```

### `isnull().sum()`

`isnull()` permite identificar los valores que están vacíos o son nulos. Al combinarlo con `sum()` podemos contar cuántos valores vacíos existen en cada columna.

Esta función es útil para identificar qué datos necesitan ser tratados durante la limpieza.

```python
df.isnull().sum()
```

### `shape`

`shape` permite conocer el tamaño del DataFrame. Devuelve dos valores: el primero corresponde a la cantidad de filas y el segundo a la cantidad de columnas.

```python
df.shape
```

### `fillna()`

La función `fillna()` permite reemplazar los valores vacíos o nulos por un valor determinado.

En este proyecto se investigará su utilización para completar los valores faltantes de la columna `Age`, por ejemplo, utilizando el promedio de edad.

```python
df["Age"].fillna(df["Age"].mean())
```

### `drop()`

La función `drop()` permite eliminar filas o columnas de un DataFrame.

En este proyecto se investigará su utilización para eliminar la columna `Cabin`, debido a que contiene una gran cantidad de valores vacíos.

```python
df.drop(columns=["Cabin"])
```

### `value_counts()`

La función `value_counts()` permite contar cuántas veces aparece cada valor dentro de una columna.

En este proyecto se utiliza para conocer cuántos pasajeros sobrevivieron y cuántos no sobrevivieron mediante la columna `Survived`.

```python
df["Survived"].value_counts()
```

## Hallazgos de la exploración

Durante la exploración inicial del dataset se identificaron diferentes características importantes de los datos.

* El dataset contiene información de los pasajeros del Titanic.
* Se revisó la estructura de los datos utilizando `info()`.
* Se consultaron las dimensiones del dataset mediante `shape`.
* Se visualizaron los primeros registros utilizando `head()`.
* Se identificaron las columnas que contienen valores vacíos utilizando `isnull().sum()`.
* La columna `Age` contiene valores faltantes, por lo que se debe realizar un tratamiento para completar estos datos.
* La columna `Cabin` contiene una gran cantidad de valores faltantes, por lo que se considera la posibilidad de eliminarla en lugar de intentar completar todos sus valores.
* Se utilizará `value_counts()` sobre la columna `Survived` para conocer la cantidad de pasajeros que sobrevivieron y los que no sobrevivieron.

## Limpieza de los datos

Como parte de la limpieza básica se analizará la columna `Age` para determinar la forma más adecuada de completar sus valores faltantes. Una opción es utilizar el promedio de las edades existentes.

También se analizará la columna `Cabin`, ya que contiene muchos valores vacíos. Debido a esta situación, puede ser más conveniente eliminar la columna utilizando `drop()`.

Después de realizar la limpieza y el análisis, se guardará una nueva versión del dataset como:

```text
data/titanic_limpio.csv
```

## Análisis de supervivencia

Para realizar un primer análisis de los pasajeros se utilizará la función `value_counts()` sobre la columna `Survived`.

En esta columna:

* `0` representa a los pasajeros que no sobrevivieron.
* `1` representa a los pasajeros que sobrevivieron.

Esto permite obtener una primera comparación entre los pasajeros que sobrevivieron y los que no sobrevivieron.

## Estructura del proyecto

```text
├── data/
│   ├── Titanic.Dataset.csv
│   └── titanic_limpio.csv
├── main.py
├── README.md
└── .gitignore
```