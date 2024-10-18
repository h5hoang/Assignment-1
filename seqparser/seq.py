# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """

    # converts the input sequence into all uppercase letters and removes white 
    # space to avoid errors with case sensitivity and white space
    seq = seq.upper().strip()

    # initializes empty string to store RNA sequence
    rna = ''

    # initialize dictionary that maps DNA bases to its complement RNA bases
    dna_to_rna = {'A': 'U', 
                  'T': 'A', 
                  'G': 'C', 
                  'C': 'G'}

    # iterates through each nucleotide in the input sequence
    for nuc in seq:

        # check to see if the nucleotide in seq is valid and has a match in the dna_to_rna dictionary
        if nuc in dna_to_rna:

            # if it does, add the corresponding RNA nucleotide to the RNA string
            rna += dna_to_rna[nuc]
        else:
            # returns an error if a character not listed in the dictionary is in the seq
            raise ValueError(f"'{nuc}' is not a DNA nucleotide")

    # returns the transcribed RNA sequence
    return rna


def reverse_transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA then reverses
    the strand
    """

    # uses the transcribe function from above to turn the seq into a complementary RNA strand
    # [::-1] reverses the strand
    rev_strand = transcribe(seq)[::-1]

    # returns the rev RNA strand
    return rev_strand
