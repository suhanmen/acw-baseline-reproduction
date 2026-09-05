Okay, so I need to write a Python function called multiple_split that splits a string using multiple delimiters. Hmm, the requirements mention that it should use regex, so I need to think about how to handle multiple delimiters.

First, I remember that Python's re.split function can use regular expressions to split strings. But by default, re.split splits on every occurrence of a pattern, which can include any character in the pattern. But I don't want that. I just want to split on the delimiters, and keep the delimiters themselves as separate elements.

Wait, no. The examples show that the delimiters are not included in the result. For example, in the first example, 'Forces of the \n...' becomes ['Forces of the ', 'darkness', 'are coming into the play.']. So the newline is removed from the result.

So I need to split the string into parts whenever any of the delimiters appear. The delimiters can be any of the characters in the regex pattern. But to make sure that the delimiters themselves are not included in the result, I need to use a regex pattern that matches the delimiters, and capture the delimiters as separate groups so that they are excluded from the result.

Wait, no. If I split on the delimiters, then the split parts are the text between the delimiters, and the delimiters themselves are not included. So I can use re.split with a pattern that matches any of the delimiters. But I also need to make sure that the delimiters are considered as separate elements. Hmm, no. Looking at the examples, the delimiters are removed from the result entirely.

Wait, but the examples don't include any delimiters in the output. So the goal is to split the string into parts wherever any delimiters appear, without including the delimiters in the result.

Wait, no. Let's look at the first example: 'Forces of the \ndarkness*...' becomes ['Forces of the ', 'darkness', 'are coming into the play.']. So the newline and asterisk are removed from the result.

So the function needs to split the string into parts using any of the delimiters, and remove the delimiters from the result.

But what exactly are the delimiters? The problem statement says "multiple delimiters," but doesn't specify which ones. In programming, common delimiters include spaces, tabs, newlines, and special characters like *, +, etc.

So perhaps the delimiters are any whitespace characters, asterisks, and other common separators.

Wait, the examples use backslash and asterisk as delimiters. So I need to consider these as delimiters.

But in the examples, the function treats backslash and asterisk as delimiters. So I need to write a regex that matches these delimiters.

But wait, what about other characters? How do I define the delimiters? Maybe the delimiters are any whitespace characters and asterisks.

Wait, in the problem statement, the user is using multiple delimiters. So perhaps the function should split on any whitespace and any asterisk.

But let me think about the problem again. The function should split the string into parts wherever any delimiter appears, and return those parts without the delimiters.

So the approach is:

1. Split the string into tokens whenever any delimiter appears.
2. Exclude the delimiters from the result.
3. Handle all edge cases, such as empty strings, single delimiters, multiple delimiters, etc.

First, I need to define what constitutes a delimiter. Since the examples include \n, \ , and * as delimiters, I can consider whitespace characters (space, tab, newline) and asterisk (*) as delimiters.

So the pattern would be [ \t\n\r\*] to match any whitespace or asterisk.

But wait, in regex, \s matches any whitespace character, including spaces, tabs, newlines, etc. So I can use \s* to match any whitespace, and \* to match asterisks.

Wait, but the union of \s and \* would capture all whitespace and asterisks as delimiters.

So the regex pattern would be (\s*|\*), but actually, since \s already includes spaces, tabs, newlines, etc., but does not include asterisks, I can combine them using |.

Wait, but in regex, \s matches any whitespace, and \* matches an asterisk. So the pattern would be [ \t\n\r\*], but it's more efficient to use \s|\*.

Wait, but in regex, \s matches any whitespace character, and \* matches an asterisk. So the pattern can be written as (\s+|\*). Or perhaps just [ \t\n\r\*].

But to cover all whitespace, I can use \s and include the asterisk separately.

Wait, but in the pattern, \s matches any whitespace, and \* matches an asterisk. So I can write the pattern as [ \t\n\r\*], but that's redundant because \s already includes \t, \n, \r. So perhaps it's better to write \s|\*.

Wait, no. Because \s matches any whitespace, including \n, \t, \r, space, etc., but does not include the asterisk. So to match either any whitespace or an asterisk, I can write \s|\*.

But in regex, when using |, the order matters. So perhaps using (\s|\*).

Alternatively, I can write [\s*], but that's not correct because [\s] is not valid. The correct way is to use [ \t\n\r\*].

Alternatively, I can use \s|\*.

So the pattern would be re.split(r'(\s+|\*)', string). But wait, I want to split on any whitespace or asterisk, and remove the delimiters from the result.

Wait, but I need to split on any occurrence of a delimiter, which is any whitespace or asterisk, and the resulting list should not contain any delimiters.

So perhaps the approach is to split the string into parts using the regex pattern that matches any delimiter, and then filter out any empty strings from the result.

Wait, but in the examples, the function returns an empty string as a possible element? No, looking at the examples, the input starts with a space, and the first element is 'Forces of the ', which is the part before the first delimiter. So perhaps empty strings are allowed as elements if they occur at the start or end.

But in the examples, the outputs do not include empty strings. So perhaps I need to filter them out.

Wait, let's look at the examples again.

First example: 'Forces of the \n...' becomes ['Forces of the ', 'darkness', 'are coming into the play.']. The split happens on \n, so the first part is 'Forces of the ', and the rest is 'darkness', etc. So no empty strings.

Second example: 'Mi Box runs on the \n ...' becomes ['Mi Box runs on the ', ' Latest android', ...]. Again, no empty strings.

Third example: 'Certain services\n ...' becomes ['Certain services', ...]. So no empty strings.

So perhaps I don't need to worry about leading or trailing empty strings. But if the string starts with a delimiter, like '\nhello', the first element would be an empty string. So I should include that.

Wait, but in the examples, it's not the case. Maybe the function should return all parts, including empty strings if they occur at the beginning or end.

So perhaps the approach is to split the string into parts using the delimiters, including any empty strings that result from leading or trailing delimiters.

So, in code, I can use re.split with a pattern that matches any delimiter, and then process the result to remove empty strings if necessary.

But wait, the examples show that empty strings are not included. So perhaps the function should return the non-empty parts.

So the steps are:

1. Define the delimiter pattern: any whitespace character (\s) or asterisk (\*).
2. Split the input string using re.split with this pattern.
3. Filter out any empty strings from the result.
4. Handle any other edge cases, such as when the string is empty, or contains only delimiters, etc.

Wait, but in the examples, the function returns the non-empty parts. So I think it's safe to split and then filter out empty strings.

But what about cases where multiple delimiters are adjacent? For example, 'hello  *world' would split into ['hello', '', 'world'] if the split is on whitespace or asterisks. But I want to treat any sequence of delimiters as a single split.

So perhaps I should use a positive lookbehind or lookforward to prevent splitting on consecutive delimiters.

Alternatively, I can split on one or more delimiters at a time.

So the pattern could be ([\s*]+), which matches one or more whitespace or asterisks.

So re.split(r'[\s*]+', string) would split the string on any sequence of whitespace or asterisks.

This way, multiple consecutive delimiters are treated as a single delimiter, and only the text in between is included.

But then, I need to remove empty strings from the result.

Wait, let's see.

For example, for the string 'a**b', the split on ** would result in ['a', 'b'].

For the string 'a \nb\tc', the split on \s+ would result in ['a', 'b', 'c'].

But in the first example, the input is 'Forces of the \n...' which includes a single newline. So re.split(r'[\s*]+', string) would split it into ['Forces of the ', 'darkness', ...], which is correct.

Wait, no. Because the pattern [\s*]+ matches any combination of whitespace or asterisks, including a single newline or a single asterisk.

Wait, but the split pattern would capture any sequence of whitespace or asterisks as a delimiter, so the split would occur on any such sequence.

So the function would return the parts between these sequences.

But in the first example, the string is 'Forces of the \n...', so the split would be on \n, resulting in ['Forces of the ', 'darkness', ...], which is correct.

Wait, no. Let me test it.

If I have 'hello\nworld', and I split on [\s*]+, then it would split into ['hello', 'world'].

If I have 'hello \n world', it would split into ['hello', 'world'].

If I have 'hello\tworld', it would split into ['hello', 'world'].

If I have 'hello***world', it would split into ['hello', 'world'].

So yes, using [\s*]+ as the pattern captures any combination of whitespace or asterisks as a single delimiter.

So the code would be:

import re

def multiple_split(string):
    # Split the string on any sequence of whitespace or asterisks
    parts = re.split(r'[\s*]+', string)
    # Filter out any empty strings from the result
    result = [p for p in parts if p]
    return result

But wait, let's test this against the examples.

First example:

multiple_split('Forces of the \ndarkness*are coming into the play.')

Split on \n, resulting in ['Forces of the ', 'darkness*are coming into the play.'].

But the expected output is ['Forces of the ', 'darkness', 'are coming into the play.'].

Wait, so the asterisk is part of the delimiter in the first example. But in the string, after the newline, the next part is 'darkness*...', but the expected output is 'darkness' followed by 'are coming...'.

So my current approach is incorrect because it's not splitting on the asterisk.

Wait, no. Because in the pattern [\s*]+, the asterisk is considered a delimiter. So in the string 'darkness*are', the split would occur at the asterisk, resulting in ['darkness', 'are'].

But in the first example, the expected output is ['Forces of the ', 'darkness', 'are coming into the play.'], which is correct.

So the function needs to split on both whitespace and asterisks.

Wait, but in the first example, the string after the newline is 'darkness*...', and the expected output is to split on the asterisk as well.

So my current code is correct because it splits on both the newline and the asterisk.

Wait, but let's see: re.split(r'[\s*]+', string) would split on any sequence of whitespace or asterisks, regardless of which comes first.

So for 'a*b c', the split would be ['a', 'b c'] because it splits on the *.

Wait, no. Because the pattern is [\s*]+, which matches any combination. So if I have 'a*b', it would split into 'a' and 'b' because it splits on the *.

Wait, let me test:

Test string: 'a*b c'

Pattern: [\s*]+

Split: the string is 'a*b c'

The split occurs at the * between a and b, resulting in ['a', 'b c'].

Which is what we want.

Similarly, in the first example, the string after the newline is 'darkness*are coming...'. So the split occurs at *, resulting in 'darkness' and 'are coming...'.

Which matches the expected output.

So the function seems to be handling that correctly.

But wait, let's look at the third example: 'Certain services\nare subjected to change*over the seperate subscriptions.'

The expected output is ['Certain services', 'are subjected to change', 'over the seperate subscriptions.'].

So the string has a newline and an asterisk after 'change'.

The code splits on the newline and the asterisk, resulting in ' Certain services', 'are subjected to change', 'over the...'.

But the expected output has 'Certain services' without the space. Wait, no. Looking at the input: 'Certain services\nare subjected to change*over the seperate subscriptions.'

So after the newline, the string is 'are subjected to change*over the...'. So the split occurs at the asterisk, resulting in 'are subjected to change' and 'over the...'.

Which matches the expected output.

So the code seems to handle that correctly.

Wait, but what about if the string starts with a delimiter? For example, '*hello'.

The code would split into ['',