print "Programme not yet ready for use. Take a nap, you deserve it"
quit()

from Bio import SeqIO
import os
import linecache
from decimal import *
getcontext().prec = 5
import math
import re
import sys

bashCommand = 'rm -f temp_seq'
os.system(bashCommand)

n_seqs = 0

with open('input.txt', 'rU') as file:
	for record in SeqIO.parse(file, 'fasta'):
		with open('temp_seq', 'a+') as file_seq:
			seq = str(record.seq)
			file_seq.write(seq + '\n')
			n_seqs = n_seqs + 1

line_number_ref = 0
convergence_ratio = 1
n_seqs_original = n_seqs
n_seqs_original_inclusion_counter = n_seqs

with open('temp_seq', 'r') as file_seq:
	max_length = len(max(file_seq, key=len)) - 1
	
not_in_counter = 0

while n_seqs_original_inclusion_counter > 0:
	with open('temp_seq', 'a+') as file_seq:
		match = 1
		no_match = 0
		line_number_ref = line_number_ref + 1
		ref = linecache.getline('temp_seq', line_number_ref).strip()
		linecache.clearcache()
		length_ref = len(ref)
		line_number_qu = 0
		while line_number_qu < n_seqs:
			line_number_qu = line_number_qu + 1
			qu = linecache.getline('temp_seq', line_number_qu).strip()
			linecache.clearcache()
			k_mer = length_ref / 2
			while k_mer < max_length:
				overlap = length_ref - k_mer
				if ref != qu and ref[overlap:length_ref] == qu[0:k_mer]:
					file_seq.write(ref[0:overlap] + qu + '\n')
					n_seqs = n_seqs + 1
				k_mer = k_mer + 1	
	with open('temp_seq', 'r') as file:
		longest_contig = max(file, key=len)
		print 'Longest contig:' + longest_contig
		max_length = len(longest_contig) - 1
		n_seqs_original_inclusion_counter = n_seqs_original
	with open('input.txt', 'r') as fragments:	
		for line in fragments:
			if line.strip() in longest_contig:
				print line
				n_seqs_original_inclusion_counter = n_seqs_original_inclusion_counter - 1
			elif line.strip() not in longest_contig:
				not_in_counter = not_in_counter + 1
		if not_in_counter > 10000:
			break

	print 'Number of sequences:' + ' ' + str(n_seqs) + '\n' + '*******************'
	n_seqs_original_inclusion_counter = n_seqs


with open('temp_seq', 'r') as seq_files:
	print '\n' + 'Complete contig:' + '\n' + max(seq_files, key=len).strip()
	print '\n' + 'Number of sequences:' + ' ' + str(n_seqs) + '\n'

bashCommand = 'rm -f temp_seq'
os.system(bashCommand)