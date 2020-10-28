from typing import List

IntMatrix = List[List[int]]

def mark(i, v):
    return i if v > 0 else -1


def passValue(value: List[int], index: int, rowIndex: int, columnIndex: int):
    if index == rowIndex:
        return value + [1]
    elif index == columnIndex:
        return value + [1]
    else:
        return value + [0]


def toIncMatrix(adjMatrix: IntMatrix) -> IntMatrix:
    incMatrix: IntMatrix = [[]]*len(adjMatrix)

    for rowIndex, row in enumerate(adjMatrix):
        for columnIndex, column in enumerate(row):
            if(column == 1 and columnIndex > rowIndex):
                incMatrix = [passValue(x, i, rowIndex, columnIndex)
                             for i, x in enumerate(incMatrix)]

    return incMatrix


def BFS(adjMatrix: IntMatrix, R: int):
    if R >= len(adjMatrix):
        raise ValueError('R must represent one point')

    V: List[int] = []
    F: List[int] = []
    X: int = 0
    incMatrix: IntMatrix = [[]]*len(adjMatrix)

    # 1. escolha a raiz (R)
    # 2. coloque R em F e em V
    # 3. Até que não haja mais vértices em F:
    # 	a) X <- desenfileire
    # 	b) acrescente em V e em F todos os vizinhos de X ausentes em V
    # 	 e em A todas as arestas de ligação desses vizinhos

    F.append(R)
    V.append(R)
    while(F):
        X = F.pop(0)

        # Marca os que não são vizinhos e deleta
        neighbors: List[int] = [mark(i, v)
                                for i, v in enumerate(adjMatrix[X])]
        neighbors = list(filter(lambda neigh: neigh >= 0, neighbors))
        # Vizinhos de X ausentes em V
        neighbors = list(filter(lambda neigh: neigh not in V, neighbors))
        # Adicionar a V e F e construindo uma matriz de incidência
        for neighbor in neighbors:
            V.append(neighbor)
            F.append(neighbor)
            incMatrix = [passValue(x, i, X, neighbor)
                         for i, x in enumerate(incMatrix)]
    return incMatrix, V


def DFS(adjMatrix: IntMatrix, R: int):
    if R >= len(adjMatrix):
        raise ValueError('R must represent one point')

    V: List[int] = []
    P: List[int] = []
    X: int = 0
    incMatrix: IntMatrix = [[]]*len(adjMatrix)

    # 1. escolha a raiz (R)
    # 2. coloque R em P e em V
    # 3. X desempilhe OR DIE
    #   a. Enquanto X tem vizinho ausente em  V
    #       i. acrescente vizinho em V, P e na lista de Arestas
    #       ii. X <- vizinho

    P.append(R)
    V.append(R)
    while(P):
        X = P.pop()

        # Não tem do-while em python: while com if:break
        while(True):
            # Marca os que não são vizinhos e deleta
            neighbors: List[int] = [mark(i, v)
                                    for i, v in enumerate(adjMatrix[X])]
            neighbors = list(filter(lambda neigh: neigh >= 0, neighbors))
            # Vizinhos de X ausentes em V
            neighbors = list(filter(lambda neigh: neigh not in V, neighbors))

            if(not neighbors):
                break

            Y = neighbors[0]

            V.append(Y)
            P.append(Y)
            incMatrix = [passValue(x, i, X, Y)
                         for i, x in enumerate(incMatrix)]
            X = Y

    return incMatrix, V