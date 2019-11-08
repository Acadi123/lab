def entrada ():
    N = int(input())
    entrada = input().split()
    return entrada

def comparando():
    global entrada
    contador = 0
    for i in range(len(entrada)):
        for j in range(i+1, len(entrada)):
            if int(entrada[j]) < int(entrada[i]):
                contador += 1
    return contador
entrada = entrada()
c = comparando()
print(c)
