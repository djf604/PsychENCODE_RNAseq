import sys

input_file_path = sys.argv[1]
cufflinks_genes = {}
bid_headers = []
with open(input_file_path) as cufflinks_file:
    for line in cufflinks_file:
        cufflinks_file_path, bid = line.rstrip('\n').split(';')
        bid_headers.append(bid)
        with open(cufflinks_file_path) as cufflinks_fpkm:
            for line in cufflinks_fpkm:
                gene_line = line.rstrip('\n').split('\t')
                (gene_name, gene_fpkm) = (gene_line[4], gene_line[9])
                if gene_name not in cufflinks_genes:
                    cufflinks_genes[gene_name] = {}
                cufflinks_genes[gene_name][bid] = gene_fpkm

print '\t'.join(['gene_name'] + bid_headers)

for gene_name in cufflinks_genes:
    gene_line = [gene_name]
    for bid in bid_headers:
        if bid in cufflinks_genes[gene_name]:
            gene_line.append(cufflinks_genes[gene_name][bid])
        else:
            gene_line.append('')
    print '\t'.join(gene_line)
    
