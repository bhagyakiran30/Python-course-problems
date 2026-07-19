'''no conditional operator in python
python has own conditional operator or ternary operator if else
examples of ternary operators  total 27 examples'''
#ex:1 greatest of two numbers
a,b=float(input()),float(input())
lar=a if a>b else b if b>a else "both are equal"
print("largest({},{})={}".format(a,b,lar))
#ex:2 smaller of two numbers
a,b=float(input()),float(input())
sma= a if a<b else b if b<a else "both are equal"
print("smallest({},{})={}".format(a,b,sma))
#ex:3 number is even or odd
n=float(input())
r="even" if n%2==0 else "odd" if n%2==1 or n%2==-1 else "neither even or odd"
print("{} is {}".format(n,r))
#ex:4 program that checks number is positive  are negative
n=float(input())
r="positive" if n>0 else "negative" if n<0 else "neither pos or neg it is zero"
print(r)
#ex:5 program which calculate whether person is eligible to vote or not
n=float(input())
r="please enter valid age" if n!=int(n) else "eligible " if n>=18 else "not eligible"
print(r)
#6.program whether student is pass of fail based on marks
m=float(input())
r= "please enter valid marks"  if ((m>100) or (m<0)) else "pass" if m>=35 else "fail"
print(r)
#7.giving grade based on marks
m=float(input())
r= "please enter valid marks"  if ((m>100) or (m<0)) else "grade E" if m>=35 and m<50 else "grade d" if m>=50 and  m<65  else "grade c" if m>=65 and m<80 else "grade b" if m>=80 and m<90 else "grade A"
print(r)
#8.largest of three numbers #check once
a=float(input())
b=float(input())
c=float(input())
r=a if a>=b and a>=c else b if b>=a and b>=c else c if c>=b and c>=a else "all are equal"
print("greater ({},{},{}):{}".format(a,b,c,r))
#9.absolute value of number
n=float(input())
r= -1*n if n<0 else n
print("the orginal value is{} &  absolute value is{}".format(n,r))
#10.absolute difference between two numbers
a=float(input())
b=float(input())
c=a-b
r=-1*c if c<0 else c   #r=-1*(a-b) if (a-b)<0 else (a-b)
print(r)
#11.year is leap year or not
year=float(input())
r= "leap year" if ((year%400==0) or ((year%4==0)and (year%100!=0))) else "not a leap year"
print(r)
#12.to check whether character is vowel or consonent
c=input().lower()
r="please enter a valid input" if len(c)>1 or not c.isalpha()  else "vowel" if c=="a" or c=="e" or c=="i" or c=="o" or c=="u" else "consonent"
print(r)
#13.to check whether a character is alphabet or not
ch=input()
print((ch>='A' and ch<="z") or (ch>='a' and ch<="z")) #checkonce
#process 2
c=input()
r="please enter the valid input"   if len(c)>1 or not c.isalpha() else 'ALPHABET'
print(r)
#14.to check whether a character is uppercase or lowercase
c=input()
r="please enter the valid input"   if len(c)>1 or not c.isalpha() else "upper case" if ((c>="A") and (c<="Z")) else "lowercase"
print(r)
#15.to check whether is number is divisible by 5
n=(input())
r="divisible by 5"   if n[-1]=="0" or n[-1]=="5" else "not divisible by 5"
print(r)
"""error:
Traceback (most recent call last):
  File "D:\python\3programs.py", line 69, in <module>
    r="divisible by 5"   if n[-1]=="0" or n[-1]=="5" else "not divisible by 5"
                            ~^^^^
IndexError: string index out of range"""
#process 2
n=float(input())
r="divisible by 5" if n%5==0 else "not divisible by 5"
print(r)
#16.the number which is divisible by 3&5
n=float(input())
r="divisible by both 3 and 5" if (n%3==0 and n%5==0)else "not divisible by both 3 and 5"
print(r)
#17.to know whether number is single digit or multi -digit
n=int(input())
r="single digit" if (n>=-9 and n<10) else "multi digit"
print(r)
#18.whether a person is eligible for senior citizen discount
age=int(input())
r="elgible for senior citizen discount" if age>60 else "not eligible"
print(r)
#19.eligible for driving license
age=int(input())
r="elgible for driving license" if age>=18 else "not eligible"
print(r)
#20.the program tells it is hot day or cool day based on temp
temp=float(input())
r="it is hot day" if temp>35 else "cool day"
print(r)
#21.business transaction results in profit or loss
sp=float(input())
cp=float(input())
r="profit" if sp>cp else "loss" if sp<cp else "not profit nor loss"
print(r)
#22.given number is multiple of 10
n=int(input())
r="multiple of 10" if n%10==0 else "not multiple of 10"
print(r)
#process 2
n=input()
r="multiple of 10" if n[-1]=="0" else "not multiple of 10"
print(r)
#23.to check number is greater than 100
n=int(input())
r="greater than 100" if n>100 else "equal"  if n==100 else "not greater than 100"
print(r)
#24.income tax applicable or not based on salary
salary=float(input())
r="income tax applicabe" if salary>250000 else "not income tax applicable"
print(r)
#25.program checks elgible to enter into movie thetre
age=int(input())
r="please enter a valid age" if (age<=0)  else "not eligible " if age<=2 else " eligible"
print(r)
#26.giving schlorship for grade a students
m=float(input())
r= "please enter valid marks"  if ((m>100) or (m<0)) else "grade E" if m>=35 and m<50 else "grade d" if m>=50 and  m<65  else "grade c" if m>=65 and m<80 else "grade b" if m>=80 and m<90 else "fail" if m<35 else "grade A hey you got a schlorship "
print(r)
#27.compare two strings
a=input()
b=input()
r="they are equal" if a==b else "they are not equal"
print(r)