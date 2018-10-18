#cursos = ["ARQUITETURA E URBANISMO","ARTES VISUAIS (LICENCIATURA)","CIENCIA DA COMPUTACAO (BACHARELADO)","CIENCIA DA COMPUTACAO (LICENCIATURA)","CIENCIAS BIOLOGICAS (BACHARELADO)","CIENCIAS BIOLOGICAS (LICENCIATURA)","CIENCIAS SOCIAIS (BACHARELADO)","CIENCIAS SOCIAIS (LICENCIATURA)","EDUCACAO FISICA (LICENCIATURA)","ENGENHARIA AMBIENTAL","ENGENHARIA CIVIL","ENGENHARIA DE ALIMENTOS","ENGENHARIA DE COMPUTACAO","ENGENHARIA DE CONTROLE E AUTOMACAO","ENGENHARIA DE PRODUCAO","ENGENHARIA ELETRICA","ENGENHARIA FLORESTAL","ENGENHARIA MECANICA","ENGENHARIA QUIMICA","ENGENHARIA","FILOSOFIA (BACHARELADO)","FILOSOFIA (LICENCIATURA)","FISICA (BACHARELADO)","FISICA (LICENCIATURA)","GEOGRAFIA (BACHARELADO)","GEOGRAFIA (LICENCIATURA)","HISTORIA (BACHARELADO)","HISTORIA (LICENCIATURA)","LETRAS-PORTUGUES (BACHARELADO)","LETRAS-PORTUGUES (LICENCIATURA)","LETRAS-PORTUGUES E ESPANHOL (LICENCIATURA)","LETRAS-PORTUGUES E INGLES (LICENCIATURA)","MATEMATICA (BACHARELADO)","MATEMATICA (LICENCIATURA)","MUSICA (LICENCIATURA)","PEDAGOGIA (LICENCIATURA)","QUIMICA (BACHARELADO)","QUIMICA (LICENCIATURA)","SISTEMAS DE INFORMACAO","TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS","TECNOLOGIA EM AUTOMACAO INDUSTRIAL","TECNOLOGIA EM GESTAO DA PRODUCAO INDUSTRIAL","TECNOLOGIA EM REDES DE COMPUTADORES"]
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict


def gera_heatmaps(dic_cursos):
	
	atributos = ["qp_i1_dificuldade_prova_fg","qp_i2_dificuldade_prova_ce","qp_i3_duracao_da_prova_adequada","qp_i4_enunciados_claros_e_objetivos_fg","qp_i5_enunciados_claros_e_objetivos_Ce","qp_i6_informacoes_e_instrucoes_suficientes","qp_i7_dificuldade_resposta","qp_i8_ja_aprendeu_conteudo","qp_i9_tempo_concluir_a_prova","i7_qtde_familiares_em_casa","i8_renda_familia","i10_situacao_trabalho","i22_qts_livros_leu_neste_ano","i23_qts_horas_estudo_a_parte_p_semana","Nota_FG","Nota_CE","Nota_GER"]
	#restantes depis de musica:
	#cursos_restantes = ["MUSICA (LICENCIATURA)","PEDAGOGIA (LICENCIATURA)","QUIMICA (BACHARELADO)","QUIMICA (LICENCIATURA)","SISTEMAS DE INFORMACAO","TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS","TECNOLOGIA EM AUTOMACAO INDUSTRIAL","TECNOLOGIA EM GESTAO DA PRODUCAO INDUSTRIAL","TECNOLOGIA EM REDES DE COMPUTADORES"]
	#atributos = ["qp_i1","qp_i2","qp_i3","qp_i4","qp_i5","qp_i6","qp_i7","qp_i8","qp_i9","i7_qtde_familiares_em_casa","i8_renda_familia","i10_situacao_trabalho","i22_qts_livros_leu_neste_ano","i23_qts_horas_estudo","Nota_FG","Nota_CE","Nota_GER"]
	for key in dic_cursos:
		#key="\""+key+"\""
		print(key)
		

		matriz = [[0 for x in range(17)] for y in range(17)]

		for k in range(0,17):
			for j in range(0,17):
				A=[]
				B=[]
				for i in range(len(dic_cursos[key][k])):
					if(dic_cursos[key][k][i] != '?' and dic_cursos[key][k][i] != '?\n' and dic_cursos[key][k][i] != -1 and dic_cursos[key][j][i] != -1 and dic_cursos[key][j][i] != '?' and dic_cursos[key][j][i] != '?\n'):
						A.append(float(dic_cursos[key][k][i]))
						B.append(float(dic_cursos[key][j][i]))
				df = pd.DataFrame({'A': A, 'B': B})
				matriz[k][j] = df['A'].corr(df['B'])
		plt.figure(figsize=(160,140))
		plt.rcParams.update({'font.size': 50})
		plt.imshow(matriz, cmap='hot', interpolation='nearest')
		plt.colorbar()
		plt.title(key[1:-1])
		plt.xticks(range(17),atributos,rotation = 90)
		plt.yticks(range(17),atributos)
		plt.savefig(key[1:-1]+'_heatmap.png')

#Codigo para gerar a tabela:

def gera_tabela(dic_cursos):
	fh_saida = open("correlacao_enade.txt","w")
	for key in dic_cursos:
		print(key[1:-1])
		fh_saida.write(key[1:-1] + "\t")
		#loop para comparar as notas(fg,ce,ger) com todos os outros atributos
		for k in range(14,17):
			for j in range(0,14):
				A=[]
				B=[]
				for i in range(len(dic_cursos[key][k])):
					if(dic_cursos[key][k][i] != '?' and dic_cursos[key][k][i] != '?\n' and dic_cursos[key][j][i] != -1):
						A.append(float(dic_cursos[key][k][i]))
						B.append(float(dic_cursos[key][j][i]))
				df = pd.DataFrame({'A': A, 'B': B})
				fh_saida.write(str(df['A'].corr(df['B']))+"\t")
		
		for p in range(1,14):
			for j in range(p,14):
				A=[]
				B=[]
				for i in range(len(dic_cursos[key][(p-1)])):
					if(dic_cursos[key][(p-1)][i] != -1 and dic_cursos[key][j][i] != -1):
						A.append(float(dic_cursos[key][(p-1)][i]))
						B.append(float(dic_cursos[key][j][i]))
				df = pd.DataFrame({'A': A, 'B': B})
				fh_saida.write(str(df['A'].corr(df['B']))+"\t")
				

		
		fh_saida.write("\n")
	fh_saida.close()

fh_entrada = open("subs_enade.txt",'r')

dic_cursos = OrderedDict()
cursos = ["ARQUITETURA E URBANISMO","ARTES VISUAIS (LICENCIATURA)","CIENCIA DA COMPUTACAO (BACHARELADO)","CIENCIA DA COMPUTACAO (LICENCIATURA)","CIENCIAS BIOLOGICAS (BACHARELADO)","CIENCIAS BIOLOGICAS (LICENCIATURA)","CIENCIAS SOCIAIS (BACHARELADO)","CIENCIAS SOCIAIS (LICENCIATURA)","EDUCACAO FISICA (LICENCIATURA)","ENGENHARIA AMBIENTAL","ENGENHARIA CIVIL","ENGENHARIA DE ALIMENTOS","ENGENHARIA DE COMPUTACAO","ENGENHARIA DE CONTROLE E AUTOMACAO","ENGENHARIA DE PRODUCAO","ENGENHARIA ELETRICA","ENGENHARIA FLORESTAL","ENGENHARIA MECANICA","ENGENHARIA QUIMICA","ENGENHARIA","FILOSOFIA (BACHARELADO)","FILOSOFIA (LICENCIATURA)","FISICA (BACHARELADO)","FISICA (LICENCIATURA)","GEOGRAFIA (BACHARELADO)","GEOGRAFIA (LICENCIATURA)","HISTORIA (BACHARELADO)","HISTORIA (LICENCIATURA)","LETRAS-PORTUGUES (BACHARELADO)","LETRAS-PORTUGUES (LICENCIATURA)","LETRAS-PORTUGUES E ESPANHOL (LICENCIATURA)","LETRAS-PORTUGUES E INGLES (LICENCIATURA)","MATEMATICA (BACHARELADO)","MATEMATICA (LICENCIATURA)","MUSICA (LICENCIATURA)","PEDAGOGIA (LICENCIATURA)","QUIMICA (BACHARELADO)","QUIMICA (LICENCIATURA)","SISTEMAS DE INFORMACAO","TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS","TECNOLOGIA EM AUTOMACAO INDUSTRIAL","TECNOLOGIA EM GESTAO DA PRODUCAO INDUSTRIAL","TECNOLOGIA EM REDES DE COMPUTADORES"]
for curso in cursos:
	dic_cursos["\""+curso+"\""] = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	

for linha in fh_entrada:
	atributos = linha.split("\t")
	for i in range(0,17):
		dic_cursos[atributos[0]][i].append((atributos[i+1]))
		
fh_entrada.close()

gera_tabela(dic_cursos)
#gera_heatmaps(dic_cursos)
