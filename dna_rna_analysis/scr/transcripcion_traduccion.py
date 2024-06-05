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
import dna_transposon import transposon_insersion
from utils.file_io import read_dna_sequence


import argparse
from dna_to_rna import transcribe_dna_to_rna, find_coding_sequence
from rna_to_protein import translate_rna_to_protein
from utils import read_dna_sequence_from_file

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

    try:
        # Leer la secuencia del archivo especificado utilizando la función proporcionada por utils.py
        dna_sequence = read_dna_sequence_from_file(dna_file_path)
        transposon_sequence = read_dna_sequence_from_file(transposon_file_path)
    except Exception as e:
        print(f"Error: {str(e)}")


    # Preguntar al usuario la posicion de la mutacion
    dna_length = len(dna_sequence)
    print(f"Tu secuencia tiene una longitud de {dna_length}. ¿En qué posición deseas insertar la secuencia del transposón?")
    position = input()
    modified_sequence = transposon_insersion(dna_sequence, seq_transposon, position)


if __name__ == "__main__":
    main()
