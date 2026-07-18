# _a=32
# 32==23
# print(_a)
# a=43
# b=int(a)
# print(b)
# c=float(a)
# print(c)
# d=3
# e=float(d)
# print(e)
# print('cat')
# print("dog")
# z=''' 
# hdhhg

# rrggg

# ggg

# '''
# print(z)

# # STRING METHODS
# g='iNDIa'
# i=g.capitalize()
# print(i)
# j=g.lower()
# print(j)
# k=g.title()
# print(k)
# z='     red'
# l=z.strip()
# print(l)
# g.capitalize()
# m=z.split()
# print(m)
# n=g.split()
# print(n)

#LIST
# a=[1,2.23,'dog',4]
# print(a[2])
# print(a[0])
# print(a[1])
# print(a[3])
# # a.append(5)
# # a.insert(0,0)
# # a.insert(0,'0')
# # a.remove(1)
# a.pop(1)
# print(a)

#TUPLE
# x=(1,2,'data')
# a=list(x)
# a.append(5)
# a.insert(0,0)
# a.remove(1)
# print(a)
# a=tuple(x)
# print(x)

#SET
# A={'HEN',1,2,3,4,4}
# B={'chich'}
# A.add(32)
# A.update(B)
# print(A)

#DICTIONARY
# x = {
#     'name':'abc',
#     'age' : 23,
#     'phone' : 98765432,
#     'addres' : "abcdefg"
# }
# print(x)
# print(x['name'])
# print(x['age'])
# print(x['phone'])
# x['email']='rr@gmail.com'
# # x.clear()
# print(x)
# OPERATORS
# a=1
# b=12
# if a<b:
#     print("b is greater")
# else:
#     print("a is greater")
# a=5787
# b=543
# c=32
# if a>b and a>c:
#     print("a is greater than b and c")
# elif b>c:
#     print('b is greater than a and c')
# else:
#     print('c is greater than a and b')
# a=int(input("enter a digit:"))
# if a%2==0:
#     print ('a is even')
# else:
#     print('a is odd')

    #divisible by 5 or not
# a=int(input('enter a number:'))
# if a%5==0 and a!=0:
#     print('a is divisible by 5')
# elif a==0:
#     print('number is zer0')
# else:
#     print('a is not divisible by 5')
    
 #Eligibility to vote   
# b=int(input('enter age of person:'))
# if b>=18:
#     print('b is eligible to vote')
# else:
#     print('b is not not eligible to vote')

#  #PASS/FAIL   
# c=int(input('enter marks obtained:'))
# if c>=50:
#     print('PASS')
# else:
#     print('FAIL')

#check if a value is inuppercase/lower case or a digit   
# a=input('enter a value:')
# if a.isupper():
#     print('a is upper case')
# elif a.islower():
#     print('a is lower')
# else:
#     print('a is a digit')
    #LOOPS
#
# for i in range(0,286):
#     print(i)

# a=input('enter a value:')
# x=['a','e','i','o','u']
# if a in x:
#     print('It is a vowel')
# else:
#     print('It is a consonent')

#FOR LOOP
# for i in range(1,21):
#     if i%2==0:
#         print(i)
# for i in range(1,21):
#      if i%2!=0:
#         print(i,'odd number')
        
# for i in range(1,11):
#  m=i*7
#  s=7
#  print(s,"*",i,'=',m)
# for i in range(50,501):
#     print(i)

#print numbers between 100 to 50

# for i in range(100,49,-1):
#     print(i)
# for i in range(1,31):
#     s=3
#     j=i*3
#     print(s,'*',i,'=',j)
# for i in range(1,11):
#     a=i*i
#     print(i,'*',i,'=',a)

#WHILE

# i=0
# while i<=10:
#     i=i+1
#     if i%2==0:
#         print(i,'is even')
#     else:
#         print(i,'is odd')
    
#multiples of 4    
# i=0
# while i<10:
#    i=i+1
#    s=4
#    m=4*i
#    print(m)

#square of numbers upto 30
# i=0
# while i<30:
#     i=i+1
#     m=i*i
#     print(m)

#find sum of even numbers below 10 using while loop
# i=0
# sum=0
# while i<10:
#     i=i+1
#     if i%2==0:
#         sum=sum+i
# print('sum of even numbers are',sum)

# print sum of numbers divisible by 3 and 5 between 1 to 50
# i=1
# sum=0
# while i<50:
#     i=i+1
#     if i%3==0 and i%5==0:
#          sum=sum+i
# print(sum)
       

#FUNCTIONS
# def abc():
#  a=43
#  b=34
#  c=a+b
#  print('sum of a and b is',c)
# abc()

# def fun(a,b):
#     c=a+b
#     print('sum is',c)
# fun(1,2)
# 
# a=range(1,10)
# print(list(a))

#leap year
# a=int(input('Enter a year:'))
# if a%4==0 and a%100!=0 or a%400==0:
#     print(a,'is a leap year')
# else:
#     print(a,"is not a leap year")

# calculator
# operator=input('enter an operator(+,-,*,/):')
# n1=int(input('enter first number:'))
# n2=int(input('enter second number:'))
# if operator=='+':
#     result=n1+n2
#     print('sum is',result)
# elif operator=='-':
#     result=n1-n2
#     print('result is',result)
# elif operator=='*':
#         result=n1*n2
#         print(n1,"*",n2,"=",result)
# elif operator=="/":
#     # if n1%2!=0:
#         result=n1/n2
#         print('result is',result)
    # else:
    #     print('division by zero is invalid')
# else:
#     print('invalid operator')
#     # arrays nly 1 
    # ARRAYS
# a=('ant','ball','cat')
# b=iter(a) 
# print(next(b))
# print(next(b))
# print(next(b))
# array iteration using for loop
# a=('ant','ball','cat')
# for x in a:
#  print(x)

# MODULES 
# a=2
# b=5
#factorial
# def fact():
#     num=5
#     factorial=1
#     for i in range(1,num+1):
#         factorial*=i
#     print('factorial of the given number is',factorial)
# fact()
 #count digits
# str=('234','32','3')
# str=('123')
# print("total number of digits are",len(str))
#sum of 1 to n
# n=8
# sum=0
# for i in range(1,n+1):
#     sum =sum+i
#     i=i+1
#     print(sum)

# for i in range(1,101):
#     print(i)
# for i in range(20,0,-1):
#     print(i)
#square
# for i in range(1,21):
#     print(i,'*',i,"=",i*i)
#count vowels
# input='hai ium'
# vowel='aeiouAEIOU'
# sum=0
# for v in input:
#     if v in vowel:
#         sum=sum+1
# print(sum)

#largest
# t=[12,34,55,56]
# largest=t[0]
# for x in t:
#     if x>largest:
#         largest=x
# print('the largest number is',largest)

# factors
# num=21
# factors=[]
# for i in range(1,num+1):
#     if num%i==0:
#         factors.append(i)

# 1 to 20 using while
# i=0
# while i<20:
#     i=i+1
#     print(i)
# print 20 to 1
# count=20
# while count>=1:
#     print(count,end="")
#     count -= 1
     
# i=0
# sum=0
# while i<=100:
#     i=i+1
#     if i%2==0:
#         sum=sum+i
# print('sum of even numbers between 1 and 100 is',sum)
# # i=0
# while i<100:
#     i=i+1
#     if i%2==0:
        # print(i)
# sum 1 to n
# n=int(input('enter a number:'))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)
#password until correct
# area of circle using python
# import math
# def areacircle(radius):
#      area=math.pi*radius*radius
#      print(area)
# areacircle(4)
#reverse string
# text='hai'
# print(text[::-1])

#reverse usingwhile loop
# n=123
# reversed=0
# while n!=0:
#      dig=n%10
#      reversed=reversed*10+dig
#      n=n//10
# print('reverse is',reversed)
    
#reverse using function
# def reverse(str):
#     reversed=0
#     while n!=0:
#         dig=n%10
#         reversed=reversed*10+dig
#         n=n//10
#     return reversed
# input=4567
# result=reverse(input)
# print('origial:',input)
# print('reversed:',result)

#factorial using while loop
# n=int(input('enter a number:'))
# fact=1
# while n>0:
#     fact=fact*n
#     n=n-1
# print ("factorial is",fact)

#fibonacci
# a=int(input('enter first value:'))
# b=int(input("enter second value:"))
# n=int(input("enter number of terms:"))
# print(a,b,end="")
# while(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c,end="")
#     n=n-1

#20 to 1 using while loop
# count=20
# while count>0:
#     print(count)
#     count=count-1
    
# sum of digits using while
# n=55
# sum=0
# while n>0:
#     d=n%10
#     sum=sum+d
#     n=n//10
# print('sum of digits:',sum)  

#count digits
# num=-33453
# count=0
# if num==0:
#     count=1
# else:
#     num=abs(num)
#     while num>0:
#         num=num//10
#         count=count+1
# print('number of digits',count)

#password until correct using while
# correct_pw='MY password'
# while True:
#     a=input('Enter the password:')
#     if correct_pw==a:
#         print('password is correct,access granted:')
#         break
#     else:
#         print('Incorrect password,try again')
 
 #largest of 3
# def largest(a,b,c):
#     if a>b and a>c:
#       return a
#     elif b>c:
#      return b
#     else:
#         return c
# d=largest(566,7,6)
# print('the largest number is',d)

#count vowels
# def countvowels(text):
#     vowel='aeiouAEIOU'
#     sum=0
#     for v in text:
#      if v in vowel:
#         sum=sum+1
#     return sum
# m='hai iam'
# result=countvowels(m)
# print('total vowels=',result)

#square using functions
# def square(x):
#     return x*x
# a=square(25)
# print('square of 5 is',a)

#check even
# def even(x):
#     if x%2==0:
#         return x
# a=even(456)
# print(a,'is even')

#remove duplicates
# list=[1,2,3,4,4,5,6,7,7]
# new=[]
# for item in list:
#     if item not in new:
#         new.append(item)
# print('original list:',list)
# print('list without duplicates:',new)

# student result
# def examresult(score):
#     if score<0 or score>100:
#         return "invalid score" 
#     if score>=90:
#         grade="A"
#     elif score>=70:
#         grade="B"
#     elif score>=50:
#          grade="C"
#     else:
#         grade="F(FAIL)"
# a=int(input("enter the marks:"))
# print(examresult(a))

 # armstrong
# num = int(input("Enter a number: "))
# temp = num
# num_digits = len(str(num))
# sum_of_powers = 0
# while temp > 0:
#     digit = temp % 10
#     sum_of_powers += digit ** num_digits
#     temp //= 10
# if num == sum_of_powers:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")
    
      #star pattern
# n = int(input("enter number of raws:"))
# for i in range(1, n + 1):
#     print("*" * i)
    
# q=int(input('Enter number of rows='))
# for i in range(q,0,-1):
#     print("*" * i)
    
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print(i, end=" ")
#     print()

# rows = 15
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


    

         

      
     
    

 
    
    