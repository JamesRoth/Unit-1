#James Roth
#1/24/18
#change.py - making change

change=int(input("Input a number of cents: "))
print("Quaters: ", change//25)
change=change%25
print("Dimes: ", change//10)
change=change%10
print("Nickels: ", change//5)
change=change%5
print("Pennies: ", change)