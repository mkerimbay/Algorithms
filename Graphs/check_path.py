'''
It takes a source vertex and a destination vertex and tells us
whether or not a path exists between the two
'''
from Graph import Graph
import sys
sys.path.append('../StacksQueues')
from Stacks import myStack

def check_path(g, start, end):
    '''
    Depth First Search traversal
    '''
    n = g.nodes
    visited = [False] * n
    stack = myStack()
    stack.push(start)

    while not stack.isEmpty():
        tmp = stack.pop()
        visited[tmp] = True
        head = g.edges[tmp].head
        while head:
            if visited[head.data] != True:
                stack.push(head.data)
                visited[head.data] = True
                if head.data == end:
                    return True
            head = head.next
    return False



g1 = Graph(9)
g1.add_edge(0, 2)
g1.add_edge(0, 5)
g1.add_edge(2, 3)
g1.add_edge(2, 4)
g1.add_edge(5, 3)
g1.add_edge(5, 6)
g1.add_edge(3, 6)
g1.add_edge(6, 7)
g1.add_edge(6, 8)
g1.add_edge(6, 4)
g1.add_edge(7, 8)
g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(2, 3)

print(check_path(g1, 0, 7))
print(check_path(g2, 3, 0))