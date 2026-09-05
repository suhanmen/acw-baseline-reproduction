def check_subset_list(list1, list2): 
    l1, l2 = list1[0], list2[0] 
    exist = True
    for i in list2: 
        if i not in list1: 
            exist = False
    return exist 