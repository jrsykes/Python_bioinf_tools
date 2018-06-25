# Example input data:
#
#	GAGCCTACTAACGGGAT
#	CATCGTAATGACGGCCT


import sys

with open(sys.argv[1]) as file:
	dat = file.read()

seq1 = dat.splitlines()[0]
seq2 = dat.splitlines()[1]

if len(seq1) == len(seq2):
	n = 0
	mutations = 0

	for letter in seq1:
		if letter != seq2[n][0]:
			mutations = mutations + 1
		n = n + 1
	
	print 'n point mutations =' , mutations
else:
	print "Input DNA strings are not of equal length"