import random
import numpy as np
class Matriz():

    def __init__(self,linhas,colunas):
        self.g = 0 #distancia do inicio
        self.lin = linhas
        self.col = colunas
        self.mat = np.zeros((linhas,colunas), dtype=int)
        self.posx = 0
        self.posy = 0
        self.dist = 0
        self.caminho = []
        self.passoulist = []

    def appendpassou(self, mat):
        self.passoulist.append(mat)

    def inserecaminho(self, cam):
        self.caminho.append(cam)

    def custo(self):
        self.dist =+ self.g

    def incg(self):
        self.g += 1

    def getg(self):
        return self.g

    def monta(self, num):
        cont = 0
        for x in range (self.lin, 2):
            for y in range (self.col/2):
                self.mat[x][y] = num [cont]
                cont += 1

    def getlin(self):
        return self.lin

    def getcol(self):
        return self.col

    def get(self):
        return self

    def monta(self):
        aux = 0
        for x in range (self.lin):
            for y in range (self.col):
                self.mat[x][y] = aux
                aux += 1


    def getMatriz(self):
        return self.mat

    def isEqual(self, matriz):
        for x in range(self.lin):
            for y in range(self.col):
                if self.mat[x][y] != matriz[x][y]:
                    return False
        return True



    def sobe(self):
        Aux = self.mat[self.posy][self.posx]
        self.mat[self.posy][self.posx] = self.mat[self.posy-1][self.posx]
        self.mat[self.posy - 1][self.posx ] = Aux
        self.posy = self.posy-1

    def desce(self):
        Aux = self.mat[self.posy][self.posx]
        self.mat[self.posy][self.posx] = self.mat[self.posy+1][self.posx]
        self.mat[self.posy + 1][self.posx] = Aux
        self.posy = self.posy+1


    def direita(self):
        Aux = self.mat[self.posy][self.posx]
        self.mat[self.posy][self.posx] = self.mat[self.posy][self.posx+1]
        self.mat[self.posy][self.posx + 1] = Aux
        self.posx = self.posx+1

    def esquerda(self):
        Aux = self.mat[self.posy][self.posx]
        self.mat[self.posy][self.posx] = self.mat[self.posy][self.posx-1]
        self.mat[self.posy][self.posx - 1] = Aux
        self.posx = self.posx - 1

    def mostra(self):
        print(self.mat)


    def podeSubir(self):
        return not(self.posy == 0)

    def podeDescer(self):
        return not(self.posy == self.lin-1)

    def podeEsquerda(self):
        return not(self.posx == 0)

    def podeDireita(self):
        return not(self.posx == self.col-1)

    def embaralha(self):
        random.seed()
        for x in range(self.lin+self.col):
            num = random.randint(0, 3)
            if num == 0:
                if self.podeSubir():
                    self.sobe()
            elif num == 1:
                if self.podeDireita():
                    self.direita()
            elif num == 2:
                if self.podeEsquerda():
                    self.esquerda()
            elif num == 3:
                if self.podeDescer():
                    self.desce()


    def qtdpecas(self, matriz):# distancia para final
        count = 0
        for x in range (self.lin):
            for y in range (self.col):
                if self.mat[x][y] != matriz[x][y]:
                    count += 1
        self.dist = count

    def existe(self, pas):
        for i in range(len(pas)):
            if self.isEqual(pas[i]):
                return True
        return False

    def __str__(self,x,y):
        return ""+self.mat[x][y]

    def __eq__(self, other):
        return self.dist == other.dist

    def __lt__(self, aux):
        return self.dist < aux.dist