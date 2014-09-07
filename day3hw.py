#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it. 
"""

import sys


linecount = 0 

#result = []
data = {}
while 1: 
    line = sys.stdin.readline()
    if line == "":
        break          
    if ">" in line: 
        flyname =  line.split()[:3]
 #       print flyname 
          
    elif line.startswith("G") or line.startswith("A") or line.startswith ("T") or line.startswith("C"):
        newcount = len(line)
        linecount = linecount + newcount         
        
    if ">" in line:
#        result.append((flyname,linecount))
        data[",".join(flyname)] = linecount       
        linecount =0
    
#print data

#for item in data.items():
#    print item

import operator
sorted_data = sorted(data.iteritems(), key=operator.itemgetter(1), reverse = True)
for items in sorted_data[0:100]:
    print items[0],items[1]       
             
## this part is for finding the ORF

import aminoacidcode

#codon = 'TTG'
#aminoacid = aminoacidcode.aminoAcidMap[codon]
#print aminoacid

ORF = []
i = 0

results =[]

s = 'ATGGCATCATTTTACGGATCATAA'

def parse(i,s):
    start = i
    results = []  
    for nt in range(i,len(s),3):
        if nt > i:
            results.append(s[start:nt])
        start = nt 
    results.append(s[start:nt+3])
    return [x for x in results if len(x) == 3]

while 1:
    print parse(i,s)
    if i + 2 > len(s) or i > 1:
        break
    i = i + 1

aminoacid = aminoacidcode.aminoAcidMap[parse(i,s)]
print aminoacid

import aminoacidcode
import sys

aminoAcidMap = {'TTT' : 'F','TTC' : 'F','TTA' : 'L',
                'TTG' : 'L',
                
                'TCT' : 'S',
                'TCC' : 'S',
                'TCA' : 'S',
                'TCG' : 'S',

                'TAT' : 'Y',
                'TAC' : 'Y',
                'TAA' : '*',
                'TAG' : '*',

                'TGT' : 'C',
                'TGC' : 'C',
                'TGA' : '*',
                'TGG' : 'W',


                'CTT' : 'L',
                'CTC' : 'L',
                'CTA' : 'L',
                'CTG' : 'L',

                'CCT' : 'P',
                'CCC' : 'P',
                'CCA' : 'P',
                'CCG' : 'P',

                'CAT' : 'H',
                'CAC' : 'H',
                'CAA' : 'Q',
                'CAG' : 'Q',

                'CGT' : 'R',
                'CGC' : 'R',
                'CGA' : 'R',
                'CGG' : 'R',


                'ATT' : 'I',
                'ATC' : 'I',
                'ATA' : 'I',
                'ATG' : 'M',

                'ACT' : 'T',
                'ACC' : 'T',
                'ACA' : 'T',
                'ACG' : 'T',

                'AAT' : 'N',
                'AAC' : 'N',
                'AAA' : 'K',
                'AAG' : 'K',

                'AGT' : 'S',
                'AGC' : 'S',
                'AGA' : 'R',
                'AGG' : 'R',


                'GTT' : 'V',
                'GTC' : 'V',
                'GTA' : 'V',
                'GTG' : 'V',

                'GCT' : 'A',
                'GCC' : 'A',
                'GCA' : 'A',
                'GCG' : 'A',

                'GAT' : 'D',
                'GAC' : 'D',
                'GAA' : 'E',
                'GAG' : 'E',

                'GGT' : 'G',
                'GGC' : 'G',
                'GGA' : 'G',
                'GGG' : 'G'}

#i = 0

#aastring = []
#codon = ('TTG', 'TTT')
#for i in codon:
#    aminoacid = aminoacidcode.aminoAcidMap[i].split()
#    print aminoacid

result = ""
to_translate = sys.argv[1]

start = to_translate.find("ATG")

for i in range (0, len(to_translate), 3):
    codon = aminoAcidMap[to_translate[i:i+3]]
    if codon != "STOP":
        result += codon
    else:   
        break
        
print result 
    
    
    
      
    

    
