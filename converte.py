import sys
from funcoesAuxiliares import limpaTela, filtra, escreve

def leAutomato(nomeArquivo):
    try:
        if not nomeArquivo.endswith(".txt"):  # Retira a obrigação de escrever o formato ".txt".
            nomeArquivo += ".txt"
        arquivo = open(nomeArquivo, 'r')
        automato = arquivo.readlines()
        arquivo.close()
        return filtra(automato)  # Retorna o autômato já sem quebra de linha, espaços, etc
    except FileNotFoundError:
        print(f"O arquivo '{nomeArquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None

def trocaInicio(gramatica, novoInicio):
    # Substitui o símbolo de início 1 pelo novo símbolo
    aux = []
    for linha in gramatica:
        linha = linha.replace("1", "0").replace(novoInicio, "1").replace("0", novoInicio)
        aux.append(linha)
    return aux

def converteSimbolos(gramatica):
    # Converte os símbolos numéricos em letras ou "S" de acordo com as regras
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
    # Obtém o símbolo de início e os estados finais do autômato
    inicio = automato[0][-1]
    finais = automato[1][3::2]

    for f in finais:
        linha = f + " -> ε"
        gramatica.append(linha)

    for transicao in automato[2:]:
        simbolo = transicao[1]
        caractere = transicao[3]
        for c in transicao[7::2]:
            linha = simbolo + " -> "
            if caractere != "@":
                linha += caractere
            linha += c
            gramatica.append(linha)

    if inicio != "1":
        # Se o símbolo de início não for 1, troca-o
        gramatica = trocaInicio(gramatica, inicio)

    gramatica = sorted(gramatica)
    gramatica = converteSimbolos(gramatica)

    return gramatica

def main():
    num = 9
    while True:
        nomeArquivo = input("Digite o nome do arquivo ( .txt é opcional!): ")
        automato = leAutomato(nomeArquivo)
        if automato is not None:
            print("\nAFND:")
            escreve(automato)

            gramatica = fazConversao(automato)
            print("\nGramatica:")
            escreve(gramatica)

        num = input("Digite [1] caso deseje continuar e [0] caso deseje parar: ")
        limpaTela()
        if (num == "0"):
            break


    print("Encerrando Programa!")

if __name__ == "__main__":
    main()
