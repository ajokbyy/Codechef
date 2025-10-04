#Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
#area = (1/2)*base*height
def calculate_area(base, height):
    area = (1/2)*base*height
    print (area)

calculate_area(4, 3)


# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def calculate_3side(length, width, shape="triangle"):
    if shape.lower() == "square":
        area = length*width
        print(area)
    elif shape.lower() == "triangle":
        area = 0.5*length*width
        print(area)
    else:
        print("error")

calculate_3side(4, 3)
calculate_3side(4, 3, shape="square")
# calculate_3side(4, 3, shape="square")



#3.
# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
#
# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def calculate_pattern(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print()


calculate_pattern(3)
calculate_pattern(5)
