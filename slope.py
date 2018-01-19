#James Roth
#1/19/18
#Slope - calculating slope

x1=float(input("What is the first x coordinate?" ))
x2=float(input("What is the second x coordinate?" ))
y1=float(input("What is the first y coordinate?" ))
y2=float(input("What is the second y coordinate?" ))

slope=float(round((y1-y2)/(x1-x2), 3))
print("The slope is", slope)

b=float(y1-slope*x1)
print("The equation of the line is y = ",slope,"x +", b)
