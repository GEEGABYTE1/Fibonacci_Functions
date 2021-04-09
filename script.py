import math
from test import first_test
from test import second_test

global lst 
lst = []

def gameplay():
    playing = True 
    while playing:
        print("Type 1 if you would like to see a specific amount of numbers in the fibonacci series ")
        print("Type 2 if you would like to see a fibonacci series from a certain minimum number ")
        print("Type 3 if you would like to see a fibonacci series from a range of a min number to a max number ")
        print("Type 4 if you would like find a certain value in the series: ")
        prompt = input()

        if prompt == str(1):
            number = int(input("Please type in the amount of values you would like to see from the series: "))
            for i in range(number):
                lst.append(fibonacci_series(i))
                #print(fibonacci_series(i))
            print(traverse_list(lst))
            
            
        elif prompt == str(2):
            amount = int(input("Please type in the amount of values you would like to see from the series: "))
            min_number = int(input("Please type in the min value you would like to see the series start from: "))
            global new_lst
            new_lst = []
            

            for i in range(amount):
                new_lst.append(fibonacci_series(i))
            
            if not min_number in new_lst:
                print("That value is not in the range you have provided! ")
            
            else:
                index = None 
                for i in range(len(new_lst)):
                    if new_lst[i] == min_number:
                        index = i 
                        break
                    else:
                        continue 
            
                new_lst = new_lst[index: ]
                print(traverse_list(new_lst))
        
        elif prompt == str(3):
            amount = int(input("Please type in the amount of values you would like to see from the series: "))
            min_number = int(input("Please type in the min value you would like to see the series start from: "))
            max_number = int(input("Please type in the max value you would like to see the series end at: "))

            lst = []
            for i in range(amount):
                lst.append(fibonacci_series(i))
            
            if not min_number in lst:
                print("That value is not in the range you have provided! ")
                print(traverse_list(lst))
            
            elif not max_number in lst:
                print("That value is not in the range you have provided! ")
                print(traverse_list(new_lst))
            else:
                start_index = None 
                end_index = None 
                for i in range(len(lst)):
                    if lst[i] == min_number:
                        start_index = i 
                    elif lst[i] == max_number:
                        end_index = i 
                    else:
                        continue 
                lst = lst[start_index: end_index]
                print(traverse_list(lst))

        elif prompt == str(4):
            value = int(input('Please type in a value you would like to find: '))
        
            if first_test(value) == True or second_test(value) == True:
                term = 1

                while fibonacci_series(term) != value:
                    if fibonacci_series(term) == value:
                        break
                    else:
                        print(fibonacci_series(term))
                        term += 1
                

                print("Value found {} at term {}".format(fibonacci_series(term), term))
            else:
                print("That value is not a fibonacci value")
        
        elif prompt == "/quit":
            break 
        
        else:
            print("That does not seem to be a correct input! ")
def fibonacci_series(n):
    if n == 1:
        return n
        
    elif n == 0:
        return n
    
    n = fibonacci_series(n - 1) + fibonacci_series(n - 2)
    return n

def traverse_list(lst):
    if len(lst) == 0:
        return 
    return traverse_list(lst[:-1])
    

gameplay()



