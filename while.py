# WHILE
#1 even or odd
# i=0
# while i<=10:
#     i=i+1
#     if i%2==0:
#         print(i,'is even')
#     else:
#         print(i,'is odd')
    
#2 multiples of 4    
# i=0
# while i<10:
#    i=i+1
#    s=4
#    m=4*i
#    print(i,'*',s,"=",m)

#3 square of numbers upto 30
# i=0
# while i<30:
#     i=i+1
#     m=i*i
#     print(m)

#4 find sum of even numbers below 10 using while loop
# i=0
# sum=0
# while i<10:
#     i=i+1
#     if i%2==0:
#         sum=sum+i
# print('sum of even numbers are',sum)

#5 print sum of numbers divisible by 3 and 5 between 1 to 50
# i=1
# sum=0
# while i<50:
#     i=i+1
#     if i%3==0 and i%5==0:
#          sum=sum+i
# print(sum)


#6 1 to 20 using while
# i=0
# while i<20:
#     i=i+1
#     print(i)

# print 20 to 1
# count=20
# while count>=1:
#     print(count,end="")
#     count -= 1

#7 even numbers below 100  
# i=0
# while i<100:
#     i=i+1
#     if i%2==0:
        # print(i)
        
#8 sum 1 to n
# n=int(input('enter a number:'))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)

#9 reverse usingwhile loop
# n=123
# reversed=0
# while n!=0:
#      dig=n%10
#      reversed=reversed*10+dig
#      n=n//10
# print('reverse is',reversed)

#10 factorial using while loop
n=int(input('enter a number:'))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print ("factorial is",fact)

#11 fibonacci
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

#12 20 to 1 using while loop
# count=20
# while count>0:
#     print(count)
#     count=count-1
    
#13 sum of digits using while
# n=55
# sum=0
# while n>0:
#     d=n%10
#     sum=sum+d
#     n=n//10
# print('sum of digits:',sum)  

#14 password until correct using while
# correct_pw='MY password'
# while True:
#     a=input('Enter the password:')
#     if correct_pw==a:
#         print('password is correct,access granted:')
#         break
#     else:
#         print('Incorrect password,try again')

#15 armstrong
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

