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
from utils.file_io import read_dna_sequence


def main():
    parser = argparse.ArgumentParser(
        description="Obtener una seceuncia de aminoacidos a partir de una secuencia de DNA.")
    parser.add_argument(
        "file", type=str, help="Archivo de ADN del cual leer la secuencia.")
    parser.add_argument("-n", "--normalize", action="store_true",
                        help="Normaliza el contenido de AT excluyendo 'N's del cálculo.")

    args = parser.parse_args()
    file_path = args.file
    normalize = args.normalize

    try:
        # Leer la secuencia del archivo especificado utilizando la función proporcionada por file_io.py
        dna_sequence = read_dna_sequence(file_path)

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
