
# Base For Every Data Structure if satisfy the Node Structure according to Need


class Node:
    def __init__(self, data,next):
        self.data = data    # Node data
        self.next = next    # Next node or None

    def __repr__(self):
        return "Node(%s)" % str(self.data)

