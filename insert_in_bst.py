def insert_iterative(root, key):
    new_node = Node(key)
    if root is None:
        return new_node
    
    current = root
    parent = None

    while current:
        parent = current
        if key < current.val:
            current = current.left
        else:
            current = current.right
    
    if key < parent.val:
        parent.left = new_node
    else:
        parent.right = new_node
        
    return root


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)

    insert_iterative(root, 10)

    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.val, end=" ")
            inorder_traversal(root.right)

    inorder_traversal(root) 
