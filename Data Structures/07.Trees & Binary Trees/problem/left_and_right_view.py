def rightView(root):
    if root is None: 
        return []
    right = []
    queue = [root]
    while queue:
        count = 0
        length = len(queue)
        while count < length:
            count += 1
            current = queue.pop(0)
            if count == length:
                right.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return right

def leftView(root):
    if root is None: 
        return []
    left = []
    queue = [root]
    while queue:
        count = 0
        length = len(queue)
        while count < length:
            count += 1
            current = queue.pop(0)
            if count == 1:
                left.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return left