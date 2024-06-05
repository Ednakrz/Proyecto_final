"""
file_io.py: Funciones para manejar operaciones de entrada/salida de archivos de ADN.
Este módulo provee funcionalidades para leer y escribir secuencias de ADN desde y hacia
archivos, asegurando que las secuencias sean válidas y estén bien formateadas.
Funciones:
    read_dna_sequence(filename) - Lee una secuencia de ADN de un archivo.
    write_dna_sequence(filename, sequence) - Escribe una secuencia de ADN en un archivo.
    
Ejemplos de uso están disponibles en el bloque principal del módulo.
Autores: [Tu Nombre]
Versión: 1.0
"""

# imports

# meta-info
__author__ = "Tu Nombre"
__version__ = "1.0"

# global vars

# functions internal

# main functions

def read_dna_sequence(filename):
    """
    Lee una secuencia de ADN de un archivo de texto.
    
    Args:
        filename (str): El nombre del archivo del cual leer la secuencia.
        
    Returns:
        str: La secuencia de ADN contenida en el archivo.
        
    Raises:
        FileNotFoundError: Si el archivo especificado no se encuentra.
        ValueError: Si el archivo está vacío o contiene caracteres no válidos.
    """
    with open(filename, 'r') as file:
        sequence = file.read().strip().upper()
    if not sequence:
        raise ValueError("El archivo está vacío.")
    if any(char not in 'ACGT' for char in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos.")
    return sequence
