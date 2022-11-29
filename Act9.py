# ask user to input a number containing more than one digit
# example-1256
# calculate 1+2+5+6 and print

a = str(input("Enter a four digit number here: "))
b = int(a[0])+int(a[1])+ int(a[2])+int(a[-1])
print(b)
