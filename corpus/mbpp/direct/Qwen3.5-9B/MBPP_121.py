def check_triplet(arr, target_sum, index, _):
    # We need to find a triplet (i, j, k) such that i < j < k and all are >= index
    # But the problem uses the array [2,7,4,0,9,5,1,3] with target_sum=8, index=0 -> returns True.
    # Likely: find three elements (not necessarily distinct values, but distinct positions)
    # whose sum equals target_sum.
    # However, the third assertion: [10,4,2,3,5], target_sum=5, index=0, returns True.
    # That means we need to find exactly three elements that sum to 5.
    # But 5 is small; the only way is 1+1+3? There is no two 1's.
    # Re-reading: maybe it's not three elements, but a triplet of (target_sum, index, something)?
    # Actually, the function signature is: check_triplet(arr, target_sum, index, _).
    # The third parameter is "index" which might be the starting index to search.
    # The fourth is unused (maybe to indicate we only need three elements total).
    # Let's try: find three elements from arr starting at 'index' that sum to 'target_sum'.
    # For [10,4,2,3,5], target_sum=5: we can have 2+3+? need 0 -> no 0. 5+0+0? no.
    # Maybe it's not three elements sum to target_sum, but something else.
    # Another possibility: the triplet is (target_sum, index, something) that satisfies some condition.
    # But the problem says "find the triplet with sum of the given array".
    # Let's look at first case: [2,7,4,0,9,5,1,3], target_sum=8, index=0 -> True.
    # Possible triplets summing to 8: (2,7,? need -1) no; (2,4,2) no duplicate 2; (2,0,6) no 6; (4,0,4) no; (9,-1) no.
    # (2,5,1) = 8 -> indices 0,5,6 -> yes.
    # Second case: [1,4,5,6,7,8,5,9], target_sum=8 -> no triplet sums to 8? 
    # (1,4,3) no 3; (1,5,2) no 2; (4,5,-1) no; (1,7,0) no; (4,?,?) ... actually (1,?,?) no.
    # (1,?,?) no 1+?+?=8 -> ?+?=7 -> (1,6,1) no duplicate 1; (1,?,?) no.
    # (4,?,?) -> ?+?=4 -> (1,3) no 3; (2,2) no.
    # (5,?,?) -> ?+?=3 -> (1,2) no 2; (3,0) no.
    # (6,?,?) -> ?+?=2 -> (1,1) no.
    # So no triplet sums to 8 -> False. Correct.
    # Third case: [10,4,2,3,5], target_sum=5 -> triplet summing to 5? 
    # (10,?,?) no; (4,?,?) -> ?+?=1 -> no; (2,?,?) -> ?+?=3 -> (2,3) no duplicate 2 and 3? 
    # We have 2 and 3, but need three elements: 2+3+? = 5 -> ?=0 -> no 0.
    # (2,?,?) no other combo. 
    # Wait, maybe it's not three elements from the array, but including the index?
    # Or maybe the "triplet" is (arr[i], arr[j], arr[k]) where i, j, k are not necessarily from the array but positions?
    # Another thought: maybe the function checks if there exists an i, j, k such that:
    # arr[i] + arr[j] + arr[k] == target_sum AND i > index, j > index, k > index?
    # For third case: [10,4,2,3,5], index=0, target_sum=5.
    # Elements after index 0: all of them.
    # Triplets: 4+2+? need -1 no; 4+3+? need -2 no; 4+5+? need -4 no; 2+3+? need 0 no; 2+5+? need -2 no; 3+5+? need -3 no.
    # So no triplet sums to 5? But assertion says True.
    # Unless the triplet can include duplicates? But array has unique values? 
    # Or maybe the triplet is not three elements from the array, but (index, something, something)?
    # Let's reconsider: maybe the "triplet" is (target_sum, index, some_value) that satisfies some property?
    # But the problem says "find the triplet with sum of the given array".
    # Another idea: maybe it's about finding three indices i, j, k such that:
    # arr[i] + arr[j] + arr[k] == target_sum AND i, j, k are distinct and >= index.
    # For third case: [10,4,2,3,5], target_sum=5, index=0.
    # The only way to get 5 is if we use 5 itself and two zeros? But no zeros.
    # Unless we can use the same element twice? But that would be unusual for "triplet".
    # Wait, what if the triplet includes the value at 'index'? 
    # For third case: index=0, arr[0]=10. Then 10 + ? + ? = 5 -> ?+?=-5 impossible.
    # This is confusing.
    # Let's look at the third assertion again: [10,4,2,3,5], 5, 15, 0 -> True.
    # Note: target_sum=5, index=15 (which is out of bounds for array of length 5).
    # Ah! The third parameter is 'index' but in the third assertion it's 15, which is greater than the array length.
    # So maybe the condition is that there exist three indices i, j, k such that:
    # i, j, k are >= 'index' AND arr[i] + arr[j] + arr[k] == target_sum.
    # For third case: index=15, which is > 4 (array length). So there are no indices >=15.
    # Therefore, no triplet exists? But assertion says True.
    # Unless the condition is that if there are no valid indices, then it returns True? That doesn't make sense.
    # Another possibility: the 'index' parameter is actually the starting position, but if it's out of bounds, 
    # we consider the whole array? Or maybe the function is supposed to return True if no valid triplet exists? 
    # But the second assertion returns False when no triplet exists.
    # Let's re-read the third assertion: [10,4,2,3,5], 5, 15, 0 -> True.
    # What if the 'index' parameter is not the starting index but something else? Like the value to match?
    # Or maybe the function is to find a triplet (i, j, k) such that:
    # arr[i] + arr[j] + arr[k] == target_sum AND the index of the triplet (min(i,j,k)) is equal to the third parameter?
    # For third case: target_sum=5, index=15 -> no index 15 in array (length 5). So impossible.
    # This is very confusing.
    # Let's try a different approach: maybe the 'index' parameter is actually the number of elements to consider from the end?
    # Or maybe it's a red herring and we should ignore it? But the first two assertions use 0.
    # Another idea: perhaps the function is to find a triplet of (target_sum, index, some_value) such that:
    # some_value = arr[index] and there exist i, j such that arr[i] + arr[j] + arr[index] == target_sum?
    # For first case: arr[0]=2, then need two elements summing to 6: (7,-1) no; (4,2) yes -> indices 2 and 0? But 0 is used.
    # (0,6) no 6; (9,-3) no; (5,1) -> arr[5]=5, arr[6]=1 -> 2+5+1=8 -> yes.
    # For second case: arr[0]=1, need two elements summing to 7: (4,3) no 3; (5,2) no 2; (6,1) duplicate 1? 
    # We have 1 at index 0, but can we use it again? If yes, then 1+1+6=8 -> indices 0,0,3? But indices must be distinct?
    # If distinct indices: 1+?+?=8 -> ?+?=7 -> (6,1) but 1 is already used -> so (6,?) need 1 -> no other 1.
    # (5,2) no 2; (4,3) no 3; (7,0) no 0; (8,-1) no. So no triplet -> False. Correct.
    # For third case: arr[0]=10, need two elements summing to -5 -> impossible. But assertion says True.
    # Unless we don't use arr[0]. Maybe the 'index' parameter is the starting index for the search, not a value to include.
    # For third case: index=15, which is out of bounds. So we search from min(len(arr), index) = 5? 
    # But 5 is out of bounds. So no elements to search? Then no triplet -> should be False, but it's True.
    # This suggests that if the start index is out of bounds, we return True? But that contradicts the logic.
    # Wait, what if the 'index' parameter is actually the target_sum for a different condition? 
    # Or maybe the function is to find a triplet of indices (i, j, k) such that:
    # i + j + k == target_sum? 
    # For first case: target_sum=8, index=0. Find i+j+k=8 with i,j,k >=0. Many solutions, e.g., 0+3+5=8 -> arr[0]=2, arr[3]=0, arr[5]=5 -> 2+0+5=7 !=8.
    # But if the condition is on indices sum, not values.
    # For first case: indices sum to 8: e.g., 0+3+5=8 -> values 2+0+5=7 !=8.
    # But the problem says "sum of the given array", so likely values.
    # Let's try: maybe the 'index' parameter is the starting index, and we need three elements from that point onward that sum to target_sum.
    # For third case: index=15, start from min(5,15)=5, which is out of bounds -> no elements -> no triplet -> should be False, but it's True.
    # Unless the function returns True when no triplet exists? But second case returns False when no triplet exists.
    # This is inconsistent.
    # Another possibility: the 'index' parameter is the value that must be included in the triplet?
    # For third case: index=15, but 15 is not in the array [10,4,2,3,5]. So cannot include 15. But returns True.
    # Maybe it's the number of elements to skip? 
    # Skip 15 elements -> start from index 15 mod 5 = 0? Then search from 0: same as before.
    # I think there's a mistake in my understanding.
    # Let's look at the third assertion again: [10,4,2,3,5], 5, 15, 0 -> True.
    # What if the 'index' parameter is not used at all? And the function is to find ANY triplet that sums to target_sum?
    # For third case: [10,4,2,3,5], target_sum=5 -> is there any triplet? 
    # 10+4+2=16, 10+4+3=17, 10+4+5=19, 10+2+3=15, 10+2+5=17, 10+3+5=18, 4+2+3=9, 4+2+5=11, 4+3+5=12, 2+3+5=10.
    # None sum to 5. So should be False, but it's True.
    # This suggests that the condition is not on the sum of three elements.
    # Maybe it's on the sum of two elements equal to the third? 
    # For third case: 2+3=5 ->