Okay, so I need to solve this problem where I have to find the element that appears only once in a sorted array. The array is sorted, which is a big hint on how to approach this. Let me think through this step by step.

First, let's understand the problem. The array is sorted, meaning the elements are in non-decreasing order. All elements except one appear exactly twice. My task is to find the single element that appears only once. For example, in the array [1,1,2,2,3], the element 3 appears only once, so the function should return 3.

Let me think about the possible approaches:

1. **Brute Force**: Check each element and count its occurrences. But this is not efficient because I have to scan the entire array.
2. **Binary Search**: Since the array is sorted, maybe I can use binary search to find the first occurrence of an element that doesn't have its next element equal to it. This would help me identify the single element quickly.
3. **Iterate Through the Array**: Loop through the array and compare each element with its next element. If they are different, it might be the single element. But I have to handle the last element case separately.

Considering the binary search approach seems the most efficient, especially for large arrays. Let me outline how this could work:

1. **Check Middle Element**: Find the middle element of the array. If the middle element is the same as the next element, then the single element must be on the left side. Otherwise, the single element is on the right side.
2. **Recursive Division**: Divide the array into two halves based on the middle element. Repeat the process on the appropriate half until the single element is found.
3. **Handle Edge Cases**: Make sure to handle cases where the array has an even number of elements, all elements are the same except one, and so on.

Wait, but let's think about the structure of the array. Since all elements except one appear twice, the array's length must be odd. Because if all elements except one appear twice, the total count would be even + 1 = odd.

So the first thing I should check is whether the length of the array is odd. If it's even, that means there is no single element, which contradicts the problem statement. But according to the problem examples, the input is always a valid array with exactly one element appearing once. So perhaps the function can assume the input is valid. However, it's better to handle it gracefully.

But given the problem statement, I can proceed under the assumption that the input is always valid. So I don't need to handle the case where the array length is even.

Now, let's think about the binary search approach in more detail:

- Start with the middle element. If the middle element is the same as the next element, then the single element is before the middle. Otherwise, it's after the middle.
- Repeat this process until the single element is found.

This approach ensures that I can find the single element in O(log n) time, which is efficient.

Let me outline the steps in code:

1. Compute the middle index.
2. Compare the middle element with the next element.
3. If they are the same, the single element is in the left half. Recur on the left half.
4. If they are different, the single element is in the right half. Recur on the right half.
5. Continue until the single element is found.

Let's test this logic with the sample inputs:

**Sample 1: [1,1,2,2,3]**
- Middle index is 2 (element 2). Next element is 2. They are the same, so the single element is in the left half [1,1].
- Middle of left half is index 0 (element 1). Next element is 1. Same, so single element is in the left half [1], but this is the base case.
- Wait, but in this case, the single element is 3, which is not found in the left half. So this suggests the logic is flawed.

Hmm, so the binary search approach as I initially thought might not work directly because the array has consecutive duplicates and the single element is not adjacent to any duplicates.

Let me rethink the approach.

Since the array is sorted and consists of pairs except for one single element, the single element will be between two different elements. For example, in [1,1,2,3,3], the single element is 2, which is between 1 and 3.

But how can I identify this? Because the array is sorted, all pairs will have two consecutive duplicates, and the single element will be the one that does not have its next element equal.

So, another approach could be:

- Iterate through the array and for each element, check if it is different from the next element. If it is, and it's the same as the previous element (indicating it's part of a pair), then it must be the single element.
- Alternatively, track whether the current element is part of a pair.

Wait, but this might be more complicated. Let's see.

Let me outline the steps:

1. Start from the first element.
2. Check if the current element is different from the next element.
   a. If yes, check if it's part of a pair (i.e., the previous element is the same as current).
      i. If yes, then current element is the single one.
      ii. If no, then current element is the start of a new pair.
   b. If no, then it's part of a pair, move to the next element.

This approach can work because each pair has two same elements, and the single element is the one that is followed by a different element.

Let me test this logic with the sample inputs.

**Sample 1: [1,1,2,2,3]**
- i=0, element=1, next=1: same, so part of a pair.
- i=1, element=1: same as previous, so part of a pair.
- i=2, element=2, next=2: same, part of a pair.
- i=3, element=2, next=3: different. Check if previous (element at i=2) is same as current (element at i=3). Yes, element=2 is same as i=2. So, check if current (i=3) is same as next (i=4). No, different. So the single element is 3.

This works.

**Sample 2: [1,1,3,3,4,4,5,5,7,7,8]**
- i=0, element=1, next=1: part of pair.
- i=1, element=1: same as previous.
- i=2, element=3, next=3: part of pair.
- i=3, element=3: same as previous.
- i=4, element=4, next=4: part of pair.
- i=5, element=4: same as previous.
- i=6, element=5, next=5: part of pair.
- i=7, element=5: same as previous.
- i=8, element=7, next=7: part of pair.
- i=9, element=7: same as previous.
- i=10, element=8, next is beyond array: different. Check if previous (element at i=9) is same as current. Yes, 7 !=8. So single element is 8.

This works.

**Sample 3: [1,2,2,3,3,4,4]**
- i=0, element=1, next=2: different. Check if previous (none, since i=0) is same as current. No. So single element is 1.

This works.

So the logic is:

Loop through the array, for each element:

- If the current element is different from the next element:
  - Check if the previous element (if any) is same as current element.
    - If yes, then current element is the single one.
    - If no, then the previous element is the single one.

Wait, no, in the first case, if the current element is different from the next, but the previous element is same as current, then current is the single element.

Wait, let's formalize this:

For each index i:

- If i is the last element (i == len(arr)-1):
   - Then, since the array is sorted, and all elements except one appear twice, i must be the single element.
- Else:
   - If arr[i] != arr[i+1]:
      - Then, check if arr[i] == arr[i-1]. If yes, then arr[i] is the single element.
      - Else, arr[i-1] is the single element.

This seems to work.

Let me test this logic with the samples.

**Sample 1: [1,1,2,2,3]**
- i=4 (last element), return arr[4] =3.

**Sample 2: [1,1,3,3,4,4,5,5,7,7,8]**
- i=10 (last element), return 8.

**Sample 3: [1,2,2,3,3,4,4]**
- i=0 is the first element. Since i is not the last element, check if arr[0] == arr[1]. arr[0]=1, arr[1]=2: different. So, check if arr[i-1] exists and equals arr[i]. Since i=0, i-1 is -1, which is invalid. So, in this case, we need to handle i=0 separately.

Wait, this suggests that for i=0, if it's different from i+1, then it's the single element.

In sample 3, i=0, element is 1, which is different from element at i+1 (2). Since it's the first element, there's no previous element, so it's the single element.

So the logic is:

For each index i:

- If i is the last element, return it as the single element.
- Else if arr[i] != arr[i+1]:
   - If i == 0: return arr[i].
   - Else if arr[i] == arr[i-1]: return arr[i].
   - Else: return arr[i-1].

Wait, but in sample 2, at i=8, arr[i]=7, arr[i+1]=7, so same, move on. At i=9, arr[i]=7, arr[i+1]=8: different. Since i !=0, and arr[i-1] =7 == arr[i], so return 7. But the single element is 8, which is at i=10. So this logic fails.

Ah, I see. So the logic is not sufficient.

Wait, because in sample 2, after i=9, the single element is 8, which is at i=10. The logic correctly returns 7 at i=9, but that's part of a pair (7,7), which is incorrect.

So the logic needs to be adjusted.

Alternative approach: When arr[i] != arr[i+1], check if arr[i] is equal to the next element (arr[i+1]). If yes, then the previous element is the single one. If no, then the current element is the single one.

Wait, let me think:

If arr[i] is not equal to arr[i+1], there are two possibilities:

1. arr[i] is part of a pair, and arr[i+1] is the single element.

2. arr[i] is the single element, and arr[i+1] is part of a pair.

Which one is it?

In the sample 2: at i=9, arr[i]=7, arr[i+1]=8.

arr[i] is same as arr[i-1] (7). So according to the previous logic, we return arr[i], which is 7, but that's part of a pair, which is incorrect.

Wait, perhaps the correct condition is:

If arr[i] is equal to arr[i+1], then the single element is before i.

Else, if arr[i] is equal to arr[i-1], then the single element is arr[i].

Else, the single element is arr[i+1].

Let me see.

In sample 2:

i=9, arr[i]=7, arr[i+1]=8.

Check arr[i] == arr[i+1]? No.

Check arr[i] == arr[i-1]? Yes (7=7).

So return arr[i]=7 as single element. But that's incorrect, because the single element is 8 at i=10.

So, this approach is not working.

Let me try another approach.

Perhaps the single element is the one that doesn't have its next element equal. So, I can loop through the array and whenever arr[i] != arr[i+1], then if arr[i] == arr[i-1], return arr[i], else return arr[i+1]. Wait, let's test this.

In sample 1: [1,1,2,2,3].

i=0: arr[i]=1, arr[i+1]=1. Same.

i=1: arr[i]=1, arr[i+1]=2. Different. Check if arr[i] == arr[i-1]. arr[i-1] is None, so no. So return arr[i+1]=2. But that's wrong; the single element is 3.

So this approach is not working.

Wait, perhaps the correct logic is: when arr[i] != arr[i+1], then if arr[i] == arr[i+1], which it's not in this case.

Wait, perhaps I'm approaching this wrong. Maybe the single element is surrounded by elements that are different from it. So, the single element will be the one where the previous and next elements are different from itself.

So, for each element, check if it's different from both its previous and next elements.

But in a sorted array, that's possible only if the array has an element that is not part of a pair.

Wait, in the array [1,1,2,2,3], 3 is the single element. 3 is followed by nothing, and its previous is 2.