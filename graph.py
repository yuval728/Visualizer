import random
import climenu

class Graph:
    def __init__(self):
        self.graphMatrix = []
        self.graphSize = 0
        self.graphEdges = 0
        self.graphNodes = []
        
    def addNode(self):
        self.graphNodes.append(self.graphSize)
        self.graphSize += 1
        self.graphMatrix.append([0] * self.graphSize)
        for i in range(self.graphSize - 1):
            self.graphMatrix[i].append(0)
            
    def addEdge(self, node1, node2, weight=1):
        self.graphEdges += 1
        node1 = int(node1)
        node2 = int(node2)
        self.graphMatrix[node1][node2] = weight
        self.graphMatrix[node2][node1] = weight
        
    def removeEdge(self, node1, node2):
        self.graphEdges -= 1
        node1 = int(node1)
        node2 = int(node2)
        self.graphMatrix[node1][node2] = 0
        self.graphMatrix[node2][node1] = 0
        
    def removeNode(self, node):
        node = int(node)
        self.graphSize -= 1
        self.graphNodes.remove(node)
        self.graphMatrix.pop(node)
        for i in range(self.graphSize):
            self.graphMatrix[i].pop(node)
            
    def printGraph(self):
        for i in range(self.graphSize):
            print(self.graphNodes[i], end=": ")
            for j in range(self.graphSize):
                if self.graphMatrix[i][j]:
                    print(self.graphNodes[j], end=" ")
            print()
            
        for i in range(self.graphSize):
            print(i,": ",self.graphMatrix[i])
        
    def BFS(self):
        visited = [False] * self.graphSize
        queue = []
        queue.append(0)
        visited[0] = True
        while queue:
            node = queue.pop(0)
            print(self.graphNodes[node])
            for i in range(self.graphSize):
                if self.graphMatrix[node][i] and not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    
    def DFS(self):
        visited = [False] * self.graphSize
        stack=[]
        stack.append(0)
        visited[0] = True
        while stack:
            node=stack.pop()
            print(self.graphNodes[node])
            for i in range(self.graphSize):
                if self.graphMatrix[node][i] and not visited[i]:
                    stack.append(i)
                    visited[i] = True
                    

if __name__=='__main__':
    graph = Graph()
    functionChoices = [
        ("Add Node", graph.addNode, []),
        ("Add Edge", graph.addEdge, ["Enter node1: ", "Enter node2: ", "Enter weight:"]),
        ("Remove Edge", graph.removeEdge, ["Enter node1: ", "Enter node2: "]),
        ("Remove Node", graph.removeNode, ["Enter node to remove: "]),
        ("BFS", graph.BFS, []),
        ("DFS", graph.DFS, []),
        ("Print", graph.printGraph, [])
    ]
    
    climenu.menu(functionChoices, "Graph", "Enter choice: ")
        
            