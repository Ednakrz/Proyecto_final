"""
File I/O for DNA Sequences

Este módulo proporciona funciones para manejar operaciones de entrada/salida de archivos de ADN.
Asegura que las secuencias sean válidas y estén bien formateadas antes de ser utilizadas.

Funciones:
    - read_dna_sequence: Lee una secuencia de ADN de un archivo de texto.
"""

def read_dna_sequence(filename):
    """
    Lee una secuencia de ADN desde un archivo de texto.

    Args:
        filename (str): El nombre del archivo que contiene la secuencia de ADN.

    Returns:
        str: La secuencia de ADN contenida en el archivo.

    Raises:
        FileNotFoundError: Si el archivo especificado no se encuentra.
        ValueError: Si el archivo está vacío o contiene caracteres no válidos.
    """
    try:
        with open(filename, 'r') as file:
            sequence = file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{filename}' no se encuentra.")

    if not sequence:
        raise ValueError("El archivo está vacío.")
    
    if any(char not in 'ACGTacgt' for char in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos.")
    
    return sequence.upper()
