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


def snc(seq):  # snc = Synonymous and Nonsynonymous Calculator
    print('There are %d possible single point mutations in total.' % (len(seq) * 3))  # Every point has 3 possibilities.
    n = 0
    synonymous = 0
    for i in range(0, len(seq) // 3):
        codon = seq[n:n + 3]
        n += 3
        aa = codons[codon]  # aa = amino acid
        if re.search('Phe|Tyr|His|Gln|Asn|Lys|Asp|Glu|Cys', aa):
            synonymous += 1
        if aa == 'Leu':
            if re.search('TT[AG]', codon):
                synonymous += 2
            if re.search('CT[TC]', codon):
                synonymous += 3
            if re.search('CT[AG]', codon):
                synonymous += 4
        if aa == 'Ile':
            synonymous += 2
        if re.search('Met|Trp', aa):
            synonymous += 0
        if re.search('Val|Pro|Thr|Ala|Gly', aa):
            synonymous += 3
        if aa == 'Ser':
            if re.search('TC[TCAG]', codon):
                synonymous += 3
            if re.search('AG[TC]', codon):
                synonymous += 1
        if aa == 'stop':
            if re.search('TA[AG]', codon):
                synonymous += 1
            if codon == 'TGA':
                synonymous += 0
        if aa == 'Arg':
            if re.search('CG[TC]', codon):
                synonymous += 3
            if re.search('CG[AG]', codon):
                synonymous += 4
            if re.search('AG[AG]', codon):
                synonymous += 2
    nonsynonymous = len(seq) * 3 - synonymous
    print('%d are synonymous, %d are nonsynonymous.' % (synonymous, nonsynonymous))
    return True
seq_2 = 'ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA'
snc(seq_2)