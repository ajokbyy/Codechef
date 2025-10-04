d = {"Raj":7000, "Rob":4000, "mih":60000}
print(d)
# d["Raj"]

#Add element in dis
d["Ola"] = 5000
# print(d["Raj"])

d["rik"] = 5000


for key in d:
    print(key, d[key])

print("--------------------------- method 2 -----------------")
#another methad to itreat is
for k, i in d.items():
    print(k, i)

#del element

del d["Ola"]
for k, i in d.items():
    print("After the delet:",k, i)


# Check the elemt is present or not
print("Raj" in d)


#We cal also clear our dir- means we can make it empty
d.clear()
print(d)





# #merge two directores -
# dict1 = {"story": "Handled NASA India crowd smoothly"}
# dict2 = {"skills": "Leadership, Problem-solving, Adaptability"}
# dict1.update(dict2)
# print(dict1)
#
#
#
# merg_dir = dict1| dict2
# print(merg_dir)
#
#
# # Find the no of uppercase cheracter in the given string
#
#
#
#
# #find the commen element in two list
#
# list3 = ['apple', 'line', 'pincial', 'elephand']
# list4 = ['apple', 'bat', 'elephand', 'oil']
#
# list1 = [1, 2, 3, 4, 5, 5]
# list2 = [4, 5, 6, 7, 5]
#
#
# common_unique = list(set(list1) & set(list2))
# print("Unique common elements:", common_unique)
# common_with_duplicates = [x for x in list1 if x in list2]
# print("Common elements with duplicates:", common_with_duplicates)
#
#
#
# #find first non repeating character in a string
#
#
#
#
#
# #check wheater the tree is a binary tree or not
#
#
#
# #check wheter the binary tree is balanced is not
#
