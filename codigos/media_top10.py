dic = {}
dic["\"UNIVERSIDADE DO OESTE PAULISTA\""] = []
dic["\"UNIVERSIDADE FEDERAL DO AMAZONAS\""] = []
dic["\"UNIVERSIDADE ESTADUAL DO CENTRO OESTE\""] = []
dic["\"UNIVERSIDADE FEDERAL DE SANTA CATARINA\""] = []
dic["\"UNIVERSIDADE FEDERAL DE ALAGOAS\""] = []
dic["\"UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE\""] = []
dic["\"UNIVERSIDADE PAULISTA\""] = []
dic["\"UNIVERSIDADE FEDERAL DE SAO JOAO DEL REI\""] = []
dic["\"UNIVERSIDADE FEDERAL DA BAHIA\""] = []
dic["\"CENTRO UNIVERSITARIO DO INSTITUTO DE EDUCACAO SUPERIOR DE BRASILIA - IESB\""] = []
dic["\"UNIVERSIDADE DE BRASILIA\""] = []
fh = open('EXAME_TOP10_CIC.txt', 'r')
for linha in fh:
	atributos = linha.split(',')
	dic[atributos[2]].append(float(atributos[99]))
fh.close()
fh = open('nt_ce_TOP10EXAME.txt', 'w')
for key in dic:
	dic[key] = sum(dic[key])/len(dic[key])
sorted_by_value = sorted(dic.items(), key=lambda kv: kv[1])
print(sorted_by_value)
for item in sorted_by_value:
	fh.write(item[0]+'\t'+str(item[1]))
	fh.write('\n')
fh.close()