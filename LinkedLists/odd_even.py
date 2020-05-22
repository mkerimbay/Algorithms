'''
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place.
The program should run in O(1) space complexity and O(nodes) time complexity.
'''

from Node import Node
from LinkedList import LinkedList


def odd_even(head: LinkedList):
    if not head:
        return None

    odd = head
    even = odd.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = odd.next

    odd.next = even_head
    return head

    #
    # def listprint(self):
    #     node = self.head
    #     s = ''
    #     if not node:
    #         return s
    #
    #     while node.next:
    #         s += str(node.data) + ' -> '
    #         node = node.next
    #     s += str(node.data) + ' -> Null'
    #     return s


lst = LinkedList()
lst.insert_at_tail(1)
lst.insert_at_tail(2)
lst.insert_at_tail(3)
lst.insert_at_tail(4)
lst.insert_at_tail(5)
odd_even(lst)

# print(lst.listprint())
# lst.odd_even()
print(lst.listprint())






