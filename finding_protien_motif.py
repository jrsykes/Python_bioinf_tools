##############################################
##############################################
#Set to download a list of named protiens, find the N-glycosylation motif: N{P}[ST]{P} and report all positions.
#Run using the command 'python finding_protien_motif.py input.txt'
#
# Example data: 
# Input: 		P28653_PGS1_MOUSE
#			P81447_MPP3_CAPHI
#			P01047_KNL2_BOVIN
#			Q7S432
#			Q5PA87
#			P28314_PER_COPCI

# Output: 		P28653_PGS1_MOUSE
#			271 312
#			P81447_MPP3_CAPHI
#			96
#			P01047_KNL2_BOVIN
#			47 87 168 169 197 204 280
#			Q7S432
#			173
#			P28314_PER_COPCI
#			162

##############################################
##############################################


import os
import wget
from Bio import SeqIO
import re
import sys

with open(sys.argv[1]) as file:


	bashCommand = 'rm -f protiens.dat'
	os.system(bashCommand)
	bashCommand = 'touch protiens.dat'
	os.system(bashCommand)


	dat = file.readlines()
	for line in dat:
		wget.download('http://www.uniprot.org/uniprot/' + line.strip() + '.fasta')
		bashCommand = 'cat *.fasta >> protiens.dat && rm -f *.fasta'
		os.system(bashCommand)
		print '\n'

ID_line = -1
with open('protiens.dat', 'rU') as file:
	for record in SeqIO.parse(file, 'fasta'):
		ID = (str(record.id[3:]).replace('|', '_'))
		p = re.compile('N''[^P]''[ST]''[^P]')
		ID_line = ID_line + 1


		iterator2 = p.finditer(str(record.seq))
		motif_or_no = 0
		for match in iterator2:
			motif_or_no = motif_or_no + 1
		if motif_or_no > 0:
			print dat[ID_line].strip()

		length = len(str(record.seq))
		S = 0
		E = 4
		loci = ''
		while length > 3:
			iterator = p.finditer(str(record.seq[S:E]))
			length = length - 1
			S = S + 1
			E = E + 1
			for match in iterator:
				if match:
					loci = loci + ' ' + str(S)
		print loci[1:]




		
		
		
		
		
bashCommand = 'rm -f *.fasta & rm -f protiens.dat'

os.system(bashCommand)
