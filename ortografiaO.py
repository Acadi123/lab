#Manipulando entrada
entrada = input().split(' ')
N = int(entrada[0])
dicionario = []
for i in range(N):
    d = input()
    dicionario.append(d)
M = int(entrada[1])
palavraUsuario = []    
for i in range(M):
    p = input()
    palavraUsuario.append(p)
    

for p in range(len(palavraUsuario)):
    saida = ''
    for d in range(len(dicionario)):
        matriz =[]
        #matriz para metodo distância Levenshtein
        for x in range(len(palavraUsuario[p])+1):
            matriz.append([])
            for y in range(len(dicionario[d])+1):
                matriz[x].append((0))

        for i in range(0, len(palavraUsuario[p])+1): 
            matriz[i][0] = i

        for j in range(0, len(dicionario[d])+1):
            matriz[0][j] = j
            
        for x in range(1, len(palavraUsuario[p])+1):
            for y in range(1, len(dicionario[d])+1):
                if palavraUsuario[p][x-1] == dicionario[d][y-1]:
                    cost = 0
                else:
                    cost = 1
                distancias = ((matriz[x-1][y-1] + cost,matriz[x-1][y] + 1, matriz[x][y-1] + 1,))
                menor = distancias[0]
                #calculando a menor entre as distancias
                for i in distancias:
                    if menor > i:
                        menor = i
                matriz[x][y] = menor

                
        distancia = matriz[len(palavraUsuario[p])][len(dicionario[d])]
        #so pega a plavra q tem distancia de no maximo 2
        if distancia <= 2:
            saida = saida + dicionario[d] + ' '
    print(saida[:-1])
