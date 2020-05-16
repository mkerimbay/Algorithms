'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)



    def countUnivalSubtree(self, root):
        self.count = 0

        def helper(node):
            # return True if all nodes have same value
            if node is None:
                return

            left = helper(node.left)
            right = helper(node.right)

            if (not left or left == node.value) and (not right or right == node.value):
                self.count += 1
                return node.value
            return "#"
        helper(root)
        return self.count


tree = BinaryTree(5)
tree.root.left = Node(1)
tree.root.left.left = Node(5)
tree.root.left.right = Node(5)

tree.root.right = Node(5)

tree.root.right.right = Node(5)


print(tree.countUnivalSubtree(tree.root))

