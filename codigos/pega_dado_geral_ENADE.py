import matplotlib.pyplot as plt
import time
import numpy as np


def getData(fh):
	fh.seek(0)
	data_nt_fg = [] #atributos[93]
	data_nt_ce = []	#atributos[99]
	data_nt_ger = []	#atributos[100]
	universidades = set()
	for linha in fh:
		atributos = linha.split(",")
		universidades.add(atributos[2])
		if(atributos[93] != "?"):
			data_nt_fg.append(float(atributos[93]))
		if(atributos[99] != "?"):
			data_nt_ce.append(float(atributos[99]))
		if(atributos[100] != "?"):
			data_nt_ger.append(float(atributos[100]))
	'''
	fh_universidades_CIC = open("universidades_CIC.txt","w")
	for universidade in universidades:
		fh_universidades_CIC.write(universidade)
		fh_universidades_CIC.write(",")
	fh_universidades_CIC.close()'''
	return data_nt_fg,data_nt_ce,data_nt_ger

def criaBoxplot(data,atributo,eixo_x,tipo_nota):
	
	largura = len(eixo_x) * 15
	# Create a figure instance
	fig = plt.figure(figsize=(largura, 30))

	# Create an axes instance
	ax = fig.add_subplot(111)

	# Create the boxplot
	bp = ax.boxplot(data, 0, '')
	ax.set_xticklabels(eixo_x)
	
	nome_arquivo = atributo+"_"+tipo_nota
	fig.suptitle(atributo+" "+tipo_nota, fontsize=20)
	fig.savefig(nome_arquivo, bbox_inches='tight')
	
start_time = time.time()
#fh = open("enade_sem_acento.txt","r",encoding="latin-1")
fh = open("cic_bacharel.txt","r",encoding="latin-1")


numero_total_instancias = 481720

return_fg,return_ce,return_ger = getData(fh)
print("NOTA_FG"+str(np.percentile(return_fg,25))+"\t"+str(np.percentile(return_fg,50))+"\t"+str(np.percentile(return_fg,75))+"\t"+str(len(return_fg))+"\t"+str(round(((len(return_fg)*100)/numero_total_instancias),3)) + "%\n")
print("NOTA_CE"+str(np.percentile(return_ce,25))+"\t"+str(np.percentile(return_ce,50))+"\t"+str(np.percentile(return_ce,75))+"\t"+str(len(return_ce))+"\t"+str(round(((len(return_ce)*100)/numero_total_instancias),3)) + "%\n")
print("NOTA_GER"+str(np.percentile(return_ger,25))+"\t"+str(np.percentile(return_ger,50))+"\t"+str(np.percentile(return_ger,75))+"\t"+str(len(return_ger))+"\t"+str(round(((len(return_ger)*100)/numero_total_instancias),3)) + "%\n")


fh.close()

print("--- %s seconds ---" % (time.time() - start_time))