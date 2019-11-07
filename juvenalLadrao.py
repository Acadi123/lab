kgs = [] 
items = [] 
ent = input().split()
n = int(ent[0])
c =int(ent[1])
itens =[]
saida = []
for i in range(int(n)):
    ent2 = input().split()
    item = int(ent2[0])
    kg = int(ent2[1])
    items.append(item)
    kgs.append(kg)
matriz = [[0 for x in range(c+1)] for x in range(n+1)]  
for i in range(n+1): 
        for j in range(c+1): 
            if i==0 or j==0: 
                matriz[i][j] = 0
            elif items[i-1] <= j:
                matriz[i][j] = max(kgs[i-1] + matriz[i-1][j-items[i-1]],  matriz[i-1][j]) 
            else: 
                matriz[i][j] = matriz[i-1][j]
print(matriz[n][c])
