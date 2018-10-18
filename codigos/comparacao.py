import matplotlib.pyplot as plt
from collections import OrderedDict
import time
import numpy as np
import texttable as tt

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

def limpaNomeArquivo(string):
	string = string.replace(" ","_")
	string = string.replace(".","")
	string = string.replace("\"","")
	string = string.replace("\\","")
	string = string.replace(";","")
	string = string.replace("/","")
	return string

def criaTabela(data):
	tab = tt.Texttable()

	x = [[]] # The empty row will have the header
	cabecalho = ["Atributo","25 quartil","Mediana","75 quartil","Numero Instancias","Porcentagem"]

	for linha in data:
		x.append(linha)
	tab.add_rows(x)

	tab.header(cabecalho)
	#print (tab.draw())
	return tab
start_time = time.time()
arquivo_entrada = "privada_enade.txt"
fh = open(arquivo_entrada,"r",encoding="ISO-8859-1")
fh_cabecalho = open("cabecalho_teste.txt","r",encoding="ISO-8859-1")
data_nt_fg = []
data_nt_ce = []
data_nt_ger = []

fh_saida_nota_fg = open("privada_regiao_enade_nota_fg_comparacao.txt","w")
fh_saida_nota_ce = open("privada_regiao_enade_nota_ce_comparacao.txt","w")
fh_saida_nota_ger = open("privada_regiao_enade_nota_ger_comparacao.txt","w")

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

for linha in fh_cabecalho:
	atributos = linha.split("\t")
	campos = atributos[2][1:-1].split(",")
	dic_fg,dic_ce,dic_ger =getData(campos,fh,int(atributos[3]))
	
	
	numero_total_instancias = file_len(arquivo_entrada)
	#numero_total_instancias = 275649
	# numero_total_instancias = 2972	#EngComp
	#numero_total_instancias = 2226	#LIC
	#numero_total_instancias = 481720	#ENADE
	
	for k in dic_fg:
		if(len(dic_fg[k]) > 0):
			fh_saida_nota_fg.write(atributos[1]+"_"+k+"\t"+str(np.percentile(dic_fg[k],25))+"\t"+str(np.percentile(dic_fg[k],50))+"\t"+str(np.percentile(dic_fg[k],75))+"\t"+str(len(dic_fg[k]))+"\t"+str(round(((len(dic_fg[k])*100)/numero_total_instancias),3)) + "%\n")
			data_nt_fg.append([atributos[1]+"_"+k,str(np.percentile(dic_fg[k],25)),str(np.percentile(dic_fg[k],50)),str(np.percentile(dic_fg[k],75)),str(len(dic_fg[k])),str(round(((len(dic_fg[k])*100)/numero_total_instancias),3))+"%"])
	for k in dic_ce:
		if(len(dic_ce[k]) > 0):
			fh_saida_nota_ce.write(atributos[1]+"_"+k+"\t"+str(np.percentile(dic_ce[k],25))+"\t"+str(np.percentile(dic_ce[k],50))+"\t"+str(np.percentile(dic_ce[k],75))+"\t"+str(len(dic_ce[k]))+"\t"+str(round(((len(dic_ce[k])*100)/numero_total_instancias),3)) + "%\n")
			data_nt_ce.append([atributos[1]+"_"+k,str(np.percentile(dic_ce[k],25)),str(np.percentile(dic_ce[k],50)),str(np.percentile(dic_ce[k],75)),str(len(dic_ce[k])),str(round(((len(dic_ce[k])*100)/numero_total_instancias),3))+"%"])
	for k in dic_ger:
		if(len(dic_ger[k]) > 0):
			fh_saida_nota_ger.write(atributos[1]+"_"+k+"\t"+str(np.percentile(dic_ger[k],25))+"\t"+str(np.percentile(dic_ger[k],50))+"\t"+str(np.percentile(dic_ger[k],75))+"\t"+str(len(dic_ger[k]))+"\t"+str(round(((len(dic_ger[k])*100)/numero_total_instancias),3)) + "%\n")
			data_nt_ger.append([atributos[1]+"_"+k,str(np.percentile(dic_ger[k],25)),str(np.percentile(dic_ger[k],50)),str(np.percentile(dic_ger[k],75)),str(len(dic_ger[k])),str(round(((len(dic_ger[k])*100)/numero_total_instancias),3))+"%"])
'''
data_nt_fg.sort(key=lambda x: x[2])
tab = criaTabela(data_nt_fg)
fh_saida_nota_fg.write(tab.draw())

data_nt_ce.sort(key=lambda x: x[2])
tab = criaTabela(data_nt_ce)
fh_saida_nota_ce.write(tab.draw())

data_nt_ger.sort(key=lambda x: x[2])
tab = criaTabela(data_nt_ger)
fh_saida_nota_ger.write(tab.draw())
'''
fh_saida_nota_fg.close()
fh_saida_nota_ce.close()
fh_saida_nota_ger.close()

fh_cabecalho.close()
fh.close()

print("--- %s seconds ---" % (time.time() - start_time))