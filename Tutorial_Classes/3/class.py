# Placeholders in Strings

name = "Jake"
sentece1 = "%s is 17 years old !"
sentece2 = "%s %s is the president of USA !"
sentece3 = "%s is %d years old !"

# %s = placeholder for String
# %d = placeholder for Integer
# %f = placeholder for float / double ( floating point numbers )
# %c = placeholder for character ( char )


print(sentece1 % name)
# in this case "%" will be subbed with the value of the variable name
print(sentece2 % ("Barack", "Obama"))
print(sentece3 % ("Sousa", 17))


# Format Strings
print(f"Hey, {name} !")








