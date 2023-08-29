'''#Write a program to find addition, subtraction, division, multiplication of two numbers.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
add= num1+num2
sub=num1-num2
mult=num1*num2
div=num1/num2
print("The addition of entered two number is: ", add)
print("The subtraction of entered two number is: ", sub)
print("The multiplication of entered two number is: ", mult)
print("The division of entered two number is: ", div)'''


'''#Write a program to find out average of 4 numbers and input will be taken from “input” function in python.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
num4=int(input("Enter fourth number: "))
add= num1+num2+num3+num4
avg= add/4 #we are calculating average between 4 numbers
print("The average of entered four numbers is: ", avg)'''


'''#Write a program to find out Simple Interest with proper use of basic functions in python and with the correct rules.
principal_amount=int(input("Enter the Principal Amount (rupees): "))
rate_0f_int=int(input("Enter the Rate of Interest value (%): "))
time_period=int(input("Enter the Time Period (years): "))
simple_interest=(principal_amount * rate_0f_int* time_period)/100
print("The simple interest calculated is: ", simple_interest)'''


'''#Write a program to find the speed with the input distance in kilometer, time in Hours.
distance=float(input("Enter the distance in KM: "))
time=float(input("Enter the time in Hour: "))
speed=distance/time
print("The speed in KM/Hour is: ", speed)'''


'''#Write a Program to Calculate the Area of a Triangle if base and height are given
base = float(input("enter the length of the base of the triangle (cm): "))
height = float(input("enter the height/altitude of the base of the triangle (cm): "))
area_triangle = 0.5 * (base*height) 
print("The area of triangle (cm^2) is (if base and height are given): ", area_triangle)'''


'''#Write a Program to Calculate the Area of a Triangle if all the sides are given 
#(Heron's Formula= area = 0.25 * √( (a + b + c) * (-a + b + c) * (a - b + c) * (a + b - c) ))
import math
side1 = float(input("enter the first side of a triangle (cm): "))
side2 = float(input("enter the second side of a triangle (cm): "))
side3 = float(input("enter the third side of a triangle (cm): "))
area_triangle= 0.25 * (math.sqrt(((side1 + side2 + side3) * (-side1 + side2 + side3) * (side1 - side2 + side3) * (side1 + side2 - side3))))
print("The area of triangle (cm^2) is (if three sides are given): ", area_triangle)'''

'''#Write a program to Solve Quadratic Equation using inbuilt function "cmath".
import cmath # import complex math module
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = (b**2) - (4*a*c) # calculate the discriminant
# find two solutions
root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)
print('The first root is: ', root1, 'The second root is: ', root2)
print('The solution are {0} and {1}'.format(root1,root2))'''


'''#Write a program to Solve Quadratic Equation without using inbuilt function.
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + (discriminant ** 0.5)) / (2*a)
    root2 = (-b - (discriminant ** 0.5)) / (2*a)
    print("Root are real: ",root1, root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("Root are same: ", root, root) 
else:
    real_part = -b / (2*a)
    imaginary_part = (abs(discriminant) ** 0.5) / (2*a)
    root1 = complex(real_part, imaginary_part)
    root2 = complex(real_part, -imaginary_part)
    print("Root are imaginary: ", root1, root2)'''









