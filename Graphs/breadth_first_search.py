import sys
sys.path.append('../StacksQueues')
sys.path.append('../LinkedLists')
from Graph import Graph
from Queues import myQueue
from LinkedList import LinkedList
# from Node import Node

def bfs(g):
    '''
    Breadth First Search traversal
    '''
    n = g.nodes
    visited = [False]*n
    print(visited)
    queue = myQueue()
    res = ''
    if n == 0:
        return res
    queue.enqueue(0)

    while not queue.isEmpty():
        tmp = queue.dequeue()
        print('----------------')
        print('performance on node {}'.format(tmp))
        visited[tmp] = True
        print('visited: ', visited)
        print('queue ', queue.queueList)
        head = g.edges[tmp].head
        res += '{} ->'.format(tmp)
        while head:
            print('node {} has child {}'.format(tmp, head.data))
            if visited[head.data] != True:
                print('enqueing {}'.format(head.data))
                queue.enqueue(head.data)
                visited[head.data] = True
                print('queue becomes ', queue.queueList)
            head = head.next
    print(res)
    return res




g = Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.print_graph()
bfs(g)
