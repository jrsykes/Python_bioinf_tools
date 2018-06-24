
from Bio import SeqIO
import os
import linecache
import math

n_seqs = 0

with open('input.txt', 'rU') as file:
	for record in SeqIO.parse(file, 'fasta'):
		with open('temp_seq', 'a') as file_seq, open('temp_rec', 'a') as file_id:
			seq = str(record.seq)
			file_seq.write(seq + '\n')
			n_seqs = n_seqs + 1
			n_seqs2 = n_seqs
			rec = str(record.id)
			file_id.write(rec + '\n')
n_seqs2_external = n_seqs

loop_counter = 0
line_number_ref = 0
with open('input.txt', 'rU') as file, open('temp_seq', 'r') as file_seq, open('temp_rec', 'r') as file_id:
	ids = file_id.readlines()
	while n_seqs > 0:
		line_number_ref = line_number_ref + 1
		ref = linecache.getline('temp_seq', line_number_ref).strip()
		length_ref = len(ref)
		line_number_qu = 0
		n_seqs2_internal = n_seqs2_external
		while line_number_qu < n_seqs2_internal:
			loop_counter = loop_counter + 1
			line_number_qu = line_number_qu + 1
			qu = linecache.getline('temp_seq', line_number_qu).strip()
			if ref != qu and ref[length_ref-3:length_ref] == qu[0:3]:
				print ids[line_number_ref - 1].strip() + ' ' + ids[line_number_qu - 1].strip()
		n_seqs = n_seqs - 1

bashCommand = 'rm -f temp_seq && rm -f temp_rec'
os.system(bashCommand)

