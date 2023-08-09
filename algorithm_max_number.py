# A function that finds the largest number in a list

def isMaximum():
    number_list = [19, 89, 34, 54, 2, 88, 14, 6, 87, 74]

    max_num = number_list[0]

    for num in number_list:
        if num > max_num:
            max_num = num
    print("The maximum Number is: ", max_num)

isMaximum()

