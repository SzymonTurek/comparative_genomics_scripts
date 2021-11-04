print("Hello world")
from Bio import SeqIO
import pandas as pd
import os

input_seqs =  pd.read_csv('/Volumes/One_Touch/promotor_extraction/gene_upregulated.tsv', sep='\t')
df = pd.DataFrame(input_seqs)

gene_names = [gene.split(".")[2] for gene in df['Gene']]

#directories_names = os.listdir('/Volumes/One_Touch/promotor_extraction/data_B10/')
directories_names = [f for f in os.listdir('/Volumes/One_Touch/promotor_extraction/data_B10/') if not f.startswith('.')]

print(directories_names)
#os.mkdir("output_promotors")

parent_dir = '/Volumes/One_Touch/promotor_extraction/'

'''
for directory in directories_names:
    parent_dir = '/Volumes/One_Touch/promotor_extraction/'
    path = os.path.join(parent_dir, "output_promotors", "{}_output".format(directory))
    os.mkdir(path)
'''

for directory in directories_names:

    path_to_upregulated_genes = os.path.join(parent_dir, "data_B10", directory,  "gene_upregulated.tsv")
    path_to_downregulated_genes = os.path.join(parent_dir, "data_B10", directory,  "gene_downregulated.tsv")
    print(path_to_upregulated_genes)
    print(path_to_downregulated_genes)


def extract_promotor(input_seqs, path_to_output, regulation_type):
    df = pd.DataFrame(input_seqs)

    gene_names = [gene.split(".")[2] for gene in df['Gene']]
    df_minus = df
    df_plus = df
    
    for i in range(len(gene_names)):
        if "+" in df["Locus"][i]:
            df_minus = df_minus.drop(i)
        else:
            df_plus = df_plus.drop(i)



    ctg_positions_in_excel_minus = [locus.split(":")[1].split("-")[1].split("(")[0] for locus in df_minus['Locus']]
    ctg_positions_in_excel_minus_int = [int(contig_position) for contig_position in ctg_positions_in_excel_minus]

    #ctg_positions_in_excel_minus_int = ctg_positions_in_excel_minus_int[:20]
    with open(os.path.join(path_to_output, "{}_promotor_output_minuses.txt".format(regulation_type)),"w") as f:
        
            for seq_record in SeqIO.parse("/Volumes/One_Touch/promotor_extraction/sekwencje_promotorów_hybrydowa_MP.fasta", "fasta"):
                
                ctg_position_in_dataset = int(str(seq_record.id).split(":")[3].split("-")[0])
                gene_name = seq_record.name.split(":")[0]
                if gene_name in gene_names and ctg_position_in_dataset in ctg_positions_in_excel_minus_int:
                    print(seq_record)
                    SeqIO.write(seq_record, f, "fasta")


    ctg_positions_in_excel_plus = [locus.split(":")[1].split("-")[0] for locus in df_plus['Locus']]
    ctg_positions_in_excel_plus_int = [int(contig_position)-1 for contig_position in ctg_positions_in_excel_plus]

    #ctg_positions_in_excel_plus_int = ctg_positions_in_excel_plus_int[:20]
    with open(os.path.join(path_to_output, "{}_promotor_output_pluses.txt".format(regulation_type)),"w") as f:
        
            for seq_record in SeqIO.parse("/Volumes/One_Touch/promotor_extraction/sekwencje_promotorów_hybrydowa_MP.fasta", "fasta"):
                
                ctg_position_in_dataset = int(str(seq_record.id).split(":")[3].split("-")[1])
                gene_name = seq_record.name.split(":")[0]
                if gene_name in gene_names and ctg_position_in_dataset in ctg_positions_in_excel_plus_int:
                    print(seq_record)
                    SeqIO.write(seq_record, f, "fasta")


#extract_promotor(input_seqs)

for directory in directories_names:

    path_to_upregulated_genes = os.path.join(parent_dir, "data_B10", directory,  "gene_upregulated.tsv")
    path_to_downregulated_genes = os.path.join(parent_dir, "data_B10", directory,  "gene_downregulated.tsv")
    path_to_output = os.path.join(parent_dir, "output_promotors", "{}_output".format(directory))
    #print(path_to_upregulated_genes)
    #print(path_to_downregulated_genes)
    input_seqs =  pd.read_csv(path_to_upregulated_genes, sep='\t')
    extract_promotor(input_seqs, path_to_output, "upregulated" )

    input_seqs =  pd.read_csv(path_to_downregulated_genes, sep='\t')
    extract_promotor(input_seqs, path_to_output, "downregulated" )



