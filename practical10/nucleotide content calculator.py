import re


def calculator(dna):
    length = len(dna)  # court the length of dna
    A = re.findall(r'A|a', dna)  # find upper case or lower case in the DNA sequence
    T = re.findall(r'T|t', dna)
    C = re.findall(r'C|c', dna)
    G = re.findall(r'G|g', dna)
    lenA = len(A)
    lenT = len(T)
    lenC = len(C)
    lenG = len(G)
    # Calculate the percentage of each nucleotide
    percent_A = int(lenA) / int(length)
    percent_T = int(lenT) / int(length)
    percent_C = int(lenC) / int(length)
    percent_G = int(lenG) / int(length)
    # return the percent of A, T, C and G
    return 'A:' + str(percent_A),\
           'T:' + str(percent_T),\
           'C:' + str(percent_C),\
           'G:' + str(percent_G)


# example
dna = 'AaTtGgGCCC'
print(calculator(dna))
