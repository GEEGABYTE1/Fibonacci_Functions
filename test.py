
global nums_after_decimal 

import math
def first_test(value):
    test = ((value ** 2) * 5) + 4

    test_string = str(math.sqrt(test))
    test_string_split = test_string.split(".")
    nums_after_decimal = []
    index = None 
    for i in range(len(test_string)):
        if test_string[i] == ".":
            index = i 
            break 
        else:
            continue 
    test_case = test_string[index:]
    global checker
    checker = 0
    return checker_funct(test_case, checker)

def second_test(value):
    test = ((value ** 2) * 5) - 4

    test_string = str(math.sqrt(test))
    test_string_split = test_string.split(".")
    nums_after_decimal = []
    index = None 
    for i in range(len(test_string)):
        if test_string[i] == ".":
            index = i 
            break 
        else:
            continue 
    test_case = test_string[index:]
    global checker
    checker = 0
    return checker_funct(test_case, checker)
    
    
def checker_funct(lst, checker):

    if checker == len(lst) - 1:
        return True
    else:
        for i in lst:
            if i == '0':
                checker += 1
        return checker_funct(lst, checker)


    


    