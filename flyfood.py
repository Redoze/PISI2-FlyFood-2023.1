import os
from itertools import permutations

class Processar_Arquivo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.tamanho = []
        self.matriz = {}

    def ler_matriz(self):
        caminho = os.path.join(os.path.dirname(__file__), self.nome_arquivo)
        arquivo = open(caminho, 'r')

        primeira_linha_do_arquivo = arquivo.readline()
        self.tamanho = list(map(int, primeira_linha_do_arquivo.split()))

        for linha_matriz in range(self.tamanho[0]):
            linha = arquivo.readline().split()

            for coluna_matriz in range(self.tamanho[1]):
                ponto = linha[coluna_matriz]

                if ponto != '0':
                    self.matriz[ponto] = [linha_matriz, coluna_matriz]

        arquivo.close()

class Processar_Caminhos(Processar_Arquivo):
    def __init__(self, nome_do_arquivo):
        super().__init__(nome_do_arquivo)

    def calcular_distancia(self, ponto1, ponto2):
        return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

    def encontrar_menor_circuito(self):
        coordenada_origem = self.matriz.pop('R')
        coord_pontos_entrega = list(self.matriz.keys())

        menor_distancia = float('inf')
        menor_circuito = 0

        for permutacao in permutations(coord_pontos_entrega):
            distancia_total = self.calcular_distancia(coordenada_origem, self.matriz[permutacao[0]])

            for i in range(len(permutacao) - 1):
                distancia_total += self.calcular_distancia(self.matriz[permutacao[i]], self.matriz[permutacao[i + 1]])

            distancia_total += self.calcular_distancia(self.matriz[permutacao[-1]], coordenada_origem)

            if distancia_total < menor_distancia:
                menor_distancia = distancia_total
                menor_circuito = permutacao

        return menor_circuito

def main():
    nome_do_arquivo = 'matriz.txt'
    
    caminho_do_drone = Processar_Caminhos(nome_do_arquivo)
    caminho_do_drone.ler_matriz()
    menor_circuito = caminho_do_drone.encontrar_menor_circuito()

    print(" ".join(menor_circuito))

if __name__ == "__main__":
    main()
