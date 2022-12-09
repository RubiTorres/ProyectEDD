import random


def countSort(arr):
    output = [0 for i in range(len(arr))]

    count = [0 for i in range(256)]

    ans = ["" for _ in arr]

    for i in arr:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


if __name__ == '__main__':
    arreglo = []
    tamaño = int(input())
    llenar = 0
    while llenar < tamaño:
        arreglo.append(random.randint(0, 100))
        llenar = llenar + 1
    cadenaDesordenada = ""
    for item in arreglo:
        cadenaDesordenada += str(item) + " "
    print(cadenaDesordenada)
    countSort(arreglo)
    for item in arreglo:
        print(str(item) + " ")