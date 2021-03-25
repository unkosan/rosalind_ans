import collections

def validateSeq(seq):
    tempseq = seq.upper()
    for element in tempseq:
        if element not in ['A', 'T', 'C', 'G']:
            return False
    return tempseq

def count_dna_nucleotides(seq):
    if validateSeq(seq) == False:
        return False
    return collections.Counter(seq)

if __name__=='__main__':
    count = count_dna_nucleotides(seq)
    print(count['A'], count['C'], count['G'], count['T'])