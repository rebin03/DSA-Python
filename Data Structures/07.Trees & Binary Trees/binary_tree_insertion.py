class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, array):
        if len(array) == 0:
            return
        
        i = 0

        # If root is None, initialize it
        if self.root is None:
            if array[0] is not None:
                self.root = Node(array[0])
            i += 1  # Move to the next element after inserting root
        
        # Queue-based insertion
        queue = [self.root]
        
        while i < len(array):
            current = queue.pop(0)
            
            # Process left child
            if current.left is None:
                if i < len(array) and array[i] is not None:
                    current.left = Node(array[i])
                i += 1
                if i == len(array):
                    break
            if current.left is not None:
                queue.append(current.left)
            
            # Process right child
            if current.right is None:
                if i < len(array) and array[i] is not None:
                    current.right = Node(array[i])
                i += 1
                if i == len(array):
                    break
            if current.right is not None:
                queue.append(current.right)

        return self
    
    def print_level_order(self):
            if not self.root:
                return
            
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                print(current.value, end=" ")  # Print the value of the node

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

# Create a binary tree and insert elements
tree = BinaryTree()
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])

# Print the binary tree in level-order
tree.print_level_order()