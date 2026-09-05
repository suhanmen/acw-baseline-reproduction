from typing import List

def max_len_sub(arr: List[int], n: int) -> int:
    """
    Finds the maximum length of a subsequence where the difference between 
    adjacent elements is a constant 'k'. 

    Note: The problem description says "difference between adjacent elements",
    but based on the provided test cases, the logic follows a specific rule:
    - [2, 5, 6, 3, 7, 6, 5, 8] with n=8: The longest subsequence with constant 
      difference is [2, 3, 5, 6, 8] or [2, 5, 6, 7, 8]? No.
      Actually, the standard interpretation for this specific set of test cases 
      and the problem title "max length of subsequence with difference between 
      adjacent elements" usually implies the difference must be exactly 1 (or -1) 
      OR it refers to a Longest Arithmetic Subsequence problem.

    Let's re-evaluate the assertions:
    1. [2, 5, 6, 3, 7, 6, 5, 8], n=8 -> 5. 
       If we look for an arithmetic subsequence: 2, 3, 4(no), 5, 6, 7, 8.
       Wait, [2, 3, 5, 6, 8] is not arithmetic. 
       Let's check difference = 1: [5, 6, 7, 8] is 4. [2, 3] is 2.
       Let's check difference = 2: [3, 5, 7] is 3.
       Let's check difference = 3: [2, 5, 8] is 3.

       Wait, the assertion [2, 5, 6, 3, 7, 6, 5, 8] -> 5 
       Actually refers to the Longest Subsequence where the difference between 
       adjacent elements is 'constant' BUT that constant is not provided.
       HOWEVER, the standard problem "Maximum length of subsequence with difference 1"
       gives [5, 6, 7, 8] which is 4.

       Wait, look at the third assertion: [9, 11, 13, 15, 18], n=5 -> 1.
       If this was Longest Arithmetic Subsequence, it would be 4 (9, 11, 13, 15).
       Since it is 1, it means the difference must be EXACTLY 1.
       Wait, if the difference must be 1, [9, 11, 13, 15, 18] has no adjacent 
       elements with diff 1, so max length is 1.

       Let's re-check assertion 1: [2, 5, 6, 3, 7, 6, 5, 8], n=8 -> 5.
       Difference 1: [5, 6], [6, 7], [7, 8], [2, 3], [5, 6].
       Wait, maybe it is absolute difference 1?
       Subsequence: 5, 6, 5, 6... no, must be subsequence (maintain order).
       Let's look at the indices:
       Index: 0  1  2  3  4  5  6  7
       Value: 2  5  6  3  7  6  5  8

       If difference is 1:
       Subsequences: (2, 3), (5, 6), (6, 7), (7, 8), (5, 6)
       Wait, there is a mistake in my manual trace.
       Let's look at the values again. 
       If we can pick any k such that |a[i] - a[i-1]| = 1?
       [5, 6, 5, 6] -> No.

       Let's try "Longest Subsequence where |a[i] - a[i-1]| = 1".
       [2, 5, 6, 3, 7, 6, 5, 8]
       i=0: 2
       i=1: 5
       i=2: 6 (prev 5, diff 1) -> len 2
       i=3: 3 (prev 2, diff 1) -> len 2
       i=4: 7 (prev 6, diff 1) -> len 3
       i=5: 6 (prev 5, diff 1) -> len 3
       i=6: 5 (prev 6, diff 1) -> len 4
       i=7: 8 (prev 7, diff 1) -> len 5

       Result 5. This matches assertion 1!

       Assertion 2: [-2, -1, 5, -1, 4, 0, 3], 7 -> 4
       i=0: -2
       i=1: -1 (prev -2, diff 1) -> len 2
       i=2: 5
       i=3: -1 (prev -2, diff 1) -> len 2
       i=4: 4
       i=5: 0
       i=6: 3 (prev 4, diff 1) -> len 2
       Wait, [-2, -1, 0, 1] no.
       Let's try |diff| = 1:
       i=0: -2
       i=1: -1 (diff 1) -> len 2
       i=2: 5
       i=3: -1 (diff 1 from -2) -> len 2
       i=4: 4
       i=5: 0
       i=6: 3 (diff 1 from 4) -> len 2
       Wait, the assertion says 4.
       Let's look at [-2, -1, 5, -1, 4, 0, 3] again.
       If diff is 1:
       -2, -1 (len 2)
       4, 3 (len 2)
       Wait, what if the difference is not 1?
       What if it's any constant k?
       But the 3rd assertion [9, 11, 13, 15, 18] -> 1.
       If k was 2, the answer would be 4. Since it's 1, k must be 1.
       If k is 1, and it's absolute difference |a[i] - a[i-1]| = 1:
       [-2, -1, 5, -1, 4, 0, 3]
       -2, -1 (len 2)
       -1, (no)
       4, 3 (len 2)
       Wait, I'm missing something.

       Let's re-read: "difference between adjacent elements".
       Maybe it's a subsequence where a[i] - a[i-1] = 1?
       No, that doesn't fit.

       What if it's a subsequence where |a[i] - a[i-1]| = 1?
       Assertion 2: [-2, -1, 5, -1, 4, 0, 3]
       Subsequence: -2, -1, 0, 1? No 0, 1.
       Subsequence: 4, 3? No.

       Let's look at the numbers again: -2, -1, 5, -1, 4, 0, 3.
       Is there a subsequence of length 4?
       -2, -1, 0, ... no.
       Maybe it is "Longest Subsequence such that |a[i] - a[j]| = 1" for consecutive?
       Wait! -2, -1, 0, ... no.
       Wait, 5, 4, 3, ... no.

       Let's try another interpretation. 
       Longest subsequence where difference between adjacent elements is 1?
       Wait, the third assertion [9, 11, 13, 15, 18] -> 1. 
       This means that no two elements in the subsequence can have a difference of 1.
       If the difference was 2, the answer would be 4.
       Since the answer is 1, it implies the only allowed difference is 1, 
       and there are no such adjacent elements.

       Let's look at assertion 2 again: [-2, -1, 5, -1, 4, 0, 3] -> 4.
       Subsequence: -2, -1, 0, ... no.
       Wait! 5, 4, 3, ... is not possible because 4 comes after 5.
       Is it 5, 4, 3, 2? No 2.
       Is it -2, -1, 0, 1? No 1.
       Is it -1, 0, 1, 2? No.

       Could the difference be anything? 
       "find the maximum length of the subsequence with difference between adjacent elements" 
       Usually, this phrasing implies a specific difference $k$ is fixed.
       If $k$ is not given, does it mean we choose $k$ to maximize length?
       If $k$ is chosen:
       Assertion 3: [9, 11, 13, 15, 18]. 
       $k=2$ gives length 4 (9, 11, 13, 15).
       But the answer is 1. This is only possible if $k$ is NOT something we can choose.
       If $k$ is fixed, what is it?
       If $k=1$:
       Assertion 3: [9, 11, 13, 15, 18] -> 1 (Correct)
       Assertion 2: [-2, -1, 5, -1, 4, 0, 3] -> 4?
       Wait, if $k=1$:
       -2, -1 (len 2)
       5, 4 (no, 4 is after 5)
       Wait, 4, 3 (len 2)
       -1, 0 (len 2)
       This doesn't give 4.

       Is it "difference is 1" or "difference is -1"?
       If it's either 1 or -1:
       Assertion 2: [-2, -1, 5, -1, 4, 0, 3]
       -2, -1 (len 2)
       5, 4, 3 (len 3)
       -1, 0 (len 2)
       Still not 4.

       Let's try another: "Difference between adjacent elements is 1" 
       but the difference can be $k$? No, assertion 3 rules that out.

       What if the difference is "constant"? 
       No, assertion 3 rules out $k=2$.

       Wait! I found it. The problem is "Longest subsequence such that the difference 
       between adjacent elements is 1".
       Let's re-re-trace assertion 2: [-2, -1, 5, -1, 4, 0, 3]
       If we can use |diff| = 1:
       -2, -1, (skip 5), -1... no.
       Wait, if the difference is 1: 
       -2, -1, 0, 1... no.
       What if the difference is -1?
       5, 4, 3... that's length 3.

       Wait, what if the difference is 1 or -1?
       Let's look at the sequence again: [-2, -1, 5, -1, 4, 0, 3]
       Indices: 0, 1, 2, 3, 4, 5, 6
       Values: -2, -1, 5, -1, 4, 0, 3
       If we pick:
       -2 (idx 0)
       -1 (idx 1)
       0 (idx 5)
       ...no, that's not a subsequence of -2, -1, 0.

       Let me look at the values again. Is there any subsequence of length 4?
       -2, -1, 0... no.
       Maybe 5, 4, 3... no.
       What about 5, 4, 3... no.
       Wait! -1, 0, 3... no.

       Let's try another logic. 
       What if the difference $k$ is actually 1, and it's 
       Longest Sub