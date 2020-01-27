"""
Circular link list is a type of normal link list in which end is not empty like singlylinkedlist bt
end represent to front so you can iterate it back to head
"""

from Node import Node


class CircularLinkedList:
    def __init__(self,data):
        if data is None:
            self.head = None
            return
        self.head = Node(data,None)
        self.head.front = self.head

    # This will circular linked list

    def printCircularLL(self):
        if self.head is None:
            print "Empty"
            return
        temp = self.head
        while True:
            print "%s" % temp.data,
            if temp.front == self.head:
                break
            temp = temp.front


    # This function push node at front

    def pushAtFront(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        temp = self.head
        while temp.front != self.head:
            temp = temp.front
        nodeForAddition = Node(data, self.head)
        self.head = nodeForAddition
        temp.front = self.head

    # This function push node at end

    def pushAtEnd(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        temp = self.head
        while temp.front != self.head:
            temp = temp.front
        nodeForAddtion = Node(data,self.head)
        temp.front = nodeForAddtion

    # This function push node at the specific index and index not found than will print Index out of bound

    def pushAtIndex(self,data,index):
        if self.head is None:
            self.head = Node(data)
            return
        elif index == 1:
            self.pushAtFront(data)
            return
        temp = self.head
        increment = 1
        while temp.front != self.head:
            if increment == index:
                previous.front = Node(data, temp.front)
                break
            increment += 1
            previous = temp
            temp = temp.front
        if increment != index:
            print "Index out of bound"


    # This function pop node from front

    def popFromFront(self):
        if self.head is None:
            print "Empty"
            return
        temp = self.head
        while temp.front != self.head:
            temp = temp.front
        self.head = self.head.front
        temp.front = self.head

    # This function pop node from end

    def popFromEnd(self):
        if self.head is None:
            print "Empty"
            return
        temp = self.head
        previous = None
        while temp.front != self.head:
            previous = temp
            temp = temp.front
        previous.front = self.head

    # This function pop node from specific Index

    def popFromIndex(self,index):
        if self.head is None:
            print "Empty"
            return
        temp = self.head
        increment = 1
        while temp.front != self.head:
            if increment == index:
                previous.front = temp.front
                break
            previous = temp
            temp = temp.front
            increment += 1
        if increment != index:
            print "Index out of bound"


if __name__ == "__main__":
    cll = CircularLinkedList(2)
    cll.pushAtFront(1)
    cll.pushAtEnd(3)
    cll.pushAtEnd(4)
    cll.pushAtEnd(6)
    cll.pushAtEnd(7)
    cll.pushAtEnd(8)
    cll.printCircularLL()
    print "\nPush at Index"
    cll.pushAtIndex(5, 5)
    cll.printCircularLL()
    print"\nPop at Progress"
    cll.popFromFront()
    cll.popFromEnd()
    cll.popFromIndex(4)
    cll.printCircularLL()
