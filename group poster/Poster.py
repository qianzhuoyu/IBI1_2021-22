import re

# Create a dictionary of codons.
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

print('The function is only for upper-case sequences.')
choose = input(
    "If you want to type the sequence directly, please type 'seq'; if the sequence is in a file, please type 'file': ")
if choose == 'seq':
    seq = input('Type the sequence here: ')
else:
    fname = input('Type the file name here: ')
    file = open(fname)
    seq = file.read()


# 1. Mutational consequences


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


"""
Example
Origin seq:
YGR242W_mRNA cdna
ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA

Mutated seq:
ATGGCCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTGGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTAGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACATACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAACAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA

"""
ori_seq_1 = 'ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA'
mut_seq_1 = 'ATGGCCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTGGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTAGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACATACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAACAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA'

mc(ori_seq_1, mut_seq_1)


# 2. Synonymous vs Nonsynonymous Calculator


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


"""
Example
YGR242W_mRNA cdna
ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA
"""
seq_2 = 'ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA'
snc(seq_2)


# 3. Vulnerability to truncating mutations


def tm(seq):  # tm = truncating mutation
    print('There are %d possible single point mutations in total.' % (len(seq) * 3))
    n = 0
    stop = 0
    for i in range(0, len(seq) // 3 - 1):
        codon = seq[n:n + 3]
        n += 3
        if re.search('[AGC]AA|T[CT]A|TA[CT]', codon):
            stop += 1
        if re.search('[AGC]AG|T[GCT]G|TA[CT]', codon):
            stop += 1
        if re.search('[AGC]GA|T[CT]A|TG[GCT]', codon):
            stop += 1
    fragment = stop / (len(seq) * 3)
    print('Among them, %d are truncating mutations. The fraction is %.6f.' % (stop, fragment))  # Six decimals.
    return True


"""
Example
YGR242W_mRNA cdna
ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA
"""
seq_3 = 'ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA'
tm(seq_3)


# 4. Transitions vs Transversions


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


"""
Example
YGR242W_mRNA cdna
ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA
"""
seq_4 = 'ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA'
tt(seq_4)

amino_acid_mass = {'Phe': 165, 'Leu': 131, 'Ile': 131, 'Met': 149, 'Val': 117, 'Ser': 105, 'Pro': 115, 'Thr': 119,
                   'Ala': 89,
                   'Tyr': 181, 'His': 155, 'Gln': 146, 'Asn': 132, 'Lys': 142, 'Asp': 133, 'Glu': 147, 'Cys': 121,
                   'Trp': 204, 'Arg': 174, 'Gly': 75, 'stop': 0}


def aam(seq):  # am = amino_acid_mass
    n = 0
    pre_mass = 0
    mass = 0
    for i in range(len(seq) // 3):
        codon = seq[n:n + 3]
        aa = codons[codon]
        pre_mass += amino_acid_mass[aa]
        n += 3
    mass = pre_mass - (len(seq) / 3 - 2) * 18
    return 'The mass is' + str(mass)

# print(aam(seq_4))
