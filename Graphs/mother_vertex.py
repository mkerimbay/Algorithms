import sys
sys.path.append('../StacksQueues')
sys.path.append('../LinkedLists')
from Graph import Graph
from Queues import myQueue
# from LinkedList import LinkedList
# from Node import Node

def bfs(g, start_node):
    '''
    Breadth First Search traversal starting from given node
    '''
    n = g.nodes
    visited = [False]*n
    queue = myQueue()
    queue.enqueue(start_node)

    while not queue.isEmpty():
        tmp = queue.dequeue()
        visited[tmp] = True
        head = g.edges[tmp].head
        while head:
            if visited[head.data] != True:
                queue.enqueue(head.data)
                visited[head.data] = True
            head = head.next
    if sum(visited) == n:
        return True
    return False

def mother_vertices(g):
    mothers = []
    for node in range(g.nodes):
        if bfs(g, node):
            mothers.append(node)
    return mothers




# g = Graph(4)
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(2,3)
# g.print_graph()
# print('mother vertices: ', mother_vertices(g))

# g1 = Graph(3)
# g1.add_edge(0,1)
# g1.add_edge(1,2)
# g1.add_edge(2,0)
# print('mother vertices: ', mother_vertices(g1))

g2 = Graph(4)
g2.add_edge(3,1)
g2.add_edge(3,0)
g2.add_edge(1,2)
print('mother vertices: ', mother_vertices(g2))