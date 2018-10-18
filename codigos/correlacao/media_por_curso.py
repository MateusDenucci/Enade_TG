fh_entrada = open("subs_enade.txt","r")
fh_saida = open("media_por_curso_E.txt","w")


dic_cursos = {}
cursos = ["ARQUITETURA E URBANISMO","ARTES VISUAIS (LICENCIATURA)","CIENCIA DA COMPUTACAO (BACHARELADO)","CIENCIA DA COMPUTACAO (LICENCIATURA)","CIENCIAS BIOLOGICAS (BACHARELADO)","CIENCIAS BIOLOGICAS (LICENCIATURA)","CIENCIAS SOCIAIS (BACHARELADO)","CIENCIAS SOCIAIS (LICENCIATURA)","EDUCACAO FISICA (LICENCIATURA)","ENGENHARIA AMBIENTAL","ENGENHARIA CIVIL","ENGENHARIA DE ALIMENTOS","ENGENHARIA DE COMPUTACAO","ENGENHARIA DE CONTROLE E AUTOMACAO","ENGENHARIA DE PRODUCAO","ENGENHARIA ELETRICA","ENGENHARIA FLORESTAL","ENGENHARIA MECANICA","ENGENHARIA QUIMICA","ENGENHARIA","FILOSOFIA (BACHARELADO)","FILOSOFIA (LICENCIATURA)","FISICA (BACHARELADO)","FISICA (LICENCIATURA)","GEOGRAFIA (BACHARELADO)","GEOGRAFIA (LICENCIATURA)","HISTORIA (BACHARELADO)","HISTORIA (LICENCIATURA)","LETRAS-PORTUGUES (BACHARELADO)","LETRAS-PORTUGUES (LICENCIATURA)","LETRAS-PORTUGUES E ESPANHOL (LICENCIATURA)","LETRAS-PORTUGUES E INGLES (LICENCIATURA)","MATEMATICA (BACHARELADO)","MATEMATICA (LICENCIATURA)","MUSICA (LICENCIATURA)","PEDAGOGIA (LICENCIATURA)","QUIMICA (BACHARELADO)","QUIMICA (LICENCIATURA)","SISTEMAS DE INFORMACAO","TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS","TECNOLOGIA EM AUTOMACAO INDUSTRIAL","TECNOLOGIA EM GESTAO DA PRODUCAO INDUSTRIAL","TECNOLOGIA EM REDES DE COMPUTADORES"]
for curso in cursos:
	dic_cursos["\""+curso+"\""] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for linha in fh_entrada:
	atributos = linha.split('\t')

	for i in range(0,17):
		if((atributos[i+1] != -1) and (atributos[i+1] != '?') and (atributos[i+1] != '?\n')):
			dic_cursos[atributos[0]][i] += float(atributos[i+1])
			dic_cursos[atributos[0]][i+17] += 1
	
fh_entrada.close()
'''	
for key in dic_cursos:
	fh_saida.write(key+"\t")
	for i in range(0,17):
		dic_cursos[key][i] = float(dic_cursos[key][i]/dic_cursos[key][i+17])
		fh_saida.write(str(round(dic_cursos[key][i],3))+"\t")
	fh_saida.write("\n")
	
'''

ENADE = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for key in dic_cursos:
	for i in range(0,34):
		ENADE[i] += dic_cursos[key][i]
		
for i in range(0,17):
	ENADE[i] = float(ENADE[i]/ENADE[i+17])
	fh_saida.write(str(round(ENADE[i],3))+"\t")


fh_saida.close()

