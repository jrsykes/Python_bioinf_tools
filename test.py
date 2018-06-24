import re

qu = re.compile("N(.)(S|T)(.)")


#qu = re.compile("Sent from my (iPhone|iPod)")



if re.match(qu, "NFSD"):
	print 'Exito!'
else:
	print "Bugger"