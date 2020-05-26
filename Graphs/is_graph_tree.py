'''
A graph can only be a tree under two conditions:

There are no cycles.
The graph is connected

A graph is connected when there is a path between every pair of vertices.
In a connected graph, there are no unreachable vertices.
Each vertex must be connected to every other vertex through either a direct edge or a graph traversal.
'''

import sys
sys.path.append('../StacksQueues')
sys.path.append('../LinkedLists')
from Graph import UGraph
from Stacks import myStack
from Queues import myQueue

def check_cycle_undirected(g, start):
    visited = [False] * g.nodes

    stack = myStack()
    stack.push((start,-1))

    while not stack.isEmpty():
        node, parent = stack.pop()
        # print('popping {}'.format((node, parent)))
        visited[node] = True
        headOfLinkedList = g.edges[node].head
        while headOfLinkedList:
            el = headOfLinkedList.data
            print(el, node)
            if el != parent:
                stack.push((el, node))
                if visited[el] == True:
                    # print('already visited')

                    print('cycle detected, not a tree')
                    return False # if considering tree or not
                    return True # if detecting cycle
            headOfLinkedList = headOfLinkedList.next
        # print('stack : ', stack.stackList)

    # for checking cycle return false
    # return False

    # for checking if it is a tree
    if sum(visited) == g.nodes:
        print('all nodes reachable, it is a tree')
        return True # it is a tree
    else:
        print('disconnected nodes detected, not a tree')
        return False # disconnected

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



def is_tree(g):
    visited = [False] * g.nodes




g = UGraph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 4)
# g.add_edge(2, 4)


# print(is_tree(g))
print(check_cycle_undirected(g, 0))