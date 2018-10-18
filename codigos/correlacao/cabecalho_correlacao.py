string = "qp_i1_grau_dificuldade_prova_parte_Formacao_Geral	qp_i2_grau_dificuldade_prova_parte_Componente_Especifico	qp_i3_duracao_da_prova_considerando_extensao	qp_i4_enunciados_questoes_parte_Formacao_Geral_claros_e_objetivos	qp_i5_enunciados_questoes_parte_Componente_Especifico_claros_e_objetivos	qp_i6_informacoes_e_instrucoes_p_resol_questoes_foram_suficientes_p_resolvelas	qp_i7_alguma_dificuldade_ao_responder_a_prova	qp_i8_considerando_questoes_objetivas_percebeu_que	qp_i9_tempo_gasto_p_concluir_a_prova	i7_qtde_familiares_em_casa	i8_renda_familia	i10_situacao_trabalho	i22_qts_livros_leu_neste_ano	i23_qts_horas_estudo_a_parte_p_semana	Nota_FG	Nota_CE	Nota_GER"

colunas = string.split('\t')

fh_saida = open("cabecalho_correlacao.txt","w")

for k in range(14,17):
	for j in range(0,14):
		print(colunas[k]+" x "+colunas[j])
		fh_saida.write(colunas[k]+" x "+colunas[j]+"\t")

for p in range(1,14):
	for j in range(p,14):
		print(colunas[(p-1)]+" x "+colunas[j])
		fh_saida.write((colunas[(p-1)]+" x "+colunas[j])+"\t")
		
fh_saida.close()