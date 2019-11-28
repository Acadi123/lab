def entrada():
    N, A, B = input().split()
    lista = [[] for x in range(int(N))]
    for i in range(int(N)-1):
        P,Q = input().split()
        #lista contem as ligaçoes das cidades
        #ex P e Q = 3 e 12
        #na lista[2] fica 11
        lista[int(P)-1].append(int(Q)-1)
        #na lista[10] fica 2
        lista[int(Q)-1].append(int(P)-1)
    return ((lista, int(A)-1, int(B)-1))

def DFS(lista, origem, destino, anterior=None, controle=0):
    if origem == destino:
        print(controle)
        return

    for l in lista[origem]:
        if l != anterior:
            DFS(lista, l, destino,origem,controle+1)

cidades, A, B = entrada()
DFS(cidades, A, B)
