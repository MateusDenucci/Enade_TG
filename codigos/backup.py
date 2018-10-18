import matplotlib.pyplot as plt
import os

def getData(campo,fh):
	
	fh.seek(0)
	data_nt_fg = [] #atributos[93]
	data_nt_ce = []	#atributos[99]
	data_nt_ger = []	#atributos[100]
	for linha in fh:
		atributos = linha.split(",")
		if (atributos[1] == campo):
			if(atributos[93] != "?"):
				data_nt_fg.append(float(atributos[93]))
			if(atributos[99] != "?"):
				data_nt_ce.append(float(atributos[99]))
			if(atributos[100] != "?"):
				data_nt_ger.append(float(atributos[100]))

	data =[data_nt_fg,data_nt_ce,data_nt_ger]
	
	return data
def criaBoxplot(campo,fh,atributo):
	
	# Create a figure instance
	fig = plt.figure()

	# Create an axes instance
	ax = fig.add_subplot(111)

	# Create the boxplot
	bp = ax.boxplot(data, 0, '')
	ax.set_xticklabels(['nt_fg', 'nt_ce', 'nt_ger'])
	
	nome_arquivo = atributo+"_"+campo[1:-1]+".png"
	fig.savefig(nome_arquivo, bbox_inches='tight')

fh = open("saida_replace.txt","r",encoding="utf8")
fh_cabecalho = open("cabecalho.txt","r",encoding="utf8")
for linha in fh_cabecalho:
	atributos = linha.split("\t")
	campos = atributos[2][1:-1].split(",")
	for campo in campos:
		criaBoxplot(campo,fh,atributos[1])

fh_cabecalho.close()
fh.close()