# Define a class Node for creating node with attributes data and pointer for pinting to next node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 
        
    # Method to get node in the specified index position
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        
        counter = 0
        current_node = self.head
        
        while counter != index:
            current_node = current_node.next
            counter +=1
        return current_node
    
    
    # Method to insert a node at begnning or at head
    # Time Complexity: O(1) as we perform constant time operations
    # Space Complexity: O(1) as no additional space is required
    def insert_begnning(self, data):
        node = Node(data)
        
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        
        self.size += 1
        
    
    # Method to insert a node at the end or at tail.
    # Time Complexity: O(1) as we perform constant time operations
    # Space Complexity: O(1) as no additional space is required
    def insert_end(self, data):
        node = Node(data)
        
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self.size += 1
        
        
    # Method to insert node in between the position of head and tail or insert at a specified index.
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def insert_at_index(self, index, data):
        if index < 0 or index > self.size:
            return 'Invalid index'
        
        if index == 0:
            return self.insert_begnning(data)
        elif index == self.size:
            return self.insert_end(data)
        else:
            node = Node(data)
            prev_node = self.get(index-1)
            
            temp_node = prev_node.next
            prev_node.next = node
            node.next = temp_node
        
        self.size += 1
        
    
    # Method to delete node from a specified index.
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def delete_at_index(self, index):
        if index < 0 or index >= self.size:
            return 'Invalid index'
        
        if index == 0:
            temp_node = self.head
            self.head = temp_node.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
                
            return temp_node.data # return the deleted data
        
        elif index == self.size - 1:
            temp_node = self.tail
            prev_node = self.get(index-1)
            self.tail = prev_node
            prev_node.next = None
            self.size -= 1
            
            return temp_node.data
        
        else:
            prev_node = self.get(index-1)
            deleted_node = prev_node.next
            prev_node.next = deleted_node.next
            self.size -= 1
            
            return deleted_node.data


ls = SinglyLinkedList()

ls.insert_begnning(2)
ls.insert_end(8)
ls.insert_at_index(1, 5)
ls.insert_at_index(2, 10)
ls.insert_at_index(1, 7)
ls.insert_end(33)

print(ls.delete_at_index(0))
print(ls.delete_at_index(2))
print(ls.delete_at_index(3))


current = ls.head
while current != None:
    print(current.data, end=' --> ')
    current = current.next
print('null')