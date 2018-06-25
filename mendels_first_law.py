##############################################
##############################################

#No nee for input file. Run with the command: "python mendels_first_law.py" and follow the prompts

##############################################
##############################################


from decimal import *
getcontext().prec = 5

import math

homd = input('n homozygous dominant: ')

het = input('n heterozygous: ')

homr = input('n homozygous recessive: ')

N = homd + het + homr

n_combinations = Decimal(math.factorial(N)/(2*(math.factorial(N-2))))

n_het_matings = Decimal(math.factorial(het)/(2*(math.factorial(het-2))))

n_het_homr_matings = Decimal((math.factorial(het+homr)/(2*(math.factorial(het+homr-2)))) - (math.factorial(het)/(2*(math.factorial(het-2)))) - (math.factorial(homr)/(2*(math.factorial(homr-2)))))

n_homd_homd_matings = Decimal(n_combinations - n_het_matings - n_het_homr_matings - ((math.factorial(homr)/(2*(math.factorial(homr-2))))))


out = Decimal((n_homd_homd_matings/n_combinations+(n_het_matings/n_combinations*3/4)+n_het_homr_matings/n_combinations*1/2))

print "probability that two randomly selected mating organisms will produce an individual possessing a dominant allele: " + str(out)



a = (9/15+(1/15*3/4)+4/15*1/2)
