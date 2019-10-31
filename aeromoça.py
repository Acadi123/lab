class Aeromoça: #classe formada com métodos para uma fila
    
    def __init__(self):
        self.pecorre=[]
        
    def isEmpty(self):
        return self.pecorre == []
    
    def enqueue(self,item):
        self.pecorre.insert(0,item)

    def unqueue(self):
        self.pecorre.pop()

    def get(self):
        return self.pecorre
    
    def qsize(self):
        return len(self.pecorre)

    def input(self):
        saida = ''
        #q = Queue()
        entrada = input().split()
        self.grafo = [[0] * int(entrada[0]) for i in range(int(entrada[0]))]
        self.adjacencia = [[0] * int(entrada[0]) for i in range(int(entrada[0]))]
        for j in range(int(entrada[1])):
            dado = input().split()
            self.grafo[int(dado[0])][int(dado[1])] = int(dado[2])
            self.grafo[int(dado[1])][int(dado[0])] = int(dado[2])
            self.adjacencia[int(dado[0])][int(dado[1])] = 1
            self.adjacencia[int(dado[1])][int(dado[0])] = 1 #forma a matriz adj colocando 1 nos vizinhosz


    def dijstkra(self):
        #calcula a distancia de cada cidade para cada cidades
        loc = 88888888
        tam = len(self.grafo)
        for c in range(tam):
            pecorrer = [loc] * tam
            vizinho = [0] * tam
            pecorrer[c] = 0
            while 0 in vizinho:
                menor = loc
                for k in range(len(vizinho)):
                    if vizinho[k] == 0 and pecorrer[k] < menor:
                        menor = pecorrer[k]
                        local = k
                vizinho[local] = True
                for n in range(len(pecorrer)): 
                    if vizinho[n] != 1:
                        if self.adjacencia[local][n] == 1:
                            resul = pecorrer[local] + self.grafo[local][n]
                            if resul < pecorrer[n]:
                                pecorrer[n] = resul
            #self.unqueue()
            maior = max(pecorrer) #depois pega a maior distancia de cada cidade
            #print(pecorrer)
            self.enqueue(maior)
            saida = self.get()
            
        return min(saida)

q = Aeromoça()
q.input()
print(q.dijstkra())
