class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
class BinaryTree:
    def __init__(self):
        self.root = None
 
    def insert(self, array):
        if not array: return
        i = 0
        if self.root is None:
            if array[0] is None: return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array): return self
        #insert elements
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            #left
            if current.left is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.left = node
                i += 1
                if i == len(array): return self
            if current.left: queue.append(current.left)
            #right
            if current.right is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.right = node
                i += 1
                if i == len(array): return self
            if current.right: queue.append(current.right)
 


def isValidBST(root):
    return helper(root, float('-inf'), float('inf'))

def helper(node, min_val, max_val):
    # base case
    if node is None:
        return True
    
    value = node.value
    
    # check if current node's value is in between min and max value
    if value <= min_val or value >= max_val:
        return False
    
    is_left_bst = helper(node.left, min_val, value)
    is_right_bst = helper(node.right, value, max_val)

    return is_left_bst and is_right_bst


tree = BinaryTree()
tree.insert([10,5,20,3,7,15,30,None,4,None,None,None,17,None,None,None,None,None,18])
 
print(isValidBST(tree.root))