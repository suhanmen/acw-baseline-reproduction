def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # Check for invalid characters
    if not set(brackets).issubset({'<', '>'}):
        return False

    stack = []
    for idx, char in enumerate(brackets):
        if char == '<':
            stack.append(idx)
        elif char == '>':
            if not stack:
                return False
            # Check if the last opening bracket matches the current closing bracket
            last_opener = stack.pop()
            if last_oponer == -1:  # If no brackets were opened before, invalid
                return False
            if last_opener < 0:
                return False
    return len(stack) == 0

# Test cases
def test_correct_bracketing():
    assert correct_bracketing("<") == False, "Single opening bracket is invalid"
    assert correct_bracketing("<>") == True, "Valid balanced brackets"
    assert correct_bracketing("<<><>>") == True, "Valid balanced nested brackets"
    assert correct_bracketing("><<>") == False, "Unmatched closing brackets"
    assert correct_bracketing("") == True, "Empty string is considered valid"
    assert correct_bracketing("<<") == True, "Only opening brackets"
    assert correct_bracketing(">>>") == False, "Only closing brackets"
    print("All test cases passed.")

test_correct_bracketing()