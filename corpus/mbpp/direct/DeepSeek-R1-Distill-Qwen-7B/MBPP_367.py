python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_tree_balanced(root):
    def is_balanced(node):
        if not node:
            return 0

        left = is_balanced(node.left)
        right = is_balanced(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return left + 1  # Height is max(left, right) + 1, but since left and right are balanced, it's left +1

    return is_balanced(root) != -1