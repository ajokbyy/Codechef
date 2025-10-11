# import multiprocessing
#
# # from docutils.nodes import target
#
# result = []
#
# def calc_square(numbers):
#     global result
#     for n in numbers:
#         result.append(n*n)
#     print("Inside Process : " + str(result))
#
#
# if __name__ == "__main__":
#     numbers = [1,2,3,4,5]
#     p = multiprocessing.Process(target = calc_square, args = (numbers, ))
#     p.start()
#     p.join()
#
#     print("Outside process : "+ str(result))
#so for overcome this problem of not able to share data in mutiprocesses we use
# many ways
#   Method 1 - using Array
import multiprocessing
def calc_square(numbers, result):
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    result = multiprocessing.Array('i', 5)
    p = multiprocessing.Process(target = calc_square, args = (numbers, result ))
    p.start()
    p.join()
    print(result[:])

