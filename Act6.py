wining_number = 3
guess_number= int(input("Enter any number here between 1 to 10: "))
if guess_number == wining_number:
    print("you win !!")
if guess_number> wining_number:
    print("too high")
if guess_number< wining_number:
    print("too low")