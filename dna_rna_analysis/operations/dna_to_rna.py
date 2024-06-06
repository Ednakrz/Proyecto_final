def transcribe_dna_to_rna(dna_sequence):
    """
    Transcribe una secuencia de ADN a ARN.

    Este método reemplaza las bases nitrogenadas de acuerdo a las siguientes reglas:
    - Adenina (A) se reemplaza por uracilo (U).
    - Citosina (C) se reemplaza por guanina (G).
    - Guanina (G) se reemplaza por citosina (C).
    - Timina (T) se reemplaza por adenina (A).

    Parameters:
    dna_sequence (str): Una cadena de caracteres que representa la secuencia de ADN.

    Returns:
    str: La secuencia de ARN resultante de la transcripción del ADN.
    """
    # Reemplazar todas las bases de acuerdo a las reglas especificadas
    rna_sequence = dna_sequence.replace('A', 'u').replace('C', 'g').replace('G', 'c').replace('T', 'a')
    return rna_sequence.upper()

# Ejemplo de uso
dna_sequence = "ATCG"
rna_sequence = transcribe_dna_to_rna(dna_sequence)
print(rna_sequence)  # Debe imprimir "UAGC"

