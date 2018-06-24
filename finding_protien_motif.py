import os
import wget
from Bio import SeqIO
import re


with open("input.txt") as file:
	dat = file.readlines()


#for line in dat:
#	wget.download('http://www.uniprot.org/uniprot/' + line.strip() + '.fasta')

#bashCommand = 'touch protiens.dat'
#bashCommand = 'cat *.fasta >> protiens.dat'
#os.system(bashCommand)

with open('protiens.dat', 'rU') as file:
	for record in SeqIO.parse(file, 'fasta'):
		ID = (record.id[3:]).replace('|', '_')
		#print(record.seq)
		ref = (record.seq)
		qu = re.compile("N(.)(S|T)(.)")
		#print qu
		#qu = 'NFSD' #
		match = 0
		index = 0
		A = 0
		B = 4
		count = 0
		position = ''
		while index < len(ref)-5:
			count = count + 1
			if re.match(ref[A:B], qu):
				position.append (count)
				match = match + 1
			index = index + 1
			A = A + 1
			B = B + 1
		if match > 0:
			print ID
			print count





#NFSD

#bashCommand = 'rm -f *.fasta'
#os.system(bashCommand)
