def check_String(str): 
    flag_l = False
    flag_n = False
    for i in str: 
        if i.isalpha(): 
            flag_l = True  
        if i.isdigit(): 
            flag_n = True
    return flag_l and flag_n 