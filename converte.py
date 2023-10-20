import sys
from funcoesAuxiliares import limpaTela, filtra, escreve

def leAutomato(nomeArquivo):
    if not ".txt" in nomeArquivo[-4::]:
        nomeArquivo += ".txt"
    arquivo = open(nomeArquivo, 'r')
    automato = arquivo.readlines()
    arquivo.close()
    return filtra(automato)

def trocaInicio(gramatica, I):
    aux = []
    for linha in gramatica:
        linha = linha.replace("1", "0").replace(I, "1").replace("0", I)
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
                    c = chr(int(c) + 63)
            auxLinha += c
        aux.append(auxLinha)
    return aux

def fazConversao(automato):
    gramatica = []
    aux = automato[0]
    inicio = aux[-1]
    aux = automato[1]
    finais = aux[3::2]

    for f in finais:
        linha = f + " -> ε"
        gramatica.append(linha)

    for transicao in automato[2::]:
        simbolo = transicao[1]
        caractere = transicao[3]
        for c in transicao[7::2]:
            linha = simbolo + " -> "
            if caractere != "@":
                linha += caractere
            linha += c
            gramatica.append(linha)

    if inicio != "1":
        gramatica = trocaInicio(gramatica, inicio)

    gramatica = sorted(gramatica)
    gramatica = converteSimbolos(gramatica)

    return gramatica

def main():
    nomeArquivo = input("Digite o nome do arquivo: ")

    automato = leAutomato(nomeArquivo)
    print("\nAFND:")
    escreve(automato)

    gramatica = fazConversao(automato)
    print("\nGramatica:")
    escreve(gramatica)

    input("Pressione ENTER para continuar . . .")

if __name__ == "__main__":
    main()
