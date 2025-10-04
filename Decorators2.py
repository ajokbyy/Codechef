import time
def time_it(func):#Defines a decorator function
    # time_it.A decorator takes a function as input
    # (func) and returns another function (usually with extra functionality wrapped around the original).
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        #Defines an inner function wrapper inside time_it.
        # *args = collects all positional arguments into a tuple.
        # **kwargs = collects all keyword arguments into a dictionary.
        # This allows the wrapper to accept any type of arguments and pass them to the original function (func).
        print(func.__name__+ "Took" + str((end - start)*1000)+"Milliseconds")
        #Prints how long the function took.
        # func.__name__ → gets the function’s name (e.g., "cal_square" or "cal_cube").
        # (end - start) → time difference in seconds.Multiply by 1000 → convert seconds into milliseconds.
        return result
    return wrapper
@time_it
def cal_square(n):
    result = []
    for i in n:
        result.append(i**i)
    return result
@time_it
def cal_cube(n):
    result = []
    for i in n:
        result.append(i*i*i)
    return result
array = range(1, 10000)
put_square = cal_square(array)
put_cube = cal_cube(array)
