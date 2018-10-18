import matplotlib.pyplot as plt
from collections import OrderedDict
import time
import numpy as np
import texttable as tt
from unicodedata import normalize\

def removerAcentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')
	
def criaDic(campos):
	dic = OrderedDict()
	if(campos[0][0] == "\""): #esses comentarios so ajudam no genero
		for campo in campos:
			dic[removerAcentos(campo)] = []
	else:
		for campo in campos:
			dic["\""+removerAcentos(campo)+"\""] = []
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
	
def getData(campos,fh,posicao,posicao_segundo,segundo_parametro):

	fh.seek(0)
	dic_fg = criaDic(campos)
	dic_ce = criaDic(campos)
	dic_ger = criaDic(campos)

	for linha in fh:
		atributos = linha.split(",")
		'''print(atributos[posicao_segundo])
		print(segundo_parametro)
		print(atributos[posicao_segundo] == segundo_parametro)
		x=input()'''
		if(atributos[posicao] != "?") and (atributos[posicao] != "?\n") and (atributos[posicao_segundo] == segundo_parametro):
			if(atributos[93] != "?"):
				dic_fg[atributos[posicao]].append(float(atributos[93]))
			if(atributos[99] != "?"):
				dic_ce[atributos[posicao]].append(float(atributos[99]))
			if(atributos[100] != "?"):
				dic_ger[atributos[posicao]].append(float(atributos[100]))
	return dic_fg,dic_ce,dic_ger

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
def criaTabela(dic,atributo,eixo_x,tipo_nota,segundo_parametro,atributo_segundo):
	tab = tt.Texttable()
	numero_total_instancias = 9822
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
	print (tab.draw())
	return tab

#codecs.open(file_name, "r",encoding='utf-8', errors='ignore') as fdata:
start_time = time.time()
fh = open("engenharia_computacao.txt","r",encoding="utf-8")
fh_cabecalho = open("cabecalho_teste.txt","r",encoding="utf-8")
fh_cabecalho_segundo = open("cabecalho_teste_segundo.txt","r",encoding="utf-8")
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
			dic_fg,dic_ce,dic_ger =getData(campos,fh,int(atributos[3]),int(atributos_segundo[3]),segundo_parametro)
			for k in dic_fg:
				eixo_x.append(k.encode('ISO-8859-1','ignore'))
			data_nt_fg = criarLista(dic_fg)
			data_nt_ce = criarLista(dic_ce)
			data_nt_ger = criarLista(dic_ger)
			
			nome_arquivo = "EngComp_"+atributos[1]+"_"+atributos_segundo[1]+"_"+segundo_parametro
			fh_tabelas = open(limpaNomeArquivo(nome_arquivo)+".txt","w")
			fh_tabelas.write(nome_arquivo)
			fh_tabelas.write("\n\n")
			tab = criaTabela(dic_fg,atributos[1],eixo_x,"nota_fg",segundo_parametro,atributos_segundo[1])
			fh_tabelas.write(tab.draw())
			fh_tabelas.write("\n\n\n\n")
			tab = criaTabela(dic_ce,atributos[1],eixo_x,"nota_ce",segundo_parametro,atributos_segundo[1])
			fh_tabelas.write(tab.draw())
			fh_tabelas.write("\n\n\n\n")
			tab = criaTabela(dic_ger,atributos[1],eixo_x,"nota_ger",segundo_parametro,atributos_segundo[1])
			fh_tabelas.write(tab.draw())
			fh_tabelas.close()
			
			criaBoxplot(data_nt_fg,atributos[1],eixo_x,"nota_fg",segundo_parametro,atributos_segundo[1])
			criaBoxplot(data_nt_ce,atributos[1],eixo_x,"nota_ce",segundo_parametro,atributos_segundo[1])
			criaBoxplot(data_nt_ger,atributos[1],eixo_x,"nota_ger",segundo_parametro,atributos_segundo[1])
	
fh_cabecalho.close()
fh_cabecalho_segundo.close()
fh.close()

print("--- %s seconds ---" % (time.time() - start_time))