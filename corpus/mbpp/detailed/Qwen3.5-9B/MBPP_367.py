from typing import Optional, Any

# Define the TreeNode class to represent nodes in a binary tree.
class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None) -> None:
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

def _get_height(root: Optional[TreeNode]) -> int:
    """
    Recursively calculates the height of the binary tree rooted at 'root'.

    The height is defined as the number of edges on the longest path from the root to a leaf.
    However, for balancing checks, it is often more convenient to define height as the number of nodes
    on the longest path (or simply 0 for a None node, 1 for a leaf node).

    This implementation defines:
    - Height of a None node as 0.
    - Height of a non-None node as 1 + max(height of left, height of right).

    This definition ensures that a single node tree has height 1, which simplifies the balance check.
    """
    # Base case: if the current node is None, its height is 0.
    if root is None:
        return 0

    # Recursive step: get the height of the left and right subtrees.
    left_subtree_height: int = _get_height(root.left)
    right_subtree_height: int = _get_height(root.right)

    # The height of the current node is 1 plus the maximum of the heights of its children.
    current_height: int = 1 + max(left_subtree_height, right_subtree_height)

    return current_height

def _check_balance_and_get_height(
    root: Optional[TreeNode]
) -> tuple[int, bool]:
    """
    Helper function to perform an optimized check for balance and compute height simultaneously.

    This function uses a post-order traversal approach to avoid recalculating heights
    for sub-trees that are already known to be unbalanced.

    Returns a tuple containing:
    1. The height of the current subtree (if balanced), or -1 if unbalanced.
    2. A boolean indicating whether the current subtree is balanced.

    Logic:
    - If the node is None, it is considered balanced with height 0.
    - Recursively check if the left and right subtrees are balanced.
    - If either subtree is not balanced, propagate the unbalance status up.
    - If both subtrees are balanced, check if the height difference is <= 1.
      If the difference is > 1, the current subtree is not balanced.
    - If the current subtree is balanced, return its height and True.
    """
    # Base case: an empty tree is balanced and has height 0.
    if root is None:
        return 0, True

    # Recursively process the left child.
    left_height: int = _check_balance_and_get_height(root.left)[0]
    left_is_balanced: bool = _check_balance_and_get_height(root.left)[1]

    # Recursively process the right child.
    right_height: int = _check_balance_and_get_height(root.right)[0]
    right_is_balanced: bool = _check_balance_and_get_height(root.right)[1]

    # If either subtree is not balanced, the current tree cannot be balanced.
    if not left_is_balanced or not right_is_balanced:
        # Return -1 as a sentinel value to indicate unbalance.
        # The boolean flag will be False.
        return -1, False

    # Both subtrees are balanced. Now check the height difference.
    height_difference: int = abs(left_height - right_height)

    # A binary tree is balanced if the height of the two subtrees differs by at most 1.
    if height_difference > 1:
        # The current tree is not balanced. Return -1 as a sentinel.
        return -1, False

    # Both subtrees are balanced, and the height difference is within the limit.
    # Calculate the height of the current node.
    current_height: int = 1 + max(left_height, right_height)

    return current_height, True

def is_tree_balanced(root: Optional[TreeNode]) -> bool:
    """
    Determines whether a binary tree is balanced.

    A binary tree is considered balanced if:
    1. The left and right subtrees of every node differ in height by no more than one.
    2. Both the left and right subtrees are themselves balanced.

    This function returns False if the tree is invalid (None is treated as valid empty tree).
    The problem statement implies valid tree structures, but we ensure robustness.

    Args:
        root: The root node of the binary tree.

    Returns:
        True if the binary tree is balanced, False otherwise.
    """
    # Validate the input type.
    if not isinstance(root, TreeNode):
        raise TypeError("The 'root' argument must be a TreeNode instance or None.")

    # Call the helper function to check balance and get height.
    # We only need the boolean result from the helper.
    _, is_balanced: bool = _check_balance_and_get_height(root)

    return is_balanced