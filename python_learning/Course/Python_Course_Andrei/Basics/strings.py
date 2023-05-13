# print("This is for learning about string manipualtion")
description = "it's for learning about strings"
print(description)

name = "This is for String Indexes"

print(name[12::2])
print(name[1:5])

# "String Immutability"
# Strings are immutable, so we cannot chnage the value once it is created, so that in memory it will remove evrything and re assigns.
# String Concatenation

first_nam = "Rajeev"
last_name = " Suravajhula"

full_name = first_nam + last_name
print(full_name )

# Escape sequence

a = 'This is Rajeev\'s Computer'

b = "Hi \\t\"What are you trying to achive\"?"

print(a)
print(b)

#Formatted Strings

name = "Rajeev Suravajhula"

print(f"Hi {name}, Nice to meet you!")

print("Hi {0} Nice to meet you".format(name))


#String Indexes

a = "abcdef"

print(a[1])

#string[start:stop:step]

print(a[0:5:2])