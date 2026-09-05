class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_tree_balanced(root):
    def height_and_balance(node):
        if node is None:
            return 0, True
        left_height, left_balanced = height_and_balance(node.left)
        right_height, right_balanced = height_and_balance(node.right)
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return max(left_height, right_height) + 1, balanced

    _, is_balanced = height_and_balance(root)
    return is_balanced

# Example trees for testing (not part of the required signature)
if __name__ == "__main__":
    # Balanced tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Unbalanced tree (left heavy)
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.left.left = TreeNode(4)

    # Another unbalanced tree (right heavy)
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    root2.right.right = TreeNode(3)
    root2.right.right.right = TreeNode(4)

    assert is_tree_balanced(root) == True
    assert is_tree_balanced(root1) == False
    assert is_tree_balanced(root2) == False