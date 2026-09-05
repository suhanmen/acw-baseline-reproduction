def find_demlo(number_str):
    # Validate the input
    if not isinstance(number_str, str) or not number_str.isdigit():
        raise ValueError("Invalid input: must be a string of digits.")

    n = len(number_str)
    if n == 0 or n < 2:
        raise ValueError("Invalid input: number must have at least two digits.")

    # Check for descending order
    for i in range(n-1):
        if number_str[i] < number_str[i+1]:
            raise ValueError("Invalid input: digits must be in strictly descending order.")

    # Check for leading zero
    if number_str[0] == '0':
        raise ValueError("Invalid input: number cannot start with zero.")

    # Check for all equal digits
    if all(c == number_str[0] for c in number_str):
        raise ValueError("Invalid input: all digits must be in strictly descending order.")

    # Compute the demlo number parts
    increasing = []
    for i in range(n):
        increasing.append(str(int(number_str[0]) + i))

    max_digit = int(number_str[0]) + n
    decreasing = []
    decreasing.append(str(max_digit))

    # Add the decreasing part
    for i in range(n-1, -1, -1):
        if i == 0:
            decreasing.append(str(int(number_str[0]) - i))
        else:
            next_digit = int(decreasing[-1]) - 1
            if next_digit < int(number_str[0]):
                decreasing.append(str(next_digit))
            else:
                break

    # Combine all parts
    result = increasing + decreasing

    # Remove duplicates in the decreasing part except for the first occurrence
    final = []
    seen = set()
    for num in result:
        if num not in seen:
            seen.add(num)
            final.append(num)

    return ''.join(final)