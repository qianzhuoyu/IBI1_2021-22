import re

file1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
file1_read = file1.read()
file1_split = re.split('>', file1_read)
select_genes = []
for i in range(len(file1_split)):  # find all gene sequences which contain 'GAATTC'
    if 'GAATTC' in file1_split[i]:
        select_genes.append(file1_split[i])

cut_genes = open('cut_genes.fa', 'w')
for i in range(len(select_genes)):
    gene_name = re.findall(r'gene:.+?\s', select_genes[i])  # find the genes' names in every selected genes
    sequence = re.sub(r'.+]', '', select_genes[i])  # delete everything that's irrelevant except the gene sequence
    one_line_sequence = re.sub(r'\n', '', sequence)
    length = len(select_genes[i])
    str_gene_name = ''.join(gene_name)
    cut_genes.write(str_gene_name)  # write down the names
    cut_genes.write(str(length))  # write down the length
    cut_genes.write('\n')
cut_genes.close()

