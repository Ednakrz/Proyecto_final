"""
transcripcion_traduccion.py

VERSION del script: 1.0

FECHA de la última actualización: 05/06/2024

ATORES: 
    -Edna Karen Rivera Zagal:  ednakrz@lcg.unam.mx
    - Gabriel Alberto Garcia Vargas: gabrielalg@lcg.unam.mx

DESCRIPCION:

    Este script esta diseñado para insertar una secuencia de DNA de algun transposon en la secuencia de DNA original 
    proporcionada por el usuario. Para posteriormente obtener la secuencia de aminoácidos que se tienen de la combinación de 
    DNA con el transposon que se ha insertado.

CATEGORIA
    Uso de secuencias de DNA y objetos de tipo Seq.

USO:
    python scr/transcripcion_traduccion tests/archivo.txt tests/archivo_transposon.txt


EJEMPLO: 
    python3 scr/transcripcion_traduccion.py tests/exemple_dna.txt tests/transposon_ejemplo.txt
    
"""

import argparse

from operations.DNA_transposon import transposon_insertion
from operations.dna_to_rna import transcribe_dna_to_rna
from operations.mRNA_proteins import secuencia_de_proteinas
from utils.file_io import read_dna_sequence


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

    # Leer la secuencia del archivo especificado utilizando la función proporcionada por utils.py
    dna_sequence = read_dna_sequence(dna_file_path)
    transposon_sequence = read_dna_sequence(transposon_file_path)

    # Secuencia de DNA y longitud
    print("La secuencia de DNA proporcionada es: ", dna_sequence)
    dna_length = len(dna_sequence)
    print(f"La secuencia tiene una longitud de {dna_length} nucleótidos. \n")

    # Secuencia de Transposón y longitud
    print("La secuencia de transposon es: ", transposon_sequence)
    transposn_length = len(transposon_sequence)
    print("La transposon tiene una longitud de {} nucleotidos. \n".format(
        transposn_length))

   # Preguntar al usuario la posición de la mutación
    while True:
        try:
            position_str = input(
                "¿En qué posición deseas insertar la secuencia del transposón? ")
            position = int(position_str)
            if position < 0 or position > dna_length:
                raise ValueError(
                    f"La posición debe estar dentro del rango [0, {dna_length}].")
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Por favor, introduce un número entero válido para la posición.")

    # Inserción del transposón
    modified_sequence = transposon_insertion(
        dna_sequence, transposon_sequence, position)

    # Transcribir la secuencia sin modificar de ADN a ARN
    mrna_sequence = transcribe_dna_to_rna(dna_sequence)
    print("\nLa secuencia de DNA convertida a mRNA es: ", mrna_sequence)
    # Obtener la secuencia de proteínas a partir del mRNA
    protein_sequence = secuencia_de_proteinas(mrna_sequence)
    print("\nLa secuencia de aminoácidos del DNA origen es: ", protein_sequence)

    # Transcribir la secuencia modificada de ADN a ARN
    mrna_sequence = transcribe_dna_to_rna(modified_sequence)
    print("\n\nLa secuencia del transposon convertida a mRNA es: ", mrna_sequence)
    # Obtener la secuencia de proteínas a partir del mRNA
    protein_sequence = secuencia_de_proteinas(mrna_sequence)
    print("\nLa secuencia de aminoácidos del DNA con el transposon insertado es: ", protein_sequence)


if __name__ == "__main__":
    main()
