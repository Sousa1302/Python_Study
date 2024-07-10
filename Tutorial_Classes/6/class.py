# Dictionaries

students = {
            'bob' : 17 ,
            'mike': 18 , 
            'joao' : 17
            }

print(students['bob'])      # will return the associated value ( 17 )
print(students['mike'])     # will return the associated value ( 18 )

students['joao'] = 20       # Updating an index associated value 

print(students['joao'])

del students['mike']        # Deleting an index and its associated value 

print(students)             # Prints the full dictionary    

print(len(students))        # Amount of indexes in the dictionary





