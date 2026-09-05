Okay, I need to write a Python function called `multiples_of_num` that finds `m` number of multiples of `n`. The function must satisfy the given assertions. Let me think about how to approach this.

First, let's understand the problem. The function takes two arguments, `n` and `m`, where `n` is the number whose multiples we need to find, and `m` is the count of those multiples. The output should be a list containing the first `m` multiples of `n`.

Looking at the examples:
- `multiples_of_num(4,3)` should return `[3,6,9,12]` which are the first 3 multiples of 3.
- `multiples_of_num(2,5)` should return `[5,10]` which are the first 2 multiples of 5.
- `multiples_of_num(9,2)` should return `[2,4,6,8,10,12,14,16,18]` which are the first 9 multiples of 2.

Wait, that seems a bit confusing. In the third example, `multiples_of_num(9,2)` returns 9 elements. So the function's parameters might be reversed. Let me check the problem statement again.

Oh, I see. The function is supposed to return the first `m` multiples of `n`. So for `multiples_of_num(9,2)`, the first 2 multiples of 9 are [9, 18], but the expected output is [2,4,6,8,10,12,14,16,18]. That doesn't make sense. Maybe there's a mistake in the example or in my understanding.

Wait, perhaps the function is supposed to return the multiples in ascending order but starting from a different point. Looking at the examples:

- For `n=4` and `m=3`, the output is `[3,6,9,12]` which suggests that the function starts counting from 1 up to `m` and multiplies each by `n`.
- For `n=2` and `m=5`, the output is `[5,10]` which suggests that the function is actually returning the first `m` positive integers multiplied by `n`.

Wait, but in that case, the third example is confusing. Let me double-check:

- `multiples_of_num(9,2)` is expected to return `[2,4,6,8,10,12,14,16,18]` which is actually the first 9 even numbers. That suggests that `m` is the number of multiples to generate, but the multiples are of 2 starting from 2.

Hmm, this is conflicting. Let's re-express the problem statement.

The function should find `m` number of multiples of `n`. The examples seem to indicate that when `n=4` and `m=3`, the result is `[3,6,9,12]` which are the first 3 multiples of 4 starting from 4. But wait, 3 is the first multiple of 4? No, 4 is the first multiple of 4, then 8, 12, etc.

Wait, this is confusing. Let me clarify.

Looking at the first example:
- `multiples_of_num(4,3)` should return `[3,6,9,12]` which are 4 multiplied by 1, 2, 3, 4. So the result is `[4*1, 4*2, 4*3, 4*4]`, but the output only includes 4*1, 4*2, 4*3. No, wait, the output is [3,6,9,12] which is 3*1, 3*2, 3*3, 3*4. So it's multiples of 3, not 4.

Wait, this is conflicting with the problem statement. Let me read the problem statement again.

The problem statement says: "Write a function to find m number of multiples of n." So, the function should return a list of multiples of `n`, starting from 1 up to `m` multiples.

Wait, that doesn't match the examples. Let's look at the examples again:

- `multiples_of_num(4,3)` returns `[3,6,9,12]`
- `multiples_of_num(2,5)` returns `[5,10]`
- `multiples_of_num(9,2)` returns `[2,4,6,8,10,12,14,16,18]`

Wait, the third example is giving 9 elements when `m` is 2. That suggests that perhaps the parameters are reversed. Maybe `n` is the number to find multiples of, but `m` is the value up to which we stop.

Alternatively, perhaps the function is supposed to return the first `m` even numbers regardless of `n`. But that doesn't make sense with the first two examples.

I think there's a misunderstanding here. Let me re-express the function's requirements based on the examples:

The function should return the first `m` multiples of `n`, starting from `n*1`, `n*2`, ..., `n*m`.

But let's test this against the examples:

For `multiples_of_num(4,3)`, the result should be `[4, 8, 12]`, but the expected output is `[3,6,9,12]`. This doesn't match.

Wait, maybe the function is supposed to return the multiples of `m` starting from `n`. No, that doesn't fit either.

Alternatively, perhaps the function is supposed to return the numbers from `1` to `m` multiplied by `n`, but the examples suggest that when `n=4`, it's returning multiples of 3. So perhaps the function parameters are swapped.

Wait, perhaps the function is supposed to return the first `n` multiples of `m`, not the first `m` multiples of `n`. Let's test that:

For `multiples_of_num(4,3)`, it would return `[3,6,9,12]` which are the first 4 multiples of 3. That doesn't match the example.

Alternatively, perhaps the function is supposed to return the multiples of `m` that are less than or equal to `n`. That also doesn't fit.

I think the best approach is to clarify the function's requirements based on the examples. Let's see:

- For `multiples_of_num(4,3)`, the output is `[3,6,9,12]`. These are multiples of 3, not 4. So perhaps the function's parameters are reversed, and the first argument is `m` and the second is `n`. But that would change the function's signature.

Wait, the problem statement says to keep the given signature exactly as it is. So the function is defined as `def multiples_of_num(n, m):` and we need to stick with that.

But the examples are conflicting. Let me think differently. Perhaps the function should return the multiples of `n` that are less than or equal to `m`. But for `multiples_of_num(4,3)`, the multiples of 4 less than or equal to 3 would be an empty list, which doesn't match the example.

Alternatively, perhaps the function is supposed to return the multiples of `n` starting from 1 up to `m`. For example:

- `multiples_of_num(4,3)` would return `[4*1, 4*2, 4*3]` → `[4,8,12]`, but the expected output is `[3,6,9,12]`, which suggests `n=3`.

This is confusing. Let me try to find a pattern in the examples:

1. `multiples_of_num(4,3)` → [3,6,9,12] → multiples of 3
2. `multiples_of_num(2,5)` → [5,10] → multiples of 5
3. `multiples_of_num(9,2)` → [2,4,6,8,10,12,14,16,18] → multiples of 2

Wait, this suggests that the function's first parameter is the multiple, and the second parameter is the starting point. But that contradicts the function signature.

Alternatively, perhaps the function's parameters are swapped, but the problem statement requires us to keep the given signature.

Alternatively, perhaps the function is supposed to return the first `m` multiples of `n` starting from `n*1`, but the examples are incorrect. Or perhaps the examples are incorrect.

Given the confusion, I think the best approach is to proceed with the assumption that the function should return the first `m` multiples of `n`, starting from `n*1`, as per the problem statement.

So, the function's logic would be:

1. Validate the inputs: `n` and `m` should be integers, and `m` should be a positive integer.
2. If `m` is zero or negative, return an empty list.
3. If `n` is zero, return a list with `m` zeros.
4. Generate the first `m` multiples of `n` by multiplying `n` by each integer from 1 to `m`.

Let me test this logic against the examples:

1. `multiples_of_num(4,3)` → [4,8,12] → but the expected output is [3,6,9,12], which doesn't match.
2. `multiples_of_num(2,5)` → [2,4,6,8,10] → but the expected output is [5,10], which doesn't match.
3. `multiples_of_num(9,2)` → [9,18] → but the expected output is [2,4,6,8,10,12,14,16,18], which doesn't match.

Clearly, this logic doesn't match the examples. So, perhaps the function is supposed to return the multiples of `m` starting from 1 up to `n`.

Let me try this:

1. `multiples_of_num(4,3)` → multiples of 3 up to 4: [3,6,9,12] → but wait, 3,6,9,12 are all larger than 4, so perhaps it's multiples of 3 starting from 1 up to 4. But that would only include 3.

This also doesn't match.

Alternatively, perhaps the function is supposed to return the multiples of `m` starting from 1 up to `n`.

Let's test this:

1. `multiples_of_num(4,3)` → multiples of 3 up to 4: [3,6,9,12] → No, 6 is larger than 4.
2. `multiples_of_num(2,5)` → multiples of 5 up to 2: [5], which doesn't match the expected output of [5,10].
3. `multiples_of_num(9,2)` → multiples of 2 up to 9: [2,4,6,8], which doesn't match the expected output of 9 elements.

This is not working.

Perhaps the function's parameters are `n` and `m`, but the output is the multiples of `m` that are less than or equal to `n`.

Wait, let's try this:

1. `multiples_of_num(4,3)` → multiples of 3 up to 4: [3,6] → but 6 is larger than 4. So only [3].
2. `multiples_of_num(2,5)` → multiples of 5 up to 2: only [5] (but 5 is larger than 2, so no multiples).
3. `multiples_of_num(9,2)` → multiples of 2 up to 9: [2,4,6,8].

This also doesn't match the examples.

At this point, I'm realizing that there's a discrepancy between the function signature and the examples. The examples suggest that the function's output is the first `m` multiples of 1, 2, and 1 respectively, but that doesn't make sense.

Given this confusion, I think the best approach is to re-express the examples in terms of the function's parameters and see what the actual logic should be.

Looking at the first example: `multiples_of_num(4,3)` returns [3,6,9,12]. This can be interpreted as the multiples of 3, but why would `n` be 4 and the multiples be of 3? That suggests that the parameters are swapped.

So, perhaps the function should be:

def multiples_of_num(m, n):
    return the first m multiples of n.

But the problem statement says to keep the given signature as it is, which is `def multiples_of_num(n, m):`. So that's not allowed.

Alternatively, perhaps the function's parameters are `n` and `m`, but the output is the multiples of `n` starting from `n*m` and going backward, but that doesn't make sense.

Alternatively, perhaps the function is supposed to return the multiples of `m` that are less than or equal to `n`.

But for the first example, `multiples_of_num(4,3)`, that would be multiples of 3 that are ≤4: [3]. Which doesn't match the expected output.

Alternatively, perhaps the function should return the multiples of `n` starting from 1 up to `m`. But that would mean `n` is 3, but in the first example `n=4`.

I'm stuck. Let me try to think differently.

Looking at the examples:

1. `multiples_of_num(4,3) == [3,6,9,12]` → The output has 4 elements, but `m=3`.
2. `multiples_of_num(2,5) == [5,10]` → The output has 2 elements, but `m=5`.
3. `multiples_of_num(9,2) ==