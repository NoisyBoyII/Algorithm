from Node import Node

"""
Singly linked list in which there is one head from which it will extend to other node via saving the address in front.
In this class, I have implemented addtion and deletion at front , end and specified index .
"""
class SinglyLinkedList:

    def __init__(self,data=None):
        if data is None:
            self.head = None
            return

        self.head = Node(data,None)

    # This function will print linked list from head to tail if Linked list in not initialized than print Empty

    def printLinkedList(self):
        if self.head is None:
            print "Empty"
            return

        temp = self.head
        while temp is not None:
            print "%s ->" % str(temp.data),
            temp = temp.front

    # This function will add new at the front position

    def pushFront(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        self.head = Node(data, self.head)

    # This function will add new node at the end position

    def pushEnd(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        temp = self.head
        while temp.front is not None:
            temp = temp.front
        new = Node(data,None)
        temp.front = new

    # This function will add new node at the Specified Position and if index is 0 than it will add at the head

    def pushAtIndex(self,data,index):
        if self.head is None:
            self.head = Node(data,None)
            return
        elif index == 0:
            self.pushFront(data)
            return
        else:
            temp = self.head
            increment = 1
            while temp.front is not None:
                if increment == index:
                    new = Node(data, temp.front)
                    temp.front = new
                    break
                temp = temp.front
                increment += 1
            if increment != index:
                print "Index out of Bound"

    # This function will pop node at front

    def popFromFront(self):
        if self.head is None:
            print "Empty"
            return
        self.head = self.head.front

    # This function will pop node from  end

    def popFromEnd(self):
        if self.head is None:
            print "Empty"
            return
        temp = self.head
        previous = None
        while temp.front is not None:
            previous = temp
            temp = temp.front
        previous.front = None

    # This function will pop the node from specific index

    def popFromIndex(self,index):
        if self.head is None:
            print "Empty"
            return
        elif index == 0:
            self.popAtFront()
            return
        else:
            temp = self.head
            increment = 1
            previous = None
            while temp.front is not None:
                if increment == index:
                    previous.front = temp.front
                    break
                increment += 1
                previous = temp
                temp = temp.front
            if increment != index:
                print "Index Out of bound"


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.printLinkedList()
    ll.pushFront(3)
    ll.pushFront(2)
    ll.pushFront(1)
    ll.pushEnd(5)
    ll.pushEnd(6)
    ll.pushEnd(7)
    ll.pushEnd(8)
    ll.pushEnd(9)
    ll.pushEnd(10)
    ll.pushAtIndex(0,0)
    ll.pushAtIndex(4,4)
    ll.printLinkedList()
    print "\nPoping at progress"
    ll.popAtFront()
    print "At Front"
    ll.printLinkedList()
    ll.popAtEnd()
    print "\nAt End"
    ll.printLinkedList()
    ll.popAtIndex(6)
    print "\nAt Specific Index"
    ll.printLinkedList()
    ll.popAtIndex(11)
    print "Index Out of Bound Case"
    ll.popAtIndex(4)
    print "At Specific Index"
    ll.printLinkedList()







