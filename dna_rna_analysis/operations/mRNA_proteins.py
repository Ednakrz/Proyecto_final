from Bio.Seq import Seq

def secuencia_de_proteinas (mrna_secuence): 
    seq_protein = mrna_secuence.translate()

    print (seq_protein)


