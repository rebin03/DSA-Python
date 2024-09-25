class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

# Creating the list
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node('a')
head.next.next.next.next.next = Node('a')

def removeDupes(head):
    
    curr = head
    
    while curr:
        next_distinct = curr.next
        
        while next_distinct is not None and curr.val == next_distinct.val:
            next_distinct = next_distinct.next
        
        curr.next = next_distinct
        curr = next_distinct
    
    return head


removeDupes(head)

curr = head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next
print("null")