BAM=intron3000.merge.sorted.bam.excluded.cor.ver1.bam
REF=/ref/analysis/References/Creinhardtii/Creinhardtii_281_v5.0.fa
PFAM=/ref/analysis/References/Pfam-A.hmm


STRINGTIE_LOC=/program/stringtie-1.2.2.Linux_x86_64/
TRANSDECR_LOC=/program/TransDecoder-2.1.0/


${STRINGTIE_LOC}stringtie -p 10 -o ${BAM}.gff ${BAM}  # (1) stringtie assembly
${TRANSDECR_LOC}util/cufflinks_gtf_to_alignment_gff3.pl ${BAM}.gff > ${BAM}.gff.gff3
${TRANSDECR_LOC}util/cufflinks_gtf_genome_to_cdna_fasta.pl ${BAM}.gff ${REF} > transcripts.fasta
${TRANSDECR_LOC}TransDecoder.LongOrfs -S -t transcripts.fasta  
hmmscan --cpu 8 --domtblout pfam.domtblout ${PFAM} transcripts.fasta.transdecoder_dir/longest_orfs.pep
${TRANSDECR_LOC}TransDecoder.Predict --cpu 10 -t transcripts.fasta --retain_pfam_hits pfam.domtblout
cd-hit-est -i transcripts.fasta.transdecoder.cds -o transcripts.fasta.transdecoder.cds.cdhit -T 10 
python 1.select_cdhit_from_gff3.py
python 1.1.select_pfamannot_from_gff3.py
${TRANSDECR_LOC}util/cdna_alignment_orf_to_genome_orf.pl transcripts.fasta.transdecoder.gff3.cdhit.pfamfilt.gff3 ${BAM}.gff.gff3 transcripts.fasta > transcripts.fasta.transdecoder.gff3.cdhit.pfamfilt.gff3.genome.gff3
${TRANSDECR_LOC}util/cdna_alignment_orf_to_genome_orf.pl transcripts.fasta.transdecoder.gff3.cdhit.gff3 ${BAM}.gff.gff3 transcripts.fasta > transcripts.fasta.transdecoder.gff3.cdhit.gff3.genome.gff3
python 3.gene_feature_redundel.py transcripts.fasta.transdecoder.gff3.cdhit.pfamfilt.gff3.genome.gff3
python 3.gene_feature_redundel.py transcripts.fasta.transdecoder.gff3.cdhit.gff3.genome.gff3
