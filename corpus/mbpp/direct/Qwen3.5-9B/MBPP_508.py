def same_order(lst1, lst2):
    if not lst1:
        return True
    index = 0
    for item in lst2:
        if item == lst1[0]:
            index = 1
            break
        index += 1
    for i in range(1, len(lst1)):
        if lst1[i] not in lst2[index:]:
            return False
        current_index = lst2.index(lst1[i], index)
        if current_index <= index:
            return False
        index = current_index + 1
    return True

if __name__ == "__main__":
    assert same_order(["red","green","black","orange"],["red","pink","green","white","black"])==True
    assert same_order(["red","pink","green","white","black"],["white","orange","pink","black"])==False
    assert same_order(["red","green","black","orange"],["red","pink","green","white","black"])==True