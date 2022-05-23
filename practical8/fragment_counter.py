import re

seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
counter = re.findall(r'GAATTC', seq)  # find all 'GAATTC' in target sequence
print(len(counter) + 1)  # prints the length of all fragments
