print("Hello world")
from Bio import SeqIO
import pandas as pd

input_seqs =  pd.read_csv('/Volumes/One_Touch/promotor_extraction/gene_upregulated.tsv', sep='\t')
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
with open("/Volumes/One_Touch/promotor_extraction/promotor_output_minuses.txt","w") as f:
       
        for seq_record in SeqIO.parse("/Volumes/One_Touch/promotor_extraction/sekwencje_promotorów_hybrydowa_MP.fasta", "fasta"):
            
            ctg_position_in_dataset = int(str(seq_record.id).split(":")[3].split("-")[0])
            gene_name = seq_record.name.split(":")[0]
            if gene_name in gene_names and ctg_position_in_dataset in ctg_positions_in_excel_minus_int:
                print(seq_record)
                SeqIO.write(seq_record, f, "fasta")


ctg_positions_in_excel_plus = [locus.split(":")[1].split("-")[0] for locus in df_plus['Locus']]
ctg_positions_in_excel_plus_int = [int(contig_position)-1 for contig_position in ctg_positions_in_excel_plus]

#ctg_positions_in_excel_plus_int = ctg_positions_in_excel_plus_int[:20]
with open("/Volumes/One_Touch/promotor_extraction/promotor_output_pluses.txt","w") as f:
       
        for seq_record in SeqIO.parse("/Volumes/One_Touch/promotor_extraction/sekwencje_promotorów_hybrydowa_MP.fasta", "fasta"):
            
            ctg_position_in_dataset = int(str(seq_record.id).split(":")[3].split("-")[1])
            gene_name = seq_record.name.split(":")[0]
            if gene_name in gene_names and ctg_position_in_dataset in ctg_positions_in_excel_plus_int:
                print(seq_record)
                SeqIO.write(seq_record, f, "fasta")

