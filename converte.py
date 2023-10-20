import sys
from funcoesAuxiliares import limpaTela, filtra, escreve

def leAutomato(nomeArquivo):
	if not ".txt" in nomeArquivo[-4::]:
		nomeArquivo += ".txt"
	arquivo	 = open(nomeArquivo, 'r')
	automato = arquivo.readlines()
	arquivo.close()
	#Filtra "\n"s e espacos
	return filtra(automato)

def trocaInicio(gramatica, I):
	aux = []
	for linha in gramatica:
		linha.replace("1", "0").replace(I, "1").replace("0", I)
		aux.append(linha)
	return aux

def converteSimbolos(gramatica):
	aux = []
	for linha in gramatica:
		auxLinha = ""
		for c in linha:
			if c.isdigit():
				if c == "1":
					c = "S"
				else:
					c = chr(int(c)+63)
			auxLinha+=c
		aux.append(auxLinha)
	return aux

def fazConversao(automato):
	#Inicia lista de linhas da gramatica
	gramatica = []
	
	#Captura estado inicial a partir da primeira linha
	aux = automato[0]
	inicio = aux[-1]
	
	#Captura estados finais a partir da segunda linha
	aux    = automato[1]
	finais = aux[3::2]

	#Traduz todos os finais
	for f in finais:
		linha = f+" -> ε"
		gramatica.append(linha)

	#Captura transições das linhas seguintes e traduz
	for transicao in automato[2::]:
		simbolo   = transicao[1]
		caractere = transicao[3]
		for c in transicao[7::2]:
			linha = simbolo + " -> "
			if caractere != "@":
				linha+=caractere
			linha+=c
			gramatica.append(linha)

	#Caso I seja diferente de 1, troca todo I com 1
	if inicio!="1":
		gramatica = trocaInicio(gramatica, inicio)

	#Ordena a gramatica
	gramatica = sorted(gramatica)
				
	#Converter numeros dos estados em seus respectivos simbolos
	gramatica = converteSimbolos(gramatica)

	return gramatica

#Captura argumentos passados
argumentos    = sys.argv
#Remove primeiro argumento(converte.py)
listaArquivos = argumentos[1::]

for nomeArquivo in listaArquivos:

	limpaTela()

	#Lê automato a partir de um arquivo
	automato  = leAutomato(nomeArquivo)
	print("\nAFND:")
	escreve(automato)
	
	#Converte o automato finito não deterministico em gramatica regular
	gramatica = fazConversao(automato)
	print("\nGramatica:")
	escreve(gramatica)
	
	input("Pressione ENTER para continuar . . .")