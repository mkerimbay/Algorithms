class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        s = printval.dataval
        while printval is not None:
            s += '->' + printval.dataval
            # print(printval.dataval + '->')
            printval = printval.nextval
        print(s)


l = LinkedList()
print(l.headval)
# e1 = Node('Mon')
# e2 = Node('Tue')
# e3 = Node('Wed')
#
# l.headval = e1
# e1.nextval = e2
# e2.nextval = e3
#
# l.listprint()
# print(e1.nextval.dataval)




