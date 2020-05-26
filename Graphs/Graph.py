import sys
sys.path.append('../LinkedLists')
from LinkedList import LinkedList

class Graph: # Directed Graph
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []
        for i in range(nodes):
            self.edges.append(LinkedList())

    def add_edge(self, source, destination):
        if source < self.nodes and destination < self.nodes:
            self.edges[source].insert_at_head(destination)
            # if graph is undirectional
            # self.edges[destination].insert_at_head(source)

    def print_graph(self):
        print('Adjacency list of directed graph')
        print()
        for i in range(self.nodes):
            print('node (', i, end='): =>')
            tmp = self.edges[i].getHead()
            while tmp:
                print('[', tmp.data, end='] ->')
                tmp = tmp.next
            print('None')


class UGraph: # Undirected Graph
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []
        for i in range(nodes):
            self.edges.append(LinkedList())

    def add_edge(self, source, destination):
        if source < self.nodes and destination < self.nodes:
            self.edges[source].insert_at_head(destination)
            self.edges[destination].insert_at_head(source)

    def print_graph(self):
        print('Adjacency list of un-directed graph')
        print()
        for i in range(self.nodes):
            print('node (', i, end='): =>')
            tmp = self.edges[i].getHead()
            while tmp:
                print('[', tmp.data, end='] ->')
                tmp = tmp.next
            print('None')


def main():
    g = Graph(4)
    g.add_edge(0,1)
    g.add_edge(0, 2)
    g.add_edge(1,3)
    g.add_edge(2, 3)
    g.print_graph()
    '''
    node: ( 0) =>[ 2] ->[ 1] ->None
    node: ( 1) =>[ 3] ->None
    node: ( 2) =>[ 3] ->None
    node: ( 3) =>None
    '''


if __name__ == '__main__':
    main()