import matplotlib.pyplot as plt
from collections import OrderedDict
import time
import numpy as np
import texttable as tt
import operator


def criaDic(campos):
	dic = OrderedDict()
	if(campos[0][0] == "\""): #esses comentarios so ajudam no genero
		for campo in campos:
			dic[campo] = [0] * 36
	else:
		for campo in campos:
			dic["\""+campo+"\""] = [0] * 36
	return dic

def getData(campos,fh,posicao):

	fh.seek(0)
	dic = criaDic(campos)

	for linha in fh:
		atributos = linha.split(",")
		#adicionando o numero de estudantes
		dic[atributos[posicao]][35] = (dic[atributos[posicao]][35] + 1)
		for i in range(48,56):
			if(atributos[i] == "acerto"):
				dic[atributos[posicao]][i-48] = (dic[atributos[posicao]][i-48] + 1)
		for i in range(58,85):
			if(atributos[i] == "acerto"):
				dic[atributos[posicao]][i-50] = (dic[atributos[posicao]][i-50] + 1)

	return dic

def limpaNomeArquivo(string):
	string = string.replace(" ","_")
	string = string.replace(".","")
	string = string.replace("\"","")
	string = string.replace("\\","")
	string = string.replace(";","")
	string = string.replace("/","")
	return string

#nome_arquivo_abrir = input("Insira o nome arquivo com a extensao .txt")
start_time = time.time()
fh = open("FOLHA_top10_CIC.txt","r",encoding="ISO-8859-1")
fh_cabecalho = open("universidades_CIC_folha.txt","r",encoding="ISO-8859-1")
TOTAL = 753
for linha in fh_cabecalho:
	atributos = linha.split("\t")
	campos = atributos[2][1:-1].split(",")

	dic =getData(campos,fh,int(atributos[3]))

	for k in dic:
		for i in range(0,35):
			dic[k][i] = str(round((((dic[k][i])*100)/dic[k][35]),3))+"%"
	fh_saida = open("porcentagem_acerto_questoes_FOLHACIC.txt","w")
	for k in dic:
		fh_saida.write(str(k)+"\t")
		for i in range(0,36):
			fh_saida.write(str(dic[k][i])+"\t")
		fh_saida.write("\n")
	fh_saida.close()




fh_cabecalho.close()
fh.close()

print("--- %s seconds ---" % (time.time() - start_time))