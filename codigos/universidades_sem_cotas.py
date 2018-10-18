fh_enade = open("enade_sem_acento.txt","r")

dic_unis = {}

for linha in fh_enade:
	atributos = linha.split(",")
	dic_unis[atributos[2]] = 0
	
fh_enade.seek(0)

for linha in fh_enade:
	atributos = linha.split(",")
	dic_unis[atributos[2]] += 1
	
fh_enade.seek(0)

for linha in fh_enade:
	atributos = linha.split(",")
	if(atributos[124] == "\"Nao.\""):
		dic_unis[atributos[2]] -= 1
fh_saida = open("Universidades_sem_cotas.txt","w")
for key in dic_unis:
	if(dic_unis[key] == 0):
		fh_saida.write("atributos[2][1:-1] != "+key+") and (")
	if(dic_unis[key] < 0):
		print("deu ruim")
		
fh_saida.close()
fh_enade.close()

