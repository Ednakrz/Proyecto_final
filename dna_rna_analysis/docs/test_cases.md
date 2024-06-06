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
- Resultado esperado: El script debe correr correctamente

```{python}
python3 scr/transcripcion_traduccion.py utils/example_dna.txt utils/transposon_ejemplo.txt

# Salida esperada: El programa contunúa sin imprimir errores

```

### Caso de prueba 2: Lectura de secuencia de ADN con caracteres no válidos
- Descripción: Verificar que el script maneje adecuadamente una secuencia de ADN que contiene caracteres no válidos.
- Datos de entrada: Archivo invalid_dna.txt con la secuencia "ATGCGTACGTTXGC".
- Resultado esperado: El script debe lanzar un ValueError indicando que la secuencia contiene caracteres no válidos.

```{python}
python3 scr/transcripcion_traduccion.py utils/invalid_dna.txt utils/transposon_ejemplo.txt

# Salida esperada
ValueError: La secuencia contiene caracteres no válidos.

```

### Caso de prueba 3: Traducción de ARN con codón incompleto al final
- Descripción: Comprobar que el script maneje adecuadamente una secuencia de ARN con un codón incompleto al final.
- Datos de entrada: Secuencia de DNA con dones completos y "AT" para el transposón.
- Resultado esperado: El script debe imprimir un mensaje indicando que la secuencia contiene un codón incompleto.

```{python}
python3 scr/transcripcion_traduccion.py tests/dna_origen_ejemplo.txt tests/transposon_codon_incompleto.txt

# Salida esperada
Advertencia: Se encontró un codón incompleto al final de la secuencia al momento de la traducción.

```

### Caso de prueba 4: Los archivos con los datos de enrtrada pueden contener minúsculas o mayúsculas
- Descripción: Comprobar que el script pueda leer y manejar archivos con secuencias en minúsculas o mayúsculas
- Datos de entrada: Secuencia de DNA en minúscula y secuencia de transposón en mayúscula.
- Resultado esperado: El script debe correr correctamente.

```{python}
python3 scr/transcripcion_traduccion.py tests/dna_origen_ejemplo.txt tests/transposon_ejemplo.txt

# Salida esperada: El programa contunúa sin imprimir errores.

```

### Caso de prueba 5: Transcripción de ADN a ARN
- Descripción: Comprobar que el script puede transcribir correctamente una secuencia de ADN a ARN.
- Datos de entrada: Secuencia de ADN "ATGCGTACGTTAGCC".
- Resultado esperado: El script debe retornar la secuencia de ARN "UACGCAUGCAAUCGG".

```{python}
python3 scr/transcripcion_traduccion.py utils/example_dna.txt utils/transposon_ejemplo.txt

# Salida esperada
La secuencia de DNA convertida a mRNA es:  UACGCAUGCAAUCGG

```

### Caso de prueba 6: Traducción de ARN a secuencia de proteínas
- Descripción: Verificar que el script puede traducir correctamente una secuencia de ARN a una secuencia de proteínas.
- Datos de entrada: Secuencia de ARN "UACGCAUGCAAUCGG".
- Resultado esperado: El script debe retornar la secuencia de proteínas "YACNR".

```{python}
python3 scr/transcripcion_traduccion.py utils/example_dna.txt utils/transposon_ejemplo.txt

# Salida esperada
La secuencia de aminoácidos del DNA origen es:  YACNR

```
