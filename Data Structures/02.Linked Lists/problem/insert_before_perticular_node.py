class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

def linkNodes(node1,node2):
    node1.next = node2
    node2.prev = node1

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.next = None
        node.prev = None

# insert a node before a particular node(both the node to be inserted and the node before 
# which the insertion is to happen will be given as input). 
# If the node to be inserted is
# -part of the linked list then shift its place to the desired location
# -a new node, then insert the new node at the place desired.

    def insertB(self, nodePosition, nodeInsert):
        
        self.remove(nodeInsert)
        
        nodeInsert.prev = nodePosition.prev
        nodeInsert.next = nodePosition
        
        if nodePosition == self.head:
            self.head = nodeInsert
        else:
            nodePosition.prev.next = nodeInsert
        
        nodePosition.prev = nodeInsert
        
        
        
        
        
        
        
        
        
