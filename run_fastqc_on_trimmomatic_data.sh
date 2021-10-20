!/bin/bash

SAMPLES="SRR6008648_1 SRR6008648_2"
data_directory="trimmomatic_output"
mkdir fastqc_output_trimmomatic_data
 
for sample in $SAMPLES; do
    docker run --platform linux/amd64 -it --rm -v $(pwd)/${data_directory}:/data  staphb/fastqc:0.11.9 fastqc -t 4 -o /data /data/${sample}.trim.fastq.gz
done

mv ./${data_directory}/*.html fastqc_output_trimmomatic_data/
mv ./${data_directory}/*fastqc.zip fastqc_output_trimmomatic_data/

