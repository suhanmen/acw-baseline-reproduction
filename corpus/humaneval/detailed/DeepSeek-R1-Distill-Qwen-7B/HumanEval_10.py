def is_palindrome(string: str) -> bool:
    """Test if a given string is a palindrome."""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string."""
    if not string:
        return ""

    # Step 1: Find the longest palindromic suffix
    max_len = len(string)
    # Start from the longest possible suffix and work backwards
    for i in range(max_len, 0, -1):
        suffix = string[max_len - i : max_len]
        if is_palindrome(suffix):
            prefix = string[:max_len - i]
            # Step 2: Append the reverse of the non-palindromic part to the front
            return prefix[::-1] + string

    # If no palindromic suffix is found, the entire string is reversed and appended
    return string[::-1] + string