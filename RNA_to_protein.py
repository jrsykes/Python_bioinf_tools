with open('input.txt', 'r') as file:
	dat = file.readline()

#import Bio
#from Bio.Seq import Seq
#from Bio.Alphabet import generic_dna
#from Bio.Data import CodonTable
#table = CodonTable.ambiguous_dna_by_id[1]
##out = _translate_str("AAA", table)
#print transcribe('ACTGN')


from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
my_dna = Seq(dat)
my_protein = my_dna.translate()
print my_protein