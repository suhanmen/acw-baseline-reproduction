from typing import List

def find_Element(
    elements: List[int], 
    rotations: List[List[int]], 
    total_rotations: int, 
    target_index: int
) -> int:
    """
    Finds the element at a specific index after a sequence of rotations.

    A rotation [i, j] means the element at index i moves to index j.
    The process is repeated 'total_rotations' times for each rotation 
    pair in the 'rotations' list, sequentially.

    However, the standard interpretation of "rotations" in these contexts 
    usually implies that each pair in the list represents a transformation 
    rule applied sequentially. Based on the provided assertions:

    Assertion 1: [1,2,3,4,5], [[0,2],[0,3]], rotations=2, target=1
    - Rotation 1: [0,2] -> index 0 moves to 2. List becomes [?, ?, 1, 4, 5]? 
      Wait, if it's a swap/move: 
      Step 1: Move index 0 to 2. [2, 3, 1, 4, 5] (shifting others)
      This logic is complex. Let's re-evaluate the transformation.

    Actually, the assertions suggest a simpler cumulative index mapping:
    - The input 'rotations' is a list of [source_index, destination_index].
    - 'total_rotations' is the number of times the *entire sequence* of 
      transformations in 'rotations' is applied.
    - 'target_index' is the final index we want to see the value of.

    To find what value ends up at 'target_index', we can work backwards.
    If we know what index 'target_index' was at before the last step, 
    we can trace it back to the original index.
    """

    # 1. Input Validation
    if not isinstance(elements, list) or not elements:
        raise ValueError("The elements list must not be empty.")

    if not isinstance(rotations, list):
        raise ValueError("Rotations must be a list of pairs.")

    n = len(elements)

    if target_index < 0 or target_index >= n:
        raise IndexError(f"Target index {target_index} is out of bounds for list of size {n}.")

    if total_rotations < 0:
        raise ValueError("Total rotations must be a non-negative integer.")

    # 2. Define the transformation logic.
    # Based on the assertions provided:
    # Assert 1: [1,2,3,4,5], [[0,2],[0,3]], 2, 1 -> 3
    # Let's trace the movement of values. 
    # A rotation [i, j] means the element at index i is moved to position j.
    # This implies elements between i and j are shifted to fill the gap.

    def apply_single_rotation(current_list: List[int], src: int, dest: int) -> List[int]:
        """
        Moves the element at 'src' to 'dest' by shifting other elements.
        If src == dest, no change.
        """
        new_list = list(current_list)
        if src == dest:
            return new_list

        # Get the value to move
        val = new_list[src]

        # Remove it from original position
        # We use a temporary list to handle the shift clearly
        temp_list = new_list[:src] + new_list[src+1:]

        # Insert it at the new position
        # The 'dest' in the original list corresponds to a different index 
        # in temp_list because the list shrunk.

        # Standard behavior for "move index i to j":
        # 1. Remove element at i.
        # 2. Insert it at j.

        # Let's re-evaluate: if we move index 0 to 2 in [1,2,3,4,5]
        # 1. Remove '1' -> [2,3,4,5]
        # 2. Insert '1' at index 2 -> [2,3,1,4,5]

        # Let's check Assert 2: [1,2,3,4], [[0,1],[0,2]], 1, 2 -> 3
        # List [1,2,3,4]
        # [0,1]: Move index 0 to 1 -> [2,1,3,4]
        # [0,2]: Move index 0 to 2 -> [1,2,3,4] ... no, that doesn't match.

        # Alternative Interpretation:
        # Rotation [i, j] means: new_index = (old_index + (j - i)) % n
        # But that's a cyclic shift.

        # Let's try: [0,2] and [0,3] are indices.
        # If it's a simple swap: [0,2] swaps 0 and 2. [0,3] swaps 0 and 3.
        # Assert 1: [1,2,3,4,5], [[0,2],[0,3]], 2, 1
        # Iter 1:
        #   Swap(0,2): [3,2,1,4,5]
        #   Swap(0,3): [4,2,1,3,5]
        # Iter 2:
        #   Swap(0,2): [1,2,4,3,5]
        #   Swap(0,3): [3,2,4,1,5]
        # Index 1 is '2'. Assertion says '3'. Still not matching.

        # Let's try: Rotation [i, j] means: 
        # The element at index i is moved to index j.
        # Elements between i and j shift to the left.
        # Assert 2: [1,2,3,4], [[0,1],[0,2]], 1, 2 -> 3
        # [1,2,3,4]
        # [0,1]: Move index 0 to 1. [2,1,3,4]
        # [0,2]: Move index 0 to 2. [1,3,2,4] (Wait, move index 0 which is '1' to index 2)
        # Index 2 is '2'. Assertion says '3'. 

        # Let's try: The index 'i' moves to 'j'. 
        # This is an index mapping: map[j] = i.
        # If multiple indices are moved, we need to be careful.

        # Let's try the most common "Rotation" meaning in these problems:
        # A rotation [i, j] means:
        # The value at index j moves to index i.
        # Assert 2: [1,2,3,4], [[0,1],[0,2]], 1, 2
        # [0,1]: Index 1 moves to 0 -> [2,1,3,4]
        # [0,2]: Index 2 moves to 0 -> [3,1,2,4]
        # Index 2 is '2'. Assertion says '3'.

        # Let's try: The rotation is a circular shift of the subsegment [i, j].
        # [0,1] on [1,2,3,4] -> [2,1,3,4]
        # [0,2] on [2,1,3,4] -> [3,2,1,4]
        # Index 2 is '1'. Assertion says '3'.

        # Let's try: Rotation [i, j] means 
        # the element at index i moves to j, and everything else stays put.
        # This is a swap: swap(elements[i], elements[j])
        # Assert 1: [1,2,3,4,5], [[0,2],[0,3]], 2, 1
        # [1,2,3,4,5]
        # 1. Swap(0,2): [3,2,1,4,5]
        # 2. Swap(0,3): [4,2,1,3,5]
        # 3. Swap(0,2): [1,2,4,3,5]
        # 4. Swap(0,3): [3,2,4,1,5]
        # Index 1 is '2'. Still no.

        # Wait! What if "Rotation" [i, j] means:
        # The element at index i moves to j.
        # If j > i, elements from i+1 to j move left.
        # If j < i, elements from j to i-1 move right.
        # Let's try Assert 2: [1,2,3,4], [[0,1],[0,2]], 1, 2
        # [1,2,3,4]
        # [0,1]: Move 0 to 1 -> [2,1,3,4]
        # [0,2]: Move 0 to 2 -> [1,3,2,4] (Wait, 2 is now at 1, 3 is at 2... if we move index 0 to 2)
        # If we move 0 to 2: remove '2' from 0, insert at 2: [1,3,2,4]

        # One more try: The rotation [i, j] is a rotation of the sub-array [i...j]
        # to the right by 1.
        # [1,2,3,4,5]
        # [0,2]: [3,1,2,4,5]
        # [0,3]: [4,3,1,2,5]
        # [0,2]: [1,4,3,2,5]
        # [0,3]: [2,1,4,3,5]
        # Index 1 is '1'.

        # Let's look at the numbers again.
        # Assert 1: [1,2,3,4,5], [[0,2],[0,3]], 2, 1 -> 3
        # Assert 2: [1,2,3,4], [[0,1],[0,2]], 1, 2 -> 3
        # Assert 3: [1,2,3,4,5,6], [[0,1],[0,2]], 1, 1 -> 1

        # If Assert 3: [1,2,3,4,5,6], [[0,1],[0,2]], 1, 1 -> 1
        # And the answer is 1. This means after [0,1] and [0,2], index 1 is 1.
        # Original [1,2,3,4,5,6]
        # If [0,1] is a swap: [2,1,3,4,5,6]
        # If [0,2] is a swap: [3,1,2,4,5,6]
        # Index 1 is '1'. YES!

        # Let's re-check Assert 2 with Swap:
        # [1,2,3,4], [[0,1],[0,2]], 1, 2
        # Swap(0,1): [2,1,3,4]
        # Swap(0,2): [3,1,2,4]
        # Index 2 is '2'. Still not 3.

        # Let's try another interpretation: [i, j] means "Rotate the list such that 
        # the element at index i moves to index j" (Circularly).
        # No, that doesn't make sense for indices.

        # Let's try: "Rotate the list such that the element at index j moves to 
        # the position i, and everything else shifts."
        # Assert 2: [1,2,3,4], [[0,1],[0,2]], 1, 2
        # [0,1]: move index 1 to 0: [2,1,3,4]
        # [0,2]: move index 2 to 0: [3,1,2,4]
        # Index 2 is '2'. 

        # Wait! What if "rotation" means:
        # Rotation [i, j] means: list[i:j+1] = list[i:j+1][1:] + list[i:j+1][:1]
        # (Cyclic shift of the subsegment [i, j] to the left by 1)
        # Assert 3: [1,2,3,4,5,6], [[0,1],[0,2]], 1, 1
        # [0,1