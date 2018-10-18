fh_nota_fg = open("tabela_folha_fg.txt","r")
fh_nota_ce = open("tabela_folha_ce.txt","r")
fh_nota_ger = open("tabela_folha_ger.txt","r")
fh_nota_percentual = open("tabela_folha_percentual.txt","r")

string_fg = fh_nota_fg.read() 
string_ce = fh_nota_ce.read() 
string_ger = fh_nota_ger.read()
string_percentual = fh_nota_percentual.read()

linhas_fg = string_fg.split("\n")
linhas_ce = string_ce.split("\n")
linhas_ger = string_ger.split("\n")
linhas_percentual = string_percentual.split("\n")

fh_nota_fg.close()
fh_nota_ce.close()
fh_nota_ger.close()
fh_nota_percentual.close()

fh_saida = open("tabela_folha_FINAL_socotas_transposta_percentual.txt","w")

for i in range(0,44):
	fh_saida.write(linhas_fg[i]+"\n"+linhas_ce[i]+"\n"+linhas_ger[i]+"\n"+linhas_percentual[i]+"\n")
	fh_saida.write("Caracteristicas	alunos brancos segundo grau escola publica	alunos negros segundo grau escola publica	alunos pardos segundo grau escola publica	alunos brancos segundo grau escola particular	alunos negros segundo grau escola particular	alunos pardos segundo grau escola particular	alunos brancos federal segundo grau escola publica	alunos negros federal segundo grau escola publica	alunos pardos federal segundo grau escola publica	alunos brancos faculdade particular segundo grau escola particular	alunos negros faculdade particular segundo grau escola particular	alunos pardos faculdade particular segundo grau escola particular	alunos brancos particular renda 1;5 a 3 salarios minimos	alunos negros  particular renda 1;5 a 3 salarios minimos	alunos pardos particular renda 1;5 a 3 salarios minimos	alunos brancos particular renda 10 a 30 salarios minimos	alunos negros  particular renda 10 a 30 salarios minimos	alunos pardos particular renda 10 a 30 salarios minimos	alunos brancos federal renda 1;5 a 3 salarios minimos	alunos negros federal renda 1;5 a 3 salarios minimos	alunos pardos federal renda 1;5 a 3 salarios minimos	alunos brancos federal renda 10 a 30 salarios minimos	alunos negros  federal renda 10 a 30 salarios minimos	alunos pardos federal renda 10 a 30 salarios minimos	alunos particular brancos	alunos particular negros	alunos particular pardos	alunos particular brancos acao afirmativa racial	alunos particular negros acao afirmativa racial	alunos particular pardos acao afirmativa racial	alunos federal brancos	alunos federal negros	alunos federal pardos	alunos federal brancos sem acao afirmativa	alunos federal brancos acao afirmativa renda	alunos federal brancos acao afirmativa escola publica	alunos federal negros sem acao afirmativa	alunos federal negros acao afirmativa escola publica	alunos federal negros acao afirmativa racial	alunos federal negros acao afirmativa renda	alunos federal pardos sem acao afirmativa	alunos federal pardos acao afirmativa escola publica	alunos federal pardos acao afirmativa racial	alunos federal pardos acao afirmativa renda	alunos brancos federal segundo grau escola particular	alunos negros federal segundo grau escola particular	alunos pardos federal segundo grau escola particular	alunos brancos faculdade particular segundo grau escola publica	alunos negros faculdade particular segundo grau escola publica	alunos pardos faculdade particular segundo grau escola publica	alunos brancos federal segundo grau escola particular acao afirmativa	alunos negros federal segundo grau escola particular acao afirmativa	alunos pardos federal segundo grau escola particular acao afirmativa	alunos brancos federal segundo grau escola particular sem acao afirmativa	alunos negros federal segundo grau escola particular sem acao afirmativa	alunos pardos federal segundo grau escola particular sem acao afirmativa\n")
	
fh_saida.close()