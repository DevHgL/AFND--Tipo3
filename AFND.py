class AFND:
    def __init__(self):
        self.estados = set()
        self.alfabeto = set()
        self.estagioInicial = set()
        self.estagioFinal = set()
        self.transicao = {}

    @classmethod
    def leArquivo(cls, filename):
        afnd = cls()

        with open(filename, 'r') as file:
            lines = file.readlines()

        if len(lines) < 5:
            print("Quantidade insuficiente de linhas!")
            return None

        # Leitura dos estágios (linha 1)
        estagios = set(map(int, lines[0].strip('{}\n').split(',')))
        afnd.estados.update(estagios)

        # Leitura do alfabeto (linha 2)
        alfabeto = set(lines[1].strip('{}\n').split(','))
        afnd.alfabeto.update(alfabeto)

        # Leitura do Estado Inicial (linha 3)
        estagioInicial = int(lines[2].strip())
        afnd.estagioInicial = estagioInicial

        # Leitura do Estágio Final (linha 4)
        estagioFinal = set(map(int, lines[3].strip('{}\n').split(',')))
        afnd.estagioFinal.update(estagioFinal)

        # Leitura das Transições (linha 5)
        transicoes = lines[4].strip().split(', ')
        for transicao in transicoes:
            parts = transicao.split('=')
            if len(parts) == 2:
                origem, destino = parts
                origem = int(origem.strip('()').split(',')[0])
                simbolo = destino.split(',')[0]
                destinos = set(map(int, destino.strip('{}').split(',')))
                afnd.transicao[(origem, simbolo)] = destinos

        return afnd

    # Não funciona direito.
    def exibirInformacoes(self):
        print("Estágios:", self.estados)
        print("Alfabeto:", self.alfabeto)
        print("Estado Inicial:", self.estagioInicial)
        print("Estados Finais:", self.estagioFinal)
        print("Transições:")
        for (origem, simbolo), destinos in self.transicao.items():
            print(f"({origem}, {simbolo}) = {destinos}")


def main():
    filename = input("Digite o nome do arquivo: ")
    afnd = AFND.leArquivo(filename)

    if afnd is not None:
        afnd.exibirInformacoes()

if __name__ == "__main__":
    main()
