# for i in range(1, 11):         # outer loop from 1 to 10
#     for j in range(1, 11):     # inner loop from 1 to 10
#         print(i * j)

# for i in range(1,10):
#     for j in range(1, 10):
#         print(i*j)
#
# -------------------------------------------
# patton

# 1  - squar pattan
# for i in range(6):
#     row = ""
#     for j in range(6):
#         row += "*"
#     print(row)
# ******
# ******
# ******
# ******
# ******
# ******  outpu

#2  - Store the Monthly expenses in a list and find out total expenses for all mounths -
# - tredition way -
exp = [2340, 2500, 2100, 3100, 2980]
# total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
# print(total)
total = 0
# by using for loop
for i in exp:
    total = total + i
print(total)

total = 0
#anther way to write this is
for i in range(len(exp)):
    print('month : ',(i + 1), 'Expense : ', exp[i])
    total = total + exp[i]
print('Total : ', total)



#ques -
# Search for lost car key in home and when found stop searching
key_location = "Chair"
location = ["Garage", "Livivng room", "Chair", "Closet"]
for i in location:
    if key_location == i:
        print("Key is found in ", i)
        break
    else:
        print("Key is not found in ", i)
