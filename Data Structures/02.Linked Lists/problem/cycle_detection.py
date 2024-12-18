class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def checkLoop(head):
    
    if not head or not head.next:
        return None
        
    tortoise = head
    hare = head
    
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        
        if hare == tortoise:
            break
        
    if hare != tortoise:
        return None
    
    pointer = head
    
    while pointer != tortoise:
        pointer = pointer.next
        tortoise = tortoise.next
        
    return pointer
    
    
    