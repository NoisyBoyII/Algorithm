
# Base For Every Data Structure if satisfy the Node Structure according to Need


class Node:
    def __init__(self, data,next=None,back=None):
        self.data = data    # Node data
        self.front = next    # Next node or None
        self.back = back    # previous node or None

    def __repr__(self):
        return "Node(%s)" % str(self.data)

