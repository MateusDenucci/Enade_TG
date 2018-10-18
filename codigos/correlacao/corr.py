#cursos = ["ARQUITETURA E URBANISMO","ARTES VISUAIS (LICENCIATURA)","CIENCIA DA COMPUTACAO (BACHARELADO)","CIENCIA DA COMPUTACAO (LICENCIATURA)","CIENCIAS BIOLOGICAS (BACHARELADO)","CIENCIAS BIOLOGICAS (LICENCIATURA)","CIENCIAS SOCIAIS (BACHARELADO)","CIENCIAS SOCIAIS (LICENCIATURA)","EDUCACAO FISICA (LICENCIATURA)","ENGENHARIA AMBIENTAL","ENGENHARIA CIVIL","ENGENHARIA DE ALIMENTOS","ENGENHARIA DE COMPUTACAO","ENGENHARIA DE CONTROLE E AUTOMACAO","ENGENHARIA DE PRODUCAO","ENGENHARIA ELETRICA","ENGENHARIA FLORESTAL","ENGENHARIA MECANICA","ENGENHARIA QUIMICA","ENGENHARIA","FILOSOFIA (BACHARELADO)","FILOSOFIA (LICENCIATURA)","FISICA (BACHARELADO)","FISICA (LICENCIATURA)","GEOGRAFIA (BACHARELADO)","GEOGRAFIA (LICENCIATURA)","HISTORIA (BACHARELADO)","HISTORIA (LICENCIATURA)","LETRAS-PORTUGUES (BACHARELADO)","LETRAS-PORTUGUES (LICENCIATURA)","LETRAS-PORTUGUES E ESPANHOL (LICENCIATURA)","LETRAS-PORTUGUES E INGLES (LICENCIATURA)","MATEMATICA (BACHARELADO)","MATEMATICA (LICENCIATURA)","MUSICA (LICENCIATURA)","PEDAGOGIA (LICENCIATURA)","QUIMICA (BACHARELADO)","QUIMICA (LICENCIATURA)","SISTEMAS DE INFORMACAO","TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS","TECNOLOGIA EM AUTOMACAO INDUSTRIAL","TECNOLOGIA EM GESTAO DA PRODUCAO INDUSTRIAL","TECNOLOGIA EM REDES DE COMPUTADORES"]
import pandas as pd

fh_entrada = open("subs_enade.txt",'r')

dic_cursos = {}
cursos = ["ARQUITETURA E URBANISMO","ARTES VISUAIS (LICENCIATURA)","CIENCIA DA COMPUTACAO (BACHARELADO)","CIENCIA DA COMPUTACAO (LICENCIATURA)","CIENCIAS BIOLOGICAS (BACHARELADO)","CIENCIAS BIOLOGICAS (LICENCIATURA)","CIENCIAS SOCIAIS (BACHARELADO)","CIENCIAS SOCIAIS (LICENCIATURA)","EDUCACAO FISICA (LICENCIATURA)","ENGENHARIA AMBIENTAL","ENGENHARIA CIVIL","ENGENHARIA DE ALIMENTOS","ENGENHARIA DE COMPUTACAO","ENGENHARIA DE CONTROLE E AUTOMACAO","ENGENHARIA DE PRODUCAO","ENGENHARIA ELETRICA","ENGENHARIA FLORESTAL","ENGENHARIA MECANICA","ENGENHARIA QUIMICA","ENGENHARIA","FILOSOFIA (BACHARELADO)","FILOSOFIA (LICENCIATURA)","FISICA (BACHARELADO)","FISICA (LICENCIATURA)","GEOGRAFIA (BACHARELADO)","GEOGRAFIA (LICENCIATURA)","HISTORIA (BACHARELADO)","HISTORIA (LICENCIATURA)","LETRAS-PORTUGUES (BACHARELADO)","LETRAS-PORTUGUES (LICENCIATURA)","LETRAS-PORTUGUES E ESPANHOL (LICENCIATURA)","LETRAS-PORTUGUES E INGLES (LICENCIATURA)","MATEMATICA (BACHARELADO)","MATEMATICA (LICENCIATURA)","MUSICA (LICENCIATURA)","PEDAGOGIA (LICENCIATURA)","QUIMICA (BACHARELADO)","QUIMICA (LICENCIATURA)","SISTEMAS DE INFORMACAO","TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS","TECNOLOGIA EM AUTOMACAO INDUSTRIAL","TECNOLOGIA EM GESTAO DA PRODUCAO INDUSTRIAL","TECNOLOGIA EM REDES DE COMPUTADORES"]
for curso in cursos:
	dic_cursos["\""+curso+"\""] = [[],[],[],[],[],[],[],[]]
	
for linha in fh_entrada:
	atributos = linha.split("\t")
	for i in range(0,8):
		dic_cursos[atributos[0]][i].append(atributos[i+10])
		
fh_entrada.close()

fh_saida = open("correlacao.txt","w")
for key in dic_cursos:
	print(key[1:-1])
	fh_saida.write(key[1:-1] + "\t")

	for k in range(5,8):
		for j in range(0,5):
			A=[]
			B=[]
			for i in range(len(dic_cursos[key][k])):
				if(dic_cursos[key][k][i] != '?' and dic_cursos[key][k][i] != '?\n' and dic_cursos[key][j][i] != -1):
					A.append(float(dic_cursos[key][k][i]))
					B.append(float(dic_cursos[key][j][i]))
			df = pd.DataFrame({'A': A, 'B': B})
			fh_saida.write(str(df['A'].corr(df['B']))+"\t")
	
	
	for j in range(1,5):
		A=[]
		B=[]
		for i in range(len(dic_cursos[key][0])):
			if(dic_cursos[key][0][i] != -1 and dic_cursos[key][j][i] != -1):
				A.append(float(dic_cursos[key][0][i]))
				B.append(float(dic_cursos[key][j][i]))
		df = pd.DataFrame({'A': A, 'B': B})
		fh_saida.write(str(df['A'].corr(df['B']))+"\t")
		
	for j in range(2,5):
		A=[]
		B=[]
		for i in range(len(dic_cursos[key][1])):
			if(dic_cursos[key][1][i] != -1 and dic_cursos[key][j][i] != -1):
				A.append(float(dic_cursos[key][1][i]))
				B.append(float(dic_cursos[key][j][i]))
		df = pd.DataFrame({'A': A, 'B': B})
		fh_saida.write(str(df['A'].corr(df['B']))+"\t")
		
		
	for j in range(3,5):
		A=[]
		B=[]
		for i in range(len(dic_cursos[key][2])):
			if(dic_cursos[key][2][i] != -1 and dic_cursos[key][j][i] != -1):
				A.append(float(dic_cursos[key][2][i]))
				B.append(float(dic_cursos[key][j][i]))
		df = pd.DataFrame({'A': A, 'B': B})
		fh_saida.write(str(df['A'].corr(df['B']))+"\t")
		
	for j in range(4,5):
		A=[]
		B=[]
		for i in range(len(dic_cursos[key][3])):
			if(dic_cursos[key][3][i] != -1 and dic_cursos[key][j][i] != -1):
				A.append(float(dic_cursos[key][3][i]))
				B.append(float(dic_cursos[key][j][i]))
		df = pd.DataFrame({'A': A, 'B': B})
		fh_saida.write(str(df['A'].corr(df['B']))+"\t")

	
	fh_saida.write("\n")
fh_saida.close()