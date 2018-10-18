import matplotlib.pyplot as plt
from collections import OrderedDict
import time
import numpy as np
import texttable as tt

#etnia = "pardos"
#nome_arquivo_abrir = "privada_lic_licenciatura_"+etnia+".txt"
#nome_arquivo_exportar = "LIC_privada_"+etnia+"_"

nome_arquivo_abrir = "federal_enade.txt"
nome_arquivo_exportar = "INTERCAMBIO_federal.txt"

def criaDic(campos):
	dic = OrderedDict()
	if(campos[0][0] == "\""): #esses comentarios so ajudam no genero
		for campo in campos:
			dic[campo] = []
	else:
		for campo in campos:
			dic["\""+campo+"\""] = []
	return dic

def criaDicForms(campos):
	dic = OrderedDict()
	for campo in campos:
		dic[campo] = []

	return dic

def criaDicUltimoCampo(campos):
	dic = OrderedDict()
	for campo in campos:
		dic[campo+"\n"] = []
	return dic

	
def criarLista(dic):
	data =[]
	for k in dic:
		data.append(dic[k])
	return data
	
def getData(campos,fh,posicao):

	fh.seek(0)
	dic_fg = criaDic(campos)
	dic_ce = criaDic(campos)
	dic_ger = criaDic(campos)
	for linha in fh:
		
		atributos = linha.split(",")
		if(atributos[posicao] != "?") and (atributos[posicao] != "?\n"):
			if(atributos[93] != "?"):
				dic_fg[atributos[posicao]].append(float(atributos[93]))
			if(atributos[99] != "?"):
				dic_ce[atributos[posicao]].append(float(atributos[99]))
			if(atributos[100] != "?"):
				dic_ger[atributos[posicao]].append(float(atributos[100]))
	return dic_fg,dic_ce,dic_ger
def criaTabela(dic,atributo,eixo_x,tipo_nota):
	tab = tt.Texttable()
	
	#numero_total_instancias = 9822 #CIC
	#numero_total_instancias = 2972	#EngComp
	#numero_total_instancias = 2226	#LIC
	#numero_total_instancias = 481720	#ENADE
	numero_total_instancias = file_len(nome_arquivo_abrir)
	x = [[]] # The empty row will have the header
	cabecalho = [tipo_nota]
	numero_instancias = ["Numero de instancias"]
	percentual_instancias = ["Percentual de instancias"]
	min_valor = ["Min"]
	max_valor = ["Max"]
	primeiro_quartil = ["25 quaril"]
	mediana = ["Mediana"]
	terceiro_quartil = ["75 quaril"]

	for k in dic:
		numero_instancias.append(len(dic[k]))
		if(len(dic[k]) > 0 ):
			percentual_instancias.append(str(round(((len(dic[k])*100)/numero_total_instancias),3)) + "%")
			min_valor.append(min(dic[k]))
			max_valor.append(max(dic[k]))
			primeiro_quartil.append(np.percentile(dic[k], 25))
			mediana.append(np.percentile(dic[k],50))
			terceiro_quartil.append(np.percentile(dic[k], 75))
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
	#tab.set_cols_align(['r','r','r'])
	cabecalho.extend(eixo_x)
	tab.header(cabecalho)
	#tab.set_cols_width([20,20,20,20,20,20,20,20,20,20,20,20])
	print (tab.draw())
	return tab

def limpaNomeArquivo(string):
	string = string.replace(" ","_")
	string = string.replace(".","")
	string = string.replace("\"","")
	string = string.replace("\\","")
	string = string.replace(";","")
	string = string.replace("/","")
	return string
	
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
	
def criaBoxplot(data,atributo,eixo_x,tipo_nota):
	
	largura = len(eixo_x) * 15
	# Create a figure instance
	fig = plt.figure(figsize=(largura, 30))

	# Create an axes instance
	ax = fig.add_subplot(111)

	# Create the boxplot
	bp = ax.boxplot(data, 0, '')
	ax.set_xticklabels(eixo_x)
	
	nome_arquivo = "CIC_"+atributo+"_"+tipo_nota
	fig.suptitle("CIC "+atributo+" "+tipo_nota, fontsize=20)
	fig.savefig(nome_arquivo, bbox_inches='tight')

#nome_arquivo_abrir = input("Insira o nome arquivo com a extensao .txt")
start_time = time.time()
fh = open(nome_arquivo_abrir,"r",encoding="ISO-8859-1")
fh_cabecalho = open("cabecalho_teste.txt","r",encoding="ISO-8859-1")
for linha in fh_cabecalho:
	atributos = linha.split("\t")
	campos = atributos[2][1:-1].split(",")
	data_nt_fg = []
	data_nt_ce = []
	data_nt_ger = []
	eixo_x = []
	
	dic_fg,dic_ce,dic_ger =getData(campos,fh,int(atributos[3]))
	for k in dic_fg:
		eixo_x.append(k)
	data_nt_fg = criarLista(dic_fg)
	data_nt_ce = criarLista(dic_ce)
	data_nt_ger = criarLista(dic_ger)
	'''criaBoxplot(data_nt_fg,atributos[1],eixo_x,"nota_fg")
	criaBoxplot(data_nt_ce,atributos[1],eixo_x,"nota_ce")
	criaBoxplot(data_nt_ger,atributos[1],eixo_x,"nota_ger")	'''
	
	
	nome_arquivo = nome_arquivo_exportar+atributos[1]
	fh_tabelas = open(limpaNomeArquivo(nome_arquivo)+".txt","w")
	fh_tabelas.write(nome_arquivo+"\n\n")
	tab = criaTabela(dic_fg,atributos[1],eixo_x,"nota_fg")
	fh_tabelas.write(tab.draw())
	fh_tabelas.write("\n\n\n\n")
	tab = criaTabela(dic_ce,atributos[1],eixo_x,"nota_ce")
	fh_tabelas.write(tab.draw())
	fh_tabelas.write("\n\n\n\n")
	tab = criaTabela(dic_ger,atributos[1],eixo_x,"nota_ger")
	fh_tabelas.write(tab.draw())
	fh_tabelas.write("\n\n\n\n")
	fh_tabelas.close()
	''''''
fh_cabecalho.close()
fh.close()

print("--- %s seconds ---" % (time.time() - start_time))