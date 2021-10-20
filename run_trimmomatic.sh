#!/bin/bash

SAMPLE1="SRR6008648_1"
SAMPLE2="SRR6008648_2"
mkdir trimmomatic_output

docker run --platform linux/amd64 -it --rm -v $(pwd):/data staphb/trimmomatic:0.39 trimmomatic PE /data/${SAMPLE1}.fastq.gz /data/${SAMPLE2}.fastq.gz /data/${SAMPLE1}.trim.fastq.gz /data/${SAMPLE1}un.trim.fastq.gz /data/${SAMPLE2}.trim.fastq.gz /data/${SAMPLE2}un.trim.fastq.gz ILLUMINACLIP:/Trimmomatic-0.39/adapters/NexteraPE-PE.fa:2:40:15

mv ${SAMPLE1}.trim.fastq.gz ${SAMPLE1}un.trim.fastq.gz ${SAMPLE2}.trim.fastq.gz ${SAMPLE2}un.trim.fastq.gz trimmomatic_output/


