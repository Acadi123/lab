p = int(input("quantas provincias são? "))
listac = ["azul", "branco", "preto", "vermelho"]
listapc = []
lista = []
for i in range(0,p):
    v = input("digite as provincias vizinhas da " + str(i+1)+" ")
    lista.append(v)
for i in range(0,p):
    listaSeq = lista[i].split(",")
    for n in range(len(listaSeq)):
            #1caso
            if len(listapc) == 0:
                add = str(i) + str(listac[0])
                listapc.append(add)
            #demais casos 
            else:
                print("we")
                for k in range(len(listapc)):
                    if str(listaSeq[n]) not in str(listapc[k]):
                        corQNpode = str(listapc[k][1:])
                        #pegar prox cor
                        for proxc in range(len(listac)):
                            print(listapc)
                            if corQNpode != listac[proxc]:
                                add = str(i) + str(listac[proxc])
                                listapc.append(add)
                            else:
                                break
                                
                        
print(listapc)
