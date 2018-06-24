with open('input.txt', 'r') as f:
	data=f.read().rstrip()
 
#data = data.split(' ')

comma = "'" 
data = data.replace(" ", " ")
#out = comma + data + comma


#print out


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

out = ( word_count(data))

#print out

for key, value in out.items():
	print key
	print value