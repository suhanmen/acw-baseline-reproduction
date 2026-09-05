def count_samepair(list1, list2, list3):
    """
    Counts the number of elements that are common across all three lists.
    Looking at the assertions provided:
    1. [1,2,3,4,5,6,7,8], [2,2,3,1,2,6,7,9], [2,1,3,1,2,6,7,9] -> Common: {1,2,3,6,7} -> Result 3? 
    Wait, the logic must be "pairs" or specific positions? 
    Let's re-examine the assertions:
    1. list1, list2, list3: Common values are 1, 2, 3, 6, 7. (Count 5). The expected result is 3.
    Wait, let's look for exact matches at the same index.
    Indices for test 1:
    Idx 0: 1, 2, 2 (No)
    Idx 1: 2, 2, 1 (No)
    Idx 2: 3, 3, 3 (Yes)
    Idx 3: 4, 1, 1 (No)
    Idx 4: 5, 2, 2 (No)
    Idx 5: 6, 6, 6 (Yes)
    Idx 6: 7, 7, 7 (Yes)
    Idx 7: 8, 9, 9 (No)
    Total matches = 3. Correct.

    Test 2:
    Idx 0: 1, 2, 2 (No)
    Idx 1: 2, 2, 1 (No)
    Idx 2: 3, 3, 3 (Yes)
    Idx 3: 4, 1, 1 (No)
    Idx 4: 5, 2, 2 (No)
    Idx 5: 6, 6, 6 (Yes)
    Idx 6: 7, 7, 7 (Yes)
    Idx 7: 8, 8, 8 (Yes)
    Wait, the expected result is 4. 
    Let's check indices again:
    Test 2: [1,2,3,4,5,6,7,8], [2,2,3,1,2,6,7,8], [2,1,3,1,2,6,7,8]
    Pos 2: 3, 3, 3 (1)
    Pos 5: 6, 6, 6 (2)
    Pos 6: 7, 7, 7 (3)
    Pos 7: 8, 8, 8 (4)
    Total matches = 4. Correct.

    Test 3:
    [1,2,3,4,2,6,7,8], [2,2,3,1,2,6,7,8], [2,1,3,1,2,6,7,8]
    Pos 2: 3, 3, 3 (1)
    Pos 4: 2, 2, 2 (2)
    Pos 5: 6, 6, 6 (3)
    Pos 6: 7, 7, 7 (4)
    Pos 7: 8, 8, 8 (5)
    Total matches = 5. Correct.

    Conclusion: The function counts indices where the value is the same in all three lists.
    """
    count = 0
    # Use zip to iterate through the elements of all three lists simultaneously
    for a, b, c in zip(list1, list2, list3):
        if a == b == c:
            count += 1
    return count