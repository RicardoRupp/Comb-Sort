# Comb Sort em Python

## Descrição
Este projeto implementa o algoritmo **Comb Sort** em Python.

O Comb Sort é uma melhoria do Bubble Sort que reduz o número de comparações necessárias utilizando um intervalo (*gap*) entre elementos. Esse intervalo diminui gradualmente até atingir 1, momento em que o algoritmo funciona de forma semelhante ao Bubble Sort.

## Funcionamento
1. Define um intervalo inicial igual ao tamanho do vetor.
2. Compara elementos separados pelo intervalo.
3. Troca os elementos quando necessário.
4. Reduz o intervalo utilizando um fator de redução (1,3).
5. Repete até que o vetor esteja completamente ordenado.

## Estrutura do código

- `getNextGap(gap)`
  - Calcula o próximo intervalo.

- `combSort(arr)`
  - Executa a ordenação.

- Código principal
  - Solicita os valores ao usuário.
  - Executa a ordenação.
  - Exibe o vetor ordenado.

## Como executar
```bash
python comb.py

```bash
python comb.py
