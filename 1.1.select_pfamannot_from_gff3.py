#!/usr/bin/python
# considering pfam annotation
from __future__ import print_function
import sys
sys.path.append('/ref/analysis/pipelines/')
import kang

file_cdhitpfam = 'pfam.domtblout'
file_cdhitfa   = 'transcripts.fasta.transdecoder.cds.cdhit'
Gene_list       = []
Transcript_list = []

for line in open(file_cdhitpfam):
	if line[0] == '#':
		continue
	
	cell = line.split()
	Gene_list.append(cell[3].replace('m','g'))
	Transcript_list.append(cell[3])

Gene_list       = set(Gene_list)
Transcript_list = set(Transcript_list)



dicFa = kang.Fasta2dic(file_cdhitfa)
dicFa_new = {}
for gene in dicFa:
	if gene in Transcript_list:
		dicFa_new[gene] = dicFa[gene]
kang.dic2fa(dicFa_new,file_cdhitfa+'.pfamfilt.fa')



file_gff = 'transcripts.fasta.transdecoder.gff3'
Outfile = open(file_gff+'.cdhit.pfamfilt.gff3','w')
for line in open(file_gff):
	if line.strip() == '':
		continue
	cell    = line.strip().split('\t')
	strT    = cell[2]
	info    = cell[-1]
	dicinfo = dict(zip([x.split('=')[0] for x in info.split(';')],[x.split('=')[1] for x in info.split(';')]))
	if strT == 'gene':
		if dicinfo['ID'] in Gene_list:
			print(line.strip(),file=Outfile)
	elif strT == 'mRNA':
		if dicinfo['ID'] in Transcript_list:
			print(line.strip(),file=Outfile)
	else:
		if dicinfo['Parent'] in Transcript_list:
                        print(line.strip(),file=Outfile)
		

