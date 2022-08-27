import numpy as np
from QueueUsingLinkedList import QueuesLinked
class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices,vertices))
        self._visited = [0] * vertices

    def insert_edge(self, u, v, x=1):
        self._adjMat[u][v] = x

    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count += 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i,end=' ')  
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i, '--', j)    


    def outdegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[v][i] != 0:
                count += 1
        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][v] != 0:
                count = count + 1
        return count

    def display_adjMat(self):
        print(self._adjMat)    

    ###########BFS###############

    def BFS(self,s):
        i = s
        q = QueuesLinked()
        visited = [0] * self._vertices
        print(i, end=' ')
        visited[i] = 1
        q.enqueue(i)
        while not q.isempty():
            i = q.dequeue()
            for j in range(self._vertices):
                if self._adjMat[i][j] == 1 and visited[j] == 0:
                    print(j, end= ' ')
                    visited[j] = 1
                    q.enqueue(j)



    #################DFS###################

    def DFS(self,s):
        if self._visited[s] == 0:
            print(s, end= ' ')
            self._visited[s] = 1
            for j in range(self._vertices):
                if self._adjMat[s][j] == 1 and self._visited[j] == 0:
                    self.DFS(j)





G = Graph(4)
G.display_adjMat()
print('vertices:', G.vertex_count())
print('Edges:',G.edge_count())

G.insert_edge(0,1)
G.insert_edge(0,2)
G.insert_edge(1,0)
G.insert_edge(1,2)
G.insert_edge(2,0)
G.insert_edge(2,1)
G.insert_edge(2,3)
G.insert_edge(3,2)

G.display_adjMat()
print('vertices:', G.vertex_count())
print('Edges:',G.edge_count())
G.edges()
print('Edge between 1-3:',G.exist_edge(1,3))
print('Edge between 1-2:',G.exist_edge(1,2))
print('Degree:', G.indegree(2))
G.remove_edge(1,2)
print('Edge between 1-2:',G.exist_edge(1,2))

print('------- Weighted undirected Graph------')
G.display_adjMat()
G.insert_edge(0,1,26)
G.insert_edge(0,2,16)
G.insert_edge(1,0,26)
G.insert_edge(1,2,12)
G.insert_edge(2,0,16)
G.insert_edge(2,1,12)
G.insert_edge(2,3,8)
G.insert_edge(3,2,8)
G.display_adjMat()
print('vertices:', G.vertex_count())
print('Edges:',G.edge_count())
G.edges()
print('Edge between 1-3:',G.exist_edge(1,3))
print('Edge between 1-2:',G.exist_edge(1,2))
print('Degree:', G.indegree(2))
G.remove_edge(1,2)
print('Edge between 1-2:',G.exist_edge(1,2))


print("-------Unweighted Directed Graph---------")
G1 = Graph(4)
G1.display_adjMat()
print('vertices:', G1.vertex_count())
G1.insert_edge(0,1)
G1.insert_edge(0,2)
G1.insert_edge(1,2)
G1.insert_edge(2,3)
G1.display_adjMat()
print('Edges:',G1.edge_count())
G1.edges()
print('Edge between 1-3:',G1.exist_edge(1,3))
print('Edge between 1-2:',G1.exist_edge(1,2))

print('Degree:', G1.indegree(2))
print('Degree:', G1.outdegree(2))
G1.remove_edge(1,2)
print('Edge between 1-2:',G1.exist_edge(1,2))

print("----Weighted Directed Graph-------")
G2 = Graph(4)
G2.display_adjMat()
print('vertices:', G2.vertex_count())
G2.insert_edge(0,1,26)
G2.insert_edge(0,2,16)
G2.insert_edge(1,2,12)
G2.insert_edge(2,3,8)
G2.display_adjMat()

print('Edges:',G2.edge_count())
G2.edges()
print('Edge between 1-3:',G2.exist_edge(1,3))
print('Edge between 1-2:',G2.exist_edge(1,2))
print('Degree:', G2.indegree(2))
print('Degree:', G2.outdegree(2))
G.remove_edge(1,2)
print('Edge between 1-2:',G.exist_edge(1,2))

print('-------------BFS--------------')

GB = Graph(7)
GB.insert_edge(0,1)
GB.insert_edge(0,5)
GB.insert_edge(0,6)
GB.insert_edge(1,0)
GB.insert_edge(1,2)
GB.insert_edge(1,5)
GB.insert_edge(1,6)
GB.insert_edge(2,3)
GB.insert_edge(2,4)
GB.insert_edge(2,6)
GB.insert_edge(3,4)
GB.insert_edge(4,2)
GB.insert_edge(4,5)
GB.insert_edge(5,2)
GB.insert_edge(5,3)
GB.insert_edge(6,3)
GB.display_adjMat()
GB.BFS(0)

print("-----------DFS-------")

GD = Graph(7)
GD.insert_edge(0,1)
GD.insert_edge(0,5)
GD.insert_edge(0,6)
GD.insert_edge(1,0)
GD.insert_edge(1,2)
GD.insert_edge(1,5)
GD.insert_edge(1,6)
GB.insert_edge(2,3)
GD.insert_edge(2,4)
GD.insert_edge(2,6)
GD.insert_edge(3,4)
GD.insert_edge(4,2)
GD.insert_edge(4,5)
GD.insert_edge(5,2)
GD.insert_edge(5,3)
GD.insert_edge(6,3)
GD.display_adjMat()
GD.DFS(1)