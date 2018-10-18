import matplotlib.pyplot as plt
from collections import OrderedDict
import time
import numpy as np
import texttable as tt

def criaDic(campos):
	dic = OrderedDict()
	if(campos[0][0] == "\""): #esses comentarios so ajudam no genero
		for campo in campos:
			dic[campo] = 0
	else:
		for campo in campos:
			dic["\""+campo+"\""] = 0
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
	
	for linha in fh:
		
		atributos = linha.split(",")
		if(atributos[posicao] != "?") and (atributos[posicao] != "?\n"):
		
			dic_fg[atributos[posicao]] = (dic_fg[atributos[posicao]]) + 1

	return dic_fg

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
fh = open("renda_inferior_1_5_salarios.txt","r",encoding="ISO-8859-1")
fh_cabecalho = open("cabecalho_teste.txt","r",encoding="ISO-8859-1")
data_nt_fg = []
data_nt_ce = []
data_nt_ger = []

fh_saida_nota_fg = open("CIC_comparacao_quantitativa_renda_baixa.txt","w")
#fh_saida_nota_ce = open("CIC_nota_ce_comparacao_baixa_renda.txt","w")
#fh_saida_nota_ger = open("CIC_nota_ger_comparacao_baixa_renda.txt","w")
for linha in fh_cabecalho:
	atributos = linha.split("\t")
	campos = atributos[2][1:-1].split(",")
	dic_fg=getData(campos,fh,int(atributos[3]))
	numero_total_instancias = 481720	#ENADE
	numero_local_instancias = 78154
	
	for k in dic_fg:
		fh_saida_nota_fg.write(atributos[1]+"_"+k+"\t"+str(dic_fg[k])+"\t"+str(round(((dic_fg[k]*100)/numero_local_instancias),3)) + "%"+"\t"+str(round(((dic_fg[k]*100)/numero_total_instancias),3)) + "%")
		fh_saida_nota_fg.write("\n")

fh_saida_nota_fg.close()
fh_cabecalho.close()
fh.close()

print("--- %s seconds ---" % (time.time() - start_time))