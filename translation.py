#!/usr/bin/python3 
# description : CDS to protein 
# usage       : python3 [thisfile] [fasta] [outfile]

import kang,sys

dicHD2seq = kang.Fasta2dic(sys.argv[1])
Outfile	= open(sys.argv[2],'w')
for strHD in dicHD2seq:
	seq = dicHD2seq[strHD]
	if len(seq) < 5:
		continue
	print('>'+strHD,file=Outfile)
	print(kang.translation(seq).strip('*'),file=Outfile)
