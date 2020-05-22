from LinkedList import LinkedList
from Node import Node


def remove_duplicates(lst):
    if not lst:
        return
    current_node = lst.getHead()
    prev_node = None
    observed = set()

    while current_node:
        if current_node.data not in observed:
            observed.add(current_node.data)
            prev_node = current_node
            current_node = current_node.next
        else:
            prev_node.next = current_node.next
            current_node = current_node.next

    return lst


lst = LinkedList()
lst.insert_at_tail(1)
lst.insert_at_tail(2)
lst.insert_at_tail(2)
lst.insert_at_tail(3)
lst.insert_at_tail(3)
lst.insert_at_tail(3)
lst.insert_at_tail(3)
lst.insert_at_head(4)
lst.insert_at_head(5)
lst.insert_at_head(5)
remove_duplicates(lst)
print(lst.listprint())