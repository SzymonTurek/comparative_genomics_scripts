#!/bin/bash

SAMPLES="SRR6008648_1 SRR6008648_2"

mkdir fastqc_output_raw_data
 
for sample in $SAMPLES; do
    docker run --platform linux/amd64 -it --rm -v $(pwd):/data  staphb/fastqc:0.11.9 fastqc -t 4 -o /data /data/${sample}.fastq.gz
done

mv *.html *fastqc.zip fastqc_output_raw_data/

