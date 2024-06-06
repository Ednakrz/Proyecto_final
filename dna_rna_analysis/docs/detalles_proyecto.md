# TRANSCRIPCION_TRADUCCION

Fecha:
05/06/2024
**Participantes**: 

- Edna Karen Rivera Zagal:  ednakrz@lcg.unam.mx
- Gabriel Alberto Garcia Vargas: gabrielalg@lcg.unam.mx


## Descripción del Problema

Este script esta diseñado para insertar una secuencia de DNA de algun transposon en la secuencia de DNA original proporcionada por el usuario. Para posteriormente obtener la secuencia de aminoácidos que se tienen de la combinación de DNA con el transposon que se ha insertado.



## Especificación de Requisitos

Requisitos funcionales

- Leer diferentes letras (A,T,G,C) de un archivo dado.
- Convierte las letras minusculas a mayusculas.
- Calcula la longitud de la cadena de DNA y del transposon.
- Convierte las secuencias de DNA y del transposon  de DNA en mRNA.
- Inserta la secuencia del tranposon en la secuencia de DNA en la posoción especificada por el usuario.
- Convierte la secuencia de DNA original en sus aminoácidos correspondientes.
- Convierte la secuencia de DNA con el transposon en su secuencia de aminoácidos.

Requisitos no funcionales

- El script deberá estar escrito en Python.
- El tiempo de respuesta debe ser rápido, incluso con archivos de gran tamaño.


## Análisis y Diseño

Para resolver este problema, se utilizarán varias funciones incorporadas en los modulos del paquete 'operation', así como el manejo de excepciones para la validación de datos y archivo. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:

pseudocogido:

```
def main():
    parser = argparse.ArgumentParser(
        description="Obtener una secuencia de aminoácidos a partir de una secuencia de ADN.")
    parser.add_argument(
        "dna_file", type=str, help="Archivo de ADN del cual leer la secuencia.")
    parser.add_argument(
        "transposon_file", type=str, help="Archivo que contiene la secuencia del transposón.")
    parser.add_argument("-n", "--normalize", action="store_true",
                        help="Normaliza el contenido de AT excluyendo 'N's del cálculo.")

    args = parser.parse_args()
    dna_file_path = args.dna_file
    transposon_file_path = args.transposon_file
    normalize = args.normalize

    proporcionada por utils.py
    dna_sequence = read_dna_sequence(dna_file_path)
    transposon_sequence = read_dna_sequence(transposon_file_path)

    print ("Tu secuencia de DNA proporcionada es:", dna_sequence)
    print ("Tu secuencia de transposon es: ", transposon_sequence)
    
   
    dna_length = len(dna_sequence)
    print(
        f"Tu secuencia tiene una longitud de {dna_length} nucleotidos.")
    position_str = input(
        "¿En qué posición deseas insertar la secuencia del transposón? ")
    position = int(position_str)

    
    transposn_length = len(transposon_sequence)
    print ("Tu transposon tiene una longitud de {} nucleotidos. ".format(transposn_length))


   
    modified_sequence = transposon_insertion(dna_sequence, transposon_sequence, position)

    
    mrna_sequence = transcribe_dna_to_rna(dna_sequence)
    print ("La secuencia de DNA convertida a mRNA es: ", mrna_sequence)
    protein_sequence = secuencia_de_proteinas(mrna_sequence)
    print("La secuencia de aminoácidos de tu DNA origen es:", protein_sequence)

    
    mrna_sequence = transcribe_dna_to_rna(modified_sequence)
    print ("La secuencia del transposon convertida a mRNA es: ", mrna_sequence)
    protein_sequence = secuencia_de_proteinas(mrna_sequence)
    print("La secuencia de aminoácidos de tu DNA con el transposon insertado es:", protein_sequence) 
```
El formato de los datos de entrada serán archivos de tipo txt.



#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada/ o parametros en la términal 
                 v
         +-------+-------+
         |Inserta un tran|
         |sposon en una  |
         |secuencia de DN|
         |A, y lo convier|
	 |te a aminoácido|
	 |s.		 |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**: El actor proporciona dos archivos de entrada de tipo txt. Uno con la secuencia de DNA original sobre la que se va a insertar el transposon y el segundo con la secuencia de DNA del transposon.
- **Flujo principal**:

1.1 El actor inicia el sistema proporcionando los archivos de entrada con las secuencias de DNA.

1.2 El sistema valida el archivo y los datos de entrada.

1.3 El sistema calcula la longitud de la secuencia de DNA.

1.4 El sistema muestra el resultado.

2.1El actor indica cual es la posicion del nucleotido de su secuencia de DNA en la que quiere ingresar su transposon.
2.2 El sistema muestra el resultado de las secuencias convertidas de DNA a mRNA
3.3 El sistema muestra las secuencias convertidas a sus análogos aminoácidos.


	
- **Flujos alternativos**:
	- Si no se proporciona un archivo entonces el programa deberá marcarlo como un error.
	- Si el formato del archivo no es correcto, imprimir a pantalla mensaje de error
         

- **Validaciones del programa**:

	- Si el archivo está vacio se manda un mensaje de error de que el archivo está vacio y por lo tanto no se puede procesar.
	- Si no se encontró el archivo proporcionado por el usuario el programa manda un mensaje de error de que el archivo no fue encontrado.
	- El programa solo acepta archivos que contengas las letras, A,T,G,C ya sea que esten en mayusculas o minusculas, de no encontrarse el programa mando un mensaje de error en el que se afirma que la secuencia contiene caracteres invalidos.
	