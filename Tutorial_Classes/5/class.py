# Lists

shopping_list = ["Banana", "Tomato","Orange"]

print(shopping_list[0])
print(shopping_list[0:1])
print(shopping_list[0:])

# add items tou our list

shopping_list.append("blueberries")         # " .append " to add a value to the final of our list
print(shopping_list)


# Replace a value

shopping_list[1] = "Coconut"
print(shopping_list)


# delete a value from our list

del shopping_list[3]                        # " del " to delete a value from a certain index of our list


# show amount of values in a list

print(len(shopping_list))                   # " len " to show us the amount of values that the list contains


# max ? min integer value in a list

list_num = [7, 47, 32, 14 ,62]
print(max(list_num))                        # " max " to show us the biggest value in that list
print(min(list_num))                        # " min " to show us the lowest value in that list

