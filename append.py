def get_squared_numbers(numbers):
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number ** 2)
        # it will add the ans to the list - here we have an empty list - squared_numbers
        #for the first iteration it was empty
        
    print(squared_numbers)
    #return squared_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
get_squared_numbers(numbers)