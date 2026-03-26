class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def printInorder(root):
    if root:
        printInorder(root.left) 
        print(root.data, end=" ")
        printInorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal:")
printInorder(root) 
