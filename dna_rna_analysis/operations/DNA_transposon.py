def transposon_insertion (seq_orginal, transposon_sequence, position): 
    parte1 = seq_orginal[:position]
    parte2 = seq_orginal[position:]

    unificar = parte1 + transposon_sequence + parte2 

    print(parte1, parte2, "\n", unificar)

    return unificar 