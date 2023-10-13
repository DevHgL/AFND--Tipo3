AFND = open('arquivo.txt', 'r')
regras = [] # regra 0 = estagios, regra 1 = alfabeto, regra 2 = estagio inicial,
            # regra 3 = estagios finais, regra 4 = transições
for linha in AFND:
    linha = linha.strip()
    regras.append(linha)

AFND.close()

for regra in regras:
    print(regra)
