def _is_valid_input_string(text):
    """
    Validates that the input is a string.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(text, str):
        return False
    return True


def _find_first_a_index(text):
    """
    Finds the index of the first occurrence of 'a' in the string.

    Args:
        text (str): The input string to search.

    Returns:
        int: The index of the first 'a', or -1 if 'a' is not found.
    """
    for current_index, character in enumerate(text):
        if character == 'a':
            return current_index
    return -1


def _check_following_characters(text, start_index):
    """
    Checks if the characters immediately following the 'a' at start_index
    are two or three 'b's.

    This function handles the counting of 'b's and ensures no other characters
    interrupt the sequence of 'b's before the count reaches 2 or 3.

    Args:
        text (str): The input string.
        start_index (int): The index of the 'a' found in the text.

    Returns:
        bool: True if the sequence is exactly 'b', 'b' followed by either nothing 
              (length 2 total for b's, wait, problem says 2 to 3 b's), 
              or 'b', 'b', 'b'. 
              Actually, re-reading: "two to three 'b'".
              So we need exactly 2 or 3 'b's immediately after 'a'.
              It implies the sequence must be "abb" or "abbb".
              If there are 4 'b's, it should not match based on "two to three".
              Let's assume strict count: 2 or 3.

    Logic:
        We iterate starting from start_index + 1.
        We count consecutive 'b's.
        If we encounter a non-'b' before reaching 2 'b's, return False.
        If we reach 2 'b's, we can stop and return True (since 2 is in [2,3]).
        If we reach 3 'b's, we must check if the next character exists.
            If the next character exists, it must NOT be 'b', otherwise we have 4 'b's.
            If the next character does not exist (end of string), it's valid (3 'b's).
        If we finish the loop (only possible if we checked up to 3 and the next was not 'b' or end),
        we need to be careful.

        Let's refine the loop logic:
        Count b's.
        If count reaches 2: Check next char.
            If next char is 'b': Count is now 3. Continue to check next.
            If next char is not 'b': Valid (count=2). Return True.
            If end of string: Valid (count=2). Return True.
        If count reaches 3: 
            We must ensure the sequence stops here.
            Check next char.
            If next char is 'b': Count is now 4 -> Invalid (too many). Return False.
            If next char is not 'b': Valid (count=3). Return True.
            If end of string: Valid (count=3). Return True.

        Actually, a simpler approach:
        Extract the substring of potential 'b's.
        But we need to be careful not to skip valid patterns if we slice blindly.

        Revised Plan for _check_following_characters:
        1. Ensure we are not at the end of the string.
        2. Count consecutive 'b's starting from start_index + 1.
        3. While counting, if we hit 2 'b's, check the next char.
           - If next char is 'b', we have 3 'b's. Check the one after that.
           - If next char is NOT 'b', we have exactly 2 'b's. This is a match. Return True.
           - If end of string, we have exactly 2 'b's. This is a match. Return True.

        Wait, the requirement is "two to three 'b'".
        So "abb" (2 b's) -> Match.
        "abbb" (3 b's) -> Match.
        "abbbbb" (5 b's) -> No Match.
        "ab" (1 b) -> No Match.
        "abba" (2 b's followed by a) -> Match.
        "abbc" (2 b's followed by c) -> Match.

        Let's implement a strict counter.
    """
    current_index = start_index
    count = 0

    # Start checking characters immediately after 'a'
    if current_index >= len(text):
        # No characters after 'a', so count is 0.
        return False

    # We will iterate through the string to count 'b's
    # We need to stop if we hit 3 'b's and the next one is also 'b' (which would make 4).
    # Or stop if we hit a non-'b'.

    # Let's just iterate and count
    index_ptr = current_index + 1

    while index_ptr < len(text):
        char = text[index_ptr]
        if char == 'b':
            count += 1
            index_ptr += 1

            # Optimization/Cleanup check:
            # If we have 3 'b's, we cannot have any more 'b's.
            if count == 3:
                # Check the very next character to ensure it's NOT 'b'
                # Because if it is 'b', we would have 4, which is invalid.
                next_ptr = index_ptr
                if next_ptr < len(text) and text[next_ptr] == 'b':
                    return False
                else:
                    # We have exactly 3 'b's and the sequence of 'b's has ended.
                    return True
        else:
            # Hit a character that is not 'b'
            # If count < 2, then we failed to get 2 'b's.
            if count < 2:
                return False
            # If count == 2 or count == 3 (though loop breaks on 3 before else), we are good.
            # Note: If count was 3, the loop would have returned True inside the 'if' block above.
            # So here, count must be 2.
            return True

    # If we exit the loop, it means we reached the end of the string.
    # If we reached here via the 'b' block with count=3, we returned True.
    # If we reached here via the 'b' block with count=2, we returned True inside the loop when count==2?
    # Wait, in the loop:
    #   if count == 3: check next and return.
    #   else: continue.
    # So if count becomes 2, we don't return immediately. We continue.
    # If the next char is 'b', count becomes 3.
    #   Then check next. If next is not 'b', return True.
    #   If next IS 'b', return False.
    # If the next char is NOT 'b':
    #   We fall into the 'else' block.
    #   We check count < 2. Since count is 2, this is False.
    #   We return True.

    # What if count is 2 and we reach end of string?
    # The loop finishes. We exit loop.
    # count is 2. 2 is between 2 and 3. So True.

    # What if count is 1 and we reach end of string?
    # We exit loop. count is 1. 1 is not between 2 and 3. So False.

    # What if count is 3 and we reach end of string?
    # Inside the loop: count becomes 3. 
    #   Check next_ptr. It is equal to len(text) (end of string).
    #   Condition `next_ptr < len(text)` is False.
    #   So we go to `else`: return True.

    return False


def text_match_two_three(text):
    """
    Matches a string that has an 'a' followed by two to three 'b's.

    The function performs validation and checks the specific pattern.

    Args:
        text (str): The input string to evaluate.

    Returns:
        str: 'Found a match!' if the pattern matches, 'Not matched!' otherwise.
    """
    # Step 1: Validate input type
    if not _is_valid_input_string(text):
        return 'Not matched!'

    # Step 2: Locate the first 'a'
    a_index = _find_first_a_index(text)

    # If 'a' is not found, no match is possible
    if a_index == -1:
        return 'Not matched!'

    # Step 3: Check if there are enough characters following 'a' to potentially have 2 'b's
    # Minimum required length is 'a' (1) + 2 'b's (2) = 3.
    if a_index + 2 >= len(text):
        return 'Not matched!'

    # Step 4: Verify the pattern of 'b's immediately following 'a'
    # We pass the text and the index of 'a' to our helper.
    # The helper ensures we have exactly 2 or 3 'b's and nothing more/less in that sequence.
    is_pattern_matched = _check_following_characters(text, a_index)

    if is_pattern_matched:
        return 'Found a match!'
    else:
        return 'Not matched!'