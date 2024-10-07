class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

def sorted_array_to_BST(nums, left = 0, right = None):
    
    if right is None:
        right = len(nums) - 1
        
    if left > right:
        return None
    
    middle = (left + right) // 2
    
    node = Node(nums[middle])
    
    node.left = sorted_array_to_BST(nums, left, middle - 1)
    node.right = sorted_array_to_BST(nums, middle + 1, right)
    
    return node


sorted_array_to_BST([1, 2, 3, 4, 6, 7])