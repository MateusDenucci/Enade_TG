fh_leitura = open("microdados_enade_2014.csv","r")
fh_escrita = open("dados.txt","w")

next(fh_leitura)
for linha in fh_leitura:
	atributos = linha.split(";")
	for i in range(155):
		if(atributos[i] == "\"\"") or (atributos[i] == ""):
			atributos[i] = '?'
		fh_escrita.write(atributos[i]+",")
	if(atributos[155] == "\n"):
		atributos[155] = '?\n'
	fh_escrita.write(atributos[155])
fh_leitura.close()
fh_escrita.close()
print("done")
