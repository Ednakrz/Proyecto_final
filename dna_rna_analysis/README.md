#TRANSCRIPCION_TRADUCCION 

Este es un script de Python diseñado para la simulación de la transposición de una secuencia de DNA de un transposon en una secuencia de DNA ingresada por el usuario, esto con la finalidad de saber cuales son los cambios que se provocan en la secuncia de aminoácidos de la secuencia original de DNA dependiendo de la posición en la que se le inserte el transposon, pudiendo obtener de manera in situ la transposición.

Además este script le permite al usuario seleccionar la posición exacta de su secuencia de DNA original en la que quiere insertar su tranposon.  

## Uso

El script acepta dos argumentos: 
	-Nombre del archivo a leer que contiene la secuencia original de DNA.
	-Nombre del archivo con la secuencia del transposon.

```
python .\transcripcion_traduccion archivo.txt archivo_transposon.txt
```

Donde 
`[archivo]` es el nombre del archivo que contiene la seucuencia de DNA.
`[archivo_transposon]` es el nombre del archivo que contiene la seucuencia del transposon.

## Salida

El script imprimirá en la consola: 
	- Secuencia original de DNA proporcionada por el usuario.
	- Secuencia original del transposon proporcionada por el usuario.
	- Longitud de la secuencia de DNA. 
	- Longitud de la secuencia del transposon.
	- La secuencia de DNA convertida a mRNA.
	- La secuencia de aminoácidos de tu DNA origen.
	- La secuencia del transposon convertida a mRNA.
	- La secuencia de aminoácidos de la secuencia orignal de DNA con el  	 	 tranposon incertado.

## Control de errores

Este código se centra en la rebición de errores de dos tipos principalmente.

1. FileNotFoundError: Este error se maneja cuando el archivo especificado por el usuario no se puede encontrar o no existe en el sistema. En este caso, el programa imprimirá un mensaje de error indicando que no se pudo encontrar el archivo.
2. Excepciones genéricas: Se utiliza un bloque 'except' genérico para manejar cualquier otra excepción inesperada que pueda ocurrir durante la ejecución del programa. 

## Pruebas

El script incluye un conjunto de pruebas unitarias. Puede ejecutar estas pruebas con:

```
python .\transcripcion_traduccion example_dna.txt transposon_ejemplo.txt 
```
Con esto podras encontrar un ejemplo del funcionamiento del programa.

## Datos
El script está diseñado para operar en archivos de texto plano. No hay restricciones en el número de líneas en el archivo.

## Metadatos y documentación
Este README ofrece información de uso básico. La documentación de los modulos se encuentra dentro de ellos.

## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia [MIT License]. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: 
	- Edna Karen Rivera Zagal. ednakrz@lcg.unam.mx
	- Gabriel Alberto G.V. gabrielalg@lcg.unam.mx

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: [ednakrz@lcg.unam.mx].

