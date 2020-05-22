from Node import Node

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def emptyHead(self):
        return self.head == None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    def insert_at_tail(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        return

    def insert_at_pos(self, pos, data):
        new_node = Node(data)

        node = self.head
        position = 1
        while node:
            position += 1
            if position == pos:
                next_node = node.next
                node.next = new_node
                new_node.next = next_node
                return
            node = node.next
        return

    def delete_head(self):

        if not self.head:
            return
        head_node = self.head

        self.head = head_node.next
        head_node.next = None
        return

    def delete_node(self, value):
        if not self.head:
            return
        node = self.head
        node_prev = None

        # value is at head
        if node.data == value:
            self.delete_head()
            return


        while node:
            if node.data == value:
                node_prev.next = node.next
                break
            node_prev = node
            node = node.next
        #     next_node = node.next
        #     if next_node and node_next.data == value:
        #         node.next = node_next.next
        #     node = node.next

    def search(self, value):
        node = self.head
        while node:
            if node.data == value:
                return True
            node = node.next
        return False

    def length(self):
        head = self.head
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def reverse(self):
        node = self.head
        prev_node = None
        next_node = None

        while next_node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
            self.head = prev_node
        return


    def listprint(self):
        node = self.head
        s = ''
        if not node:
            return s

        while node.next:
            s += str(node.data) + ' -> '
            node = node.next
        s += str(node.data) + ' -> Null'
        return s

if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_at_tail(1)
    lst.insert_at_tail(2)
    lst.insert_at_tail(3)
    lst.insert_at_tail(4)
    lst.insert_at_tail(5)
    lst.insert_at_tail(6)
    lst.insert_at_tail(7)
    print(lst.listprint())
    # lst.insert_at_pos(2, 10)
    lst.delete_head()
    # lst.delete_node(7)
    print(lst.length())

    print(lst.listprint())

# l.listprint()
# l.insert_at_head(456)

#
# lst.listprint()
# print(e1.nextval.dataval)




