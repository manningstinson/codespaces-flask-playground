print ("this is a solution")
print ("this is using the master branch")

# function name (value);

#this is a comment
#this is a comment 2

# Datatype -float
num1 = 15
num2 = 20

sum = num1+num2
print (sum)

multiply1 = 35
multiply2 = 45

multiply = multiply1 * multiply2
print (multiply)

subtract1 = 90
subtract2 = 45

subtract = subtract1 - subtract2
print (subtract)

divide1 = 90
divide2 = 45
divide = divide1 / divide2
print (divide)

# Datatype -string

myname = ("Hi,I'm Manning")
print (myname)

# using escape character

firstName = "Manning"
lastName = "Stinson"
bio = "I'm a \"developer\""
print (firstName +  " " + lastName)
print (bio)

firstName = "Manning"
lastName = "Stinson"
bio = "I'm a \"developer\""

# the "f" stands for "formatted." 
# F-strings are a way to create formatted strings in a concise and readable manner

fullname = f"{firstName} {lastName}"
print (fullname)  
print (bio)

# printing with an escape character
print ("Hello\nWorld") 

# printing with a tab
print ("Hello\tWorld")

#finding position of a character
print (fullname[0])

# finding the last character 
print (fullname[-1])

# finding the length of a string
print (len(fullname))

print (fullname[0])

catName1 = "Cheetah"
catName2 = "Sorbet"
catName3 = "Faith"

# Concatenating strings & slicing strings
# Finding the position of a word in a string
allCatNames = "Cheetah, Sorbet, Faith"
print (allCatNames[0:7])

allCatNames = "Cheetah, Sorbet, Faith"
print (allCatNames[0:20:3])

allCatNames = "Cheetah, Sorbet, Faith"
print (allCatNames[15:])

allCatNames = "Cheetah, Sorbet, Faith"
print (allCatNames[-10:])

# using the upper method
allCatNames = "Cheetah, Sorbet, Faith"

#Assigning the upper method to a variable
rescueCatNames = allCatNames.upper()
print (rescueCatNames)

#Assigning the upper method to the current variable
print (allCatNames.upper())

#using the lower method
print (allCatNames.lower())

#using the capitalize method
print (allCatNames.capitalize())

# using the title method
print (allCatNames.title())

# swapping the case of the string
print (allCatNames.swapcase())

# Using is digit method - returns boolean value
print (allCatNames.isdigit())




