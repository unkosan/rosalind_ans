def counting_point_mutations(seq1, seq2):
    if len(seq1) != len(seq2):
        raise Exception('sequences are not the same length')
    count = 0
    for elem1, elem2 in zip(seq1, seq2):
        if elem1 != elem2:
            count += 1
    return count
    
if __name__ == '__main__':
    seq1 = 'GACGCGACCTCTAGGCTTTTCCTGACGCCAAGTTTATCCCCTCTCTACCCAGGAGAGTAGGATATAGGAGGCGAATACGTGTAGGCCAGTTGCCGTACGTACAGATTAATAAATTGTCAGACGAGTTGGAGCACCCCGGTACAGCAAAATTACGTTTCCTTGTGGTCAGTTAGTTGTGCCTATACGGTTTAAACCGCTTACGGTCACTCGGATTTTGCGTTTAGGGTGGACTGGGGGAGGCTCACAATGCACTCCGAAACCATGAGTAGCGTATTGCAATTACTTGGTACGTGATACCTACATCTATACTTTTCCCTAATCGTTGCGATCGCGTGTAGTATGCACAGACCATGCCTTCAATTTTCCGTGAAAGACGTCCGGCGATAGGCTACAGATCCAGATTCTAGCCGAAAATGGCACAGTCACATGGGCTCCCCATCACATCTCCCTCAATTCATGACGCTGTCCATGCGTAAGTTGCTCATTTGACAGGTCCAAGTGACTAAAAGATCGACTTCTCATTATTAGCGCAAGCGAACGCCCCAACCCAGCCATGACAATATTACGGGCCAGATCACGTGGCGGATGCTCGCATCAGAGAAGAGGACGCCGCTTAGCTTCTGCGACAAGGTACTGAGTGTAGGGGCGAAACATCAACCAGTTTTAAATATAGTATCCATCATGAACAGTCTTTTTCACCGGGCAAGACGCATTCCGATGACTTTAAGAATGACCGCGCCAATATCGCTACAGCGCTTACCTTGTATACCTGATATACGTCTCGATTTATGATGTAATCAACGCTAACGTAATTAGCTCTATGGTCCGTGGTTGAGATCGACAGTTCACCATTACTTGCGGACACGAGGTAGTCCAACTGACGTCCCGGTTCAGTCTTCTTTCTTGTCTTTGTACACGATATAGTGAATCATCTCGCAATTTAGGAGCAGGGCCCCACGGCATGACCA'
    seq2 = 'GCAGACGCAGGACGGTTTCCGGTGAGGACGACATCGGTATAGGCTCTCCCAGTCACACAAGCCCCTGGTGACGAGGCCGTCTTGTGGAAGAGCGCGACTTACAGGTTAATTGATGGTTACACAGGCTACAGGGGCGCAGTGATGAGAAAACTTCCTTCCCCGCGTTCAGCGTTTTTAGACGGTCCTTTTATGGGCGCTCACGGCTATTCCCATAGGCCATGTAAGGTAGAGTGGCGGAGGAAACCAAGGAGTTTCAAAACGGGGATATACCCGTTGACTTTTCTTGGTATGATACAATAACATATCGTTTCCCCCGCTAAAGGTACAGACGCTTTAGATATGGGTAGATCATACCAGTCACATGGTATAAGATAGTTCTGTGGAATTCGTACTGATTCAGATAAGCTATGAGAGTGGCACAGAAACCCCCGGCCAGCAGTTGATCTCCCAGAATTCGCTCCGTAGCATCCAAGAAAGTTTCTCGTAGAGGACATGCAAGTTAATACTGAAGAGCCATTTAACGACCCGACGAATCGACTGCGCCATCTCAGCTTGGTCAATATGACGATCCACCTAACGCGTTGGTAACACATATTAAAGTAGAGGACACGCCATACCTTCAGGTAAATGGGCAAAAGGGTACGTGTTCATGTTAGCCCAGTCTCACATCTTCTAGCACAATTGTGGACACGGCTTAAACGTTCAACCTGCCCACAGATGAATGTAAAGATGGGACCGCGCACTTCTCTCCAGTGCTGCTCTAGGATATTGGAATGAAAGCCCGAATTCTTTTCTGATCAAAGGCGACGTATTTCTCCCCCTGGCCAGTAGCTGCGCGCGCCAGAACCGCCCTTATACGGCCCGACGATATGTCCAAGCGATGTCCGAGAGTAGACTTCATTCTTGTGGGCGTACCCGACCCATATAATGAACTCGCCTGGTATGATCTGACCTCCACGGCGTGGTGA'
    print(counting_point_mutations(seq1, seq2))