from LinkedList import LinkedList
from Node import Node

def reverse(lst):
  # To reverse linked, we need to keep track of three things
  previous = None # Maintain track of the previous node
  current = lst.getHead() # The current node
  next = None # The next node in the list

  #Reversal
  while current:
    next = current.next
    current.next = previous
    previous = current
    current = next

    #Set the last element as the new head node
    lst.head = previous
  return lst

lst = LinkedList()
lst.insert_at_head(6)
lst.insert_at_head(4)
lst.insert_at_head(9)
lst.insert_at_head(10)
print(lst.listprint())

reverse(lst)
print(lst.listprint())