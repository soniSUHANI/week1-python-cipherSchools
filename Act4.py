# take two comma seperated input from user 
# output-2  print lines
# 1.) user name length
# 2.)count the character that user inputed

name, input = input("Enter the name and input word: ").split(",")
print(len(name))
print(name.lower().count(input.lower()))