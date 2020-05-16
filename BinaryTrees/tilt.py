class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def tilt(self, root):
        '''
        Given a binary tree, return the tilt of the whole tree.

        The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values
        and the sum of all right subtree node values. Null node has tilt 0.

        The tilt of the whole tree is defined as the sum of all nodes' tilt.
        :return: abs(root.left - root.right)


                                    Input:
                                     1
                                   /   \
                                  2     3
                            Output: 1
                            Explanation:
                            Tilt of node 2 : 0
                            Tilt of node 3 : 0
                            Tilt of node 1 : |2-3| = 1
                            Tilt of binary tree : 0 + 0 + 1 = 1
                                    '''
        self.ans = 0
        def getsum(node):
            if node is None:
                return 0
            left = getsum(node.left)
            right = getsum(node.right)
            self.ans += abs(left - right)
            return node.value + left + right
        getsum(root)
        return self.ans




# [3,9,20,null,null,15,7]
#
#               3
#         /           \
#        9            20
#     /    \         /   \
#    8     11      15     7
#   /                \
#  2                  1


tree = BinaryTree(3)
tree.root.left = Node(9)
tree.root.left.left = Node(8)
tree.root.left.left.left = Node(2)

tree.root.left.right = Node(11)

tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)
tree.root.right.left.right = Node(1)


print(tree.tilt(tree.root))

