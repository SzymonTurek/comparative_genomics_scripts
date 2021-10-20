#!/bin/bash

SAMPLE1="SRR6008648_1"
SAMPLE2="SRR6008648_2"
mkdir fastp_output_genome


docker run --platform linux/amd64 -it --rm -v $(pwd):/data nanozoo/fastp:0.20.0--78a7c63 fastp -i /data/${SAMPLE1}.fastq.gz -I /data/${SAMPLE2}.fastq.gz -o /data/fastp_output_genome/out_${SAMPLE1}.fastq.gz -O /data/fastp_output_genome/out_${SAMPLE2}.fastq.gz




