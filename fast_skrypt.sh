#!/bin/bash

SAMPLES="SRR6008648_2"

for sample in $SAMPLES; do
    docker run --platform linux/amd64 -it --rm -v $(pwd)/data_input:/data  staphb/fastqc:0.11.9 fastqc -t 4 -o /data /data/${sample}.fastq.gz
done
