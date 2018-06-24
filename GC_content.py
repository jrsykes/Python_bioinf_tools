import os
try:
	os.remove('out.tsv')
except OSError:
	pass

import decimal

names = ''
GC_CONTENT = ''

with open('input.txt', 'r') as file:
	dat = file.read().strip('\n').split()
	for line in dat:
		if line.startswith('>'):
			names += line.replace('>','') + '\n'

with open('input.txt', 'r') as file:
	seqs = file.read().replace('\n','').replace('>','\n').replace('Rosalind_','').strip()

	for line in seqs.split():
			
		AT = line.count('A') + line.count('T')
		GC = line.count('G') + line.count('C') 
		

		AT = decimal.Decimal(AT)
		GC = decimal.Decimal(GC)

		GC_content = 100 * GC/(AT + GC)
		GC_CONTENT += str(round(GC_content, 7)) + '\n'

with open('out.tsv', 'a') as out:
	out.write(GC_CONTENT)


bashCommand = 'sort -rnk 3,3 out.tsv | cat'
os.system(bashCommand)

print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

print names
print GC_CONTENT