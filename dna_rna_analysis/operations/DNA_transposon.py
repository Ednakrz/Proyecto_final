"""
DNA_transposon.py: Módulo para agregar la secuencia de DNA del transposon en la secuencia origen, en la posoción del 
nucleótido ingresado por el usuario.

Este módulo proporciona funciones para unificar la cadena de caracteres que es la secuencia de DNA del transposon con la 
cadena de carcteres que es la secuencia de DNA origen.

Funciones:
- transposon_insertion: Devuelve la cadena de caracteres de la secuencia de DNA con la secuencia del transposon insertada
  donde especificó el usuario.
"""



def transposon_insertion (seq_orginal,seq_transposon,posicion):
    """
    Inserta la cadena de DNA de un transposon en la posición del nucleótido especificada por el usuario. Tambien esta 
    función muestra la longitud de la secunecia unificada.

    Args:
        -seq_orginal: Es la secuencia de DNA original 
        -seq_transposon: Seecuencia del transposon de DNA 
        -posicion: Es la posición o el nucleótido donde queremos que se inserte el transposon

    Returns:
        char: Se regresa la cadena de caracteres correspondiente a la secuencia de DNA unificada con el transposon

    """ 
    parte1 = seq_orginal[:posicion]
    parte2 = seq_orginal[posicion:]

    unificar = parte1 + seq_transposon + parte2 

    longitud = len (unificar)
    print ("La longitud de tu cadena de DNA con el transposon es: {}".format(longitud))

    return unificar 