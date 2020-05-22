from LinkedList import LinkedList
from Node import Node


def find_mid(lst):
    if not lst:
        return -1
    current_node = lst.getHead()
    if current_node.next == None:
        # Only 1 element exist in array so return its value.
        return current_node.data

    mid_node = current_node
    current_node = current_node.next.next
    # Move mid_node (Slower) one step at a time
    # Move current_node (Faster) two steps at a time
    # When current_node reaches at end, mid_node will be at the middle of List
    while current_node:
        mid_node = mid_node.next
        current_node = current_node.next
        if current_node:
            current_node = current_node.next
    if mid_node:
        return mid_node.data
    return -1


lst = LinkedList()
lst.insert_at_head(22)
lst.insert_at_head(21)
lst.insert_at_head(10)
lst.insert_at_head(14)
lst.insert_at_head(7)
print(lst.length())
print(lst.listprint())
print(find_mid(lst))