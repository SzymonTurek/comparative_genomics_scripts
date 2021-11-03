print("Hello world")
from Bio import SeqIO
import pandas as pd
import re

#my_sheet = 'Sheet1'
#file_name = '/Volumes/One_Touch/promotor_extraction/gene_upregulated.xls'
#df = read_excel(file_name, sheet_name = my_sheet, engine='openpyxl')

#gene_name = df[:1]
#print(gene_name)
#fasta_sequences = SeqIO.parse(open('/Volumes/One_Touch/promotor_extraction/sekwencje_promotorów_hybrydowa_MP.fasta'),'fasta')

input_seqs =  pd.read_csv('/Volumes/One_Touch/promotor_extraction/gene_upregulated.tsv', sep='\t')
#print(input_seqs)
df = pd.DataFrame(input_seqs)
#for gene in df['Gene']:
#    gene_names = gene.split(".")[2]


gene_names = [gene.split(".")[2] for gene in df['Gene']]
#print(gene_names)

ctg_positions_in_excel = [locus.split(":")[1].split("-")[0] for locus in df['Locus']]
ctg_positions_in_excel_int = [int(contig_position) -1 for contig_position in ctg_positions_in_excel]
#print(ctg_positions_in_excel_int[:10])

ctg_positions_in_excel_int = ctg_positions_in_excel_int[:20]

locus_type = [locus.split(":")[1].split("-")[1].split("(")[1] for locus in df['Locus']]
#print(locus_type)

plus_promotors = pd.DataFrame()
minus_promotors = []


#minus_promotors = df[~df["Locus"].isin(['(-)'])]
#discard = ["+"]
#minus_promotors = df[~df.Locus.str.contains('|'.join(discard))]
#print(df["Locus"])

#print(minus_promotors)
#print(df["Locus"])

df_minus = df
for i in range(len(locus_type)):
    if "+" in df["Locus"][i]:
        #print(df["Locus"][i])
        #print(df.loc[[i]])
        df_minus = df_minus.drop(i)
print(df_minus["Locus"][:10])
    #if locus_type[i] == "+)":
        #plus_promotors = df.iloc[[i]])
        #df1.loc[df2.index[0]] = df2.iloc[0]
#        pass
#    else:
#        minus_promotors.append(df.iloc[[i]])


ctg_positions_in_excel_minus = [locus.split(":")[1].split("-")[1].split("(")[0] for locus in df_minus['Locus']]
print(ctg_positions_in_excel_minus[:10])
ctg_positions_in_excel_minus_int = [int(contig_position) for contig_position in ctg_positions_in_excel_minus]
print(ctg_positions_in_excel_minus_int[:10])

ctg_positions_in_excel_minus_int = ctg_positions_in_excel_minus_int[:20]
print(ctg_positions_in_excel_minus_int)
with open("/Volumes/One_Touch/promotor_extraction/promotor_output_minuses.txt","w") as f:
       
        for seq_record in SeqIO.parse("/Volumes/One_Touch/promotor_extraction/sekwencje_promotorów_hybrydowa_MP.fasta", "fasta"):
            
            ctg_position_in_dataset = int(str(seq_record.id).split(":")[3].split("-")[0])
            #print(ctg_position_in_dataset)
            gene_name = seq_record.name.split(":")[0]
            #print(gene_name)
            if gene_name in gene_names and ctg_position_in_dataset in ctg_positions_in_excel_minus_int:
                print(seq_record)
                SeqIO.write(seq_record, f, "fasta")
#print(plus_promotors[0])
#print(plus_promotors[1])
#print(minus_promotors[0])

#df2 = pd.DataFrame(plus_promotors)
#print(df2)
'''
with open("/Volumes/One_Touch/promotor_extraction/promotor_output.txt","w") as f:
       
        for seq_record in SeqIO.parse("/Volumes/One_Touch/promotor_extraction/sekwencje_promotorów_hybrydowa_MP.fasta", "fasta"):
            
            ctg_position_in_dataset = int(str(seq_record.id).split(":")[3].split("-")[1])
            #print(ctg_position_in_dataset)
            gene_name = seq_record.name.split(":")[0]
            #print(gene_name)
            if gene_name in gene_names and ctg_position_in_dataset in ctg_positions_in_excel_int:
                print(seq_record)
                SeqIO.write(seq_record, f, "fasta")
'''

#for i in range(len(locus_type)):
#    if locus_type[i] == "+)":
#        #print(locus_type[i], gene_names[i])
#        with open("/Volumes/One_Touch/promotor_extraction/promotor_output.txt","w") as f:
#            for seq_record in SeqIO.parse("/Volumes/One_Touch/promotor_extraction/sekwencje_promotorów_hybrydowa_MP.fasta", "fasta"):
#                ctg_position_in_dataset = int(str(seq_record.id).split(":")[3].split("-")[1])
#                gene_name = seq_record.name.split(":")[0]
#                if gene_name == gene_names[i] and ctg_position_in_dataset == ctg_positions_in_excel_int[i]:
#                    SeqIO.write(seq_record, f, "fasta")
#    if locus_type[i] == "":
#        #print(locus_type[i], gene_names[i])
#        pass







'''



with open("/Volumes/One_Touch/promotor_extraction/promotor_output.txt","w") as f:
       
        for seq_record in SeqIO.parse("/Volumes/One_Touch/promotor_extraction/sekwencje_promotorów_hybrydowa_MP.fasta", "fasta"):
            
            ctg_position_in_dataset = int(str(seq_record.id).split(":")[3].split("-")[1])
            #print(ctg_position_in_dataset)
            gene_name = seq_record.name.split(":")[0]
            #print(gene_name)
            if gene_name in gene_names and ctg_position_in_dataset in ctg_positions_in_excel_int:
                print(seq_record)
                SeqIO.write(seq_record, f, "fasta")
          
          
'''       
          
'''
          
            #print(seq_record)
            #f.write(str(seq_record.seq[:10]) + "\n")  #first 10 base positions
            #print(seq_record.name)
            #ctg_position_in_dataset = str(seq_record.id).split(":")[3].split("-")[0]
            
            
            for locus in df['Locus']:
                ctg_position_in_excel = locus.split(":")[1].split("-")[0]
                #print(ctg_position_in_excel)
                ctg_position_in_excel_int = int(ctg_position_in_excel) - 1
                if(ctg_position_in_excel_int == ctg_position_in_dataset):
                    print(seq_record)
            
            
            #ctg_position = str(seq_record.id).split(":")
            
            #print(ctg_position_in_dataset)
            if "G18110" in seq_record.name:
                #print(seq_record) 
                pass
input_seqs =  pd.read_csv('/Volumes/One_Touch/promotor_extraction/gene_upregulated.tsv', sep='\t')
df = pd.DataFrame(input_seqs)
#first_coulmn = df.iloc[:,0]
#for word in first_column:
#print(first_coulmn)
#print(input_seqs)
#print(df['Locus'])
#for gene in df['Gene']:
#    print(gene.split(".")[2])
for locus in df['Locus'][:10]:
    print(locus.split(":")[1].split("-")[0])
#print(df['Gene'].split(".")[2])
'''