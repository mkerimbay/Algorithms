class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    # Traversals (preOrder, inOrder, postOrder, levelOrder, reverseLevelOrder)
    def preOrder_print(self, start, res):
        # (root -> left -> right)
        if start:
            res += str(start.value) + '-'
            res = self.preOrder_print(start.left, res)
            res = self.preOrder_print(start.right, res)
        return res

    def inOrder_print(self, start, res):
        # (left -> root -> right)
        if start:
            res = self.inOrder_print(start.left, res)
            res += str(start.value) + '-'
            res = self.inOrder_print(start.right, res)
        return res

    def postOrder_print(self, start, res):
        # (Left -> Right -> Root)
        if start:
            res = self.postOrder_print(start.left, res)
            res = self.postOrder_print(start.right, res)
            res += str(start.value) + '-'
        return res

    def levelOrder_print(self, start):
        # from roots to leaves, level by level
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)

        res = ''
        while len(queue) > 0:
            res += str(queue.peek()) + '-'
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return res

    def reverse_levelOrder_print(self, start):
        # from leaves to root, level by level
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        res = ""
        while len(queue) > 0:
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            res += str(node.value) + "-"

        return res

    def height(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.right) + self.size(node.left)

    def isUnival(self, root):
        # return True if all nodes have same value
        if root is None:
            return True
        if root.left and root.left.value != root.value:
            return False
        if root.right and root.right.value != root.value:
            return False
        return self.isUnival(root.right) and self.isUnival(root.left)

    def find_ancestors(self, lst, node, n):
        if node is None:
            return False

        val = node.value
        if val == n:
            return True

        if self.find_ancestors(lst, node.left, n):
            lst.append(val)
            return True
        if self.find_ancestors(lst, node.right, n):
            lst.append(val)
            return True
        return False

    def diameter(self, root):
        # 1) the longest path passes through the root
        # 2) the longest path is on left subtree
        # 3) the longest path is on right subtree
        # ans-take maximum of l/r diameters, and max with root diameter

        if root is None:
            return 0

        root_diameter = self.height(root.left) + self.height(root.right)
        left_diameter = self.diameter(root.left)
        right_diameter = self.diameter(root.right)

        return max(root_diameter, max(left_diameter, right_diameter))

    def longest_path_from_root(self, root):
        def argmax(lst1, lst2):
            return lst1 if len(lst1) > len(lst2) else lst2

        if root is None:
            return []
        rightpath = [root.value] + self.longest_path_from_root(root.right)
        leftpath = [root.value] + self.longest_path_from_root(root.left)
        return argmax(rightpath, leftpath)

    def longest_path(self, root):

        if root is None:
            return []
        rightpath = self.longest_path_from_root(root.right)
        leftpath = self.longest_path_from_root(root.left)
        return leftpath[::-1] + [root.value] + rightpath

    def diameter_path(self, root):
        # 1) the longest path passes through the root
        # 2) the longest path is on left subtree
        # 3) the longest path is on right subtree
        # ans-take maximum of l/r diameters, and max with root diameter

        if root is None:
            return 0

        root_diameter = self.height(root.left) + self.height(root.right)
        left_diameter = self.diameter(root.left)
        right_diameter = self.diameter(root.right)

        if (root_diameter > left_diameter) and (root_diameter > right_diameter): # 1-case
            return self.longest_path(root)
        else:
            if left_diameter > right_diameter: # 2-case
                return self.longest_path(root.left)
            else:# 3-case
                return self.longest_path(root.right)


class Solution:
    def maxDepth(self, root):
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



# [3,9,20,null,null,15,7]
#
#               3
#         /           \
#        9            20
#     /    \         /   \
#    8     11      15     7
#   /                \
#  2                  1

def main():

    tree = BinaryTree(3)
    tree.root.left = Node(9)
    tree.root.left.left = Node(8)
    tree.root.left.left.left = Node(2)
    tree.root.left.left.left.left = Node(2.1)
    tree.root.left.left.left.left.left = Node(2.2)
    tree.root.left.left.left.left.left.left = Node(2.3)
    tree.root.left.left.left.left.left.left.left = Node(2.4)


    tree.root.left.right = Node(11)
    tree.root.left.right.left = Node(12)
    tree.root.left.right.left.left = Node(13)
    tree.root.left.right.left.left.left = Node(14)
    tree.root.left.right.left.left.left.left = Node(25)


    tree.root.right = Node(20)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(7)
    tree.root.right.left.right = Node(1)

    print(tree.preOrder_print(tree.root, ''))
    print(tree.inOrder_print(tree.root, ''))
    print(tree.postOrder_print(tree.root, ''))
    print(tree.levelOrder_print(tree.root))
    print(tree.reverse_levelOrder_print(tree.root))
    print('height of tree: {}'.format(tree.height(tree.root)))
    print('size of tree: {}'.format(tree.size(tree.root)))
    print('is tree Unival: {}'.format(tree.isUnival(tree.root)))

    anc = []
    tree.find_ancestors(anc, tree.root, 15)
    print(anc)

    print(tree.diameter(tree.root))
    print('longest path from root')
    print(tree.longest_path_from_root(tree.root))
    print('diameter path')
    print(tree.diameter_path(tree.root))


if __name__ == '__main__':
    main()