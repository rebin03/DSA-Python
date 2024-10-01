class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def addAtBeginning(self, value):
        node = Node(value)
        if not self.first:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        
        self.size += 1
        return self

    def removeFromBeginning(self):
        if not self.first:
            return None
        
        pop_val = self.first.value
        self.first = self.first.next
        
        self.size -= 1
    
        return pop_val

