
def transposon_insertion (seq_orginal,seq_transposon,posicion): 
    parte1 = seq_orginal[:posicion]
    parte2 = seq_orginal[posicion:]

    unificar = parte1 + seq_transposon + parte2 

    print (parte1, parte2)
    print (unificar)

    return unificar 