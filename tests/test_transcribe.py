# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    TODO: Write your unit test for the
    transcribe function here.
    """

    # test if transcribe works as intended for each DNA base
    assert transcribe("ATGC") == "UACG"  

    # test random DNA string
    assert transcribe("GTCGATCGTGGGGATC") == "CAGCUAGCACCCCUAG"  

    # test repeats
    assert transcribe("AAAAATTTTTGGGGGCCCCC") == "UUUUUAAAAACCCCCGGGGG"  

    # test blank strings
    assert transcribe("") == ""  

    # test lower case dna inputs
    assert transcribe("aagtc   ") == "UUCAG"

    # TESTING FOR INVALID INPUT
    # test if my transcribe function raises an error when there is an invalid nucleotide in the input
    try:
        # transcribes random DNA sequence with invalid base (H)
        transcribe("ATHGC") 
    # catch the ValueError raised by the transcribe function
    except ValueError as e:
        #check if the raised error message matches the expected error message for invalid nucleotides
        assert str(e) == "'H' is not a DNA nucleotide"  


def test_reverse_transcribe():
    """
    TODO: Write your unit test for the
    reverse transcribe function here.
    """
    # test if transcribe works as intended for each DNA base
    assert reverse_transcribe("ATGC") == "GCAU"  

    # test random DNA string
    assert reverse_transcribe("GTCGATCGTGGGGATC") == "GAUCCCCACGAUCGAC"

    # test repeats
    assert reverse_transcribe("AAAAATTTTTGGGGGCCCCC") == "GGGGGCCCCCAAAAAUUUUU"  

    # test blank strings
    assert reverse_transcribe("") == ""  

    # test lower case dna inputs with spaces
    assert reverse_transcribe("   aagtc  ") == "GACUU"

    # TESTING FOR INVALID INPUT
    # test if my reverse_transcribe function raises an error (from the transcribe function) when there is an invalid nucleotide in the input
    try:
        # reverse_transcribes random DNA sequence with invalid base (H)
        reverse_transcribe("ATHGC") 
    # catch the ValueError raised by the transcribe function
    except ValueError as e:
        #check if the raised error message matches the expected error message for invalid nucleotides
        assert str(e) == "'H' is not a DNA nucleotide"  
