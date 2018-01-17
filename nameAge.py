#James Roth
#1/17/18
#nameAge.py - splitting and characters in a string
name=input("What is your first and last name? ")
age=int(input("What is your age? "))
firstName,lastName=name.split()
print("Your first name has ", len(firstName), "letters")
print("Your last name has ", len(lastName), "letters")
print("You will be", age+1, "next year")