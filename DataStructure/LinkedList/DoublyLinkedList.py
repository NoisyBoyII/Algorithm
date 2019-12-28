from Node import Node

"""
Doubly Linked list in which every node have back and front for saving the next and the previous node link so that we 
can traverse at both side. I have implemented addition and deletion from front , end , specified index.
"""


class DoublyLinkedList:
    def __init__(self,data,front=None,previous=None):
        if data is None:
            self.head = None
            return

        self.head = Node(data, front, previous)

    # This function print doubly linked list

    def printDoublyLinkedList(self):
        if self.head is None:
            print "Empty"
            return
        temp = self.head
        while temp is not None:
            print "%s <->" % temp.data,
            temp = temp.front

    # This function push node at front and if DLL head is empty than it will create new node and add that to head

    def pushAtFront(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        self.head = Node(data,self.head)

    # This function push node at end

    def pushAtEnd(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.front is not None:
            temp = temp.front
        temp.front = Node(data,None,temp)

    # This function push node at the specific index and index not found than will print Index out of bound

    def pustAtIndex(self,data,index):
        if self.head is None:
            self.head = Node(data)
            return
        elif index == 1:
            self.pushAtFront(data)
            return
        temp = self.head
        increment = 1
        while temp.front is not None:
            if increment == index:
                temp.front = Node(data,temp.front,temp)
                break
            increment += 1
            temp = temp.front
        if increment != index:
            print "Index out of bound"

    # This function pop node from front

    def popFromFront(self):
        if self.head is None:
            print "Empty"
            return
        self.head = self.head.front
        self.head.back = None

    # This function pop node from end

    def popFromEnd(self):
        if self.head is None:
            print "Empty"
            return
        temp = self.head
        while temp.front is not None:
            temp = temp.front
        temp.back.front = None

    # This function pop node from specific Index

    def popFromIndex(self,index):
        if self.head is None:
            print "Empty"
            return
        temp = self.head
        increment = 1
        while temp.front is not None:
            if increment == index:
                temp.back.front = temp.front
                temp.front.back = temp.back
                temp.front = None
                temp.back = None
                break
            temp = temp.front
            increment += 1
        if increment != index:
            print "Index out of bound"


if __name__ == "__main__":
    dll = DoublyLinkedList(1)
    dll.pushAtFront(0)
    dll.pushAtEnd(2)
    dll.pushAtEnd(3)
    dll.pushAtEnd(5)
    dll.pushAtEnd(6)
    dll.printDoublyLinkedList()
    print "\nPush at Index"
    dll.pustAtIndex(4,4)
    dll.printDoublyLinkedList()
    print"\nPop at Progress"
    dll.popAtFront()
    dll.popAtEnd()
    dll.popAtIndex(4)
    dll.printDoublyLinkedList()
