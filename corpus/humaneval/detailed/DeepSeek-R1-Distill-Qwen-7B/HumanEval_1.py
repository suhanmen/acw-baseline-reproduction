Okay, I need to solve this problem where I have to separate parentheses groups from a given string. The input is a string containing multiple groups of nested parentheses, and I have to return a list of these groups. The groups should be balanced and not nested within each other. Also, I need to ignore any spaces in the input string.

Let me start by understanding the problem better. So, the input string can have multiple parentheses groups, like '((()))', '()()', and '(())()'. My task is to extract each of these groups as separate strings in a list. 

First, I should ignore any spaces. So I need to process the string and remove all the spaces first. That makes it easier to handle the actual parentheses.

Next, I need to find each individual group of parentheses. These groups are not nested, which means once a group starts, it doesn't contain another group. So I can use a stack data structure to help identify the groups.

Wait, no. Since the groups are not nested, maybe I can track when I find an opening parenthesis and then find the corresponding closing parenthesis. But since the groups are not nested, each opening parenthesis will belong to exactly one group.

Alternatively, I can iterate through the string and keep track of the current group's start and end indices. Whenever I encounter an opening parenthesis, I note its index and look for the next closing parenthesis to mark the end of this group. Then, I can collect the substring between these indices as one group.

But I have to make sure that I don't include any spaces. So, perhaps after removing the spaces, I can iterate through each character and manage a stack to track the current level of nesting. However, since the groups are not nested, each time I encounter an opening parenthesis, it starts a new group, and each closing parenthesis ends the current group.

So, here's the plan:

1. Preprocess the input string by removing all spaces.
2. Iterate through each character in the cleaned string.
3. Use a stack to keep track of the indices of opening parentheses.
4. When I encounter a closing parenthesis, if there's an opening parenthesis in the stack, pop it and record the indices of this group.
5. Collect all such groups and add them to the result list.

Wait, but the groups are not nested, so the stack approach might not be necessary. Because in a non-nested scenario, each opening parenthesis will always have a closing parenthesis that's not nested within another group.

Alternatively, I can iterate through the string and whenever I find an opening parenthesis, I start collecting characters until I find the corresponding closing parenthesis, ensuring that I don't include any nested groups.

Hmm, but how do I ensure that I don't include nested groups? Since the problem states that the groups are not nested, I can collect all characters from an opening parenthesis to the next closing parenthesis, as long as there are no unclosed parentheses in between.

Wait, perhaps that's not sufficient. Because even if the groups are not nested, there could be multiple groups that are adjacent or overlapping if not handled correctly.

Let me think differently. After removing the spaces, I can iterate through each character and track the current depth of parentheses. Each time I encounter an opening parenthesis, I increase the depth, and each time I encounter a closing parenthesis, I decrease the depth. When the depth becomes zero after a closing parenthesis, I record the substring from the start of the current group to this closing parenthesis.

But wait, if the depth is zero, that means we're not inside any group, so the closing parenthesis ends the current group. But what if there are multiple groups at the same level? Then, I'll have to collect each group as I hit the closing parenthesis when depth returns to zero.

So the steps would be:

1. Remove all spaces from the input string.
2. Initialize variables:
   - result = empty list to store the groups
   - start = 0 to mark the start of a group
   - depth = 0 to track the current parentheses depth
3. Iterate over each character in the cleaned string, keeping track of the index (i).
4. For each character:
   a. If it's an opening parenthesis '(', increment depth.
   b. If it's a closing parenthesis ')':
      i. Decrement depth.
      ii. If depth is 0, it means we've closed a group. So, add the substring from start to i+1 to the result.
5. Return the result list.

Let me test this logic with the sample input.

Sample Input: '( ) (( )) (( )( ))'
After removing spaces: '(()((()))((()()))'

Wait, no. Let me recheck. The sample input is '( ) (( )) (( )( ))'. Removing spaces would result in '(()())((()))'? Wait, no, the input is '(() ) ( () () )'. Let me write it without spaces: '(()())((()))'. Wait, no, the sample input is '( ) (( )) (( )( ))', which becomes '(()())((()))'.

Wait, perhaps I should re-express the sample input correctly after removing spaces.

Original string: '( ) (( )) (( )( ))'

Removing spaces: '(()())((()))'.

Wait, that's not right. Let's see:

Original string: '( ) (( )) (( )( ))'

Let's write it without spaces:

'( )' becomes '()' when spaces are removed. Wait no, let's see:

Wait, the string is '( )' which after removing spaces is '()'?

No. The string '( )' has a space after the first parenthesis and before the closing parenthesis. Removing spaces gives us '()' which is a valid group.

Similarly, '(( ))' becomes '(())' when spaces are removed.

And '(( )( ))' becomes '((()()))' when spaces are removed? No, wait:

Wait, '(( )( ))' has spaces after the first '(', after ')', and after the second '('.

So removing spaces would give '(()())'.

So the full cleaned string is '() (()) (()())'.

Wait, no. Let me break it down:

Original string: '( ) (( )) (( )( ))'

Breaking down each part:
- '( )' → becomes '()'
- ' (( ))' → becomes '(())'
- ' (( )( ))' → becomes '((()))'

Wait, no. The original string is '( ) (( )) (( )( ))'

Let me write it as a list of characters without spaces:

The string is: '(', ')', '(', '(', ')', ')', '(', '(', ')', ')', '(', ')', ')'

So the cleaned string is '(()())((()))'.

Wait, let me see:

Original string:
' ( ) (( )) (( )( )) '

Wait, with spaces in between:

So without spaces, it's '(()())((()))'.

Wait, perhaps the sample input after removing spaces becomes '(()())((()))'?

Wait, let me write the original string:

'( ) (( )) (( )( ))'

Breaking down:

'(' ')' ' ' '(' '(' ')' ')' ' ' '(' '(' ')' ')' ' ' '(' ')' ')'

Removing spaces, we get '(()())((()))'.

So the cleaned string is '(()())((()))'.

So when processed:

- i=0: '(', depth becomes 1. Since depth is not 0, do nothing.
- i=1: ')', depth decreases to 0. Since depth is 0, we record substring from start=0 to i+1=2, which is '()'. Add to result.
- i=2: '(', depth becomes 1. Since depth is not 0, do nothing.
- i=3: '(', depth becomes 2.
- i=4: '(', depth becomes 3.
- i=5: ')', depth becomes 2.
- i=6: ')', depth becomes 1.
- i=7: ')', depth becomes 0. Since depth is 0, record substring from start=2 to i+1=8, which is '(())'. Add to result.
- i=8: '(', depth becomes 1.
- i=9: '(', depth becomes 2.
- i=10: ')', depth becomes 1.
- i=11: ')', depth becomes 0. Record substring from start=8 to i+1=12, which is '(()())'. Add to result.

So the result list is ['()', '(())', '(()())'], which matches the sample output.

Great, so the logic seems correct.

Now, let's think about edge cases:

1. Empty input: return empty list.
2. Single element: like '()', which should be in the result.
3. All elements equal: e.g., '((( )))' should be a single group.
4. Zero or negative numbers: since the input is a string, numbers are not directly relevant, but the function can handle any string with parentheses and spaces.
5. Nested groups: but the problem states that the groups are not nested, so we don't need to handle nested cases.

Wait, but in the function, should we validate that the input is a string? The function signature says it's a string, so perhaps no need to validate. But in the problem statement, it says to validate inputs and deal with invalid ones explicitly. So maybe the function should handle cases where the input is not a string, but in Python, the function is typed to accept a string.

So, in this case, the function can assume that the input is a string.

Another edge case: multiple groups at the same depth. Like '()(())'.

Wait, the string '()(())' after removing spaces is the same. Let's see:

Processing:
- i=0: '(', depth 1
- i=1: ')', depth 0 → record substring 0-2 → '()'
- i=2: '(', depth 1
- i=3: '(', depth 2
- i=4: '(', depth 3
- i=5: ')', depth 2
- i=6: ')', depth 1
- i=7: ')', depth 0 → record substring 2-8 → '(()())'

So the result is ['()', '(()())'].

But according to the problem statement, groups are not nested. So is '()(())' a valid input? The problem says that the input string can have multiple groups that are not nested. So in this case, '()(())' is valid because the first group ends before the second group starts, but the second group is not nested. Wait, no, in '()(())', the first group '()' is followed by '(())', which is a single group.

Wait, in this case, the second group starts at index 2 and is nested. So perhaps in the problem statement, the function should return ['()', '(()())'] as the result, even though the second group is not entirely contained within the first.

But according to the problem statement, the groups are not nested, so maybe the input will only contain groups that are at the same level, not nested within each other.

But the function should still correctly handle any input string, regardless of nesting.

So in our logic, even if nested groups are present, our function will correctly capture each group as per the depth approach. Because each time depth returns to zero, a new group is closed.

Wait, but the problem states that the groups are not nested. So perhaps the function can safely assume that the groups are not nested, but still, it's better to handle any string correctly, regardless of nesting, just as the problem states that the groups are not nested.

But the function doesn't need to validate whether the groups are nested or not. It's supposed to extract groups as per the input, regardless of their nesting.

Wait, the problem statement says: "Separate those groups into separate strings and return the list of those." Separate groups are balanced and not nested within each other.

So the function is only supposed to extract groups that are balanced and not nested. But the input may not be valid if it contains nested groups, but in that case, perhaps the function can ignore or handle it as per the requirements.

But according to the problem statement, the function can assume that the input is valid, meaning the groups are not nested. So perhaps we don't need to handle nested groups, but in the code, we can still process any string correctly.

So, to summarize, the approach is:

- Remove all spaces from the input string.
- Iterate through the string, track the depth of parentheses.
- When depth reaches zero after a closing parenthesis, it marks the end of a group. Record the substring from the start to the current index+1.

Now, let's implement this step by step in Python.

First, I'll import the necessary modules. The function is supposed to be a part of a module, and in the given code, it's already imported from typing as List. So I'll use that.

The function signature is given as:

from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

So, I need to write this function.

Step 1: Remove spaces from the input string.

cleaned = paren_string.replace(' ', '')

But wait, what about other whitespace characters like tabs or newlines? The problem says to ignore spaces, so perhaps only spaces are removed, not other whitespace. So I think it's safe to use .replace(' ', '').

Step 2: Initialize variables.

result = []
start = 0
depth = 0

Step 3: Iterate through each character with index.

for i, char in enumerate(cleaned):
    if char == '(':
        depth += 1
    elif char == ')':
        depth -= 1
        if depth == 0:
            # Found a group, add it to result
            group = cleaned[start:i+1]
            result.append(group)
    # else, do nothing as it's not a parenthesis

Step 4: Return the result.

return result

Putting it all together:

def separate_paren_groups(paren_string: str) -> List[str]:
    cleaned = paren_string.replace(' ', '')
    result = []
    start = 0
    depth = 0
    for i, char in enumerate(cleaned):
        if char == '(':
            depth += 1