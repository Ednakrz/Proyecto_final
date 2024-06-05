def transcribe_dna_to_rna(dna_sequence):
    """
    Transcribe una secuencia de ADN a ARN.

    Este método reemplaza todas las apariciones de la base nitrogenada timina (T)
    en la secuencia de ADN por uracilo (U) para obtener la secuencia de ARN.

    Parameters:
    dna_sequence (str): Una cadena de caracteres que representa la secuencia de ADN.

    Returns:
    str: La secuencia de ARN resultante de la transcripción del ADN.
    """
    rna_sequence = dna_sequence.replace('T', 'U')
    return rna_sequence
