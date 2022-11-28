# EXERCISE - watch COCO
# ask users name and age
# if users name start with(a or A) and age is above 10 then
# print you acn watch COCO
# else print sorry you can't watch coco movie


name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
if age >= 10 and (name[0]=="A" or name[0]=="a"):
    print("you can watch coco")
else:
    print("sorry! you can't watch coco")
