Okay, so I need to write a Python function that finds the maximum product subarray of a given array. Hmm, let's think about how to approach this problem.

First, I should understand what a subarray is. A subarray is a contiguous part of an array. For example, the subarrays of [1, 2, 3] are [1], [2], [3], [1, 2], [2, 3], and [1, 2, 3]. The product of a subarray is the result of multiplying all its elements together. So, my goal is to find the subarray with the highest product.

I remember that this problem is a classic dynamic programming problem. The key idea is to keep track of the maximum and minimum products ending at each position because a negative number can turn a minimum product into a maximum product when multiplied by another negative number.

Alright, let's outline the steps:

1. **Initialization**: Start by initializing two variables, `max_ending_here` and `min_ending_here`, both set to the first element of the array. Also, initialize `max_so_far` with the first element since the maximum product could be the first element itself if the array contains only negative numbers.

2. **Iterate through the array**: For each element starting from the second one, calculate the possible new products:
   - Multiply the current element by `max_ending_here` and `min_ending_here` to consider extending the subarray.
   - Also, consider starting a new subarray at the current element by taking its value itself.
   - Update `max_ending_here` to be the maximum of these possibilities.
   - Similarly, update `min_ending_here` to be the minimum of these possibilities.

3. **Update the overall maximum**: After calculating the new `max_ending_here` and `min_ending_here`, update `max_so_far` if `max_ending_here` is greater than the current `max_so_far`.

4. **Edge cases**: Handle edge cases such as empty input, single element, all equal elements, zero, and negative numbers. If the array is empty, return None. If it contains zeros, the maximum product could still be zero or a positive number.

5. **Return the result**: After processing all elements, return `max_so_far`.

Let's apply this logic to an example. Take the array [1, -2, -3, 0, 7, -8, -2]:

- Initialize `max_ending_here = -2`, `min_ending_here = -2`, `max_so_far = -3` (but wait, this seems incorrect. Oh, right, the first element is 1, not -2. Let me correct this.)
  
Wait, let me re-initialize properly. For the array [1, -2, -3, 0, 7, -8, -2]:

1. **Initialization**:
   - `max_ending_here = 1`
   - `min_ending_here = 1`
   - `max_so_far = 1`

2. **Iterate through the array**:
   - **Element -2**:
     - `max_ending_here = max(-2 * 1, -2, -2 * 1) = max(-2, -2, -2) = -2`
     - `min_ending_here = min(-2 * 1, -2, -2 * 1) = min(-2, -2, -2) = -2`
     - `max_so_far` remains 1
   - **Element -3**:
     - `max_ending_here = max(-3 * -2, -3, -3 * -2) = max(6, -3, 6) = 6`
     - `min_ending_here = min(-3 * -2, -3, -3 * -2) = min(6, -3, 6) = -3`
     - `max_so_far` updates to max(1, 6) = 6
   - **Element 0**:
     - `max_ending_here = max(0 * -3, 0, 0 * -3) = max(0, 0, 0) = 0`
     - `min_ending_here = min(0 * -3, 0, 0 * -3) = min(0, 0, 0) = 0`
     - `max_so_far` remains 6
   - **Element 7**:
     - `max_ending_here = max(7 * 0, 7, 7 * 0) = max(0, 7, 0) = 7`
     - `min_ending_here = min(7 * 0, 7, 7 * 0) = min(0, 7, 0) = 0`
     - `max_so_far` updates to max(6, 7) = 7
   - **Element -8**:
     - `max_ending_here = max(-8 * 7, -8, -8 * 7) = max(-56, -8, -56) = -8`
     - `min_ending_here = min(-8 * 7, -8, -8 * 7) = min(-56, -8, -56) = -56`
     - `max_so_far` remains 7
   - **Element -2**:
     - `max_ending_here = max(-2 * -8, -2, -2 * -8) = max(16, -2, 16) = 16`
     - `min_ending_here = min(-2 * -8, -2, -2 * -8) = min(16, -2, 16) = -2`
     - `max_so_far` updates to max(7, 16) = 16

Wait, but the expected output for this example is 112. Oh, I see what I did wrong. Let me re-examine the array: [1, -2, -3, 0, 7, -8, -2]. The maximum product subarray is [7, -8, -2], which is 7 * -8 * -2 = 112.

So I must have made a mistake in my calculation. Let me correct this.

After element 7:
- `max_ending_here` is 7
- `min_ending_here` is 0

After element -8:
- `max_ending_here` = max(-8 * 7, -8, -8 * 7) = max(-56, -8, -56) = -8
- `min_ending_here` = min(-8 * 7, -8, -8 * 7) = min(-56, -8, -56) = -56
- `max_so_far` remains 7

After element -2:
- `max_ending_here` = max(-2 * -8, -2, -2 * -8) = max(16, -2, 16) = 16
- `min_ending_here` = min(-2 * -8, -2, -2 * -8) = min(16, -2, 16) = -2
- `max_so_far` updates to max(7, 16) = 16

Hmm, still not matching the expected output. I think I missed a subarray that includes 7 and -8 and -2. Let me think differently.

Wait, perhaps my approach is missing something. Maybe I should also consider that the maximum product could come from a positive product that's higher than any subarray ending with negative numbers.

Let me adjust the approach to ensure that I correctly track the maximum and minimum products.

In the correct implementation, the algorithm should:

- Keep track of both the maximum and minimum products up to the current position.
- For each element, calculate the current maximum and minimum as:
   - current_max = max(num, current_max * num, current_min * num)
   - current_min = min(num, current_max * num, current_min * num)
- Update the overall maximum if current_max is larger.

Let's apply this correctly.

For the array [1, -2, -3, 0, 7, -8, -2]:

1. **Initialization**:
   - `current_max = 1`
   - `current_min = 1`
   - `max_product = 1`

2. **Element -2**:
   - `current_max = max(-2, 1 * -2, 1 * -2) = max(-2, -2, -2) = -2`
   - `current_min = min(-2, 1 * -2, 1 * -2) = min(-2, -2, -2) = -2`
   - `max_product` remains 1

3. **Element -3**:
   - `current_max = max(-3, -2 * -3, -2 * -3) = max(-3, 6, 6) = 6`
   - `current_min = min(-3, -2 * -3, -2 * -3) = min(-3, 6, 6) = -3`
   - `max_product` updates to 6

4. **Element 0**:
   - `current_max = max(0, 6 * 0, -3 * 0) = max(0, 0, 0) = 0`
   - `current_min = min(0, 6 * 0, -3 * 0) = min(0, 0, 0) = 0`
   - `max_product` remains 6

5. **Element 7**:
   - `current_max = max(7, 0 * 7, 0 * 7) = max(7, 0, 0) = 7`
   - `current_min = min(7, 0 * 7, 0 * 7) = min(7, 0, 0) = 0`
   - `max_product` updates to 7

6. **Element -8**:
   - `current_max = max(-8, 7 * -8, 0 * -8) = max(-8, -56, 0) = 0`
   - `current_min = min(-8, 7 * -8, 0 * -8) = min(-8, -56, 0) = -56`
   - `max_product` remains 7

7. **Element -2**:
   - `current_max = max(-2, 0 * -2, -56 * -2) = max(-2, 0, 112) = 112`
   - `current_min = min(-2, 0 * -2, -56 * -2) = min(-2, 0, 112) = -2`
   - `max_product` updates to 112

So the maximum product subarray is [7, -8, -2], which gives 7 * -8 * -2 = 112.

Let's test another example: [6, -3, -10, 0, 2]

1. **Initialization**:
   - `current_max = 6`
   - `current_min = 6`
   - `max_product = 6`

2. **Element -3**:
   - `current_max = max(-3, 6 * -3, 6 * -3) = max(-3, -18, -18) = -3`
   - `current_min = min(-3, 6 * -3, 6 * -3) = min(-3, -18, -18) = -18`
   - `max_product` updates to max(6, -3) = 6

3. **Element -10**:
   - `current_max = max(-10, -3 * -10, -18 * -10) = max(-10, 30, 180) = 180`
   - `current_min = min(-10, -3 * -10, -18 * -10) = min(-10, 30, 180) = -10`
   - `max_product` updates to 180

4. **Element 0**:
   - `current_max = max(0, 180 * 0, -10 * 0) = max(0, 0, 0) = 0`
   - `current_min = min(0, 180 * 0, -10 * 0) = min(0, 0, 0) = 0`
   - `max_product` remains 180

5. **Element 2**:
   - `current_max = max(2, 0 * 2, 0 * 2) = max(2, 0, 0) = 2`
   - `current_min = min(2, 0 * 2, 0 * 2) = min(2, 0, 0) = 0`
   - `max_product` remains 180

So the maximum product subarray is [-3, -10], which gives (-3) * (-10) = 30, but wait, that's not right. Oh, no, the maximum is actually the subarray [-10, 0, 2], which is (-10) * 0 * 2 = 0. Hmm, that doesn't make sense because 180 is larger.

Wait, actually, the subarray that gives 180 is [6, -3, -10], which is 6 * (-3) * (-10) = 180. So the algorithm correctly captures that.

Another example: [-2, -40, 0, -2, -3]

1. **