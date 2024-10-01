class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)
        
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        
        self.size += 1

    def dequeue(self):
        
        if not self.first:
            return None
            
        val = self.first.value
        self.first = self.first.next
    
        self.size -= 1
        
        if self.size == 0:
            self.last = None
        
        return val
