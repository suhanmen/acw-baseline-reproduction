def get_Inv_Count(arr, n):
    """
    Counts the number of inversions in an array using a merge sort based approach.
    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].
    """
    def merge_and_count(temp_arr, left, mid, right):
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0

        while i <= mid and j <= right:
            if temp_arr[i] <= temp_arr[j]:
                arr[k] = temp_arr[i]
                i += 1
            else:
                # There is an inversion because temp_arr[i] > temp_arr[j]
                # Since the left subarray is sorted, all elements from 
                # temp_arr[i] to temp_arr[mid] are greater than temp_arr[j]
                arr[k] = temp_arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            arr[k] = temp_arr[i]
            i += 1
            k += 1

        while j <= right:
            arr[k] = temp_arr[j]
            j += 1
            k += 1

        # Copy back to temp_arr for the next merge step
        for idx in range(left, right + 1):
            temp_arr[idx] = arr[idx]

        return inv_count

    def merge_sort_and_count(temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            inv_count += merge_sort_and_count(temp_arr, left, mid)
            inv_count += merge_sort_and_count(temp_arr, mid + 1, right)
            inv_count += merge_and_count(temp_arr, left, mid, right)

        return inv_count

    # Create a copy to avoid modifying the original list if desired, 
    # though the logic here modifies the local 'arr' reference.
    working_arr = list(arr)
    temp_arr = list(working_arr)
    return merge_sort_and_count(temp_arr, 0, n - 1)