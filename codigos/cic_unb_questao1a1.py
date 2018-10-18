fh = open("CIC_UNB.txt","r")
numero_total_instancias = 24
vetor_form_geral = []
vetor_form_especifico = []
for linha in fh:
	atributos = linha.split(",")
	vetor_form_geral.append(atributos[46])
	vetor_form_especifico.append(atributos[56])
fh_saida = open("CIC_unb_questao_individual.txt","w")
for j in range(0,8):
	A = 0
	B = 0
	C = 0
	D = 0
	E = 0
	branco = 0
	branco2 = 0
	for i in range(0,len(vetor_form_geral)):
		if(vetor_form_geral[i][1:-1][j] == 'A'):
			A += 1
		elif(vetor_form_geral[i][1:-1][j] == 'B'):
			B += 1	
		elif(vetor_form_geral[i][1:-1][j] == 'C'):
			C += 1	
		elif(vetor_form_geral[i][1:-1][j] == 'D'):
			D += 1	
		elif(vetor_form_geral[i][1:-1][j] == 'E'):
			E += 1
		elif(vetor_form_geral[i][1:-1][j] == '.'):
			branco += 1
		elif(vetor_form_geral[i][1:-1][j] == '*'):
			branco2 += 1
	fh_saida.write("Questao "+str(j+1)+":\n")
	fh_saida.write("a) "+str(round(((A*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("b) "+str(round(((B*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("c) "+str(round(((C*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("d) "+str(round(((D*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("e) "+str(round(((E*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("em branco) "+str(round(((branco*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("multiplas respostas) "+str(round(((branco2*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("\n\n")
for j in range(0,27):
	A = 0
	B = 0
	C = 0
	D = 0
	E = 0
	branco = 0
	branco2 = 0
	for i in range(0,len(vetor_form_especifico)):
		if(vetor_form_especifico[i][1:-1][j] == 'A'):
			A += 1
		elif(vetor_form_especifico[i][1:-1][j] == 'B'):
			B += 1	
		elif(vetor_form_especifico[i][1:-1][j] == 'C'):
			C += 1	
		elif(vetor_form_especifico[i][1:-1][j] == 'D'):
			D += 1	
		elif(vetor_form_especifico[i][1:-1][j] == 'E'):
			E += 1
		elif(vetor_form_especifico[i][1:-1][j] == '.'):
			branco += 1
		elif(vetor_form_especifico[i][1:-1][j] == '*'):
			branco2 += 1
	fh_saida.write("Questao "+str(j+9)+":\n")
	fh_saida.write("a) "+str(round(((A*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("b) "+str(round(((B*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("c) "+str(round(((C*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("d) "+str(round(((D*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("e) "+str(round(((E*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("em branco) "+str(round(((branco*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("multiplas respostas) "+str(round(((branco2*100)/numero_total_instancias),3)) + "%\n")
	fh_saida.write("\n\n")
fh_saida.close()
	