def rearrange_string(s):
    # Count the frequency of each character in the string
    from collections import Counter
    char_count = Counter(s)
    max_count = max(char_count.values(), default=0)
    length = len(s)

    # Check if any character occurs more than half the length of the string
    if max_count > length // 2:
        return None

    # Helper function to construct the rearranged string
    def construct_rearranged_string(s):
        # Split the string into two halves based on the most frequent character
        most_common = max(char_count, key=lambda k: char_count[k])
        split = char_count[most_common] == 1 and len(s) % 2 == 0

        # Get the two parts of the string
        part1 = s.replace(most_common, '', 1)
        part2 = s.replace(most_common, '')

        # Combine the parts to form the rearranged string
        if split:
            return part2 + part1 + most_common
        else:
            return part1 + part2 + most_common

    # Check if the string is empty
    if not s:
        return None

    # Construct the rearranged string
    result = construct_rearranged_string(s)

    # If the rearranged string has the same length as the original, return it
    if len(result) == len(s):
        return result

    # If not, try a different approach
    result = construct_rearranged_string(s)
    if len(result) == len(s):
        return result

    # If all else fails, return None
    return None

# Test cases
assert rearrange_string("aab") == 'aba'
assert rearrange_string("aabb") == 'abab'
assert rearrange_string("abccdd") == 'cdabcd'