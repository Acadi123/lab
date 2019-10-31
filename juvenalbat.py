navio = []
mar = []
navioafundado = 0
cont = 0
def tabuleiro (local, posicao):
    global cont
    global navio, mar
    for j in range(local):
        linha = input()
        for i in range(len(linha)):
            navioparte =[]
            marlocal =[]
            if linha[i] == "#": #pega as posiçoes que são navio
                #print((x,i))
                navioparte.append(j)
                navioparte.append(i)
                navio.append(navioparte)
            if linha[i] == ".": #pega as posiçoe q sao agua 
                marlocal.append(j)
                marlocal.append(i)
                mar.append(marlocal)
                cont +=1
    return navio
def localizar(posicao, local, navioposicao, naviolocal):
    localizacao = [posicao, local]
    if localizacao in naviolocal:
        navioposicao.append(localizacao)
        naviolocal.remove(localizacao)
        mapa = localizar(posicao - 1, local, navioposicao, naviolocal)
        navioposicao.append(localizacao)
        mapa.remove(localizacao)
        mapa = localizar(posicao + 1, local, navioposicao, naviolocal)
        navioposicao.append(localizacao)
        mapa.remove(localizacao)
        mapa = localizar(posicao, local - 1, navioposicao, naviolocal)
        navioposicao.append(localizacao)
        mapa.remove(localizacao)
        mapa = localizar(posicao, local + 1, navioposicao, naviolocal)
        navioposicao.append(localizacao)
        mapa.remove(localizacao)
    return navioposicao
def chamandoMetodo(navio):
    navios = []
    global navioafundado
    #print(navio)
    while len(navio) != 0:
        posicao = navio[0]
        listaNavio = []
        if cont==0:
            navioafundado = 1
            break
        else:
            navios.append(localizar(posicao[0], posicao[1], listaNavio, navio))
    return navios
def Entrada2(qtd):
    tiros = []
    for i in range(qtd):
        tirosfora = input().split()
        d = [int(tirosfora[0])-1,int(tirosfora[1])-1]
        tiros.append(d)
    return tiros
def afundados (navios, tirosacertados):
    global navioafundado
    acertados = []
    for navio in navios:
        naviolivre = []
        for parte in navio:
            for tiro in tirosacertados:
                if parte == tiro:
                    naviolivre.append(parte)
        acertados.append(naviolivre)
    numeronavio = len(navios)
    for navio in range(0,numeronavio):
        if len(navios[navio]) == len(acertados[navio]):
            navioafundado += 1
    print(navioafundado)
digite = input().split(" ")#entrada
local, posicao = int(digite[0]), int(digite[1])
navio = tabuleiro(local,posicao)
navios = chamandoMetodo(navio)
qtd = int(input())
tirosacertados = Entrada2(qtd)
afundados(navios,tirosacertados)
