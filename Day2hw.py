#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import sys, csv, operator

cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"
df = pd.read_table(cufflinks_output)
df2 = pd.read_table(cufflinks_output2)

#data = list(df["FPKM"])
data = [x for x in list(df["FPKM"]) if x > 0]

data.sort()

seg = int(len(data)/3)
print seg


oput_part1 = data [0:seg]
oput_part2 = data [seg:seg*2]
oput_part3 = data [seg*2:]

SRR_893 = [oput_part1, oput_part2, oput_part3]
plt.figure()
plt.boxplot (SRR_893)
plt.savefig ("boxplotSRR893_1.png")

#data = list(df2["FPKM"])
data2 = [x for x in list(df2["FPKM"]) if x > 0]

data2.sort()

seg = int(len(data2)/3)
print seg


oput_part4 = data2 [0:seg]
oput_part5 = data2 [seg:seg*2]
oput_part6 = data2 [seg*2:]

SRR_915 = [oput_part4, oput_part5, oput_part6]
plt.figure()
plt.boxplot (SRR_915)
plt.savefig ("boxplotSRR915_1.png")

#This is for problem 2 & 3

f = open("day2hw2_metadata.txt")

names = []
for line in f.readlines():
	line = line.strip()
	data = line.split(',')
	if data [1] == 'female':
		names.append("%s_clout" % data [0])
f.close()

root = "/Users/cmdb/data/results/"
filename = "genes.fpkm_tracking"

result = []

for dirname in names:
	datapath = "%s/%s/%s" % (root, dirname,filename)
	f = open(datapath)
	for line in f.readlines():
		data = line.split("\t")
		if data and data[6].startswith("dme"):
			result.append(data[9])
	f.close()
			
w = open("/Users/cmdb/data/day2/hw2prob3.txt","w")
w.write(",".join(result))
w.close()

import matplotlib.pyplot as plt
plt.figure()
plt.plot(result)
plt.show()





