# For Loops 

list1 = ["apples", "bananas", "cherries"]
tupple1 = (2,6,10)

for item in list1:
    print(item)

for item in tupple1:
    print(item)

for y in range(0, 11):
    print(y)

for x in range(0, 11, 2):
    print(x)

for z in range(5, 51, 5):
    print(z)

for a in range(0,4):
    for b in range(0,3):
        print(a * b)

for char in "hello":
    print(char)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print() 
