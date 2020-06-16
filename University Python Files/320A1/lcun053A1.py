import math
import sys
import heapq

class Node:
    def __init__(self, cost):
        self.cost = cost
        self.dist = math.inf
        self.previous = None
        self.neighbours = []
        self.isVisited = False
        self.isStart = False
        self.isEnd = False

def main():
    results = [] 
    getFieldSize(results) 

def getFieldSize(results):
    fieldSize = input()
    fieldSize = fieldSize.split()
    fieldSize = [i for i in fieldSize if i.isdigit()]
    row = int(fieldSize[0])
    column = int(fieldSize[1])
    if row != 0 and column != 0:
        cellValues = getVals(row)
        nodes = generateNodes(cellValues, row, column)
        source = nodes[len(nodes) - column]
        endPoint = nodes[column - 1]
        DijkstrasV2(source) #Faster
        results += [getMinimum(endPoint)]
        getMinimum(endPoint)
        getFieldSize(results)
    else:
        for i in results:
            print(i)
        return

def getMinimum(node):
    if node.previous == None:
        return node.cost
    else:
        return node.cost + getMinimum(node.previous)

def getVals(row):
    fieldValues = []
    for i in range(row):
        values = input()
        values = values.split()
        values = [Node(int(i)) for i in values if i.isdigit()]
        fieldValues += [values]
    return fieldValues

def generateNodes(nodeSet, row, column):
    newNodeSet = []
    for i in range(row):
        for j in range(column):
            node = nodeSet[i][j]
            if i == 0:  #FIRST ROW
                
                if j == 0:  #FIRST COLUMN                  
                    node.neighbours += [nodeSet[i][j + 1]]
                    node.neighbours += [nodeSet[i + 1][j]]
                    node.neighbours += [nodeSet[i + 1][j + 1]]
                elif j == column - 1: #LAST COLUMN
                    node.isEnd = True
                    node.neighbours += [nodeSet[i][j - 1]]
                    node.neighbours += [nodeSet[i + 1][j]]
                    node.neighbours += [nodeSet[i + 1][j - 1]]
                else: #ALL OTHER COLUMNS
                    node.neighbours += [nodeSet[i][j - 1]]
                    node.neighbours += [nodeSet[i + 1][j - 1]]
                    node.neighbours += [nodeSet[i + 1][j]]
                    node.neighbours += [nodeSet[i + 1][j + 1]]
                    node.neighbours += [nodeSet[i][j + 1]]
                    
            elif i == row - 1: #LAST ROW
                
                if j == 0: #FIRST COLUMN IN LAST ROW
                    node.isStart = True
                    node.neighbours += [nodeSet[i - 1][j]]
                    node.neighbours += [nodeSet[i - 1][j + 1]]
                    node.neighbours += [nodeSet[i][j + 1]]
                elif j == column - 1: #LAST COLUMN IN LAST ROW
                    node.neighbours += [nodeSet[i][j - 1]]
                    node.neighbours += [nodeSet[i - 1][j - 1]]
                    node.neighbours += [nodeSet[i - 1][j]]
                else: #ALL OTHER COLUMNS IN LAST ROW
                    node.neighbours += [nodeSet[i][j - 1]]
                    node.neighbours += [nodeSet[i - 1][j - 1]]
                    node.neighbours += [nodeSet[i - 1][j]]
                    node.neighbours += [nodeSet[i - 1][j + 1]]
                    node.neighbours += [nodeSet[i][j + 1]]
                    
            else: #ALL OTHER ROWS INBETWEEN FIRST AND LAST ROW
                
                if j == 0: #FIRST COLUMN IN ALL OTHER ROWS INBETWEEN FIRST AND LAST ROW
                    node.neighbours += [nodeSet[i - 1][j]]
                    node.neighbours += [nodeSet[i - 1][j + 1]]
                    node.neighbours += [nodeSet[i][j + 1]]
                    node.neighbours += [nodeSet[i + 1][j + 1]]
                    node.neighbours += [nodeSet[i + 1][j]]
                elif j == column - 1: #LAST COLUMN ALL OTHER ROWS INBETWEEN FIRST AND LAST ROW
                    node.neighbours += [nodeSet[i - 1][j]]
                    node.neighbours += [nodeSet[i - 1][j - 1]]
                    node.neighbours += [nodeSet[i][j - 1]]
                    node.neighbours += [nodeSet[i + 1][j - 1]]
                    node.neighbours += [nodeSet[i + 1][j]]
                else: #ALL OTHER COLUMNS ALL OTHER ROWS INBETWEEN FIRST AND LAST ROW
                    node.neighbours += [nodeSet[i - 1][j]]
                    node.neighbours += [nodeSet[i - 1][j - 1]]
                    node.neighbours += [nodeSet[i][j - 1]]
                    node.neighbours += [nodeSet[i + 1][j - 1]]
                    node.neighbours += [nodeSet[i + 1][j]]
                    node.neighbours += [nodeSet[i + 1][j + 1]]
                    node.neighbours += [nodeSet[i][j + 1]]
                    node.neighbours += [nodeSet[i - 1][j + 1]]
                    
            newNodeSet += [node] #ADDS NODE TO AN ARRAY OF NODES

    return newNodeSet          

def DijkstrasV2(source):
    source.dist = 0
    Q = [source]
    while len(Q) is not 0:
        u = getMin(Q)
        Q.remove(u)
        for v in u.neighbours:
            if v not in Q and v.isVisited == False:
                Q.append(v)
                v.isVisited = True
            relax(u, v)

def relax(u, v):
    path = u.dist + v.cost
    if path < v.dist:
        v.dist = path
        v.previous = u                            
    
def getMin(nodes):
    minimum = nodes[0]
    minimumDist = nodes[0].dist
    for i in nodes:
        if i.dist < minimumDist:
            minimum = i
    return minimum
        
main()