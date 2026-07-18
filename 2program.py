#10 This program calculates how many 500notes are there ,200 notes and 100notes
wda=float(input("enter the withdraw ammount:"))
fn=wda//500
rm1=wda%500
tn=rm1//200
rm2=rm1%200
on=rm2//100
rm3=rm2%100
print("500 notes:{},200notes:{},100 notes:{}".format(fn,tn,on))
# 11.program on relational operators
a,b=float(input("enter the a:")),float(input("enter the b"))
print("{} is greater than {} :{}".format(a,b,a>b))
print("{} is lesser than {} :{}".format(a,b,a<b))
print("{} is equal than {} :{}".format(a,b,a==b))
print("{} is not equal than {} :{}".format(a,b,a!=b))
print("{} is greater 'or equal than {} :{}".format(a,b,a>=b))
print("{} is less or equal than {} :{}".format(a,b,a<=b))
