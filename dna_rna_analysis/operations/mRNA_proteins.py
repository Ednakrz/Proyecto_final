from Bio.Seq import Seq
from Bio.SeqUtils import translate

def secuencia_de_proteinas(mrna_sequence):
    protein_sequence = ""
    for i in range(0, len(mrna_sequence), 3):
        codon = mrna_sequence[i:i+3]
        if len(codon) != 3:
            break
        amino_acid = translate(codon)
        protein_sequence += amino_acid
    return protein_sequence


