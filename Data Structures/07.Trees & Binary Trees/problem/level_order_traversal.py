from collections import deque

def level_order_traversal(root):
    if root is None:  
        return []

    output = []
    queue = deque([root])
    
    while queue:
        count = 0
        length = len(queue)
        
        curr_level = []
        
        while count < length:
            current = queue.popleft()
            curr_level.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
            count += 1
        
        output.append(curr_level)

    return output  