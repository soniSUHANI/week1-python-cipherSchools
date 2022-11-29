# sum of n natural numbes
# ask a user for natural number n
# print total from 1 to n
a = input("Enter a number here: ")
total = 0
i = 1
while i <= int(a):
    total = total + i
    i = i+1
print(total)
