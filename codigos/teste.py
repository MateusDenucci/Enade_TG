fh = open("cic_bacharel.txt","r",encoding="latin-1")
count = 0
for line in fh:
	elements = line.split(",")
	if(int(elements[9]) > 40):
		count+=1
print(count)	
fh.close()