"""
posibles.py: Script para ...

Este script...

Uso:
    python posibles_regiones_codificantes.py <path_to_dna_file> [--normalize]

Argumentos:
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de ADN.
    --normalize        : Opción para normalizar el contenido de AT excluyendo 'N's del c
"""

import argparse
from operations.DNA_transposon import transposon_insertion
from utils.file_io import read_dna_sequence
from operations.dna_to_rna import transcribe_dna_to_rna
from operations.DNA_transposon import transposon_insertion
from operations.mRNA_proteins import secuencia_de_proteinas


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

    # Preguntar al usuario la posicion de la mutacion
    dna_length = len(dna_sequence)
    print(
        f"Tu secuencia tiene una longitud de {dna_length}. ¿En qué posición deseas insertar la secuencia del transposón?")
    position_str = input(
        "¿En qué posición deseas insertar la secuencia del transposón? ")
    position = int(position_str)

    # Inserción del transposón
    modified_sequence = transposon_insertion(dna_sequence, transposon_sequence, position)

    #Transcribir la secuencia sin modificar de ADN a ARN
    mrna_sequence = transcribe_dna_to_rna(dna_sequence)
    # Obtener la secuencia de proteínas a partir del mRNA
    protein_sequence = secuencia_de_proteinas(mrna_sequence)
    print("La secuencia de aminoácidos de tu DNA origen es:\n ", protein_sequence)

    # Transcribir la secuencia modificada de ADN a ARN
    mrna_sequence = transcribe_dna_to_rna(modified_sequence)
    # Obtener la secuencia de proteínas a partir del mRNA
    protein_sequence = secuencia_de_proteinas(mrna_sequence)
    print("La secuencia de aminoácidos de tu DNA con el transposon insertado es:\n ", protein_sequence)

    


if __name__ == "__main__":
    main()
