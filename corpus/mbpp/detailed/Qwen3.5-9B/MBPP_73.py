import re
from typing import List, Tuple, Any

# Sentinel object to distinguish between None and an empty string in parsing
_EMPTY_STRING_SENTINEL = object()


def _validate_and_normalize_input(text: str) -> Tuple[Any, str]:
    """
    Validates the input text and returns a tuple of (status, normalized_text).

    If the text is None, returns (None, None).
    If the text is an empty string, returns ('', '').
    Otherwise, returns the text as is (after stripping leading/trailing whitespace if desired, 
    but here we preserve exact content for regex accuracy, just checking it's a string).

    For the purposes of this specific problem based on assertions, we assume valid string inputs
    but prepare for edge cases like empty strings or None.
    """
    if text is None:
        return None, None

    if isinstance(text, str):
        return 'valid', text
    else:
        # Invalid type
        return None, None


def _extract_delimiters_from_text(text: str) -> List[str]:
    """
    Extracts potential delimiters from the text.

    In this specific problem context, the delimiters are seemingly embedded in the text 
    as specific patterns that separate logical chunks. Looking at the examples:
    'Forces of the \ndarkness*are' -> split at '\n' and '*'
    'Latest android*which' -> split at '*'
    'Certain services\nare' -> split at '\n'

    The pattern appears to be: any non-alphanumeric, non-space, non-newline character 
    acts as a delimiter, OR specific whitespace combinations act as delimiters.

    However, a closer inspection of the desired output reveals a more specific logic:
    The splits occur exactly at the boundary of a newline followed by a word, 
    or a special character (like '*') followed by a word.

    Actually, looking at the first example: 
    Input: 'Forces of the \ndarkness*are coming into the play.'
    Output: ['Forces of the ', 'darkness', 'are coming into the play.']
    Split points: before 'darkness' (after newline+space?) and before 'are' (after '*').

    Let's look at the second example:
    Input: 'Mi Box runs on the \n Latest android*which has google assistance and chromecast.'
    Output: ['Mi Box runs on the ', ' Latest android', 'which has google assistance and chromecast.']
    Split points: before ' Latest' (after newline) and before 'which' (after '*').

    Third example:
    Input: 'Certain services\nare subjected to change*over the seperate subscriptions.'
    Output: ['Certain services', 'are subjected to change', 'over the seperate subscriptions.']
    Split points: before 'are' (after newline) and before 'over' (after '*').

    Hypothesis: The delimiters are the sequences that separate the words. 
    Specifically, it seems like the problem wants us to split on whitespace/newlines/special chars 
    but keep the non-space parts as elements? No, that's too complex.

    Let's re-examine the split locations strictly.
    Ex 1: 'Forces of the ' | 'darkness' | 'are coming into the play.'
    The split happens:
    1. After ' ' (space) and before 'd' in 'darkness'. The character before is a newline.
       So pattern: `\n\s*`? 
       Wait, in 'Forces of the \ndarkness', there is a space before the newline.
       Result segment 1: 'Forces of the ' (includes the space before newline).
       Result segment 2: 'darkness' (no leading space).

    2. After 's' in 'darkness' and before 'a' in 'are'. The character is '*'.
       So pattern: `*`?
       Result segment 2: 'darkness' (no trailing space).
       Result segment 3: 'are coming...' (no leading space).

    Ex 2: 'Mi Box runs on the ' | ' Latest android' | 'which...'
    1. 'Mi Box runs on the \n Latest...' -> 'Mi Box runs on the ' + '\n ' + 'Latest...'
       Split happens after the space before newline? 
       Segment 1: 'Mi Box runs on the '
       Segment 2: ' Latest android' (starts with space).
       So the newline acts as a delimiter, but the space AFTER the newline is kept in the NEXT segment?
       Or maybe the delimiter is just the newline, and spaces are preserved naturally?

    Let's try to find a regex that matches the boundaries.
    The boundaries seem to be:
    - Newline characters (`\n`)
    - Special characters like `*`

    But we must be careful about what to keep.

    Let's look at the "tokens" logic.
    Maybe the rule is: Split on any sequence of non-alphanumeric, non-space characters?
    If we split on `\n` and `*`:
    Text 1: "Forces of the \ndarkness*are..."
    If we use `re.split(r'[\n*]', text)`, we get:
    ['Forces of the ', 'darkness', 'are coming...']
    This matches exactly!

    Text 2: "Mi Box runs on the \n Latest android*which..."
    `re.split(r'[\n*]', text)`:
    1. 'Mi Box runs on the '
    2. ' Latest android'
    3. 'which has google assistance and chromecast.'
    This matches exactly!

    Text 3: "Certain services\nare subjected to change*over..."
    `re.split(r'[\n*]', text)`:
    1. 'Certain services'
    2. 'are subjected to change'
    3. 'over the seperate subscriptions.'
    This matches exactly!

    Conclusion: The delimiter pattern is simply a newline character or an asterisk.
    We need to split the string by the regex pattern `[\n*]`.

    Edge case handling:
    - Empty string: split returns [''] or [] depending on flags. We need to handle this.
    - Single element: should return a list with the string (if no delimiters found).
    - Multiple delimiters in a row: `re.split` will produce empty strings between them.
      Does the problem specify behavior for this? The examples don't show consecutive delimiters.
      However, "defensive" code should handle this. 
      If the input is "a\n\nb", should we get ['a', '', 'b'] or ['a', 'b']?
      Given the strict requirements of "exact behavior" based on provided assertions, 
      and lack of tests for consecutive delimiters, standard `re.split` behavior (producing empty strings) 
      is the safest bet unless specified otherwise. But often in "split by delimiter" problems, 
      consecutive delimiters might imply empty segments. Let's stick to standard `re.split`.

    Wait, let's double check if there are other hidden delimiters.
    The problem says "multiple delimiters by using regex".
    The examples only show `\n` and `*`.
    Is it possible the delimiters are defined dynamically? 
    "Write a function to split the given string with multiple delimiters..."
    Usually, this phrasing implies the delimiters are part of the input or specified.
    Since no delimiters are passed as arguments, the function MUST infer them from the context or the problem assumes a fixed set based on the examples.
    Given the specificity of the assertions, the "multiple delimiters" refers to the set of characters that act as separators in these specific examples (newline and asterisk).

    Refined Plan:
    1. Validate input is not None.
    2. Define the regex pattern for delimiters: `[\n*]`.
    3. Use `re.split` with this pattern.
    4. Handle the case where the result contains empty strings (e.g., if the string starts/ends with a delimiter or has consecutive delimiters). 
       Should we filter them out? 
       Standard `split` behavior keeps them. 
       Example: `"a*b"`.split('*') -> ['a', 'b'].
       Example: `"a**b"`.split('*') -> ['a', '', 'b'].
       Given the examples don't show consecutive delimiters, we will return the raw split result.
       However, if the string is just delimiters (e.g., "\n*"), result is ['', '', ''].
       If the string is empty, `re.split` returns `['']`.
       We need to decide: if input is empty, return [] or ['']?
       In Python `"".split(',')` is `['']`. 
       But logically, splitting an empty string with no content usually yields an empty list in custom implementations, or `['']` in Python.
       Let's look at the assertion: `multiple_split('...')`.
       If we pass an empty string, what should happen?
       If I strictly follow Python's `split` behavior: `"".split('\n')` is `['']`.
       However, if we interpret "split" as "find parts separated by delimiters", an empty string has no parts.
       Given the defensive nature required, returning an empty list for an empty string is often more intuitive, 
       BUT to maintain consistency with `re.split` behavior which is the core requirement ("by using regex"), 
       we should likely mimic `re.split` exactly unless the empty string case is explicitly handled as an exception.
       Actually, `re.split` with a pattern that matches nothing returns `['']` for an empty string? 
       Let's verify mentally: `re.split(r'\n', '')` returns `['']`.
       If the problem expects `[]` for empty input, we must filter.
       If it expects `['']`, we don't.
       Without a test case for empty string, I will implement a helper to filter out empty strings IF they are the only result, 
       OR simply return the raw `re.split` result.
       Wait, looking at the examples, they produce lists of non-empty strings.
       Let's assume the goal is to extract non-empty segments if the delimiters are consecutive, 
       but preserve structure if intended.
       Actually, the most robust approach for "split by regex" is to return exactly what `re.split` returns, 
       because `re.split` is the tool requested. Any filtering would be an additional requirement not stated.
       EXCEPTION: If the input is empty string `""`, `re.split` returns `['']`. 
       Does "split the given string" imply returning the components? An empty string has no components.
       I will add a step to remove empty strings from the result list ONLY IF the input was empty or if the result consists entirely of empty strings?
       No, let's look at the examples again. They are very specific.
       Let's stick to the simplest interpretation: 
       1. Validate input.
       2. Run `re.split`.
       3. Return the list.

       BUT, wait. What if the input is just "\n"? 
       `re.split(r'[\n*]', '\n')` -> `['', '']`.
       Should this be `[]`?
       Given the instruction "Handle edge cases explicitly... empty input", 
       I should probably define behavior for empty input.
       If input is "", expected output is likely [].
       If `re.split` gives [''], we should map that to [] for the empty input case.
       What about "\n"? Returns ['', '']. Should that be []? Probably yes, as it contains no text.
       What about "a\n"? Returns ['a', '']. Should the trailing empty string be kept?
       In many split functions, trailing empty strings are kept (`"a,".split(',')` -> `['a', '']`).
       But here, since the delimiter is internal to the text structure in the examples, 
       and we are splitting logical blocks, an empty trailing block might be noise.
       However, to be "defensive" and "exact", I should probably NOT silently drop empty strings unless the input is purely delimiters.
       Actually, let's re-read the first assertion carefully.
       'Forces of the \ndarkness*are coming into the play.'
       There is no trailing delimiter.
       If we had 'Forces of the \ndarkness*are coming into the play.*', 
       would we expect a trailing empty string?
       Standard split behavior says yes.

       Decision: 
       I will implement the logic using `re.split`.
       I will handle the `None` input case by returning `None` or raising an error? 
       The problem says "Validate the inputs and deal with invalid ones explicitly".
       Returning `None` for `None` input is a safe explicit deal with.
       For empty string, I will return an empty list `[]` as a defensive measure for "no content", 
       overriding `re.split`'s `['']` for the specific case of empty input to avoid returning a list with a single empty element for nothing.
       What about `\n*`? `re.split` -> `['', '', '']`. 
       I think filtering out empty strings is a reasonable interpretation of "split text into parts" where parts must have content, 
       EXCEPT if the empty string is a valid part of the data (e.g. CSV). 
       Given the text examples, the parts are semantic chunks. 
       I will filter out empty strings from the final result list to ensure only meaningful segments are returned, 
       unless the input is empty (where we return `[]`). 
       Wait, if I filter all empty strings