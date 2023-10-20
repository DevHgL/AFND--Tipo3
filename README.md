# Trabalho de Implementação
## LFTC - Conversão de Automato para Gramatica
Este repositório é a implementação de um trabalho de Linguagens Formais e Teoria da Computação do curso de Ciência da Computação na UFF-PURO no período de 2022-1.
<br>
O grupo composto por Hugo Leonardo Melo e Felipe Alves deve implementar um programa que converta um automato finito não deterministico em uma gramatica regular.

## Uso

Para usar o programa tenha arquivos texto criados com os AFNDs que você quer converter, sendo:

* K o estado inicial;
* L um estado final;
* M um estado intermediario;
* @ uma cadeia vazia;

no seguinte formato:

```
  I = K
  F = {L, ...}
  (K, a) = {K, L, ...}
  (K, b) = {K, M, L, ...}
  (L, a) = {L, ...}
```

Em seguida, no seu sistema operacional preferido, abra o terminal ou prompt de comando, va para o diretorio onde está o programa e digite:

```
  py converte.py (automato1.txt) [(automato2.txt), ..., (automatoN.txt)]
```

O programa ira converter cada automato e exibir na tela o automato e sua respectiva gramatica.

### ATENÇÃO

* O AFND que será convertido deve ter no maximo 9 estados(1 a 9).