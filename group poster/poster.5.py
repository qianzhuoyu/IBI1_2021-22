amino_acid_weight = {'Phe': 165, 'Leu': 131, 'Ile': 131, 'Met': 149, 'Val': 117, 'Ser': 105, 'Pro': 115, 'Thr': 119,
                   'Ala': 89,
                   'Tyr': 181, 'His': 155, 'Gln': 146, 'Asn': 132, 'Lys': 142, 'Asp': 133, 'Glu': 147, 'Cys': 121,
                   'Trp': 204, 'Arg': 174, 'Gly': 75, 'stop': 0}

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


# 5 based on the cDNA sequence to get the  molecular mass of the proteins. only for single chain proteins.
def aam(seq):  # am = amino_acid_mass
    n = 0
    pre_weight = 0  # pre_mass is the sum of the molecular mass of all individual amino acids.
    mass = 0  # mass is the molecular mass of the protein
    for i in range(len(seq) // 3):
        codon = seq[n:n + 3]
        aa = codons[codon]  # aa = amino acid
        pre_weight += amino_acid_weight[aa]  # Calculate the sum of the  molecular mass of all individual amino acids
        n += 3
    molecular_weight = pre_weight - (len(seq) // 3 - 2) * 18  # Minus the molecular mass of the water removed
    return 'The molecular weight is ' + str(molecular_weight)


# example:
seq_4 = 'ATGGTCCAGGCTGTATCAGACAACCTTATATCCAATGCGTGGGTAATCTCTTGCAATCCTCTTGCGCTCGAAGTGCCCGAGAGAATAGGGTCCACATATTTTTGCTTTGGAGGGGCCATCTTTATTTTGGTCGCCCCTTTAACCAACTTAGTATATAATGAAGACATTGTTTCACAAACACGCCTCTATATCTATTATAGGGGTAGCCGAGACAGTCGCGCTTGTATGCTTGATATTGTTACTCTCGTAGATGTTAGCAAGCGTAGCAAATTGGTACTCCTGCTACAGATTTATTTTTTCTCCTTCTAA'
print(aam(seq_4))
