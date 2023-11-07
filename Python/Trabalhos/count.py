for item in range(2, 9, 2):
    print(item)

even_number = item / 2
print(f"We have {even_number} even number")

#####Solution#####

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")
