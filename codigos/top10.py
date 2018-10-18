import matplotlib.pyplot as plt
from collections import OrderedDict
import time

def criaDic(campos):
	dic = OrderedDict()
	for campo in campos:
		dic[campo] = []

	return dic

def criarLista(dic):
	data =[]
	for k in dic:
		data.append(dic[k])
	return data
	
def getData(campos,fh,posicao):

	fh.seek(0)

	dic_ger = criaDic(campos)

	for linha in fh:
		atributos = linha.split(",")
		if(atributos[posicao] != "?") and (atributos[posicao] != "?\n"):
			if(atributos[100] != "?"):
				dic_ger[atributos[posicao]].append(float(atributos[100]))
	return dic_ger

def calculaMedia(dic):
	for k in dic:
		if(len(dic[k]) > 0):
			media = sum(dic[k])/float(len(dic[k]))
		else:
			media = 0.0
		dic[k] = media
	return dic
	
start_time = time.time()
#fh = open("saida_replace.txt","r",encoding="utf8")
fh = open("cic_bacharel.txt","r",encoding="utf8")
#fh_cabecalho = open("universidades.txt","r",encoding="utf8")
fh_cabecalho = open("universidades_CIC.txt","r",encoding="utf8")
for linha in fh_cabecalho:
	atributos = linha.split("\t")
	campos = atributos[2][1:-1].split(",")
	dic_ger =getData(campos,fh,int(atributos[3]))

	dic_saida = OrderedDict()
	dic_saida = calculaMedia(dic_ger)
	
	d_descending = OrderedDict(sorted(dic_saida.items(), key=lambda t: t[1],reverse=True))
	print(d_descending["\"UNIVERSIDADE DE BRASILIA\""])
	count = 0
	for k in d_descending:
		count+=1
		'''
		if(k == "\"UNIVERSIDADE DE BRASILIA\""):
			print(count)
			break'''
		print(k+"media = "+str(d_descending[k]))
		x=input()
	
fh_cabecalho.close()
fh.close()

print("--- %s seconds ---" % (time.time() - start_time))