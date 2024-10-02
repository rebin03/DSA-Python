class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeF



# Test
print("root.right.left.data:", root.right.left.data)