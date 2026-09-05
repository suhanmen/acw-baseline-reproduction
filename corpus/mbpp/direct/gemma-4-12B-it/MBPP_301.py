def dict_depth(d):
    """
    Finds the maximum depth of a nested dictionary.
    A dictionary with no nested dictionaries has a depth of 1.
    An empty dictionary has a depth of 1.
    """
    if not isinstance(d, dict) or not d:
        return 1

    max_depth = 0
    for value in d.values():
        if isinstance(value, dict):
            max_depth = max(max_depth, dict_depth(value))
        else:
            max_depth = max(max_depth, 1)

    return 1 + max_depth if max_depth > 0 else 1

# The recursive logic needs to handle the base case correctly.
# Let's refine it to match the specific assertions.
def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    if not d:
        return 1

    depths = []
    for v in d.values():
        if isinstance(v, dict):
            depths.append(dict_depth(v))
        else:
            depths.append(1)

    return 1 + max(depths) if depths else 1

# Re-verifying the assertions logic:
# {'a':1, 'b': {'c': {'d': {}}}}
# d={} -> 1
# c:{d: {}} -> 1 + 1 = 2
# b:{c: {d: {}}} -> 1 + 2 = 3
# a:{b: ...} -> 1 + 3 = 4. Correct.

# {'a':1, 'b': {'c':'python'}}
# c:'python' -> 1
# b:{c:'python'} -> 1 + 1 = 2
# a:{b: ...} -> 1 + 2 = 3? No, wait.
# Let's re-evaluate the logic.
# If the value is NOT a dict, it contributes 0 to the nesting level.

def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    if not d:
        return 1

    max_sub_depth = 0
    for v in d.values():
        if isinstance(v, dict):
            max_sub_depth = max(max_sub_depth, dict_depth(v))
        else:
            max_sub_depth = max(max_sub_depth, 0)

    return 1 + max_sub_depth

# Final check:
# {'a':1, 'b': {'c':'python'}}
# b.values() -> 'python' (not dict) -> max_sub = 0 -> depth = 1 + 0 = 1 ? 
# No, if 'c' is inside 'b', 'b' is a dict.
# Let's trace:
# dict_depth({'c':'python'}) -> max_sub = 0 (since 'python' is not dict) -> returns 1 + 0 = 1.
# dict_depth({'b': {'c':'python'}}) -> max_sub = dict_depth({'c':'python'}) = 1 -> returns 1 + 1 = 2.
# dict_depth({'a':1, 'b': {'c':'python'}}) -> max_sub = max(0, 2) = 2 -> returns 1 + 2 = 3?
# Wait, the assertion says 2.
# This means if a value is NOT a dict, it doesn't count as a level.
# Let's re-trace assertion 2: {'a':1, 'b': {'c':'python'}}
# 'a' value is 1 (depth 0)
# 'b' value is {'c':'python'}
#   'c' value is 'python' (depth 0)
#   dict_depth({'c':'python'}) should be 1.
#   dict_depth({'b':...}) should be 1 + 1 = 2.
#   dict_depth({'a':1, 'b':...}) should be 1 + 2 = 3.
# The only way to get 2 is if the top level dict is NOT counted or 
# if the values that are not dicts are treated as depth 0 and the 
# presence of the key matters.

# Let's try:
def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    if not d:
        return 1

    max_d = 0
    for v in d.values():
        if isinstance(v, dict):
            max_d = max(max_d, dict_depth(v))

    return 1 + max_d

# Trace assertion 2 again: {'a':1, 'b': {'c':'python'}}
# dict_depth({'c':'python'}) -> max_d = 0 -> returns 1 + 0 = 1
# dict_depth({'b': {'c':'python'}}) -> max_d = 1 -> returns 1 + 1 = 2
# dict_depth({'a':1, 'b': {'c':'python'}}) -> max_d = 2 -> returns 1 + 2 = 3.
# Still 3. Why is it 2?
# Maybe the root dictionary doesn't count? No, then 1 would be 0.
# Maybe it's the number of nested dictionaries?
# {'a':1, 'b': {'c': {'d': {}}}} -> b, c, d are dicts. Total 3? No, assertion says 4.
# The only way {'a':1, 'b': {'c':'python'}} is 2 is if the top level is ignored
# OR if 'a':1 doesn't count as a level and 'b' is the first level.
# Wait! If 'b' is a dict, its depth is 1. If 'c' is a dict, its depth is 1.
# In {'a':1, 'b': {'c':'python'}}, the only nested dict is {'c':'python'}.
# That is 1 nested dict. If the root is level 1, total is 2.
# In {'a':1, 'b': {'c': {'d': {}}}}, the nested dicts are {'c':...}, {'d':{}}, and {}.
# That is 3 nested dicts. If the root is level 1, total is 4.
# In {1: 'Sun', 2: {3: {4:'Mon'}}}, the nested dicts are {3:...} and {4:'Mon'}.
# That is 2 nested dicts. If the root is level 1, total is 3.
# This works! So the rule is: 1 + max(depth of values that are dicts, else 0).

# Wait, that's what my code does. Let's re-trace {'a':1, 'b': {'c':'python'}}
# dict_depth({'c':'python'}) -> max_d = 0 (since 'python' is not dict) -> returns 1 + 0 = 1
# dict_depth({'b': {'c':'python'}}) -> max_d = 1 -> returns 1 + 1 = 2
# dict_depth({'a':1, 'b': {'c':'python'}}) -> max_d = 2 -> returns 1 + 2 = 3.
# I keep getting 3. Let me look at the dict again.
# {'a':1, 'b': {'c':'python'}}
# The only dicts are the root and {'c':'python'}.
# If root is 1 and {'c':'python'} is 1, and it's nested, it should be 2.
# My code:
# dict_depth({'c':'python'}) -> v='python' (not dict), max_d=0, returns 1+0=1
# dict_depth({'b': {'c':'python'}}) -> v={'c':'python'} (is dict), max_d=dict_depth({'c':'python'})=1, returns 1+1=2
# dict_depth({'a':1, 'b': {'c':'python'}}) -> v=1 (not dict), v={'c':'python'} (is dict), max_d=max(0, 2) = 2, returns 1+2=3.
# Ah! The 'b' in the root dictionary IS a dict.
# So dict_depth({'b': {'c':'python'}}) is indeed 2.
# Then dict_depth({'a':1, 'b': {'c':'python'}})
# Here, 'b' is a key whose value is a dict.
# That dict is {'c':'python'}.
# So dict_depth(value_of_b) is dict_depth({'c':'python'}) which is 1.
# So max_d = 1.
# Result = 1 + 1 = 2.
# YES! The logic is correct. The mistake was my manual trace.

def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 1

    max_sub_depth = 0
    for v in d.values():
        if isinstance(v, dict):
            max_sub_depth = max(max_sub_depth, dict_depth(v))

    return 1 + max_sub_depth