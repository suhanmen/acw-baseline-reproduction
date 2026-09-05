def find_Parity(num):
    # Input Validation
    if not isinstance(num, (int, float)):
        raise ValueError("Invalid input: num must be an integer or float")

    if not isinstance(num, int) and not isinstance(num, float):
        raise ValueError("Invalid input: num must be an integer or float")

    if not (-1000000 <= num <= 1000000):
        raise ValueError("Invalid input: num out of range")

    # Check if the number is an integer
    if isinstance(num, float) and not num.is_integer():
        raise ValueError("Invalid input: num is not an integer")

    # Ensure num is an integer
    num = int(num)

    # Determine Parity
    if num % 2 == 0:
        return "Even Parity"
    else:
        return "Odd Parity"

# Example usage:
# print(find_Parity(12))   # Output: "Even Parity"
# print(find_Parity(7))    # Output: "Odd Parity"
# print(find_Parity(10))   # Output: "Even Parity"