##############################################
##############################################

# Example data: 
# Input: Two DNA strings, s & t 	
#			s = GATATATGCATATACTT
#			t = ATAT
# Output: All locations of t as a substring of s
#			2, 4 & 10

##############################################
##############################################


import sys

with open(sys.argv[1]) as file:
	dat = file.read()


ref = dat.splitlines()[0]
qu = dat.splitlines()[1]


length = len(ref)

index = 0
A = 0
B = len(qu)
count = 0
while index < len(ref)-len(qu)+1:
	count = count + 1
	if ref[A:B] == qu:
		print count
	index = index + 1
	A = A + 1
	B = B + 1
