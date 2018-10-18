import matplotlib.pyplot as plt
import time
import numpy as np
import texttable as tt

def getData(fh,posicao,min,max,posicao_segundo,item_segundo):
	fh.seek(0)
	data_nt_fg = [] #atributos[93]
	data_nt_ce = []	#atributos[99]
	data_nt_ger = []	#atributos[100]
	for linha in fh:
		atributos = linha.split(",")
		'''print(atributos[posicao_segundo])
		print(item_segundo)
		x=input()'''
		
		if ((atributos[posicao] != "?") and (int(atributos[posicao]) >= min ) and (int(atributos[posicao]) <= max ) and (atributos[posicao_segundo] == "\""+item_segundo+"\"")):
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
	
def criaBoxplot(data,atributo,eixo_x,tipo_nota,item_segundo):
	
	largura = len(eixo_x) * 15
	# Create a figure instance
	fig = plt.figure(figsize=(largura, 30))

	# Create an axes instance
	ax = fig.add_subplot(111)

	# Create the boxplot
	bp = ax.boxplot(data, 0, '')
	ax.set_xticklabels(eixo_x)
	
	nome_arquivo = "EngComp_"+atributo+"_sexo_"+item_segundo+"_"+tipo_nota
	fig.suptitle("EngComp "+atributo+" sexo "+item_segundo+" "+tipo_nota, fontsize=20)
	fig.savefig(limpaNomeArquivo(nome_arquivo), bbox_inches='tight')

def criaTabela(data,atributo,eixo_x,tipo_nota,segundo_parametro):
	tab = tt.Texttable()
	numero_total_instancias = 2972
	x = [[]] # The empty row will have the header
	cabecalho = [tipo_nota]
	numero_instancias = ["Numero de instancias"]
	percentual_instancias = ["Percentual de instancias"]
	min_valor = ["Min"]
	max_valor = ["Max"]
	primeiro_quartil = ["25 quaril"]
	mediana = ["Mediana"]
	terceiro_quartil = ["75 quaril"]
	#str(round(numvar,9))
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
	#tab.set_cols_align(['r','r','r'])
	cabecalho.extend(eixo_x)
	tab.header(cabecalho)
	print (tab.draw())
	print("\n\n\n\n")
	return tab

	
start_time = time.time()
#fh = open("saida_replace.txt","r",encoding="latin-1")
fh = open("engenharia_computacao.txt","r",encoding="ISO-8859-1")
itens_segundo =["M","F"]
posicao_segundo = 10

for item_segundo in itens_segundo:
	print(item_segundo)
	data_nt_fg = []
	data_nt_ce = []
	data_nt_ger = []
	eixo_x = []
	return_fg,return_ce,return_ger = getData(fh,9,0,25,posicao_segundo,item_segundo)
	data_nt_fg.append(return_fg)
	data_nt_ce.append(return_ce)
	data_nt_ger.append(return_ger)
	eixo_x.append("idade <= 25")

	return_fg,return_ce,return_ger = getData(fh,9,26,30,posicao_segundo,item_segundo)
	data_nt_fg.append(return_fg)
	data_nt_ce.append(return_ce)
	data_nt_ger.append(return_ger)
	eixo_x.append("26 <= idade <= 30")

	return_fg,return_ce,return_ger = getData(fh,9,31,35,posicao_segundo,item_segundo)
	data_nt_fg.append(return_fg)
	data_nt_ce.append(return_ce)
	data_nt_ger.append(return_ger)
	eixo_x.append("31 <= idade <= 35")

	return_fg,return_ce,return_ger = getData(fh,9,36,40,posicao_segundo,item_segundo)
	data_nt_fg.append(return_fg)
	data_nt_ce.append(return_ce)
	data_nt_ger.append(return_ger)
	eixo_x.append("36 <= idade <= 40")

	return_fg,return_ce,return_ger = getData(fh,9,41,1000,posicao_segundo,item_segundo)
	data_nt_fg.append(return_fg)
	data_nt_ce.append(return_ce)
	data_nt_ger.append(return_ger)
	eixo_x.append("40 < idade")
	
	nome_arquivo = "EngComp_"+"nu_idade"+"_sexo_"+item_segundo
	fh_tabelas = open(limpaNomeArquivo(nome_arquivo)+".txt","w")
	fh_tabelas.write(nome_arquivo)
	fh_tabelas.write("\n\n")
	tab = criaTabela(data_nt_fg,"nu_idade",eixo_x,"nota_fg",item_segundo)
	fh_tabelas.write(tab.draw())
	fh_tabelas.write("\n\n\n\n")
	tab = criaTabela(data_nt_ce,"nu_idade",eixo_x,"nota_ce",item_segundo)
	fh_tabelas.write(tab.draw())
	fh_tabelas.write("\n\n\n\n")
	tab = criaTabela(data_nt_ger,"nu_idade",eixo_x,"nota_ger",item_segundo)
	fh_tabelas.write(tab.draw())
	fh_tabelas.write("\n\n\n\n")

	
	criaBoxplot(data_nt_fg,"nu_idade",eixo_x,"nota_fg",item_segundo)
	criaBoxplot(data_nt_ce,"nu_idade",eixo_x,"nota_ce",item_segundo)
	criaBoxplot(data_nt_ger,"nu_idade",eixo_x,"nota_ger",item_segundo)

fh.close()

print("--- %s seconds ---" % (time.time() - start_time))