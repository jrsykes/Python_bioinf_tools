##############################################
##############################################

# Example data: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

##############################################
##############################################

import sys

with open(sys.argv[1]) as file:
	dat = file.readline()


from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
my_dna = Seq(dat)
my_protein = my_dna.translate()
print str(my_protein).replace("*", "")