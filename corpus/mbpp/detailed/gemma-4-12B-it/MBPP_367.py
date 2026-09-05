from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def is_tree_balanced(root: Optional[TreeNode]) -> bool:
    """
    Determines if a binary tree is height-balanced.
    A height-balanced binary tree is defined as a binary tree in which the 
    depth of the two subtrees of every node differs by no more than one.

    Args:
        root: The root node of the binary tree.

    Returns:
        bool: True if the tree is balanced, False otherwise.
    """
    # Edge Case: An empty tree (None) is considered balanced.
    if root is None:
        return True

    # Validation: Ensure the input is either a TreeNode or None.
    if root is not None and not isinstance(root, TreeNode):
        raise ValueError("Input must be a TreeNode instance or None.")

    # We use a helper function to perform a bottom-up recursive check.
    # This approach allows us to calculate height and check balance in a 
    # single pass, resulting in O(N) time complexity.
    def check_height_and_balance(node: Optional[TreeNode]) -> int:
        """
        Recursive helper that returns the height of the tree if balanced,
        or -1 if any subtree is found to be unbalanced.
        """
        # Base Case: A null node has a height of 0.
        if node is None:
            return 0

        # Recursively check the left subtree.
        left_height = check_height_and_balance(node.left)

        # If the left subtree is unbalanced, propagate the -1 up.
        if left_height == -1:
            return -1

        # Recursively check the right subtree.
        right_height = check_height_and_balance(node.right)

        # If the right subtree is unbalanced, propagate the -1 up.
        if right_height == -1:
            return -1

        # Calculate the height difference between the two subtrees.
        height_difference = abs(left_height - right_height)

        # Check the balance condition: difference must be <= 1.
        if height_difference > 1:
            # Tree is unbalanced at this node.
            return -1

        # If balanced, return the height of the current node.
        # Height is 1 + the maximum height of the two subtrees.
        current_height = 1 + max(left_height, right_height)
        return current_height

    # If the helper returns -1, it means the tree is unbalanced.
    result_height = check_height_and_balance(root)

    if result_height == -1:
        return False
    else:
        return True


# Example test structures to verify logic (Internal logic check)
if __name__ == "__main__":
    # Case 1: Unbalanced tree
    #      1
    #     /
    #    2
    #   /
    #  3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    # is_tree_balanced(root) should be False
    assert is_tree_balanced(root) == False

    # Case 2: Balanced tree
    #     1
    #    / \
    #   2   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    # is_tree_balanced(root1) should be True
    assert is_tree_balanced(root1) == True

    # Case 3: Unbalanced tree (diff > 1)
    #      1
    #     / \
    #    2   3
    #   /
    #  4
    # /
    # 5
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.left.left = TreeNode(5)
    # is_tree_balanced(root2) should be False
    assert is_tree_balanced(root2) == False