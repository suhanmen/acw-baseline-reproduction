def odd_Equivalent(s: str, n: int) -> int:
    """
    Finds the count of rotations of a binary string s of length n 
    that have an odd sum (i.e., an odd number of '1's).

    Actually, looking at the assertions:
    "011001", 6 -> Total 1s is 3. Rotations:
    011001 (3), 110010 (3), 100101 (3), 001011 (3), 010110 (3), 101100 (3)
    All rotations have 3 ones. If the count is 3, it means the logic 
    might be checking if the value of the binary string (as an integer) 
    is odd.

    Let's re-check:
    "011001" (binary 13) -> Odd.
    "110010" (binary 50) -> Even.
    "100101" (binary 37) -> Odd.
    "001011" (binary 11) -> Odd.
    "010110" (binary 22) -> Even.
    "101100" (binary 44) -> Even.
    Total odd values: 3. Correct.

    "11011" (binary 27) -> Odd.
    "10111" (binary 23) -> Odd.
    "11110" (binary 30) -> Even.
    "11101" (binary 29) -> Odd.
    "11011" (binary 27) -> Odd.
    Wait, there are 5 rotations for length 5.
    "11011" -> 27 (Odd)
    "11101" -> 29 (Odd)
    "11110" -> 30 (Even)
    "11011" -> 27 (Odd)
    "01101" -> 13 (Odd)
    Total odd: 4. Correct.

    "1010" (binary 10) -> Even.
    "0101" -> 5 (Odd)
    "1010" -> 10 (Even)
    "0101" -> 5 (Odd)
    Wait, 1010 is 4 bits.
    "1010" -> 10 (Even)
    "0101" -> 5 (Odd)
    "1010" -> 10 (Even)
    "0101" -> 5 (Odd)
    Total odd: 2. Correct.
    """
    count = 0
    current_s = s
    for _ in range(n):
        # Convert binary string to integer
        val = int(current_s, 2)
        if val % 2 != 0:
            count += 1
        # Rotate left by 1
        current_s = current_s[1:] + current_s[0]
    return count