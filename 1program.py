#1.Program which will calculate SI and total amount to pay
p,t,r=float(input("enter principal")),float(input("enter time")),float(input("enter rate of interest"))
print("si:{} &total amount:{}".format((p*t*r)/100,((p*t*r)/100)+p))
#this another way to calculate Simple interest
print("si:{}".format((float(input("enter principal"))*float(input("enter time"))*float(input("enter rate of interest")))/100))
#2.Program which will calculate area of circle
print("area of circle:{}".format(3.14*float(input("enter radius of circle:"))**2))
# Another method to calculate the area of circle
import math
print("area of circle:{}".format(math.pi*float(input('enter radius of circle:'))**2))
#3.This program calculates the area of square
print("the area of square:{}".format((float(input("enter the area"))**2)))
#4.This program performs arithmetic operations
a=float(input("enter the value of a"))
b=float(input("enter the value of b"))
print("add :{}".format(a+b))
print("sub :{}".format(a-b))
print("mul :{}".format(a*b))
print("div :{}".format(a/b))
print("floor div :{}".format(a//b))
print("moddiv :{}".format(a%b))
print("exp :{}".format(a**b))
#5.program which will calculate the square
n=float(input("enter the n value"))
print("the {} sqaure is {}".format(n,n**2))
#6.program which will calculate the square root
n=float(input("enter the n"))
print("the square root is {}".format(n**(1/2)))
#7.program which will calculate the cube root of no.
n=float(input("enter the n"))
print("the cube root is {}".format(n**(1/3)))
#8.program which will calculate a power m/a power n
a,m,n=float(input("enter the value of a")),float(input("enter the value of m")),float(input("enter the n value"))
print("the value is:{}".format((a**m)/(a**n)))
print("the value is:{}".format(a**(m-n)))
print("the value is:{}".format((a**m)*(a**-n)))
#9.program which will accept any values & swap them
#process 1 using multiline assignment
a,b=input("enter the a:"),input('enter the b:')
a,b=b,a
print(a,b)
#process 2 using temp variable
a,b=input("enter the a:"),input('enter the b:')
temp=a
a=b
b=temp
print(a,b)
#process 3 using addition and subtraction
a,b=float(input("enter the a:")),float(input('enter the b:'))
c=a+b
a=c-a
b=c-a
print(a)
print(b)
#process 4 using floor div
a,b=float(input("enter the a:")),float(input('enter the b:'))
c=a*b
a=c//a
b=c//b
print(a,b)
#using 2 variables
a,b=float(input("enter the a:")),float(input('enter the b:'))
a=a*b
b=a//b
a=a//b
print(a,b)








