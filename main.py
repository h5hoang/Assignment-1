from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    TODO: The main function
    """
    # load in fasta and fastq files
    # Create instance of FastaParser
    aparser = FastaParser('data/test.fa')
    # Create instance of FastqParser
    qparser = FastqParser('data/test.fq')    
    
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    # prints header and the sequence for every sequence in test.fa using the transcribe function
    print("\napplying transcribe function on test.fa:")
    for header, sequence in aparser:
        #print(transcribe(sequence))
        rna_sequence = transcribe(sequence)
        print(f"{header}: {rna_sequence}")

    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    # prints header and the sequence for every sequence in test.fq using the transcribe function
    print("\napplying transcribe function on test.fq:")
    for header, sequence, quality in qparser:
        rna_sequence = transcribe(sequence)
        print(f"{header}: {rna_sequence}, {quality}")


    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    # prints header and the sequence for every sequence in test.fa using the reverse transcribe function
    print("\napplying reverse transcribe  function on test.fa:")
    for header, sequence in aparser:
        reverse_rna_sequence = reverse_transcribe(sequence)
        print(f"{header}: {reverse_rna_sequence}")

    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    # prints header and the sequence for every sequence in test.fq using the reverse transcribe function
    print("\napplying reverse transcribe function on test.fq:")
    for header, sequence, quality in qparser:
        reverse_rna_sequence = reverse_transcribe(sequence)
        print(f"{header}: {reverse_rna_sequence}, {quality}")


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
