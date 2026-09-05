def comb_sort(lst):
    if len(lst) <= 1:
        return lst

    gap = len(lst)
    shrink_factor = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink_factor)
        if gap < 1:
            gap = 1

        swapped = False

        i = 0
        while i + gap < len(lst):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
            i += 1

    return lst