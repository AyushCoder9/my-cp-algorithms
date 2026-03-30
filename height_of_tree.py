class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def get_height(root):
    if root is None:
        return -1
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    
    return 1 + max(left_height, right_height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(f"Height of tree: {get_height(root)}")
