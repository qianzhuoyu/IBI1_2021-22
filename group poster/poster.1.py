import re

codons = {'TTT': 'Phe', 'TTC': 'Phe', 'TTA': 'Leu', 'TTG': 'Leu', 'CTT': 'Leu', 'CTC': 'Leu', 'CTA': 'Leu',
          'CTG': 'Leu',
          'ATT': 'Ile', 'ATC': 'Ile', 'ATA': 'Ile', 'ATG': 'Met', 'GTT': 'Val', 'GTC': 'Val', 'GTA': 'Val',
          'GTG': 'Val',
          'TCT': 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser', 'CCT': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro',
          'CCG': 'Pro',
          'ACT': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr', 'GCT': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala',
          'GCG': 'Ala',
          'TAT': 'Tyr', 'TAC': 'Tyr', 'TAA': 'stop', 'TAG': 'stop', 'CAT': 'His', 'CAC': 'His', 'CAA': 'Gln',
          'CAG': 'Gln',
          'AAT': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys', 'GAT': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu',
          'GAG': 'Glu',
          'TGT': 'Cys', 'TGC': 'Cys', 'TGA': 'stop', 'TGG': 'Trp', 'CGT': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg',
          'CGG': 'Arg',
          'AGT': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg', 'GGT': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly',
          'GGG': 'Gly'}


def mc(seq1, seq2):  # mc = mutation calculator  seq1 = ori_seq  seq2 = mut_seq
    n = 0
    for x, y in zip(seq1, seq2):
        n += 1
        if x == y:
            continue
        else:
            print(">Position %s is mutated from '%s' to '%s'." % (n, x, y))
        if n % 3 == 0:
            codon1 = seq1[n - 3: n]
            codon2 = seq2[n - 3: n]
            aa1 = codons[codon1]  # aa = amino acid
            aa2 = codons[codon2]
            if aa1 == aa2:
                print("This amino acid doesn't change.")
            else:
                print('%s is mutated to %s.' % (aa1, aa2))
        if n % 3 == 1:
            codon1 = seq1[n - 1: n + 2]
            codon2 = seq2[n - 1: n + 2]
            aa1 = codons[codon1]  # aa = amino acid
            aa2 = codons[codon2]
            if aa1 == aa2:
                print("This amino acid doesn't change.")
            else:
                print('%s is mutated to %s.' % (aa1, aa2))
        if n % 3 == 2:
            codon1 = seq1[n - 2: n + 1]
            codon2 = seq2[n - 2: n + 1]
            aa1 = codons[codon1]  # aa = amino acid
            aa2 = codons[codon2]
            if aa1 == aa2:
                print("This amino acid doesn't change.")
            else:
                print('%s is mutated to %s.' % (aa1, aa2))
    return True
ori_seq_1 = 'ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA'
mut_seq_1 = 'ATGGCCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTGGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTAGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACATACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAACAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA'

mc(ori_seq_1, mut_seq_1)