
amount_students = int(input("Students in this class: "))
 
avg_grade = 0
total = 0
biggest_grade = -1
lowest_grade = 101
reproved = 0

for x in range(amount_students) :
    name = input("Name: ")
    grade = float(input("Grade: "))

    total += grade

    if grade > biggest_grade:
        biggest_grade = grade
    
    if grade < lowest_grade:
        lowest_grade = grade
    
    if grade <= 60:
        reproved += 1


avg_grade = total / amount_students

print(f"Total Grades: {total}")
print(f"Average Grade: {avg_grade}")
print(f"Biggest Grade: {biggest_grade}")
print(f"Lowest Grade: {lowest_grade}")
print(f"Reproved: {reproved}")





