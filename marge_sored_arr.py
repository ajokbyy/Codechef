#
# def merge(nums1, m: int, nums2, n: int) -> None:
#     last = m + n - 1
#     while m>0 and n>0:
#         if nums1[m-1] > nums2[n-1]:
#             nums1[last] = nums1[m-1]
#             m -= 1
#         else:
#             nums1[last] = nums2[n-1]
#             n -= 1
#         last -=1
#
#     while n>0:
#         nums1[last] = nums2[n-1]
#         n , last = n-1 , last - 1
#
# if __name__ == '__main__':
#     nums1 = list(map(int, input().split()))
#     print(nums1)
#     nums2 = list(map(int, input().split()))
#     print(nums2)
#
#     m = len(nums1)
#     n = len(nums2)
#
#     merge(nums1, m, nums2, n)
#     print(nums1)
#

# #-----------------------ai ans
def merge(nums1, m, nums2, n):
    # Start filling from the last index
    last = m + n - 1

    # Pointers for nums1 and nums2
    i = m - 1
    j = n - 1

    # Merge in reverse order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1
        last -= 1

    # If nums2 still has elements left
    while j >= 0:
        nums1[last] = nums2[j]
        j -= 1
        last -= 1


if __name__ == '__main__':
    print("Enter nums1 elements (space-separated):")
    nums1 = list(map(int, input().split()))

    print("Enter m (number of valid elements in nums1):")
    m = int(input())

    print("Enter nums2 elements (space-separated):")
    nums2 = list(map(int, input().split()))

    print("Enter n (number of valid elements in nums2):")
    n = int(input())

    # Extend nums1 to correct size if user did not add zeros
    while len(nums1) < m + n:
        nums1.append(0)

    merge(nums1, m, nums2, n)

    print("Merged array:")
    print(nums1)
