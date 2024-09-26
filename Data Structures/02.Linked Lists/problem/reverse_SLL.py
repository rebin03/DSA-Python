class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating the list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

def reverseLinkedList(head):
    
    prev = None
    curr = head
    
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    
    return prev