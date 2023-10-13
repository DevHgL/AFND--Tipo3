AFND = open('arquivo.txt', 'r')
regras = [] # regra 0 = estagios, regra 1 = alfabeto, regra 2 = estagio inicial,
            # regra 3 = estagios finais, regra 4 = transições
for linha in AFND:
    linha = linha.strip()
    regras.append(linha)

AFND.close()

def afndParaGr3(regras):
    estados = set(regras[0].split(','))
    alfabeto = set(regras[1].split(' '))
    estagioInicial = set(regras[2])
    estagiosFinais = set(regras[3].split(' '))
    transicoes = set(regras[4].split(' '))

