# While Loops
a = 10
b = 5
c = 0 

while c < 5:
    c += 1
    if c == 3:
        break
    print(c)
print()


while b < 10:
    b += 1
    if b == 9:
        continue        # When it gets to 3 it will skip it and go to 4
    print(b)
print() 


while a < 15:
    a += 1
    if a == 13:
        pass
    print(a)
print()

