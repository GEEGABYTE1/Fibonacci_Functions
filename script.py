
def gameplay():
    print("Type 1 if you would like to see a specific amount of numbers in the fibonacci series ")
    print("Type 2 if you would like to see a fibonacci series from a certain minimum number ")
    print("Type 3 if you would like to see a fibonacci series from a range of a min number to a max number ")
    prompt = input()

    if prompt == str(1):
        number = int(input("Please type in the amount of values you would like to see from the series: "))
        for i in range(number):
            print(fibonacci_series(i))
    elif prompt == str(2):
        amount = int(input("Please type in the amount of values you would like to see from the series: "))
        min_number = int(input("Please type in the min value you would like to see the series start from: "))

        for i in range(amount):
            print(fibonacci_series_min(amount, minimum=min_number))



