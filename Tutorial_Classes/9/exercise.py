
list_nums = []
even = 0
odd = 0
sum = 0



while len(list_nums) < 5:    
    nums = int(input("Type a integer: "))
    list_nums.append(nums)

    sum += nums

    if nums % 2 == 0:
        even += 1
    else:
        odd += 1
    
print(f"Your list: {list_nums}")
print(f"Odd numbers: {odd}")
print(f"Even numbers: {even}")
print(f"Sum of all of the numbers: {sum}")




