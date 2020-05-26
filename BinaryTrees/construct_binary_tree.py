from binary_trees import BinaryTree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




def construct_binary_tree(arr):
    t = Node(arr[0])


    # print(root.value)

    for i in range(1, len(arr)):

        root = t
        while root:
            if arr[i] < root.value:
                print('{} < {}'.format(arr[i], root.value))
                if root.left is None:
                    root.left = Node(arr[i])
                    print('assigning to left')
                    break
                else:
                    root = root.left
            else:
                print('{} > {}'.format(arr[i], root.value))
                if root.right is None:
                    root.right = Node(arr[i])
                    print('assigning to right')
                    break
                else:
                    root = root.right
    t.preOrder_print(t, '')






arr = [8, 5, 1, 7, 10, 12]

construct_binary_tree(arr)