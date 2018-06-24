with open('input.txt', 'r') as file:
	dat = file.read()

ref = dat.splitlines()[0]
qu = dat.splitlines()[1]

#print ref.find(qu, 0, len(ref))

print ref
print qu
print ''
print [[[[[[[[[[[[[[[[88]]]]]]]]]]]]]]]]
print ''

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
