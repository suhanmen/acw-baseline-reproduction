Alright, so I need to write a Python function called `median` that calculates the median of a list of numbers. Let me think through how to approach this.

First, I need to understand what a median is. The median is the middle value in an ordered list of numbers. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle numbers.

Okay, so the function needs to handle both cases. I'll start by considering the edge cases:
- An empty list should probably return `None` or raise an error since the median of an empty list is undefined.
- A single-element list should just return that element.
- A list with all equal elements will return that element as the median.

Next, I need to think about how to handle invalid inputs. The problem states that the list should contain numbers, so I should validate that each element in the list is either an integer or a float. If any element is not a number, the function should raise a `ValueError`.

I'll break down the steps:
1. Validate the input list.
2. Check if the list is empty and handle it.
3. Sort the list.
4. Determine if the list length is even or odd.
5. Calculate the median based on the length.

Let me think about how to validate the list. I can loop through each element in the list and check if it's an instance of `int` or `float`. If any element is not, I raise an error.

After validation, I'll sort the list. Sorting will help me easily find the middle elements.

Now, calculating the median:
- If the length of the list is odd, the median is the middle element.
- If the length is even, it's the average of the two middle elements.

Let me structure this step by step.

Wait, what about the case when the list has only two elements? Sorting them first will help, and then I'll take the average of the two.

I should also ensure that the function returns a float when necessary, like in the example given where the median of [-10, 4, 6, 1000, 10, 20] is 15.0.

Another point: if the input list has even length, ensure that the average is calculated correctly, even if it results in an integer value. For example, [2, 4] should return 3.0, not 3.

Let me outline the code structure:

1. Check if the list is empty:
   - If `len(l) == 0`, return `None` or raise an error. But looking at the examples, when the list is valid but has elements, it returns a number. So for empty list, perhaps the function can return `None` or raise a meaningful error.

2. Validate each element in the list:
   - Loop through each element and check if it's an `int` or `float`.
   - If any element is not, raise `ValueError`.

3. Sort the list:
   - Use `sorted()` to sort the list, which returns a new list.

4. Determine the length of the list:
   - If `len(l) % 2 == 1` (odd), the median is `l[mid]` where `mid` is `len(l)//2`.
   - If `len(l) % 2 == 0` (even), the median is the average of `l[mid_left]` and `l[mid_right]` where `mid_left` is `len(l)//2 - 1` and `mid_right` is `len(l)//2`.

5. Return the calculated median.

Let me also think about testing the function with the given examples.

For the first example:
median([3, 1, 2, 4, 5])
After sorting: [1, 2, 3, 4, 5]
Length is 5 (odd), median is the 3rd element (index 2), which is 3.

For the second example:
median([-10, 4, 6, 1000, 10, 20])
After sorting: [-10, 4, 10, 20, 6, 1000] wait no, sorted in numerical order it's:
[-10, 4, 6, 10, 20, 1000]
Length is 6 (even), so mid_left is 2 and mid_right is 3. Values at indices 2 and 3 are 6 and 10. Average is (6 + 10)/2 = 16/2 = 8. Wait, but the expected output is 15.0.

Wait, wait, did I sort correctly? Let me re-sort the second example:

Original list: [-10, 4, 6, 1000, 10, 20]
Sorting in ascending order:
-10, 4, 6, 10, 20, 1000 → wait, no, 1000 is the largest, 20 is next.

Wait, correct sorted order is [-10, 4, 6, 10, 20, 1000]. So the middle elements are 6 (index 2) and 10 (index 3). The average is (6 + 10)/2 = 16/2 = 8.0. But the expected output is 15.0.

Hmm, that's conflicting. Did I make a mistake in sorting?

Wait no, perhaps I misread the example. Let me double-check the second example.

The example given is median([-10, 4, 6, 1000, 10, 20]) → 15.0

Wait, let's sort this list:

[-10, 4, 6, 1000, 10, 20]

So the numbers in order are: -10, 4, 6, 10, 20, 1000.

Wait, that's 6 elements. The median is the average of the 2nd and 3rd elements (since index starts at 0, it's elements at indices 2 and 3? Or wait, perhaps I'm counting from 1-based index?

Wait, when the list has even length, the median is the average of the two middle numbers. For 6 elements, the two middle ones are the 3rd and 4th elements (1-based index). Wait, no:

Wait, for an even length n, the median is the average of the elements at positions n//2 -1 and n//2 (using 0-based indexing). For n=6, positions 2 and 3 (since 6//2 -1 =2, and 6//2=3). Let's see:

Indices 2 and 3 are 6 and 10, average is 8.0. But the expected output is 15.0. That doesn't make sense.

Wait, did I sort the list correctly?

Wait, the original list is [-10, 4, 6, 1000, 10, 20]. Let's sort it step by step:

- Start with -10.

- Next is 4, which is larger.

- Then 6.

- Then 10, larger than 6.

- Then 20.

- Then 1000, which is the largest.

Wait, so sorted list is [-10,4,6,10,20,1000]. So indices 2 and 3 are 6 and 10. Average is 8.0. But the expected output is 15.0. Hmm, that's conflicting.

Wait, perhaps the expected output in the problem statement is incorrect? Or did I make a mistake?

Wait, let's try calculating the median again. Let's sort the list again.

Original list: [-10, 4, 6, 1000, 10, 20]

After sorting:

-10, 4, 6, 10, 20, 1000

Yes, that's correct. So median should be (6 + 10)/2 = 8.0.

But the problem expects 15.0. That suggests that perhaps the example is wrong, or perhaps I'm misunderstanding the problem.

Wait, perhaps the problem has a typo. Let me double-check.

The given example is:

median([-10, 4, 6, 1000, 10, 20]) → 15.0

But according to my calculation, it's 8.0. Hmm.

Wait, maybe I made a mistake in the sorting step.

Wait, wait, 1000 is the fourth element, 1000 is indeed larger than all. So after 1000 comes 20? No, 1000 is larger than 20, so in the sorted list, 20 comes before 1000. So the correct sorted list is:

[-10,4,6,10,20,1000]

Yes, so median is 8.0.

But the problem says it's 15.0. So either the problem is wrong, or perhaps the example is incorrect. But as a problem solver, I have to follow the problem's expected output.

Wait, perhaps I'm miscounting the indexes. Let me think: for a list with 6 elements, indexes 0,1,2,3,4,5.

The two middle elements are at indexes 2 and 3, which are 6 and 10. Average is (6+10)/2=8.0.

But the problem expects 15.0. That suggests that perhaps the example is incorrect, or perhaps I'm missing something.

Wait, perhaps the example was:

median([-10, 4, 6, 1000, 10, 20]) → (6 + 20)/2 = 13.0. That still doesn't give 15.0.

Alternatively, perhaps the example is:

median([-10, 4, 6, 1000, 10, 20]) → (6 + 1000)/2=503.0. That also doesn't make sense.

Hmm, perhaps the example was a typo, and the correct output should be 8.0. But since the problem gives the example as 15.0, I have to think why.

Wait, perhaps I misread the problem's sample. Let me check again.

No, the problem says:

>>> median([-10, 4, 6, 1000, 10, 20])
15.0

But according to my calculations, it's 8.0. So I'm confused.

Alternatively, perhaps the function is supposed to return a float when necessary, but in this case, perhaps the calculation is different.

Alternatively, perhaps the list is not what I think. Let me re-express the list:

Is the list [-10, 4, 6, 1000, 10, 20]?

Yes.

Wait, but if I arrange them in order:

-10, 4, 6, 10, 20, 1000 → Wait, no. 1000 is larger than 20, so 20 comes before 1000.

So the list is sorted as [-10,4,6,10,20,1000]. So the median is (6 + 10)/2=8.0.

But the problem says 15.0. So perhaps the problem statement is wrong. Alternatively, perhaps I'm misunderstanding the problem.

Wait, perhaps the function should be the average of the third and fourth elements? That would be (6 + 1000)/2 = 503.0, which is not 15.

Hmm, perhaps I'm missing something else.

Alternatively, perhaps the problem statement intended for the function to return the mean of all elements. But no, the examples don't support that.

Let me see the sample outputs again:

Sample 1:
median([3, 1, 2, 4, 5]) → 3

After sorting: [1,2,3,4,5]. Median is 3. Correct.

Sample 2:
median([-10, 4, 6, 1000, 10, 20]) → 15.0

But as we saw, the correct median is 8.0.

This suggests that either the problem is incorrect, or perhaps I'm misunderstanding the problem.

Alternatively, perhaps the example is wrong, and the function should return 8.0. But that's just me thinking.

In any case, perhaps I should proceed with the correct calculation.

But since the problem expects 15.0, perhaps I'm missing something else.

Wait, perhaps the function is supposed to return the mode, not the median? No, the function name is median, so that can't be.

Alternatively, perhaps the problem intended for even-length lists to return the second of the two middle elements, not the average. But that would make the median function return a different value.

Wait, but in statistics, the median is defined as the average of the two middle numbers when the length is even. So that's correct.

Given that, I'm confident that the example in the problem statement might have an error. But as a problem solver, I have to code according to the problem statement, so perhaps the function should handle that example correctly, but in reality, the example is wrong.

Alternatively, perhaps the function is supposed to return the middle element in even-length lists. But that's not standard practice. The standard practice is to average the two middle elements.

So perhaps the problem's example is incorrect. But I have to code as per the problem statement, regardless.

So, moving forward, I'll proceed to code the function as per standard median calculation.

Now, to structure