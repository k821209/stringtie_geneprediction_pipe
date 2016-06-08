#!/usr/bin/python

file_in = 'transcript.excluded.fa.transdecoder.cds.cdhit.pep.pfamtbl'


genelist = []
for line in open(file_in):
	if line[0] == '#':
		continue
	cell = line.strip().split()
	genelist.append(cell[3])
print len(genelist)
print len(set(genelist))
	
