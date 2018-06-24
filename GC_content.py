##############################################
##############################################

# Input should be in FASTA format.

##############################################
##############################################


import os
try:
	os.remove('out.tsv')
except OSError:
	pass

import decimal
import linecache
import sys


names = ''
GC_CONTENT = ''

with open(sys.argv[1]) as file:
	dat = file.read().strip('\n').split()
	for line in dat:
		if line.startswith('>'):
			names += line.replace('>','') + '\n'


with open(sys.argv[1]) as file:
	seqs = file.read().replace('\n','').replace('>','\n').replace('Rosalind_','').strip()


	for line in seqs.split():
			
		AT = line.count('A') + line.count('T')
		GC = line.count('G') + line.count('C') 
		

		AT = decimal.Decimal(AT)
		GC = decimal.Decimal(GC)

		GC_content = 100 * GC/(AT + GC)
		GC_CONTENT += str(round(GC_content, 7)) + '\n'

with open('out_names.tsv', 'a') as out:
	out.write(names)

with open('out.tsv', 'a') as out:
	out.write(GC_CONTENT)




line_number = 1
with open('out.tsv') as file, open('out_names.tsv') as file2, open('output.tsv', 'w') as file3:
	for line in file:
		file3.write (linecache.getline('out_names.tsv', line_number).strip() + '\t' + linecache.getline('out.tsv', line_number).strip() + '\n')
		line_number = line_number + 1

bashCommand = 'sort -rnk 2 output.tsv'
os.system(bashCommand)


bashCommand = 'rm -f out.tsv && rm -f out_names.tsv'
os.system(bashCommand)