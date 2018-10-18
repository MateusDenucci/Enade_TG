fh_unis = open("todas_universidades.txt","r")
fh_enade = open("enade_sem_acento.txt","r")

dic_unis = {}
#for linha in fh_unis:
#	dic_unis[linha[0:-1]] = 0

for linha in fh_enade:
	atributos = linha.split(",")
	dic_unis[atributos[2]] = 0
	
fh_enade.seek(0)

for linha in fh_enade:
	atributos = linha.split(",")
	dic_unis[atributos[2]] += 1
	
for key in dic_unis:
	print(key+"    "+str(dic_unis[key]))

fh_enade.close()
fh_unis.close()
