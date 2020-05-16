'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2


Example 2:
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def solution(self, root):
        self.res = 0
        def helper(node):
            if not node:
                return 0
            left_len = helper(node.left)
            right_len = helper(node.right)
            left = 1+left_len if node.left and node.left.value == node.value else 0
            right = 1+right_len if node.right and node.right.value == node.value else 0
            self.res = max(self.res, left+right)
            return max(left, right)
        helper(root)
        return self.res



# [3,9,20,null,null,15,7]
#
#               5
#         /        \
#        4           5
#     /    \           \
#    1     1             5



tree = BinaryTree(5)
tree.root.left = Node(4)
tree.root.left.left = Node(1)
tree.root.left.right = Node(1)

tree.root.right = Node(5)
tree.root.right.right = Node(5)

# Solution
print(tree.solution(tree.root))