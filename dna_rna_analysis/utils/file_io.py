"""

DESCRIPTION
    This script counts the occurrence of nucleotides 'A', 'T', 'G' and 'C' in a file with a .txt extension.
    The file is provided as a positional argument from the command line.

"""


# library
import argparse

# main

def leer_archivo():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(
        description='Count occurrences of DNA symbols in a file.')

    # Add argument for input file
    parser.add_argument('inputfile', type=str,
                        help='Path to the input file containing DNA sequences.')

    # Add optional argument for nucleotides of interest
    parser.add_argument('-n', '--nucleotides', nargs='+', default=['A', 'T', 'G', 'C'],
                        choices=['A', 'T', 'G', 'C', 'a', 't', 'g', 'c'],
                        help='List of nucleotides to count. Default: A, T, G, C.')

    # Parse command-line arguments
    args = parser.parse_args()

    # Read DNA sequences from the input file
    try:
        with open(args.inputfile, 'r') as file:
            dna_sequence = file.read()
            # Check if the file is empty
            if len(dna_sequence) == 0:
                print("Sorry, the file is empty.")
                return
            # Check if the file contains uppercase letters
            if any(char.isupper() for char in dna_sequence):
                # Convert the entire content to lowercase
                dna_sequence = dna_sequence.upper()
    except IOError as ex:
        print("Sorry, couldn't find the file: " + ex.strerror)
    
    return dna_sequence
