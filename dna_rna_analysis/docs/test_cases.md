# Casos de prueba o escenarios

Este documento describe los casos de prueba para el script de Python 
desarrollado para transcribir ADN a ARN, insertar transposones y traducir 
ARN a secuencias de proteínas.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes 
funcionalidades del script así como los posibles errores que puedan 
surgir.

El script permite leer secuencias de ADN desde archivos, insertar 
secuencias de transposones en posiciones especificadas, transcribir ADN a 
ARN y traducir ARN a proteínas utilizando el código genético estándar.

Los casos de prueba cubren las características clave del programa y 
prueban varias condiciones para garantizar la robustez y fiabilidad del 
script.

La ejecución exitosa de estos casos de prueba asegura que el script está 
listo para su uso y puede manejar diferentes condiciones de entrada y 
situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso 
de prueba incluye una descripción del caso de prueba, los datos de entrada 
utilizados y el resultado esperado.
    

### Caso de prueba 1: Lectura de secuencia de ADN válida

- Descripción: Comprobar que el script puede leer correctamente una secuencia de ADN desde un archivo.
- Datos de entrada: Archivo `example_dna.txt` con la secuencia "ATGCGTACGTTAGC".
- Resultado esperado: El script debe leer y retornar la secuencia "ATGCGTACGTTAGC".

```{python}
python3 transcripcion_traduccion.py utils/example_dna.txt utils/transposon_ejemplo.txt

# Salida esperada: El programa contunúa sin imprimir errores

```

### Caso de prueba 2: Lectura de secuencia de ADN con caracteres no válidos
- Descripción: Verificar que el script maneje adecuadamente una secuencia de ADN que contiene caracteres no válidos.
- Datos de entrada: Archivo invalid_dna.txt con la secuencia "ATGCGTACGTTXGC".
- Resultado esperado: El script debe lanzar un ValueError indicando que la secuencia contiene caracteres no válidos.

```{python}
python3 transcripcion_traduccion.py utils/invalid_dna.txt utils/transposon_ejemplo.txt

# Salida esperada
ValueError: La secuencia contiene caracteres no válidos.

```