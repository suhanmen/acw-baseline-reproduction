from typing import List, Tuple

def extract_missing(ranges: List[Tuple[int, int]], start_range: int, end_range: int) -> List[Tuple[int, int]]:
    """
    Extracts the missing ranges from a given list of ranges, considering a 
    global start and end range. 

    The logic interprets a range (a, b) as covering the interval between 
    min(a, b) and max(a, b). For every range in the input list, the function
    identifies the gaps between the global start/end and the boundaries of 
    the provided ranges.

    Specifically, for a range (a, b):
    1. It identifies the interval [min(a, b), max(a, b)].
    2. It checks the gap between the global start and the lower bound.
    3. It checks the gap between the upper bound and the global end.
    4. It identifies the gap between the lower bound and the upper bound 
       (effectively the "internal" missing part if the input range is 
       interpreted as a point or if boundaries are inverted).

    Based on the provided test cases:
    - If an input range is (x, y), the function generates:
        - (start_range, min(x, y))
        - (max(x, y), end_range)
        - (min(x, y), max(x, y)) if we treat the range as a "hole" or a "boundary".

    Wait, looking closer at the test cases:
    Case 1: ranges=[(6, 9), (15, 34), (48, 70)], start=2, end=100
    Outputs: (2, 6), (9, 100), (9, 15), (34, 100), (34, 48), (70, 100)

    Analysis of Case 1:
    For (6, 9): output (2, 6) and (9, 100).
    For (15, 34): output (9, 15) and (34, 100).
    For (48, 70): output (34, 48) and (70, 100).
    Wait, that's not quite it. Let's re-examine.

    Case 1 Details:
    Range 1 (6, 9): (2, 6), (9, 100)
    Range 2 (15, 34): (9, 15), (34, 100)
    Range 3 (48, 70): (34, 48), (70, 100)

    Actually, the pattern is:
    For each range (r1, r2) in the list:
    Let lower = min(r1, r2)
    Let upper = max(r1, r2)
    The outputs associated with this range are:
    1. (previous_upper, lower) -- where previous_upper is the max(r1, r2) of the 
       previous range in the list, or the start_range if it's the first.
    2. (upper, end_range)

    Let's check Case 2: ranges=[(7, 2), (15, 19), (38, 50)], start=5, end=60
    Range 1 (7, 2): lower=2, upper=7. Outputs: (5, 7), (2, 60)
    Range 2 (15, 19): lower=15, upper=19. Outputs: (2, 15), (19, 60)
    Range 3 (38, 50): lower=38, upper=50. Outputs: (19, 38), (50, 60)

    Logic found:
    For each range (r1, r2) in the list:
    - Get lower = min(r1, r2)
    - Get upper = max(r1, r2)
    - If it's the first range in the list:
        - Result 1: (start_range, upper)
        - Result 2: (lower, end_range)
    - If it's NOT the first range:
        - Let prev_upper = max of the previous range.
        - Result 1: (prev_upper, lower)
        - Result 2: (upper, end_range)

    Wait, Case 1 again:
    (6, 9): lower=6, upper=9. prev_upper=2.
    Outputs: (2, 6), (9, 100)
    (15, 34): lower=15, upper=34. prev_upper=9.
    Outputs: (9, 15), (34, 100)
    (48, 70): lower=48, upper=70. prev_upper=34.
    Outputs: (34, 48), (70, 100)

    This matches perfectly!

    Check Case 2 again:
    (7, 2): lower=2, upper=7. prev_upper=5.
    Outputs: (5, 7), (2, 60)
    (15, 19): lower=15, upper=19. prev_upper=7.
    Wait, the output says (2, 15). Ah, the prev_upper is the 'lower' of the previous range?
    Let's re-evaluate Case 2:
    Input: [(7, 2), (15, 19), (38, 50)], start=5, end=60
    1. (7, 2) -> lower=2, upper=7. prev_upper=5.
       Output: (5, 7), (2, 60)
    2. (15, 19) -> lower=15, upper=19. prev_upper=2 (the lower of the first range).
       Output: (2, 15), (19, 60)
    3. (38, 50) -> lower=38, upper=50. prev_upper=19 (the upper of the second range).
       Output: (19, 38), (50, 60)

    Actually, let's look at the output pairs:
    Case 1: (2,6), (9,100), (9,15), (34,100), (34,48), (70,100)
    Case 2: (5,7), (2,60), (2,15), (19,60), (19,38), (50,60)

    Correct Logic Extraction:
    For each range (r1, r2) at index i:
    1. lower = min(r1, r2)
    2. upper = max(r1, r2)
    3. If i == 0:
       - Part A: (start_range, upper)
       - Part B: (lower, end_range)
    4. If i > 0:
       - Let prev_lower = min(ranges[i-1][0], ranges[i-1][1])
       - Let prev_upper = max(ranges[i-1][0], ranges[i-1][1])
       - Part A: (prev_lower, lower)
       - Part B: (prev_upper, end_range)
       Wait, no. Let's look at Case 1 again.
       i=0: (2, 6), (9, 100) -> (start, upper), (lower, end) ? No, (2,6) is (start, lower).

       Let's try this:
       For each range (r1, r2):
       lower = min(r1, r2)
       upper = max(r1, r2)
       If i == 0:
           append (start_range, lower)
           append (upper, end_range)
           # But wait, Case 1 i=0 is (2, 6) and (9, 100). 
           # (2, 6) is (start_range, lower)
           # (9, 100) is (upper, end_range)
           # Wait, why is (9, 15) there?

       Let's look at the list of results as a sequence:
       Case 1: [(2, 6), (9, 100), (9, 15), (34, 100), (34, 48), (70, 100)]
       This is:
       1. (start_range, lower_0)
       2. (upper_0, end_range)
       3. (upper_0, lower_1)
       4. (upper_1, end_range)
       5. (upper_1, lower_2)
       6. (upper_2, end_range)

       Let's test this logic on Case 2:
       ranges=[(7, 2), (15, 19), (38, 50)], start=5, end=60
       i=0: lower=2, upper=7.
           (start_range, lower_0) = (5, 2) -> Wait, the output is (5, 7).
           Something is wrong. Let's re-re-examine.

       Case 2 Output: (5, 7), (2, 60), (2, 15), (19, 60), (19, 38), (50, 60)
       i=0: (7, 2) -> lower=2, upper=7.
           (start_range, upper_0) = (5, 7)
           (lower_0, end_range) = (2, 60)
       i=1: (15, 19) -> lower=15, upper=19.
           (lower_0, lower_1) = (2, 15)
           (upper_1, end_range) = (19, 60)
       i=2: (38, 50) -> lower=38, upper=50.
           (upper_1, lower_2) = (19, 38)
           (upper_2, end_range) = (50, 60)

       Let's check Case 1 with this logic:
       ranges=[(6, 9), (15, 34), (48, 70)], start=2, end=100
       i=0: (6, 9) -> lower=6, upper=9.
           (start_range, upper_0) = (2, 9) -> Wait, Case 1 first element is (2, 6).

       Okay, the logic is actually simpler and I was overcomplicating. 
       Look at Case 1:
       (2, 6), (9, 100), (9, 15), (34, 100), (34, 48), (70, 100)
       The first number of each pair is the "end" of the previous range's "lower" or "upper".

       Let's try again.
       Case 1:
       r0=(6,9), r1=(15,34), r2=(48,70). start=2, end=100.
       Output: (2, 6), (9, 100), (9, 15), (34, 100), (34, 48), (70, 100)
       Pair 1: (start_range, lower_0)
       Pair 2: (upper_0, end_range)
       Pair 3: (upper_0, lower_1)
       Pair 4: (upper_1, end_range)
       Pair 5: (upper_1, lower_2)
       Pair 6: (upper_2, end_range)

       Now check Case 2:
       r0=(7,2), r1=(15,19), r2=(38,50). start=5, end=60.
       lower_0=2, upper_0=7
       lower_1=15, upper_1=19
       lower_2=38, upper_2=50
       Pair 1: (start_range, upper_0) = (5, 7)  <-- Matches!
       Pair 2: (lower_0, end_range) =