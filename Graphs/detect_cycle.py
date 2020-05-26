import sys
sys.path.append('../StacksQueues')
sys.path.append('../LinkedLists')
from Graph import Graph
from Stacks import myStack

def detect_cycle(g):
    '''
    detect cycle via Depth First Search traversal
    '''
    n = g.nodes
    visited = [False]*n
    print(visited)
    stack = myStack()
    res = ''
    if n == 0:
        return False
    stack.push(0)

    while not stack.isEmpty():
        tmp = stack.pop()
        visited[tmp] = True
        print('----------------')
        print('performance on node {}'.format(tmp))
        print('visited: ', visited)
        print('stack ', stack.stackList)
        head = g.edges[tmp].head
        res += '{} ->'.format(tmp)
        while head:
            print('node {} has child {}'.format(tmp, head.data))
            if visited[head.data] == True:
                print('already visited {}, cycle detected!'.format(head.data))
                return True


            stack.push(head.data)
            print('stack becomes ', stack.stackList)
            visited[head.data] = True
            head = head.next
    print(res)
    return False

def check_cycle_undirected(g, start):
    visited = [False] * g.nodes

    stack = myStack()
    stack.push((start, -1)) # keep track of parent

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
                    # print('')
                    print('already visited, cycle detected')
                    return True
            headOfLinkedList = headOfLinkedList.next
        # print('stack : ', stack.stackList)
    return False




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
detect_cycle(g1)
