class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def printPostorder(node):
    if node is None:
        return
    printPostorder(node.left) 
    printPostorder(node.right) 
    print(node.data, end=' ')

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Postorder traversal:")
    printPostorder(root)
    print()
