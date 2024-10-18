# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    TODO: Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """

    # CHECKING IF FUNCTION IS ABLE TO RETRIEVE RECORDS
    # reads test.fa fasta file and checks if the first 2 headers and sequences match of the records
    fasta_parser = FastaParser("data/test.fa")

    # converts the records into a list
    has_records = list(fasta_parser)

    # headers and sequences for the first 3 lines of test.fa
    has_expected = [
        (">seq0", "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"),
        (">seq1", "TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT"),
        (">seq2", "TGTAGAGGCATTATTAGAGTTTCGCCACAACGGGGGCCTGCTGATCAAATCAGAATTCGTACAATCGGTTCGGGAGACACGGCTCTAAAGATACCGCTAG")
    ]

    # header and sequence for last sequence in file
    last_seq = (">seq99", "CAAACCGGCGATGCGGGTACTCCCTACAAGTTGGACTCCGCAGCGAACGCCGCAGGGGCCATTATACGGCGGTCTTGGCGGCGTCGACCAGGCCGGTCCA")

    # checks if the records for the first two records match what is expect
    assert has_records[0] == has_expected[0]
    assert has_records[1] == has_expected[1]
    assert has_records[2] == has_expected[2]

    # checks if records for last sequence matches
    assert has_records[len(has_records) -1] == last_seq 

    ##CHECKING IF FUNCTION IS ABLE TO READ EMPTY FASTA FILES
    #reads empty fasta file i generated
    fasta_parser_empty = FastaParser("data/empty.fa")
    # converts the records onto a list
    no_records = list(fasta_parser_empty)
    
    # checks that the number of records is 0 so  no sequences were parsed
    assert len(no_records) == 0


def test_FastqParser():
    """
    TODO: Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """

    # CHECKING IF FUNCTION IS ABLE TO RETRIEVE RECORDS
    # reads test.fa fasta file and checks if the first 3 headers, sequences, and quality scores match
    fastq_parser = FastqParser("data/test.fq")
    # converts records into a list
    has_records = list(fastq_parser)

    # headers, sequences, and quality scores for the first two records of test.fq
    has_expected = [
        ("@seq0", "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG", "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7\"94(>7='(!5\"2/!%\"4#32="),
        ("@seq1", "CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG", "'(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,,:%0!<),%646<8#%\".\"-'*-0:.+*&$5!'8)(%3*+9/&/%=363*,6$20($97,\""),
        ("@seq2", "GATAAACTTCTATCACGAATACTGCGGGACCATGCAGTTGTCCCTCACCTCGATAGTTCAGGTCTTTTGGTTCTGAGCGATATTGGGCGCGTCACCACTG", """1,758$,:7654/7<0%5/12%-3>-2.>$$443-,'9,5$;""%7**)-'%:**&;<35(!<1'.5>51)1%:9>4=(&+3$2!-.8!>=+1$:,*&9!""")
    ]
    
    # header and sequence for last sequence in file
    # quality score read got iffy with quotiations so assigning it to a variable made it easier
    last_seq_quality = """2$7)*5:"=+++!:.=>!5>79)8!566$!3*/4$=4.%=//;900$9)!%)4%$=0":02"0=!0#/>+*1$1$39!.8+9<'1$*1$321&<'&9,)2"""

    last_seq = ("@seq99", "CCGAGTTTTGTAGTGGGCTCAACTGAAATCCTATTCTTAGACGATTGGTCATAAAACCCTTTCACTGTACGGACGTAGACCCTGCTCCGTCTTCCAGCAG", last_seq_quality)

    # checks if the records for the first two records match what is expected
    assert has_records[0] == has_expected[0]
    assert has_records[1] == has_expected[1]
    assert has_records[2] == has_expected[2]

    #checks if the records for the last sequence matches
    assert has_records[len(has_records)-1] == last_seq

    ##CHECKING IF FUNCTION IS ABLE TO READ EMPTY FASTQ FILES
    #reads empty fasta file i generated
    fastq_parser_empty = FastaParser("data/empty.fa")
    # converts the records onto a list
    no_records = list(fastq_parser_empty)
    
    # checks that the number of records is 0 so  no sequences were parsed
    assert len(no_records) == 0
