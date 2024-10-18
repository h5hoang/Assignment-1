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
    aparser = FastaParser('data/test.fa')
    qparser = FastqParser('data/test.fq')    
    
    print("\napplying ranscribe function on test.fa:")
    for header, sequence in aparser:
        rna_sequence = transcribe(sequence)
        print(f"{header}: {rna_sequence}")
   
    print("\napplying ranscribe function on test.fq:")
    for header, sequence, quality in qparser:
        rna_sequence = transcribe(sequence)
        print(f"{header}: {rna_sequence}, {quality}")


    print("\napplying reverse ranscribe function on test.fa:")
    for header, sequence in aparser:
        reverse_rna_sequence = reverse_transcribe(sequence)
        print(f"{header}: {reverse_rna_sequence}")

    print("\napplying reverse ranscribe function on test.fq:")
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
