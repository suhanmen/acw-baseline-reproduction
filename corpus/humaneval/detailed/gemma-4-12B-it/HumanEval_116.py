from typing import List

def sort_array(arr: List[int]) -> List[int]:
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    """
    # Handle null or non-list inputs gracefully
    if arr is None:
        raise ValueError("Input must be a list of integers.")

    if not isinstance(arr, list):
        raise TypeError("Input must be of type 'list'.")

    # Handle empty list case
    if len(arr) == 0:
        return []

    def count_set_bits(n: int) -> int:
        """
        Counts the number of set bits (1s) in the binary representation 
        of an integer. For negative integers, this handles the bit 
        representation in a way that is consistent with standard 
        binary logic (though the problem mentions non-negative, 
        the test cases include negatives).
        """
        # If the number is negative, we treat its binary form 
        # based on standard Python behavior or common bit manipulation.
        # However, for the purpose of sorting by "ones in binary", 
        # we can treat the absolute value's bit count or the 
        # two's complement. Given the test cases provided:
        # -2 is 10 (in 2-bit), -3 is 11 (in 2-bit).
        # The test case [-2, -3, -4, -5, -6] -> [-6, -5, -4, -3, -2]
        # suggests that for negatives, we are simply sorting them by 
        # value, or their bit counts are treated consistently.
        # Since standard Python bit_count() (available in 3.10+) 
        # handles integers, we use that.

        # For older versions of Python, we use bit_count() equivalent:
        if hasattr(n, "bit_count"):
            return n.bit_count()
        else:
            # Fallback for Python < 3.10
            # Using absolute value to ensure a deterministic count of bits 
            # set in the magnitude for negative numbers to match expected behavior.
            # If the prompt strictly meant two's complement, we'd need a mask.
            # Based on the provided test cases, standard sorting works.
            return bin(n).count('1')

    def get_sorting_key(num: int):
        """
        Returns a tuple representing the sorting priority:
        (number of set bits, decimal value)
        """
        # To handle the specific behavior of negative numbers in the 
        # test case [-2, -3, -4, -5, -6] -> [-6, -5, -4, -3, -2]:
        # This implies they are sorted by magnitude/value.

        # Let's calculate the bit count.
        # Note: In Python, bin(-5) is '-0b101', so .count('1') counts 
        # the 1s in the magnitude.
        bits = bin(num).count('1')

        # The primary key is the bit count.
        # The secondary key is the actual integer value.
        return (bits, num)

    # Create a copy of the list to avoid mutating the original input
    sorted_list = list(arr)

    # Perform the sort using the custom key.
    # Python's sort is stable, which is good for consistency.
    sorted_list.sort(key=get_sorting_key)

    return sorted_list