from Bio.SeqUtils import translate


def secuencia_de_proteinas(mrna_sequence):
    """
    Traduce una secuencia de ARN mensajero (ARNm) en una secuencia de aminoácidos.

    Parameters:
    mrna_sequence (str): La secuencia de ARN mensajero a traducir.

    Returns:
    str: La secuencia de aminoácidos traducida.

    Raises:
    None

    Esta función itera sobre la secuencia de ARNm en pasos de tres nucleótidos,
    traduciendo cada codón en un aminoácido utilizando la función 'translate' de BioPython.
    La secuencia de aminoácidos resultante se acumula y se devuelve al final de la función.
    """
    protein_sequence = ""
    for i in range(0, len(mrna_sequence), 3):
        codon = mrna_sequence[i:i+3]
        if len(codon) != 3:
            print("Advertencia: Se encontró un codón incompleto al final de la secuencia al momento de la traducción.")
            break
        amino_acid = translate(codon)
        protein_sequence += amino_acid

    return protein_sequence
