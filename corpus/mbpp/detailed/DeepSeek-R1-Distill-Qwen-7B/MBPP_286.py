Okay, so I need to solve this problem where I have to find the largest sum of contiguous subarrays in an array that's been repeated multiple times. Hmm, let's see. The function is called max_sub_array_sum_repeated, and it takes three arguments: the original array, the number of times it's repeated (k), and the desired sum (the third value in the test cases, but actually, in the problem statement, it's the sum of the modified array formed by repeating the array k times). Wait, no—the function needs to return the largest sum of contiguous subarrays in the modified array formed by repeating the original array k times.

Wait, the test cases are:
- max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) should return 30.
- max_sub_array_sum_repeated([-1, 10, 20], 3, 2) should return 59.
- max_sub_array_sum_repeated([-1, -2, -3], 3, 3) should return -1.

Wait, no—the third argument in the test cases is the sum, but in the problem statement, it's the "desired sum". Hmm, I'm a bit confused. Let me re-read the problem statement.

The problem is to find the largest sum of contiguous subarrays in the modified array formed by repeating the given array k times. So the function needs to take the original array, the number of repetitions (k), and then return the maximum subarray sum of the repeated array.

But in the test cases, the third argument is called the "desired sum". Oh, wait, looking at the test cases again:

Wait, in the first test case, [10, 20, -30, -1], repeated 4 times, and the desired sum is 3. The function returns 30. Hmm, maybe I misunderstood the problem statement.

Wait, perhaps the function is supposed to find the largest sum of contiguous subarrays in the modified array, but the modified array is formed by repeating the original array k times. So the function needs to return the maximum subarray sum of the k-times repeated array.

But the test cases suggest something else. Let's look at the first test case:

Original array: [10, 20, -30, -1], repeated 4 times, so the modified array is [10, 20, -30, -1, 10, 20, -30, -1, 10, 20, -30, -1, 10, 20, -30, -1].

The maximum subarray sum in this modified array is 30. How does that happen? Let's see.

Looking at the original array: the subarray [10, 20] sums to 30. Since the array is repeated 4 times, this subarray appears in each repetition. So the maximum sum remains 30.

Similarly, in the second test case: original array [-1, 10, 20], repeated 3 times. The modified array is [-1, 10, 20, -1, 10, 20, -1, 10, 20]. The maximum subarray sum is 59. Wait, that's 10+20 repeated twice, but 10+20 is 30, so 30*2=60, but 59 is one less. Hmm, maybe because of the negative elements.

Wait, perhaps the function should also consider the case where the entire array is part of the subarray, especially when the array has both positive and negative values.

But in any case, I need to write a function that correctly computes the maximum subarray sum of the k-times repeated array.

Let me plan how to approach this.

First, for the function, the inputs are:
- arr: the original array
- k: the number of times to repeat the array
- sum: the desired sum (though I'm a bit confused about its role here)

Wait, maybe the sum is not directly used, except perhaps to determine if we need to calculate a specific sum. Wait, looking at the first test case: desired sum is 3, but the function returns 30. So perhaps the third argument is not used as the desired sum but rather the function is supposed to compute the sum of the contiguous subarrays regardless of the desired sum.

Wait, maybe the function signature is incorrect. Looking back at the problem statement: "Find the largest sum of contiguous array in the modified array which is formed by repeating the given array k times." So the function needs to return the largest sum, regardless of any desired sum. So the third argument is probably a misinterpretation. Or perhaps it's used to indicate the number of repetitions.

Wait, looking at the test cases, the third argument in the first call is 3, but the function returns 30. So perhaps the function is supposed to repeat the array k times, and then return the maximum subarray sum.

Wait, but the test cases have the third argument as the desired sum, but perhaps it's a typo. Let me check the initial problem statement again.

The initial problem statement says: "Write a function to find the largest sum of contiguous array in the modified array which is formed by repeating the given array k times."

So the function's third argument is the sum of the modified array, which is formed by repeating the given array k times. So the function needs to return this sum.

Wait, but in the test cases, the third argument is the sum. For example, in the first test case, the modified array is the original array repeated 4 times, and the function returns 30, which is the sum of the maximum subarray.

Wait, no. The function is supposed to return the largest sum of contiguous subarrays in the modified array, which is formed by repeating the given array k times. So the function should return that maximum sum.

But in the test cases, the third argument is the desired sum. So perhaps the function is supposed to find the sum of the maximum contiguous subarray in the modified array, which is formed by repeating the given array k times.

So, I think I can ignore the third argument and focus on computing the maximum subarray sum of the k-times repeated array.

But to be precise, I need to read the problem statement again.

Problem statement: "Write a function to find the largest sum of contiguous array in the modified array which is formed by repeating the given array k times."

So the function should return the maximum sum of contiguous subarrays of the modified array (which is the original array repeated k times).

The test cases are:

- max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) should return 30.
- max_sub_array_sum_repeated([-1, 10, 20], 3, 2) should return 59.
- max_sub_array_sum_repeated([-1, -2, -3], 3, 3) should return -1.

Wait, the third argument in the test cases is the sum that the function is supposed to compute. So the function's signature is:

def max_sub_array_sum_repeated(arr, k, sum):

But that doesn't make sense, because the function's name is to find the largest sum of contiguous subarrays in the modified array formed by repeating the array k times. So perhaps the third argument is a typo, and it should be the number of repetitions. Or perhaps the third argument is not used at all.

Wait, perhaps the function signature in the test cases is different. Let me see the sample test cases:

Sample test case 1: max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30

Sample test case 2: max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59

Sample test case 3: max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

So the function has three arguments: arr, k, sum.

Wait, but that seems confusing. Let's clarify:

- arr: the original array
- k: the number of times to repeat the array
- sum: perhaps the desired sum (but not sure)

But in the problem statement, the function is supposed to return the largest sum of contiguous subarrays in the modified array formed by repeating the given array k times.

So perhaps the function's third argument is not the sum, but the number of repetitions, and there's a typo in the test cases.

Alternatively, perhaps the function is supposed to return the sum of the maximum contiguous subarray in the modified array.

In any case, I'll proceed with the understanding that the function needs to return the maximum sum of contiguous subarrays in the modified array formed by repeating the original array k times.

Given that, I'll ignore the third argument's role and focus on writing a function that computes the maximum subarray sum of the k-times repeated array.

So, to implement this, the steps are:

1. Generate the modified array by repeating the original array k times.
2. Compute the maximum subarray sum of this modified array.

But generating the modified array could be memory-intensive for large k. So instead, we can compute the maximum subarray sum without generating the entire array.

To do this efficiently, we can use the following approach:

- Compute the sum of the original array.
- Compute the maximum subarray sum of the original array (without repetition).
- Depending on whether the sum of the original array is positive or not, decide how many times to repeat it to maximize the subarray sum.

Let me outline the steps:

1. Compute the maximum prefix sum (max_prefix), maximum suffix sum (max_suffix), and the total sum (total_sum) of the original array.
2. If the total_sum is positive, the maximum subarray sum in the modified array is the maximum between the maximum subarray sum of the original array, the total_sum multiplied by k, the sum of max_prefix + max_suffix * (k-1), etc.
3. If the total_sum is zero or negative, the maximum subarray sum is simply the maximum between the original maximum subarray sum and the maximum subarray sum when considering parts of the array in one repetition.

This approach avoids generating the modified array and works in O(n) time, which is efficient.

Now, let's implement this in Python:

- Compute the maximum subarray sum for one repetition.
- Compute the max_prefix and max_suffix.
- If total_sum > 0, the maximum sum can be the original max_sum multiplied by k, but we also need to consider adding the max_prefix and max_suffix multiple times.
- Handle edge cases where the array has all negative numbers, which means the maximum sum is the largest single element.
- Handle cases where k is 1.

Let me write the code step by step.

First, compute the maximum subarray sum, max_prefix, max_suffix, and total_sum of the original array.

Next, handle the cases based on the total_sum.

If total_sum > 0, the maximum sum in the modified array is max(2 * max_suffix + max_prefix * (k-1), max_prefix * k, max_suffix * k, max_sum * k, ... ). Wait, perhaps the correct formula is:

If the original array's total_sum is positive, then the maximum subarray sum is max(original_max_sum, max_prefix + (total_sum * (k - 1)), max_suffix + (total_sum * (k - 1)), max_prefix + max_suffix + (total_sum * (k - 2)), ... )

But to simplify, the maximum sum can be calculated as:

max_sum = max(original_max_sum, total_sum * k, max_prefix + (total_sum * (k - 1)), max_suffix + (total_sum * (k - 1)))

But let me think about this.

If the original array has a positive total_sum, then repeating it k times will allow us to concatenate the suffix of the original array with the prefix of the next repetition, which could give a larger sum.

So, for k >= 2, the maximum sum could be the original maximum sum, or the sum of max_suffix and max_prefix multiplied by (k - 1), but no, that's not right. Wait, no: if you have the original array with a positive total_sum, then the best subarray could be:

- The best subarray in a single repetition.

- The best subarray that starts in one repetition and ends in another, which would be max_suffix + (total_sum * (k - 2)) + max_prefix.

But since the original array is repeated k times, the number of transitions between repetitions is k - 1. So the maximum possible sum in such a case would be:

max_suffix (from the first repetition) + total_sum * (k - 1) + max_prefix (from the last repetition).

Wait, yes! Because when you repeat the array, the maximum subarray could span from the suffix of one array to the prefix of the next, and so on.

So the formula becomes:

max_candidate = max_suffix + (total_sum * (k - 1)) + max_prefix

So, the overall maximum sum would be the maximum between the original_max_sum, max_candidate, and (total_sum * k).

But wait, what about cases where k is 1? Then (k - 1) is 0, so max_candidate becomes max_suffix + 0 + max_prefix = max_prefix + max_suffix.

But in that case, we need to compare that with the original_max_sum.

Similarly, when total_sum is positive, the best sum is either the original max sum, or the sum of max_prefix + (total_sum) * (k - 1) + max_suffix.

But wait, when you repeat the array k times, the maximum subarray could be the original max subarray, or it could be the combination of the suffix of one array and the prefix of the next, repeated (k - 1) times.

So, putting it all together:

If total_sum > 0:
    max_sum = max(max_original_sum, max_suffix + (total_sum * (k - 1)) + max_prefix)
else:
    # We can't use the repeated arrays to get a higher sum, so the maximum is either the original max or parts in one repetition.
    #