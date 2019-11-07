import sys
#biblioteca usado para aumentar recursividade do idle 
sys.setrecursionlimit(3000)
 
def resto(linhas, colunas, u,d,w): #verificando cada elemento da matriz
    global num_loc
    global num2_loc
    #print(w)
    if w[u][d] == ".":
        w[u][d] = "x"
    elif w[u][d] == "#":
        return
    elif w[u][d] == "x":
        return
    elif w[u][d] == "k":
        num_loc +=1
        w[u][d] = "x"
    elif w[u][d] == "v":
        num2_loc +=1
        w[u][d] = "x"
    if u-1 >= 0:
        resto(linhas, colunas,u-1,d,w)
    if d+1 < colunas:
        resto(linhas,colunas,u,d+1,w)
    if u+1 < linhas:
        resto(linhas,colunas,u+1,d,w)
    if d-1 >= 0:
        resto(linhas,colunas,u,d-1,w)
        
entrada = input().split()
linhas = int(entrada[0])
colunas = int(entrada[1])
v = []
local2 = 0
local1 = 0
for k in range(linhas): #manipula entrada e forma matriz c os elementos da entrada
    entrada2 = input()
    num1 = []
    for c in range(colunas):
        if entrada2[c] == "k":
            local2 +=1
        if entrada2[c] == "v":
            local1 +=1
        num1.append(entrada2[c])
    v.append(num1)#contem matriz onde cada posicao é um . ou #
#print(len(v[0]))
#print(v[1])

for i in range(linhas):#for q passa cada elemento da matriz para a funçao
    for j in range(colunas):
        num_loc = 0
        num2_loc = 0
        resto(linhas, colunas,i,j,v)
        if num2_loc >= num_loc:
            local2 -= num_loc
        else:
            local1 -= num2_loc
print(local2,local1)
