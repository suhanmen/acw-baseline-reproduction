def get_Position(arr, n, k):
    """
    Finds the position of the k-th element removed from the beginning 
    of the array when elements are removed sequentially (Josephus-like logic 
    applied to position tracking). 
    Based on the provided test cases:
    - [2,5,4], 3, 2 -> 2 (The 2nd removed element is at index 2 in a 1-based count)
    - [4,3], 2, 2 -> 2 (The 2nd removed element is at index 2)
    - [1,2,3,4], 4, 1 -> 4 (The 1st removed element is at index 4)

    Actually, looking at the assertions:
    1. [2,5,4], n=3, k=2. Elements are 2,5,4. Removing k-th from index 0? 
       No, the pattern suggests the result is the k-th position of the array 
       if we consider the list as 1-indexed.
       Wait, let's re-examine:
       assert get_Position([2,5,4],3,2) == 2
       assert get_Position([4,3],2,2) == 2
       assert get_Position([1,2,3,4],4,1) == 4

       In [1,2,3,4], k=1 returns 4. This implies the "last removed" logic 
       might be a Josephus-style problem or a specific sequence.
       Let's trace:
       [2,5,4], n=3, k=2. If we remove 1st element, then 2nd...
       If we remove elements using (i + k - 1) % current_length:
       Ex 3: [1,2,3,4], n=4, k=1. 
       Pos 1: (0 + 1 - 1) % 4 = 0. Element 1 removed. List [2,3,4].
       Next: (0 + 1 - 1) % 3 = 0. Element 2 removed. List [3,4].
       Next: (0 + 1 - 1) % 2 = 0. Element 3 removed. List [4].
       Next: (0 + 1 - 1) % 1 = 0. Element 4 removed.
       The "last removed" is the 4th element (value 4). Position is 4.

       Ex 1: [2,5,4], n=3, k=2.
       Pos 1: (0 + 2 - 1) % 3 = 1. Element 5 removed. List [2,4].
       Pos 2: (1 + 2 - 1) % 2 = 0. Element 2 removed. List [4].
       Pos 3: (0 + 2 - 1) % 1 = 0. Element 4 removed.
       The "k-th removed" element. In Ex 1, k=2. The 2nd removed was '2'.
       Wait, if the position is 1-based index in the original array:
       [2,5,4] -> 2 is index 1, 5 is index 2, 4 is index 3.
       If 2 was removed 2nd, and its original index was 1? No, result is 2.

       Let's try standard Josephus for the index of the last element remaining:
       f(n, k) = (f(n-1, k) + k) % n
       f(1, k) = 0
       For n=3, k=2:
       f(1, 2) = 0
       f(2, 2) = (0 + 2) % 2 = 0
       f(3, 2) = (0 + 2) % 3 = 2. (0-indexed, so 3rd position? No, 2 is 3rd pos).

       Let's try f(n, k) where f(n, k) is the 1-based position of the last element:
       g(n, k) = (g(n-1, k) + k - 1) % n + 1
       g(1, k) = 1
       Ex 1: n=3, k=2. g(1,2)=1. g(2,2)=(1+2-1)%2 + 1 = 1. g(3,2)=(1+2-1)%3 + 1 = 3.
       Ex 2: n=2, k=2. g(1,2)=1. g(2,2)=(1+2-1)%2 + 1 = 1.

       Wait, the problem says "last removed element". In Josephus, the last one removed is 
       the last one remaining. 
       Let's check the assertions again.
       get_Position([2,5,4], 3, 2) == 2
       get_Position([4,3], 2, 2) == 2
       get_Position([1,2,3,4], 4, 1) == 4

       If the question is simply the k-th element in the array (1-indexed):
       [2,5,4], k=2 -> 5 (index 2). Assertion says 2.
       [4,3], k=2 -> 3 (index 2). Assertion says 2.
       [1,2,3,4], k=1 -> 1 (index 1). Assertion says 4.

       Alternative: The k-th element removed in a Josephus sequence of n people.
       In Josephus(n, k), the order of removal is:
       n=3, k=2: [2,5,4] -> 5 removed (pos 2), then 2 removed (pos 1), then 4 removed (pos 3).
       2nd removed is 2. Position of 2 in original array is 1. Assertion says 2.

       Wait! Let's look at the values.
       [2,5,4], n=3, k=2. The result is 2. The value 2 is at index 0.
       [4,3], n=2, k=2. The result is 2.
       [1,2,3,4], n=4, k=1. The result is 4.

       Is it possible the function is:
       pos = (f(n, k) + k - 1) % n? No.

       Let's try Josephus calculation again.
       n=3, k=2: 
       1. (0+2-1)%3 = 1. Removed index 1.
       2. (1+2-1)%2 = 0. Removed index 0.
       3. (0+2-1)%1 = 0. Removed index 0.
       The removals were at original indices: 1, 0, 2.
       The k=2nd removed index was 0. 1-indexed is 1. Assertion says 2.

       Wait, what if the position is the value at that index?
       Ex 1: [2,5,4], n=3, k=2. Removals: 5, 2, 4. k=2 is value 2.
       Ex 2: [4,3], n=2, k=2. Removals: 4, 3. k=2 is value 3. Assertion says 2.

       Let's try another: Josephus position formula f(n, k) = (f(n-1, k) + k) % n.
       f(1, k) = 0
       f(2, 2) = (0+2)%2 = 0
       f(3, 2) = (0+2)%3 = 2
       f(4, 1) = (f(3,1)+1)%4. f(1,1)=0, f(2,1)=0, f(3,1)=0, f(4,1)=0.

       Let's look at the assertions one more time.
       [2,5,4], 3, 2 -> 2
       [4,3], 2, 2 -> 2
       [1,2,3,4], 4, 1 -> 4

       If the answer is simply: (k + n - 1) % n + 1 if we adjust for some logic?
       For [2,5,4], 3, 2: (2 + 3 - 1) % 3 + 1 = 1 + 1 = 2.
       For [4,3], 2, 2: (2 + 2 - 1) % 2 + 1 = 1 + 1 = 2.
       For [1,2,3,4], 4, 1: (1 + 4 - 1) % 4 + 1 = 0 + 1 = 1. (Assertion is 4).

       What if it's (n - k + 1)?
       Ex 1: 3 - 2 + 1 = 2.
       Ex 2: 2 - 2 + 1 = 1. (Assertion is 2).

       What if it's the k-th element from the end?
       Ex 1: [2,5,4], 3, 2 -> 2nd from end is 5.
       Ex 3: [1,2,3,4], 4, 1 -> 1st from end is 4. (Matches!)
       Ex 2: [4,3], 2, 2 -> 2nd from end is 4. (Assertion is 2).

       Wait, look at the inputs again:
       get_Position([2,5,4],3,2) == 2
       get_Position([4,3],2,2) == 2
       get_Position([1,2,3,4],4,1) == 4

       In all cases, the result is k if we treat the array as a sequence where we remove 
       the last element n-k+1 times? No.

       Let's try: the position is (n - k + 1) mod n + 1?
       Ex 1: (3 - 2 + 1) % 3 + 1 = 2 + 1 = 3. No.

       Let's try: f(n, k) where f(n, k) is the Josephus result.
       f(3, 2) = 2. (0-indexed). 1-indexed is 3.
       f(2, 2) = 0. (0-indexed). 1-indexed is 1.
       f(4, 1) = 0. (0-indexed). 1-indexed is 1.

       Is there a pattern in the results 2, 2, 4?
       They are exactly the values of k for the first two, and n for the last one? No.

       Wait! 
       [2,5,4], 3, 2 -> k is 2. Result is 2.
       [4,3], 2, 2 -> k is 2. Result is 2.
       [1,2,3,4], 4, 1 -> k is 1. Result is 4.

       Is it (n - k + 1) if k=1? No.

       Let's try Josephus again but removing from the end?
       Or maybe the formula is: (k + n - 2) % (n - 1) + 1? No.

       Wait! Josephus with k=2:
       n=3: 2, 1, 3 (Last is 3)
       n=2: 2, 1 (Last is 1)

       Let's try the Josephus problem: "Find the position of the k-th element removed."
       If we remove elements one by one:
       Ex 3: [1,2,3,4], n=4, k=1.
       If k=1 means we skip 1 and remove the next?
       Remove at index (k-1)%n:
       1. (1-1)%4 = 0. Remove element at index 0 (value 1). List: [2,3,4]
       2. (1-1)%3 = 0. Remove element at index 0 (value 2). List: [3,4]
       3. (1-1)%2 = 0. Remove element at index 0 (value 3). List: [4]
       4. (1-1)%1 = 0. Remove element at index 0 (value 4).
       The "last removed" is value 4. Its position in the original array was 4.
       Matches