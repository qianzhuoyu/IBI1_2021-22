import re

file1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
file1_read = file1.read()
file1_split = re.split('>', file1_read)
select_genes = []
for i in range(len(file1_split)):  # find all gene sequences which contain 'GAATTC'
    if 'GAATTC' in file1_split[i]:
        select_genes.append(file1_split[i])

file2 = input(' please input your file name:')  # ask the user to input a filename as the new file to be written to
file3 = open("%s.fa" % file2, 'w')
f = 0
for i in range(0, len(select_genes)):
    sequence = re.sub(r'.+]', '', select_genes[i])  # delete everything that's irrelevant except the gene sequence
    one_line_sequence = re.sub(r'\n', '', sequence)  # delete '\n', to show the entire sequence on one line
    fragment = re.split('GAATTC', one_line_sequence)  # cut the sequence, 'GAATTC' is intermedium
    length = len(fragment)
    gene_name = re.findall(r'gene:.+?\s', select_genes[i])  # extract the gene name
    str_gene_name = ''.join(gene_name)
    file3.write(str_gene_name)
    file3.write('          ')
    file3.write(str(length))
    file3.write('\n')
    file3.write(one_line_sequence)  # show the entire sequence on one line
    file3.write('\n')
file3.close()
