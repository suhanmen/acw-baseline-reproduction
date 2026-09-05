class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_height(node):
    if node is None:
        return 0
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    return max(left_height, right_height) + 1

def is_tree_balanced(root):
    def check_balance(node):
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return check_balance(node.left) and check_balance(node.right)

    if root is None:
        return True
    return check_balance(root)