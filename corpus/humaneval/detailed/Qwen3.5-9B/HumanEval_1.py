from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def is_balanced(s: str) -> bool:
        """
        Helper function to check if a string of parentheses is balanced.

        Args:
            s: The string to check.

        Returns:
            True if balanced, False otherwise.
        """
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            else:
                return False

            if balance < 0:
                return False

        return balance == 0

    def extract_group(paren_string: str, start_index: int) -> tuple:
        """
        Helper function to extract a balanced group starting from start_index.

        Args:
            paren_string: The full string of parentheses.
            start_index: The starting index in the string.

        Returns:
            A tuple containing (extracted_group_string, end_index_of_group).
            If no group can be found starting at start_index, returns (None, -1).
        """
        if start_index >= len(paren_string):
            return None, -1

        # Skip any leading spaces from the start_index
        clean_start = start_index
        while clean_start < len(paren_string) and paren_string[clean_start] == ' ':
            clean_start += 1

        if clean_start >= len(paren_string):
            return None, -1

        # We need to find the matching closing parenthesis for paren_string[start_index]
        # and handle nested structures correctly.

        # Check if the character at start_index is actually an open parenthesis
        if paren_string[start_index] != '(':
            # If it's not '(', we can't form a group starting here (unless it's empty which isn't allowed by logic below)
            # However, based on the problem description, input consists of groups.
            # If we hit a closing paren or something else unexpectedly, this is invalid for a new group.
            # But since we process linearly, we expect to find '('.
            return None, -1

        # Use a counter to track nesting depth
        depth = 0
        group_chars = []

        # Start scanning from the cleaned start index
        scan_index = clean_start

        while scan_index < len(paren_string):
            char = paren_string[scan_index]

            if char == ' ':
                # Spaces are ignored in the logic but part of the traversal to find the boundary
                # However, the requirement says "Ignore any spaces in the input string" for grouping logic.
                # This usually means we treat spaces as non-existent when counting depth,
                # but we might need to decide if they are part of the output group or skipped.
                # Looking at the example: '( )' -> '()' suggests spaces are removed from the result too.
                group_chars.append(char) # We will filter spaces out later when building the final string
                scan_index += 1
                continue

            if char == '(':
                depth += 1
                group_chars.append(char)
                scan_index += 1
            elif char == ')':
                depth -= 1
                group_chars.append(char)
                scan_index += 1
                if depth == 0:
                    # We found the matching closing parenthesis
                    # Construct the result string by removing spaces
                    group_str = "".join(group_chars)
                    return group_str, scan_index
            else:
                # Found an invalid character inside the parenthesis group
                return None, -1

        # If we exit the loop without finding a matching closing paren
        return None, -1

    def process_string(input_str: str) -> List[str]:
        """
        Main logic to separate groups from the input string.

        Args:
            input_str: The input string containing parentheses groups and spaces.

        Returns:
            A list of strings, each representing a balanced group of parentheses.
        """
        # Remove all spaces from the input string initially to simplify processing logic
        # This aligns with "Ignore any spaces in the input string"
        cleaned_str = input_str.replace(" ", "")

        result_groups = []
        current_index = 0
        length = len(cleaned_str)

        # Edge case: Empty input after cleaning
        if length == 0:
            return result_groups

        while current_index < length:
            # We expect to find an open parenthesis at current_index
            if cleaned_str[current_index] == '(':
                # Extract the group starting at current_index
                group, end_index = extract_group(cleaned_str, current_index)

                if group is not None:
                    result_groups.append(group)
                    # Move index to just after the end of this group
                    current_index = end_index + 1
                else:
                    # This indicates an error in structure (e.g., unexpected close or garbage)
                    # Given the constraints of the problem (valid input assumption usually),
                    # we break or handle error. Since we must validate:
                    raise ValueError(f"Invalid parentheses structure at index {current_index}")
            else:
                # If the string contains characters other than '(', ')', or if we expected a '(' but didn't find it
                # (though cleaning handles spaces), this is unexpected.
                if not cleaned_str[current_index].isalnum(): # Just a safety check for non-paren chars if input allows weirdness
                     # Actually, the problem implies only parens and spaces. 
                     # If there's something else, it's invalid.
                     raise ValueError(f"Unexpected character '{cleaned_str[current_index]}' in parentheses string")
                # If it's just an unknown char, treat as invalid or skip? 
                # "Input to this function is a string containing multiple groups..." implies purity.
                # Let's raise an error for non-paren content to be defensive.
                raise ValueError(f"Unexpected character '{cleaned_str[current_index]}' at index {current_index}")

            # Move to the next character
            current_index += 1

        return result_groups

    # Validation and Pre-processing
    if not isinstance(paren_string, str):
        raise TypeError("Input must be a string")

    # Process the string
    groups = process_string(paren_string)

    # Final validation: Ensure we didn't leave any dangling content that wasn't processed as a group
    # Our logic consumes the string via `current_index < length`.
    # However, `extract_group` logic consumes a full balanced group.
    # If the loop finishes and `current_index` equals `length`, we are good.
    # Wait, my loop logic `current_index += 1` at the end combined with `current_index = end_index + 1` 
    # might skip characters if `extract_group` returns correctly.
    # Let's re-verify the loop flow:
    # 1. Start at 0.
    # 2. Check char at 0. It's '('.
    # 3. Call extract_group(0). It returns group and end_index (inclusive).
    # 4. Set current_index = end_index + 1.
    # 5. Loop condition checks `current_index < length`.
    # 6. Increment `current_index` at the end of loop? 
    # Ah, in the draft above:
    #   if cleaned_str[current_index] == '(':
    #       ... extract_group ...
    #       current_index = end_index + 1  <-- Updated position
    #   else:
    #       ... error ...
    #   current_index += 1 <-- This line is WRONG if we just updated current_index to the start of the NEXT group.
    #
    # Correction: The `current_index` should be updated to point to the character AFTER the current group.
    # Then the loop continues. We do NOT increment again inside the loop block for valid groups.
    # The increment `current_index += 1` should only happen if we didn't consume a full group or at the very end?
    # Actually, the standard pattern is:
    # while current_index < length:
    #    consume group
    #    current_index = new_index
    #
    # Let's rewrite the loop structure to be crystal clear.

    groups = []
    current_index = 0
    length = len(cleaned_str)

    while current_index < length:
        # Verify the character at current_index is '('
        if cleaned_str[current_index] == '(':
            # Extract the balanced group
            extracted, end_idx = extract_group(cleaned_str, current_index)

            if extracted is None:
                # Should not happen for well-formed input starting with '('
                raise ValueError(f"Failed to extract balanced group starting at index {current_index}")

            groups.append(extracted)

            # Update current_index to the position right after the extracted group
            current_index = end_idx + 1
        else:
            # This case implies we have non-parenthesis characters or we are out of sync
            # Given the cleaning step, this should only happen if there are non-paren, non-space chars.
            # Or if the input is malformed (e.g., trailing garbage not in a group).
            # Based on "Input ... is a string containing multiple groups", we expect full coverage.
            # If we hit something else, it's invalid.
            char = cleaned_str[current_index]
            raise ValueError(f"Unexpected character '{char}' at index {current_index}. Expected start of a group.")

    return groups