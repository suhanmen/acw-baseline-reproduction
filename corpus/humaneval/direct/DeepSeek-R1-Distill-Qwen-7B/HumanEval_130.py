def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n == 0:
        return [1]

    # Initialize the sequence with the first two values
    sequence = [1, 3]  # tri(0)=1, tri(1)=3

    for current_n in range(2, n + 1):
        if current_n % 2 == 0:
            next_val = 1 + current_n / 2
        else:
            # For odd current_n, we need tri(current_n + 1)
            # Since current_n is odd, current_n +1 is even, which we can compute directly
            next_val = sequence[current_n - 1] + sequence[current_n - 2] + sequence[current_n]
            # Append the computed value to the sequence
            sequence.append(next_val)

    # Generate the required sequence up to n, but ensure we return first n+1 elements
    # However, for n >=2, the initial list has 2 elements (indices 0 and 1), so for n=3 we need up to index 3 (4 elements)
    # So, we might need to compute up to current_n = n, but for n >=1
    # Wait, wait, initial sequence is [1,3], which is for n=0 and n=1.
    # So for n >=2, we need to compute from 2 up to n.
    # Hence, the for loop from 2 to n (inclusive) correctly builds the sequence.
    # However, the initial list already has 2 elements for n=0 and n=1.
    # Therefore, if n=3, the for loop runs for current_n =2, 3: which are 2 iterations, and appends 2 elements, making the list have 4 elements (indices 0-3), which is correct for n=3.
    # So when n=3, the function returns sequence[:n+1]?
    # Wait, no, the for loop from 2 to n would compute for each current_n and append, starting with current_n=2, then 3 up to n.
    # Let's see for n=3:
    # Initial sequence is [1,3]
    # current_n=2: even, so next_val=1 + 2/2=2. Append. sequence becomes [1,3,2]
    # current_n=3: odd. next_val = sequence[2] + sequence[1] + sequence[3], but sequence[3] is not yet computed.
    # Wait no: in the else clause, current_n is 3. So the code is sequence[current_n-1] is 2 (since current_n is 3, index is 2), sequence[current_n-2] is index 1 (3), and sequence[current_n] is index 3 which hasn't been computed yet. That's a problem.

Wait, I made a mistake in the iterative approach. The initial code I thought of may have a bug. Specifically, when computing for an odd current_n, we need to access tri(current_n +1), which hasn't been computed yet. That's a problem because the current_n is the term we're trying to compute.

So, the initial approach of building the sequence step by step and using sequence[current_n] which is not yet computed is incorrect. We need to adjust the computation to use already computed terms.

Wait, but how else can we compute tri(current_n) when it depends on tri(current_n + 1)? That creates a dependency that can't be resolved in a straightforward iterative manner. So, perhaps the initial approach isn't correct.

Wait, let's re-examine the recurrence:

For even n: tri(n) = 1 + n/2. This is a direct formula and easy to compute.

For odd n: tri(n) = tri(n-1) + tri(n-2) + tri(n+1)

But wait, tri(n) depends on tri(n+1), which is a future term. That makes it impossible to compute in a straightforward left-to-right manner.

This suggests that the recurrence is not suitable for an iterative approach unless we can find a way to compute terms without needing future values. But for n >=2, computing in order is impossible because odd n depends on n+1, which isn't yet computed.

Therefore, this recurrence relation is similar to some kind of non-linear recurrence which may not be straightforward to compute iteratively.

Wait, let me see the examples:

For n=2 (even), tri(2) = 1 + 2/2 = 2.

For n=3 (odd), tri(3) = tri(2) + tri(1) + tri(4). But tri(4) is even, so tri(4) is 1 +4/2=3. So tri(3)=2+3+3=8.

Wait, but in this case, we needed to compute tri(4) before computing tri(3). So if we compute in increasing order, we'll hit an issue because tri(3) requires tri(4), which we haven't computed yet.

This suggests that the recurrence cannot be computed in a simple iterative way because for odd n, tri(n) requires a term with higher n.

So, to compute up to a certain n, we would need to compute beyond that n, which complicates things.

An alternative approach could be to precompute up to a certain point, then use memoization to retrieve the required terms when needed.

But for the purpose of this problem, let's see what n is given.

Given that n can be up to any non-negative integer, and for the function to return the first n+1 terms, for n up to say 4:

n=4: sequence is [1,3,2,8,3] as per example.

But how was tri(4) computed? tri(4) is 3, which is based on tri(3)=8, which was computed as 2+3+3. But wait, the examples say:

tri(4)=3, which is consistent with the formula for even n: 1 +4/2 = 3.

So, for n=4, it's an even number, so directly computable as 3.

Wait, for n=3, which is odd, the tri(3) depends on tri(4), which is the next even number, but can we precompute tri(4) before tri(3)?

Yes, because when n is 3, which is odd, the tri(3) uses tri(4), which is even. So, if we compute all even terms first, then the odd terms can be computed.

But this seems complicated.

Alternative approach:

We can realize that for any n >= 2, whether even or odd, to compute tri(n), we may need to compute tri(n+1) if it's odd. So perhaps we should compute all terms up to n+1, then compute the lower terms.

But this requires computing up to n+1 first, then going back to compute the previous terms. Which may be computationally expensive for large n.

Given the problem constraints, and considering that the function must return the first n+1 terms, perhaps a better approach is to precompute all terms up to the maximum required n, which is given as input, but since the terms can depend on higher terms, this is challenging.

An alternative is to compute all terms using memoization, storing computed values to avoid redundant calculations. This way, even if we have to compute higher terms, we can retrieve them quickly when needed.

Implementing memoization in Python can be done using a dictionary to store computed tri(n) values.

Here's a revised approach:

1. Use a dictionary to memoize computed values.
2. Base case: memo[1] =3.
3. For n=0, return 1.
4. For even n, compute as 1 +n/2.
5. For odd n, compute as memo[n-1] + memo[n-2] + memo[n+1].
6. To compute memo[n], we may need to compute memo[n+1] first, which may require further computation.

But this leads to a problem where to compute memo[n], we might need to compute memo[n+1], which may require memo[n+2], and so on. This could create an infinite loop or require memoizing all possible n, which is not feasible.

Given this, perhaps an iterative approach isn't suitable for this recurrence relation due to dependencies on future terms for some cases.

So, instead, let's rethink the problem and try to find a way to compute the sequence in a forward manner, possibly by computing higher terms first before computing lower terms when needed.

Alternatively, perhaps we can separate the sequence into even and odd indexed terms and compute them in a specific order.

Alternatively, since the problem statement provides an example where tri(3) depends on tri(4), but for n=3, which is less than 4, perhaps we can compute the necessary higher terms up front.

But this approach might not be efficient and could require a lot of memory for large n.

Given that, perhaps the problem requires a dynamic programming approach that builds the sequence step by step, but handles the dependencies correctly.

Wait, perhaps for all even n, we can compute directly as 1 + n/2. For odd n, we can compute as tri(n-1) + tri(n-2) + tri(n+1). But tri(n+1) is even, so it can be computed directly using the even formula.

So, for example, for n=3:

tri(3) = tri(2) + tri(1) + tri(4)
tri(4) is even, so it's 1 +4/2=3.

So tri(3) = 2 + 3 +3 =8.

Therefore, to compute tri(n) when n is odd, we can directly compute tri(n+1) using the even formula and then proceed.

So, perhaps we can proceed as follows:

Initialize memo with memo[1] =3.

For n=0, return 1.

For n=1, return 3.

For n>=2:

- If n is even: memo[n] =1 +n/2
- If n is odd: memo[n] = memo[n-1] + memo[n-2] + memo[n+1], where memo[n+1] is computed using the even formula.

So, for a given n that's odd, we need to compute memo[n+1] before computing memo[n].

Therefore, to compute the sequence up to n:

We can compute each term in order, but when we encounter an odd term, we need to compute the next term first.

This suggests that for n >=2, if the required term is odd, we might need to compute higher terms first.

So, how can we implement this in Python?

An iterative approach that processes each term from 0 upwards, and when an odd term is encountered, computes the next term to resolve the dependency.

Alternatively, we can precompute all even terms and then compute odd terms using the precomputed even terms.

But the problem is that for a given n, which could be up to a large value, this could be inefficient.

Another approach is to memoize the computed terms and, when computing a term, ensure that any required higher terms are computed.

Given this, here's how the function can be structured:

1. Check if n is 0: return [1]
2. Check if n is 1: return [1,3]
3. Create a memo dictionary with memo[1] =3.
4. For each i from 2 to n:
   a. If i is even: memo[i] =1 + i/2
   b. If i is odd: memo[i] = memo[i-1] + memo[i-2] + memo[i+1]
5. However, computing memo[i+1] may require computing higher indices, leading to infinite recursion.

Wait, this again leads to the problem of needing to compute higher terms first.

Therefore, perhaps an alternative approach is to compute terms in a specific order: compute all even terms up to the maximum even term, then compute odd terms in reverse order (from higher to lower), using the