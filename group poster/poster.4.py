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


def tt(seq):  # tt = Transitions and Transversions
    n = 0
    transitional_change = 0
    transversional_change = 0
    for i in range(0, len(seq) // 3):
        codon = seq[n:n + 3]
        n += 3
        aa = codons[codon]  # aa = amino acid
        if re.search('Phe|Tyr|His|Gln|Asn|Lys|Asp|Glu|Cys', aa):
            transitional_change += 2
            transversional_change += 6
        if aa == 'Leu':
            if re.search('TT[AG]', codon):
                transitional_change += 1
                transversional_change += 6
            if re.search('CT[TC]', codon):
                transitional_change += 2
                transversional_change += 4
            if re.search('CT[AG]', codon):
                transitional_change += 1
                transversional_change += 4
        if aa == 'Ile':
            if re.search('AT[TC]', codon):
                transitional_change += 2
                transversional_change += 5
            if re.search('ATA', codon):
                transitional_change += 3
                transversional_change += 4
        if re.search('Met|Trp', aa):
            transitional_change += 3
            transversional_change += 6
        if re.search('Val|Pro|Thr|Ala|Gly', aa):
            transitional_change += 2
            transversional_change += 4
        if aa == 'Ser':
            if re.search('TC[TCAG]', codon):
                transitional_change += 2
                transversional_change += 4
            if re.search('AG[TC]', codon):
                transitional_change += 2
                transversional_change += 6
        if aa == 'stop':
            if re.search('TAG|TGA', codon):
                transitional_change += 2
                transversional_change += 6
            if codon == 'TAA':
                transitional_change += 1
                transversional_change += 6
        if aa == 'Arg':
            if re.search('CG[TC]', codon):
                transitional_change += 2
                transversional_change += 4
            if re.search('CG[AG]', codon):
                transitional_change += 2
                transversional_change += 3
            if re.search('AG[AG]', codon):
                transitional_change += 2
                transversional_change += 5
    print(
        'Among all possible single mutations, %d transitions result amino acid change, %d transversions result amino acid change.' % (
            transitional_change, transversional_change))
    if transitional_change > transversional_change:
        print('Transitional mutations are more damaging to the encoded protein.')
    if transitional_change < transversional_change:
        print('Transversional mutations are more damaging to the encoded protein.')
    if transitional_change == transversional_change:
        print('Transitional mutations and transversional mutations have equal influence on the encoded protein.')
seq_4 = 'ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA'
tt(seq_4)
