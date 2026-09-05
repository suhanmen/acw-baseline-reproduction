from typing import List

def intersection_array(nums1: List[int], nums2: List[int]) -> List[int]:
    """Find the intersection of two arrays using lambda function."""
    return list(map(lambda x: x, filter(lambda x: x in nums2, nums1)))

# Verification (uncomment to run tests)
# assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
# assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
# assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]