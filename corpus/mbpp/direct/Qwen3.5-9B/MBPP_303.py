def solve(arr, n):
    def count_inversions(arr):
        count = 0
        length = len(arr)
        for i in range(length):
            for j in range(i + 1, length):
                if arr[i] > arr[j]:
                    count += 1
        return count

    count1 = count_inversions(arr)
    count2 = count_inversions(arr[::-1])
    return count1 == count2