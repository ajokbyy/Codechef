# # Without multithreading
# import time
# def cal_square(numbers):
#     print("Calculating Square of numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("square : ", n*n)
# def cal_cube(numbers):
#     print("Calculating Cube of numbers")
#     for n in numbers:
#         time.sleep(0.2)
#         print("cube : ", n*n*n)
#
# number = [2, 4, 5, 6, 7]
# t = time.time()
# cal_square(number)
# cal_cube(number)
# print(time.time() - t)
# befor multithreading it take 2.0053677558898926 sec to compet the proh]gram
#------------------------With multithreading
import time
import threading

def cal_square(numbers):
    print("Calculating Square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square : ", n*n)
def cal_cube(numbers):
    print("Calculating Cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube : ", n*n*n)

number = [2, 4, 5, 6, 7]
t = time.time()
t1 = threading.Thread(target=cal_square, args=(number,))
t2 = threading.Thread(target=cal_cube, args=(number,))
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time() - t)

#After using multithreading it is using 1.0042247772216797