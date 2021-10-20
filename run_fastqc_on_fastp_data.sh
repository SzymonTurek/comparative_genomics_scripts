!/bin/bash

SAMPLES="SRR6008648_1 SRR6008648_2"

mkdir fastqc_output_fastp_data
 
for sample in $SAMPLES; do
    docker run --platform linux/amd64 -it --rm -v $(pwd)/fastp_output_genome:/data  staphb/fastqc:0.11.9 fastqc -t 4 -o /data /data/out_${sample}.fastq.gz
done

mv ./fastp_output_genome/*.html fastqc_output_fastp_data/
mv ./fastp_output_genome/*fastqc.zip fastqc_output_fastp_data/

