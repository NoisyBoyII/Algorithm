"""
Stack is a abstract data type in which elements push at the end and pop at first basically it follows
the "last in first out" policy .
"""

class Stack:
    def __init__(self,limit=10):
        self.stack = []
        self.limit = limit

    def __str__(self):
        return str(self.stack)

    # we will push the element at the end of the stack
    def push(self,data):
        if len(self.stack) >= self.limit:
            print "OverFlow"
            return
        self.stack.append(data)

    # we will pop the last inserted element in stack
    def pop(self):
        if len(self.stack) == 0:
            print "UnderFlow"
            return
        self.stack.pop()

    # By this we can get the top most element in stack
    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return not bool(self.stack)

if __name__ == "__main__":
    s = Stack()
    for i in range(1,10):
        s.push(i)

    print str(s)

    s.pop()
    print str(s)
    s.pop()
    print str(s)
    s.pop()
    print str(s)
    print s.peek()
    print s.isEmpty()








