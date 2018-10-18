fh_entrada = open("enade_sem_acento.txt","r")
fh_saida = open("subs_enade.txt","w")


dic_renda = {"Ate 1;5 salario minimo (ate R$ 1.086;00).":543,"De 1;5 a 3 salarios minimos (R$ 1.086;01 a R$ 2.172;00).":1629,"De 3 a 4;5 salarios minimos (R$ 2.172;01 a R$ 3.258;00).":2715,"De 4;5 a 6 salarios minimos (R$ 3.258;01 a R$ 4.344;00).":3801,"De 6 a 10 salarios minimos (R$ 4.344;01 a R$ 7.240;00).":5792,"De 10 a 30 salarios minimos (R$ 7.240;01 a R$ 21.720;00).":14480,"Acima de 30 salarios minimos (mais de R$ 21.720;01).":21720,"":-1}
#117 renda

dic_livros = {"Nenhum.":0,"Um ou dois.":1.5,"De tres a cinco.":4,"De seis a oito.":7,"Mais de oito.":8,"":-1}	
#131 livros

dic_horas_estudo = {"Nenhuma; apenas assisto as aulas.":0,"De uma a tres.":2,"De quatro a sete.":5.5,"De oito a doze.":10,"Mais de doze.":12,"":-1}
#132 horas


dic_horas_trabalho = {"Nao estou trabalhando.": 0,"Trabalho eventualmente.": 5,"Trabalho ate 20 horas semanais.":20,"Trabalho de 21 a 39 horas semanais.":30,"Trabalho 40 horas semanais ou mais.":40,"":-1}
#119 trabalho

dic_familiares  = {"Nenhuma.":0,"Uma.":1,"Duas.":2,"Tres.":3,"Quatro.":4,"Cinco.":5,"Seis.":6,"Sete ou mais.":7,"":-1}
#116

dic_dificuldade = {"Muito facil.": 1,"Facil.": 2,"Medio.": 3,"Dificil.": 4,"Muito dificil.": 5,".": -1,"*": -1,"":-1}
#101 e 102

dic_duracao = {"Muito longa.": 5,"Longa.": 4,"Adequada.": 3,"Curta.": 2,"Muito curta.": 1,".": -1,"*": -1,"":-1}
#103

dic_clareza = {"Sim; todos.": 5,"Sim; a maioria.": 4,"Apenas cerca da metade.": 3,"Poucos.": 2,"Poucos se apresentam.": 2,"Nao; nenhum.": 1,".": -1,"*": -1,"":-1}
#104 e 105 foi adicionado um extra pro 105.


dic_info_suficiente = {"Sim; ate excessivas.": 5,"Sim; em todas elas.": 4,"Sim; na maioria delas.": 3,"Sim; somente em algumas.": 2,"Nao; em nenhuma delas.": 1,".": -1,"*": -1,"":-1}
#106

dic_dificuldade_resposta = {"Desconhecimento do conteudo.": 5,"Forma diferente de abordagem do conteudo.": 4,"Espaco insuficiente para responder as questoes.": 3,"Falta de motivacao para fazer a prova.": 2,"Nao tive qualquer tipo de dificuldade para responder a prova.": 1,"*": -1,".": -1,"":-1}
#107

dic_aprendeu_conteudo = {"Nao estudou ainda a maioria desses conteudos.": 1,"Estudou alguns desses conteudos; mas nao os aprendeu.": 2,"Estudou a maioria desses conteudos; mas nao os aprendeu.": 3,"Estudou e aprendeu muitos desses conteudos.": 4,"Estudou e aprendeu todos esses conteudos.": 5,".": -1,"*": -1,"":-1}
#108

dic_tempo_gasto = {"Menos de uma hora.": 0.5,"Entre uma e duas horas.": 1.5,"Entre duas e tres horas.": 2.5,"Entre tres e quatro horas.": 3.5,"Quatro horas e nao consegui terminar.": 4,".": -1,"*": -1,"":-1}
#109

def numeroEstudantesCurso():
	cursos = ["ARQUITETURA E URBANISMO","ARTES VISUAIS (LICENCIATURA)","CIENCIA DA COMPUTACAO (BACHARELADO)","CIENCIA DA COMPUTACAO (LICENCIATURA)","CIENCIAS BIOLOGICAS (BACHARELADO)","CIENCIAS BIOLOGICAS (LICENCIATURA)","CIENCIAS SOCIAIS (BACHARELADO)","CIENCIAS SOCIAIS (LICENCIATURA)","EDUCACAO FISICA (LICENCIATURA)","ENGENHARIA AMBIENTAL","ENGENHARIA CIVIL","ENGENHARIA DE ALIMENTOS","ENGENHARIA DE COMPUTACAO","ENGENHARIA DE CONTROLE E AUTOMACAO","ENGENHARIA DE PRODUCAO","ENGENHARIA ELETRICA","ENGENHARIA FLORESTAL","ENGENHARIA MECANICA","ENGENHARIA QUIMICA","ENGENHARIA","FILOSOFIA (BACHARELADO)","FILOSOFIA (LICENCIATURA)","FISICA (BACHARELADO)","FISICA (LICENCIATURA)","GEOGRAFIA (BACHARELADO)","GEOGRAFIA (LICENCIATURA)","HISTORIA (BACHARELADO)","HISTORIA (LICENCIATURA)","LETRAS-PORTUGUES (BACHARELADO)","LETRAS-PORTUGUES (LICENCIATURA)","LETRAS-PORTUGUES E ESPANHOL (LICENCIATURA)","LETRAS-PORTUGUES E INGLES (LICENCIATURA)","MATEMATICA (BACHARELADO)","MATEMATICA (LICENCIATURA)","MUSICA (LICENCIATURA)","PEDAGOGIA (LICENCIATURA)","QUIMICA (BACHARELADO)","QUIMICA (LICENCIATURA)","SISTEMAS DE INFORMACAO","TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS","TECNOLOGIA EM AUTOMACAO INDUSTRIAL","TECNOLOGIA EM GESTAO DA PRODUCAO INDUSTRIAL","TECNOLOGIA EM REDES DE COMPUTADORES",""]
	dic_qtd_cursos = {}
	for curso in cursos:
		dic_qtd_cursos["\""+curso+"\""] = 0
	dic_qtd_cursos["\"\""] = 480923
	fh_ENADE = open("enade_sem_acento.txt","r")
	for linha in fh_ENADE:
		atributos = linha.split(",")
		dic_qtd_cursos[atributos[1]] += 1
	fh_ENADE.close()
	
	return dic_qtd_cursos

	
#dic_qtd_cursos = numeroEstudantesCurso()
for linha in fh_entrada:
	atributos = linha.split(",")
	fh_saida.write(atributos[1]+"\t"+str(dic_dificuldade[atributos[101][1:-1]])+"\t"+str(dic_dificuldade[atributos[102][1:-1]])+"\t"+str(dic_duracao[atributos[103][1:-1]])+"\t"+str(dic_clareza[atributos[104][1:-1]])+"\t"+str(dic_clareza[atributos[105][1:-1]])+"\t"+str(dic_info_suficiente[atributos[106][1:-1]])+"\t"+str(dic_dificuldade_resposta[atributos[107][1:-1]])+"\t"+str(dic_aprendeu_conteudo[atributos[108][1:-1]])+"\t"+str(dic_tempo_gasto[atributos[109][1:-1]])+"\t"+str(dic_familiares[atributos[116][1:-1]])+"\t"+str(dic_renda[atributos[117][1:-1]])+"\t"+str(dic_horas_trabalho[atributos[119][1:-1]])+"\t"+str(dic_livros[atributos[131][1:-1]])+"\t"+str(dic_horas_estudo[atributos[132][1:-1]])+"\t"+atributos[93]+"\t"+atributos[99]+"\t"+atributos[100])
	#fh_saida.write(atributos[2]+"\t"+str(dic_dificuldade[atributos[101][1:-1]]))
	fh_saida.write("\n")
	#print(dic_dificuldade[atributos[101][1:-1]])
fh_entrada.close()
fh_saida.close()