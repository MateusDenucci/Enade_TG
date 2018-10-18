import matplotlib.pyplot as plt
import time
import numpy as np
import texttable as tt


def tipoIEE(tipo_iee,atributo):
	if tipo_iee == "privada":
		if(atributo == "\"Privada sem fins lucrativos\"" or atributo == "\"Privada com fins lucrativos\""):
			return True
		else:
			return False
	elif tipo_iee == "federal":
		if(atributo == "\"Pessoa Juridica de Direito Publico - Federal\""):
			return True
		else:
			return False
				
	
def limpaNomeArquivo(string):
	string = string.replace(" ","_")
	string = string.replace(".","")
	string = string.replace("\"","")
	string = string.replace("\\","")
	string = string.replace(";","")
	string = string.replace("/","")
	return string

def getData(fh,etnia,curso,tipo_iee,posicao_extra,campo_extra):
	fh.seek(0)
	data_nt_fg = [] #atributos[93]
	data_nt_ce = []	#atributos[99]
	data_nt_ger = []	#atributos[100]
	qtd = 0
	for linha in fh:
		atributos = linha.split(",")
		
		if (atributos[1] == "\""+curso+"\"") or (curso==""):

			if tipo_iee != "":
				if tipoIEE(tipo_iee,atributos[3]) == False:
					continue
			if campo_extra != "":
				if atributos[posicao_extra] != "\""+campo_extra+"\"":
					continue
			if(atributos[93] != "?"):
				data_nt_fg.append(float(atributos[93]))
			if(atributos[99] != "?"):
				data_nt_ce.append(float(atributos[99]))
			if(atributos[100] != "?"):
				data_nt_ger.append(float(atributos[100]))
			qtd += 1
	return data_nt_fg,data_nt_ce,data_nt_ger,qtd
	
def getDataDuplo(fh,etnia,curso,tipo_iee,posicao_extra,campo_extra,posicao_extra2,campo_extra2):
	fh.seek(0)
	data_nt_fg = [] #atributos[93]
	data_nt_ce = []	#atributos[99]
	data_nt_ger = []	#atributos[100]
	qtd = 0
	for linha in fh:
		atributos = linha.split(",")
		if (atributos[1] == "\""+curso+"\"") or (curso==""):

			if tipo_iee != "":
				if tipoIEE(tipo_iee,atributos[3]) == False:
					continue
			if campo_extra != "":
				if atributos[posicao_extra] != "\""+campo_extra+"\"":
					continue
			if campo_extra2 != "":
				if atributos[posicao_extra2] != "\""+campo_extra2+"\"":
					continue
			if(atributos[93] != "?"):
				data_nt_fg.append(float(atributos[93]))
			if(atributos[99] != "?"):
				data_nt_ce.append(float(atributos[99]))
			if(atributos[100] != "?"):
				data_nt_ger.append(float(atributos[100]))
			qtd += 1
	return data_nt_fg,data_nt_ce,data_nt_ger,qtd
def numeroEstudantesCurso():
	cursos = ["ARQUITETURA E URBANISMO","ARTES VISUAIS (LICENCIATURA)","CIENCIA DA COMPUTACAO (BACHARELADO)","CIENCIA DA COMPUTACAO (LICENCIATURA)","CIENCIAS BIOLOGICAS (BACHARELADO)","CIENCIAS BIOLOGICAS (LICENCIATURA)","CIENCIAS SOCIAIS (BACHARELADO)","CIENCIAS SOCIAIS (LICENCIATURA)","EDUCACAO FISICA (LICENCIATURA)","ENGENHARIA AMBIENTAL","ENGENHARIA CIVIL","ENGENHARIA DE ALIMENTOS","ENGENHARIA DE COMPUTACAO","ENGENHARIA DE CONTROLE E AUTOMACAO","ENGENHARIA DE PRODUCAO","ENGENHARIA ELETRICA","ENGENHARIA FLORESTAL","ENGENHARIA MECANICA","ENGENHARIA QUIMICA","ENGENHARIA","FILOSOFIA (BACHARELADO)","FILOSOFIA (LICENCIATURA)","FISICA (BACHARELADO)","FISICA (LICENCIATURA)","GEOGRAFIA (BACHARELADO)","GEOGRAFIA (LICENCIATURA)","HISTORIA (BACHARELADO)","HISTORIA (LICENCIATURA)","LETRAS-PORTUGUES (BACHARELADO)","LETRAS-PORTUGUES (LICENCIATURA)","LETRAS-PORTUGUES E ESPANHOL (LICENCIATURA)","LETRAS-PORTUGUES E INGLES (LICENCIATURA)","MATEMATICA (BACHARELADO)","MATEMATICA (LICENCIATURA)","MUSICA (LICENCIATURA)","PEDAGOGIA (LICENCIATURA)","QUIMICA (BACHARELADO)","QUIMICA (LICENCIATURA)","SISTEMAS DE INFORMACAO","TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS","TECNOLOGIA EM AUTOMACAO INDUSTRIAL","TECNOLOGIA EM GESTAO DA PRODUCAO INDUSTRIAL","TECNOLOGIA EM REDES DE COMPUTADORES",""]
	dic_qtd_cursos = {}
	for curso in cursos:
		dic_qtd_cursos["\""+curso+"\""] = 0
	dic_qtd_cursos["\"\""] = 480923
	fh_ENADE = open("enade_so_cotas.txt","r")
	for linha in fh_ENADE:
		atributos = linha.split(",")
		dic_qtd_cursos[atributos[1]] += 1
	fh_ENADE.close()
	
	return dic_qtd_cursos
def calculaMediana(data):
	if len(data) > 0:
		return str(np.percentile(data,50))
	else:
		return "0"
def main():
	start_time = time.time()
	dic_qtd_cursos = numeroEstudantesCurso()
	cursos = ["ARQUITETURA E URBANISMO","ARTES VISUAIS (LICENCIATURA)","CIENCIA DA COMPUTACAO (BACHARELADO)","CIENCIA DA COMPUTACAO (LICENCIATURA)","CIENCIAS BIOLOGICAS (BACHARELADO)","CIENCIAS BIOLOGICAS (LICENCIATURA)","CIENCIAS SOCIAIS (BACHARELADO)","CIENCIAS SOCIAIS (LICENCIATURA)","EDUCACAO FISICA (LICENCIATURA)","ENGENHARIA AMBIENTAL","ENGENHARIA CIVIL","ENGENHARIA DE ALIMENTOS","ENGENHARIA DE COMPUTACAO","ENGENHARIA DE CONTROLE E AUTOMACAO","ENGENHARIA DE PRODUCAO","ENGENHARIA ELETRICA","ENGENHARIA FLORESTAL","ENGENHARIA MECANICA","ENGENHARIA QUIMICA","ENGENHARIA","FILOSOFIA (BACHARELADO)","FILOSOFIA (LICENCIATURA)","FISICA (BACHARELADO)","FISICA (LICENCIATURA)","GEOGRAFIA (BACHARELADO)","GEOGRAFIA (LICENCIATURA)","HISTORIA (BACHARELADO)","HISTORIA (LICENCIATURA)","LETRAS-PORTUGUES (BACHARELADO)","LETRAS-PORTUGUES (LICENCIATURA)","LETRAS-PORTUGUES E ESPANHOL (LICENCIATURA)","LETRAS-PORTUGUES E INGLES (LICENCIATURA)","MATEMATICA (BACHARELADO)","MATEMATICA (LICENCIATURA)","MUSICA (LICENCIATURA)","PEDAGOGIA (LICENCIATURA)","QUIMICA (BACHARELADO)","QUIMICA (LICENCIATURA)","SISTEMAS DE INFORMACAO","TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS","TECNOLOGIA EM AUTOMACAO INDUSTRIAL","TECNOLOGIA EM GESTAO DA PRODUCAO INDUSTRIAL","TECNOLOGIA EM REDES DE COMPUTADORES",""]
	#cursos = [""]
	#etnias = ["Branco(a).","Negro(a).","Pardo(a)/mulato(a)."]
	fh_brancos = open("enade_so_cotas_brancos.txt","r",encoding="utf-8")
	fh_negros = open("enade_so_cotas_negros.txt","r",encoding="utf-8")
	fh_pardos = open("enade_so_cotas_pardos.txt","r",encoding="utf-8")
	etnias = [fh_brancos,fh_negros,fh_pardos] 
	fh_saida_fg = open("tabela_folha_fg.txt","w")
	fh_saida_ce = open("tabela_folha_ce.txt","w")
	fh_saida_ger = open("tabela_folha_ger.txt","w")
	fh_saida_percentual = open("tabela_folha_percentual.txt","w")
	for curso in cursos:
		data_nt_fg = []
		data_nt_ce = []
		data_nt_ger = []
		fh_saida_fg.write(curso+"_fg\t")
		fh_saida_ce.write(curso+"_ce\t")
		fh_saida_ger.write(curso+"_ger\t")
		fh_saida_percentual.write(curso+"_percentual\t")

		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"",126,"Todo em escola publica.")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"",126,"Todo em escola privada (particular).")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"federal",126,"Todo em escola publica.")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"privada",126,"Todo em escola privada (particular).")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"privada",117,"De 1;5 a 3 salarios minimos (R$ 1.086;01 a R$ 2.172;00).")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"privada",117,"De 10 a 30 salarios minimos (R$ 7.240;01 a R$ 21.720;00).")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"federal",117,"De 1;5 a 3 salarios minimos (R$ 1.086;01 a R$ 2.172;00).")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"federal",117,"De 10 a 30 salarios minimos (R$ 7.240;01 a R$ 21.720;00).")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"privada",0,"")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"privada",124,"Sim; por criterio etnico-racial.")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"federal",0,"")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
			
		return_fg,return_ce,return_ger,qtd = getData(fh_brancos,"Branco(a).",curso,"federal",124,"Nao.")
		fh_saida_fg.write(calculaMediana(return_fg)+"\t")
		fh_saida_ce.write(calculaMediana(return_ce)+"\t")
		fh_saida_ger.write(calculaMediana(return_ger)+"\t")
		fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		
		return_fg,return_ce,return_ger,qtd = getData(fh_brancos,"Branco(a).",curso,"federal",124,"Sim; por criterio de renda.")
		fh_saida_fg.write(calculaMediana(return_fg)+"\t")
		fh_saida_ce.write(calculaMediana(return_ce)+"\t")
		fh_saida_ger.write(calculaMediana(return_ger)+"\t")
		fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		
		return_fg,return_ce,return_ger,qtd = getData(fh_brancos,"Branco(a).",curso,"federal",124,"Sim; por ter estudado em escola publica ou particular com bolsa de estudos.")
		fh_saida_fg.write(calculaMediana(return_fg)+"\t")
		fh_saida_ce.write(calculaMediana(return_ce)+"\t")
		fh_saida_ger.write(calculaMediana(return_ger)+"\t")
		fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		
		
		etnias.pop(0)
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"federal",124,"Nao.")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
			
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"federal",124,"Sim; por ter estudado em escola publica ou particular com bolsa de estudos.")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")

			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"federal",124,"Sim; por criterio etnico-racial.")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
			
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"federal",124,"Sim; por criterio de renda.")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		etnias.insert(0,fh_brancos)

		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"federal",126,"Todo em escola privada (particular).")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
		
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"privada",126,"Todo em escola publica.")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
			
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getData(etnia,etnia,curso,"federal",124,"Sim; por ter estudado em escola publica ou particular com bolsa de estudos.")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
			
		for etnia in etnias:
			return_fg,return_ce,return_ger,qtd = getDataDuplo(etnia,etnia,curso,"federal",126,"Todo em escola privada (particular).",124,"Nao.")
			fh_saida_fg.write(calculaMediana(return_fg)+"\t")
			fh_saida_ce.write(calculaMediana(return_ce)+"\t")
			fh_saida_ger.write(calculaMediana(return_ger)+"\t")
			fh_saida_percentual.write(str(round(((qtd*100)/dic_qtd_cursos["\""+curso+"\""]),3)) + "%"+"\t")
			
		fh_saida_fg.write("\n")
		fh_saida_ce.write("\n")
		fh_saida_ger.write("\n")
		fh_saida_percentual.write("\n")
			
	fh_saida_fg.write("\n")
	fh_saida_ce.write("\n")
	fh_saida_ger.write("\n")
	fh_saida_percentual.write("\n")
	fh_brancos.close()
	fh_negros.close()
	fh_pardos.close()
	fh_saida_fg.close()
	fh_saida_ce.close()
	fh_saida_ger.close()
	fh_saida_percentual.close()
			
	print("--- %s seconds ---" % (time.time() - start_time))
main()