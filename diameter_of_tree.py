class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.max_diameter = 0
        def get_height(node):
            if not node: return 0
            left = get_height(node.left)
            right = get_height(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)
        get_height(root)
        return self.max_diameter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().diameterOfBinaryTree(root))