weight = int(input("Wheight: "))
Wich_one = input("(L)bs or k(g)?")

if Wich_one.upper() == "L":
    converted = weight * 0.45
    print(converted)

else:
    converted = weight / 0.45 
    print(converted)
 
 