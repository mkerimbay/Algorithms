import sys
sys.path.append('../StacksQueues')
sys.path.append('../LinkedLists')
from Graph import Graph
# from Queues import myQueue
from Stacks import myStack
# from LinkedList import LinkedList
# from Node import Node

def dfs(g):
    '''
    Depth First Search traversal
    '''
    n = g.nodes
    visited = [False]*n
    print(visited)
    stack = myStack()
    res = ''
    if n == 0:
        return res
    stack.push(0)

    while not stack.isEmpty():
        tmp = stack.pop()
        print('----------------')
        print('performance on node {}'.format(tmp))
        visited[tmp] = True
        print('visited: ', visited)
        print('stack ', stack.stackList)
        head = g.edges[tmp].head
        res += '{} ->'.format(tmp)
        while head:
            print('node {} has child {}'.format(tmp, head.data))
            if visited[head.data] != True:
                print('pushing {}'.format(head.data))
                stack.push(head.data)
                visited[head.data] = True
                print('stack becomes ', stack.stackList)
            head = head.next
    print(res)
    return res




# g = Graph(4)
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(2,3)
# g.print_graph()
# dfs(g)

g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(3, 0)
g1.print_graph()
dfs(g1)
