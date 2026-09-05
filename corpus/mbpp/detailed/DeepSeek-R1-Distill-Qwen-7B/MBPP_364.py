def min_flip_to_make_string_alternate(binary_string):
    """
    Calculate the minimum number of flips required to make the given binary string alternate between '0's and '1's.

    Args:
        binary_string (str): The input binary string consisting of '0's and '1's.

    Returns:
        int: The minimum number of flips required.
    """
    # Edge case: empty string
    if not binary_string:
        return 0

    # Generate the two possible target patterns
    target0 = '0' if len(binary_string) % 2 == 0 else '0' + '10'*(len(binary_string)//2 - 1)
    target1 = '1' if len(binary_string) % 2 == 0 else '1' + '01'*(len(binary_string)//2 - 1)

    def calculate_flips(pattern):
        """
        Calculate the number of flips needed to convert the binary string to the given pattern.
        """
        flips = 0
        for i in range(len(binary_string)):
            if binary_string[i] != pattern[i]:
                flips += 1
        return flips

    flips_for_target0 = calculate_flips(target0)
    flips_for_target1 = calculate_flips(target1)

    return min(flips_for_target0, flips_for_target1)