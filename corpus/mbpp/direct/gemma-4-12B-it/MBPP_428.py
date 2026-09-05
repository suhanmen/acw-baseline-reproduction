def shell_sort(arr):
    """
    Sorts the given array using the Shell Sort algorithm.

    Shell sort is an optimization of insertion sort that allows the 
    exchange of items that are far apart. The elements are arranged 
    into sublists based on a gap, and each sublist is sorted using 
    insertion sort. The gap is reduced in each pass until it becomes 1.
    """
    n = len(arr)
    # Start with a large gap, then reduce the gap
    gap = n // 2

    while gap > 0:
        # Perform a gapped insertion sort for this gap size.
        # The first gap elements arr[0..gap-1] are already in gapped order
        # keep adding one more element until the entire array is gap-sorted.
        for i in range(gap, n):
            # add arr[i] to the elements that have been gap sorted.
            # save arr[i] in temp and make it-gap a gap to the element before it.
            temp = arr[i]
            j = i

            # Shift earlier gap-sorted elements up until the correct 
            # location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp

        # Reduce the gap for the next pass
        gap //= 2

    return arr

if __name__ == "__main__":
    assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
    assert shell_sort([24, 22, 39, 34, 87, 73, 68]) == [22, 24, 34, 39, 68, 73, 87]
    assert shell_sort([32, 30, 16, 96, 82, 83, 74]) == [16, 30, 32, 74, 82, 83, 96]