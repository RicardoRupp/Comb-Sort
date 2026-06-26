# Função para encontrar o próximo intervalo
def getNextGap(gap):

    # Reduz o intervalo pelo fator de redução
    gap = (gap * 10) // 13

    if gap < 1:
        return 1

    return gap


# Função para ordenar usando Comb Sort
def combSort(arr):

    n = len(arr)

    gap = n

    swapped = True

    while gap != 1 or swapped:

        gap = getNextGap(gap)

        swapped = False

        for i in range(0, n - gap):

            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True


# Código principal

quantidade = int(input("Digite a quantidade de elementos: "))

arr = []

for i in range(quantidade):
    valor = int(input(f"Digite o {i+1}º valor: "))
    arr.append(valor)

combSort(arr)

print("\nVetor ordenado:")

for i in range(len(arr)):
    print(arr[i], end=" ")