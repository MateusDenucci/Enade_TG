import pandas as pd
'''
fh_entrada = open("media_por_curso.txt","r")

enade = [[],[],[],[],[],[],[],[]]

for linha in fh_entrada:
	atributos = linha.split("\t")
	for i in range(0,8):
		enade[i].append(atributos[i+10])

fh_entrada.close()

fh_saida = open("correlacao_enade.txt","w")

for k in range(5,8):
	for j in range(0,5):
		A=[]
		B=[]
		for i in range(len(enade[k])):
			A.append(float(enade[k][i]))
			B.append(float(enade[j][i]))
		df = pd.DataFrame({'A': A, 'B': B})
		fh_saida.write(str(df['A'].corr(df['B']))+"\t")
		
		
for j in range(1,5):
	A=[]
	B=[]
	for i in range(len(enade[0])):
		A.append(float(enade[0][i]))
		B.append(float(enade[j][i]))
	df = pd.DataFrame({'A': A, 'B': B})
	fh_saida.write(str(df['A'].corr(df['B']))+"\t")
	
for j in range(2,5):
	A=[]
	B=[]
	for i in range(len(enade[1])):
		A.append(float(enade[1][i]))
		B.append(float(enade[j][i]))
	df = pd.DataFrame({'A': A, 'B': B})
	fh_saida.write(str(df['A'].corr(df['B']))+"\t")
	
	
for j in range(3,5):
	A=[]
	B=[]
	for i in range(len(enade[2])):
		A.append(float(enade[2][i]))
		B.append(float(enade[j][i]))
	df = pd.DataFrame({'A': A, 'B': B})
	fh_saida.write(str(df['A'].corr(df['B']))+"\t")
	
for j in range(4,5):
	A=[]
	B=[]
	for i in range(len(enade[3])):
		A.append(float(enade[3][i]))
		B.append(float(enade[j][i]))
	df = pd.DataFrame({'A': A, 'B': B})
	fh_saida.write(str(df['A'].corr(df['B']))+"\t")
	
fh_saida.close()
'''

fh_entrada = open("media_por_curso.txt","r")
A=[]
B=[]
for linha in fh_entrada:
	atributos = linha.split("\t")
	A.append(float(atributos[13]))
	B.append(float(atributos[14]))
df = pd.DataFrame({'A': A, 'B': B})
print(df['A'].corr(df['B']))

fh_entrada.close()