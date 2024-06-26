def getList():
    user_list = []
    for x in range(5):
        
        value = int(input(f"Type the {x + 1} value: "))
        user_list.append(value)
    return user_list

def stats(lst):
    even_list = []

    even = 0
    odd = 0

    sum = 0
    for x in lst:
        sum += x
    
    avg = sum / len(lst)

    for y in lst:
        if y % 2 == 0:
            even_list.append(y)
            even += 1
        else:
            odd += 1

    
    print(f"The sum: {sum}")
    print(f"The average: {avg}")
    print(f"The biggest num: {max(lst)}")
    print(f"The lowest num: {min(lst)}")
    print(f"Odd nums: {odd}")
    print(f"Even nums: {even}")
    print(f"The even nums: {even_list}")


def main():
    user_list = getList()
    stats(user_list)


if __name__ == "__main__":
    main()
