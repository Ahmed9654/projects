class Graph:
    def __init__(self):
        self.numberofnodes = 0
        self.adjacentlist = {}

    def addVertex(self, num):
        self.adjacentlist[num] = []
        self.numberofnodes += 1

    def addEdge(self, node1, node2):
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)

    def showconnection(self):
        for x in self.adjacentlist.keys():
            print(f"{x} -> {self.adjacentlist[x]}\n")
        print(self.numberofnodes)


myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')
(myGraph.showconnection())

# 0-->1 2
# 1-->3 2 0
# 2-->4 1 0
# 3-->1 4
# 4-->3 2 5
# 5-->4 6
# 6-->5
