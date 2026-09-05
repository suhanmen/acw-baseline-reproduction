def _validate_input_string(input_string):
    """
    Validates that the input is a non-empty string containing only alphanumeric characters.
    Raises a ValueError if the input is invalid.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty.")

    for char in input_string:
        if not char.isalnum():
            raise ValueError("Input string must contain only alphanumeric characters.")

    return input_string


def _count_character_frequencies(input_string):
    """
    Counts the frequency of each character in the input string.
    Returns a dictionary where keys are characters and values are counts.
    """
    frequencies = {}
    for char in input_string:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


def _get_max_frequency(frequencies):
    """
    Determines the highest frequency of any single character.
    Returns the integer count of the most frequent character.
    """
    max_freq = 0
    if not frequencies:
        return 0

    for char, count in frequencies.items():
        if count > max_freq:
            max_freq = count

    return max_freq


def _get_total_length(frequencies):
    """
    Calculates the total number of characters in the string by summing frequencies.
    """
    total = 0
    for count in frequencies.values():
        total += count
    return total


def _check_feasibility(max_freq, total_length):
    """
    Checks if a valid rearrangement is possible.
    A valid rearrangement where adjacent characters differ is possible
    if and only if: max_freq <= ceil(total_length / 2).
    Mathematically: max_freq * 2 <= total_length + 1 (for odd/even handling).
    Or simply: max_freq <= (total_length + 1) // 2 using integer division.

    Returns True if feasible, False otherwise.
    """
    half_length = (total_length + 1) // 2
    return max_freq <= half_length


def _build_alternating_sequence(input_string, frequencies):
    """
    Constructs a string where no two adjacent characters are the same.
    Uses a strategy of placing the most frequent character first, then filling gaps.
    """
    # Sort characters by frequency in descending order to handle the most constrained ones first
    char_counts = [(char, count) for char, count in frequencies.items()]
    char_counts.sort(key=lambda x: x[1], reverse=True)

    # Prepare a list for the result, initialized with empty slots
    total_length = len(input_string)
    result = [''] * total_length

    # Placeholder index to keep track of where to place the next character
    current_index = 0

    # Helper to calculate the next valid position (skip current if it's the same char)
    def get_next_position(current_idx):
        """
        Calculates the next available position such that it doesn't conflict
        with the immediate predecessor in the result list.
        This ensures we skip the spot right before us if we are repeating a char.
        Actually, a simpler robust strategy for this specific problem (rearrangement)
        is to fill in steps of length (max_freq). If max_freq is k, we step by k.
        But a universal fill for 'no adjacent duplicates' is often:
        Place most frequent first, then wrap around.

        Let's use the "gap filling" or "rotation" approach which is standard:
        1. Place the most frequent character at indices 0, k, 2k... (where k is enough to separate)
        Actually, the most robust way without complex logic is:
        Sort by frequency descending.
        Place chars at indices: 0, 1, 2... then 0, 1, 2... shifted? No.

        Standard Algorithm for "Rearrange String k Distance Apart" (here k=2):
        1. Create frequency map.
        2. Sort characters by frequency descending.
        3. Create a result list of size N.
        4. Iterate through the sorted characters.
        5. For each character with count C:
           - Place it in the result list at indices: i, i + N//2? 
           No, that's for specific k.

        Let's use the constructive approach:
        We have the most frequent char. It needs ceil(N/2) spots max.
        Let's try filling the array in two passes or by step.

        Better Approach:
        1. Identify the most frequent character.
        2. If it violates the condition, we return None (feasibility check already handled).
        3. Otherwise, we can construct the string by placing the most frequent char,
           then the next, etc., but ensuring separation.

        Actually, the simplest constructive algorithm for this constraint:
        Sort characters by frequency descending.
        Place the character with highest frequency at index 0.
        Then move to the next highest frequency character.
        Continue until the end of the string is filled?
        No, that only works if frequencies are balanced.

        Correct Constructive Strategy (Bucket Sort / Interleaving):
        Since we verified feasibility, we know a solution exists.
        We can use a simple heuristic:
        Sort unique chars by frequency descending.
        Fill the result array by placing characters in a circular buffer manner?

        Let's use the specific algorithm:
        1. Sort characters by frequency descending.
        2. Create a list of (char, count) sorted.
        3. Initialize result list of empty strings.
        4. Fill the result list by iterating through the sorted chars and placing them
           starting from current_index, wrapping around modulo total_length.
           current_index is incremented by 1 after each placement.

        Why this works:
        If we fill indices 0, 1, 2... N-1 with the most frequent character first,
        then the next, etc., the most frequent character will occupy indices 0, 1, ..., count-1.
        Wait, if I place 'a' 4 times in a string of 6: 0, 1, 2, 3. Then 'b' at 4, 5.
        Result: a a a a b b -> Fails.

        Correct Logic for "No Adjacent Duplicates":
        We need to space out the most frequent character.
        The safest way is to place the most frequent character at indices:
        0, (max_freq), 2*max_freq ... ? No, spacing must be at least 2.

        Let's use the proven "gap" method:
        1. Calculate the length of the string (N).
        2. Calculate the number of slots the most frequent char (M) takes.
        3. We can place the most frequent char at indices: 0, 2, 4, ... if N is large enough?
           No, we need to ensure distance >= 2.

        Let's try the "interleave sorted list" method again carefully.
        We have counts: {'a':4, 'b':2}, N=6. Max freq 4. Feasible (4 <= 3.5? No, 4 > 3.5, so impossible).
        Wait, assertion 2: "aabb" -> 4 chars, max freq 2. 2 <= 2. OK.
        Result: abab.

        Let's try "abccdd": N=6. Counts: a:1, b:1, c:2, d:2. Max freq 2. 2 <= 3. OK.

        Algorithm:
        1. Sort characters by frequency descending.
        2. Create a result list of size N.
        3. We will fill the result list by taking characters from our sorted list and placing them
           at indices 0, 1, 2... then wrapping?
           Let's try the "step = ceil(N / max_freq)"? No.

        Robust Algorithm (verified in similar problems):
        1. Sort chars by freq descending.
        2. Flatten the chars into a single list where each char appears 'count' times.
           e.g., "abccdd" -> ['a', 'b', 'c', 'c', 'd', 'd'] (already sorted by freq).
        3. We have a list L of length N.
        4. We want to rearrange L such that L[i] != L[i+1].
        5. Since we already checked feasibility, we can simply rotate the most frequent elements?

        Actually, the most straightforward construction when feasibility is guaranteed:
        Place the characters in the order of their frequency, but distribute them evenly.
        We can simulate placing them at indices:
        idx = 0
        for char, count in sorted_chars:
            for _ in range(count):
                result[idx] = char
                idx = (idx + 1) % total_length?
                If we do (idx + 1) % N, we are just rotating the list.
                Does rotation guarantee no adjacent duplicates?
                Only if the most frequent element doesn't exceed ceil(N/2).
                Proof: If max_freq <= (N+1)/2, then in a circular arrangement, no two instances of the same char are adjacent.
                In a linear arrangement, the wrap-around (last and first) might conflict.
                However, if max_freq <= (N+1)/2, the linear arrangement obtained by rotating the list
                such that the max_freq element is not at the end (if N is odd) or handling the wrap carefully works.

        Let's try the rotation method:
        1. Create list L of characters sorted by frequency descending.
        2. Create result array R of size N.
        3. Place L into R such that R[i] = L[i].
        4. Now check if R[i] == R[i+1]. If so, shift?

        Actually, there is a deterministic construction:
        1. Sort chars by frequency descending.
        2. Construct a list L of all characters in that order.
        3. The length of L is N.
        4. We know max_freq <= (N+1)//2.
        5. We can place these characters at indices:
           0, 2, 4, ... ? No, that assumes we only have one type.

        Let's use the specific strategy for this problem:
        "Place the most frequent character, skip one, place next, skip one..."
        No, that requires knowing the counts beforehand.

        Re-evaluating the "Rotation" strategy:
        If we arrange the characters as: [Most Freq 1], [Others], [Most Freq 2], [Most Freq 3]...
        Then rotate the whole list so that the two ends don't clash?

        Correct Construction Strategy (Standard Solution for "Rearrange String k Distance Apart" where k=2):
        1. Count frequencies.
        2. Sort characters by frequency descending.
        3. Create a list of characters: [char1, char1, ..., char2, char2, ...] where counts are preserved.
        4. We need to insert these into a result buffer of size N.
        5. We fill the buffer at indices: 0, 1, 2, ..., N-1.
        6. BUT, we don't place them sequentially 0,1,2. We place them with a stride.
           Stride = max_freq? No.

        Let's go with the "Two Pointers" or "Gap" filling which is explicit and safe:
        Since we have the counts, we can determine the position of the most frequent char.
        Let's assume we put the most frequent char at 0, 2, 4, ... as much as possible?
        No, if we have 'a':4, 'b':2, N=6. 'a' needs 4 slots. 0, 2, 4... only gives 3 slots (0,2,4).
        So 'a' must take 0, 2, 4, and ONE of the odd slots? No, then it touches.

        Wait, my feasibility check was: max_freq <= (N+1)//2.
        For N=6, (6+1)//2 = 3. So max_freq can be at most 3.
        If input is "aaaabbc" (N=7), max_freq=4. 4 <= (7+1)//2 = 4. OK.
        Slots for 'a': 4.
        Indices: 0, 2, 4, 6. (Step 2).
        Remaining indices: 1, 3, 5.
        Fill remaining with others: b, b, c.
        Result: a b a b a c a. (Adjacent: a-b, b-a, a-b, b-a, a-c, c-a). Valid.

        Algorithm Refined:
        1. Identify the character with the maximum frequency. Call it 'major'.
        2. If there is a tie, pick any (doesn't matter for validity).
        3. Place 'major' at indices: 0, 2, 4, 6, ... until count of 'major' is exhausted OR we hit the limit.
           How many slots can 'major' take in a linear array with step 2?
           Max slots = (