import matplotlib.pyplot as plt
import time
import numpy as np
import texttable as tt

def getData(campo,fh,posicao,campo_segundo,posicao_segundo):
	fh.seek(0)
	data_nt_fg = [] #atributos[93]
	data_nt_ce = []	#atributos[99]
	data_nt_ger = []	#atributos[100]
	for linha in fh:
		atributos = linha.split(",")
		if (atributos[posicao] == campo) and (atributos[posicao_segundo] == campo_segundo):
			if(atributos[93] != "?"):
				data_nt_fg.append(float(atributos[93]))
			if(atributos[99] != "?"):
				data_nt_ce.append(float(atributos[99]))
			if(atributos[100] != "?"):
				data_nt_ger.append(float(atributos[100]))
	return data_nt_fg,data_nt_ce,data_nt_ger
def limpaNomeArquivo(string):
	string = string.replace(" ","_")
	string = string.replace(".","")
	string = string.replace("\"","")
	string = string.replace("\\","")
	string = string.replace(";","")
	string = string.replace("/","")
	return string
def criaBoxplot(data,atributo,eixo_x,tipo_nota,segundo_parametro,atributo_segundo):
	
	largura = len(eixo_x) * 15
	# Create a figure instance
	fig = plt.figure(figsize=(largura, 30))

	# Create an axes instance
	ax = fig.add_subplot(111)

	# Create the boxplot
	bp = ax.boxplot(data, 0, '')
	ax.set_xticklabels(eixo_x)
	
	nome_arquivo = "EngComp_"+atributo+"_"+atributo_segundo+"_"+segundo_parametro+"_"+tipo_nota
	fig.suptitle("EngComp "+atributo+" "+atributo_segundo+" "+segundo_parametro+" "+tipo_nota, fontsize=20)
	fig.savefig(limpaNomeArquivo(nome_arquivo), bbox_inches='tight')

def criaTabela(data,atributo,eixo_x,tipo_nota,segundo_parametro):

	tab = tt.Texttable()
	numero_total_instancias = 2226
	x = [[]] # The empty row will have the header
	cabecalho = [tipo_nota]
	numero_instancias = ["Numero de instancias"]
	percentual_instancias = ["Percentual de instancias"]
	min_valor = ["Min"]
	max_valor = ["Max"]
	primeiro_quartil = ["25 quaril"]
	mediana = ["Mediana"]
	terceiro_quartil = ["75 quaril"]
	for lista in data:
		numero_instancias.append(len(lista))
		if(len(lista) != 0 ):
			percentual_instancias.append(str(round(((len(lista)*100)/numero_total_instancias),3))+"%")
			min_valor.append(min(lista))
			max_valor.append(max(lista))
			primeiro_quartil.append(np.percentile(lista, 25))
			mediana.append(np.percentile(lista,50))
			terceiro_quartil.append(np.percentile(lista, 75))
		else:
			percentual_instancias.append(0)
			min_valor.append(0)
			max_valor.append(0)
			primeiro_quartil.append(0)
			mediana.append(0)
			terceiro_quartil.append(0)
	
	x.append(numero_instancias)
	x.append(percentual_instancias)
	x.append(min_valor)
	x.append(primeiro_quartil)
	x.append(mediana)
	x.append(terceiro_quartil)
	x.append(max_valor)
	tab.add_rows(x)
	cabecalho.extend(eixo_x)
	tab.header(cabecalho)
	print (tab.draw())
	print("\n\n\n\n")
	return tab
	
start_time = time.time()
fh = open("engenharia_computacao.txt","r",encoding="utf-8")
fh_cabecalho = open("cabecalho_uni.txt","r",encoding="utf-8")
#fh_cabecalho = open("cabecalho_teste_segundo.txt","r",encoding="utf-8")
fh_cabecalho_segundo = open("cabecalho_teste.txt","r",encoding="utf-8")
for linha_segundo in fh_cabecalho_segundo:
	atributos_segundo = linha_segundo.split("\t")
	campos_segundo = atributos_segundo[2][1:-1].split(",")
	for segundo_parametro in campos_segundo:
		fh_cabecalho.seek(0)
		for linha in fh_cabecalho:
			atributos = linha.split("\t")
			campos = atributos[2][1:-1].split(",")
			data_nt_fg = []
			data_nt_ce = []
			data_nt_ger = []
			eixo_x = []

			for campo in campos:
				return_fg,return_ce,return_ger = getData(campo,fh,int(atributos[3]),segundo_parametro,int(atributos_segundo[3]))
				data_nt_fg.append(return_fg)
				data_nt_ce.append(return_ce)
				data_nt_ger.append(return_ger)
				eixo_x.append(campo)
			'''
			tab = criaTabela(data_nt_ger,atributos[1],eixo_x,"nota_ger",segundo_parametro)
			'''
			criaBoxplot(data_nt_fg,atributos[1],eixo_x,"nota_fg",segundo_parametro,atributos_segundo[1])
			criaBoxplot(data_nt_ce,atributos[1],eixo_x,"nota_ce",segundo_parametro,atributos_segundo[1])
			criaBoxplot(data_nt_ger,atributos[1],eixo_x,"nota_ger",segundo_parametro,atributos_segundo[1])
			
fh_cabecalho.close()
fh.close()

print("--- %s seconds ---" % (time.time() - start_time))