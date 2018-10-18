from unicodedata import normalize

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

	
fh = open("dics.txt","r",encoding="utf-8")
data = fh.read()
fh.close()
fh = open("dics.txt","w",encoding="utf-8")
fh.write(remover_acentos(data))
fh.close()
'''
fh = open("saida_replace.txt","r",encoding="utf-8")
fh_saida = open("enade_sem_acento.txt","w",encoding="utf-8")
for linha in fh:
	fh_saida.write(remover_acentos(linha))
fh.close()
fh_saida.close()'''