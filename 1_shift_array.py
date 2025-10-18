a = [3, 4, 5, 2, 6]

print(a)

temp = a[0]
n = len(a)
for i in range(1, n):
    a[i-1] = a[i]
a[n-1] = temp

print(a)

# ---------------------------------------cpp - code -----------------------------
# # include <iostream>
# using
# namespace
# std;
# int
# main()
# {
#     int
# arr[5] = {1, 3, 4, 5, 6};
# // int
# n = arr.size();
# int
# n = sizeof(arr) / sizeof(arr[0]);
#
# for (int i= 0; i < n; i++)
# {
#     cout << arr[i] << "\n";
# }
#
# int
# temp = arr[0];
#
# for (int i = 1; i < n; i++)
# {
#     arr[i - 1] = arr[i];
# }
# arr[n - 1] = temp;
# cout << "After the rotation - " << "\n";
# for (int i= 0; i < n; i++)
# {
#     cout << arr[i] << "\n";
# }
# }