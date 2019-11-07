ent = input().split()
Linhas = int(ent[0])
Colunas = int(ent[1])
MLinhas = int(ent[2])
NColunas = int(ent[3])
matriz = []
somaAreas = [] 
maior = 0
for L in range(Linhas): #manipula entrada e forma matriz c os elementos da entrada
    entrada2 = input().split()
    aux = []
    for C in range(Colunas):
        aux.append(int(entrada2[C]))
    matriz.append(aux)

for i in range(Linhas-MLinhas+1):
    for j in range(Colunas-NColunas+1):
        areas = []
        for u in range(i, i+MLinhas):
            try:
                area = matriz[u][j:j+NColunas]
                if len(area) == NColunas:
                    areas.append(sum(area))
            except:
                somaAreas.append(sum(areas))
        #print(areas) mostra as areas de acordo c o M e N
        somaAreas.append(sum(areas))

print(max(somaAreas))
