#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
fly_gene=SRR072

GENOME_DIR=/Users/cmdb/data/genomes
file =d mel5
ANNOTATION=dmel-all-r5.57.gff

CORES=4

for i in {1..24} 
do
  echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR: $i
  echo tophat: -p4 -G/Users/cmdb/data/day1/dmel-all-r5.57.gff -o/Users/cmdb/data/day1/ --no-novel-juncs --segment-length 20 /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57 /Users/cmdb/data/day1/SRR072893.fastq: $i
  echo cufflinks: $i
done
