#Assingment 1.1: WAP to print your name three time
for i in range(1,4):
    print("Abhitej Singh Dhaliwal")

#Assingment 2.1: WAP to add three numbers and print the result.
a=int(input("enter the first number "))
b=int(input("enter the second number "))
c=int(input("enter the third number "))
print ("sum is ",a+b+c)

#Assingment 2.2: WAP to concatinate three strings and print the result.
a=input("enter the first string ")
b=input("enter the second string ")
c=input("enter the third string ")
print(a+b+c)

#Assingment 4.1: WAP to print the table of 7, 9.
for i in range(1,11):
    print("7 x " ,i," = " ,i*7)

for i in range(1,11):
    print("9 x " ,i," = " ,i*9)

#Assingment 4.2: WAP to print the table of n and n is given by user.
n=int(input("enter the number for table" ))
for i in range(1,11):
    print(n," x " ,i," = " ,i*n)

#Assingment 4.3: WAP to add all the numbers from 1 to n and n is given by user.
n=int(input("enter the number " ))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum is " ,sum)

#Assingment 5.1: WAP to find max amoung three numbers and input from user. [Try max() function]
a=int(input("enter the first number "))
b=int(input("enter the second number "))
c=int(input("enter the third number "))

d=max(a,b,c)
print("Maximum number is ",d)

#Assingment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.
n=int(input("enter the number " ))
sum=0
for i in range(1,n+1):
    if i%7==0 and i%9==0 :
        sum=sum+i
        print("sum for ",i," is ",sum)

print("sum is ",sum)

#Assingment 5.3: WAP to add all prime numbers from 1 to n and n is given by the user.
n=int(input("enter the number " ))
sum=0

for i in range(2,n+1):
    flag=0
    for j in range(2,i//2+1):
        if i%j==0:
            flag=1
            break
            
            
    if flag==0:
        sum=sum+i
        print("sum for i =  ",i," is " ,sum)

print("sum is " ,sum)

#Assingment 6.1: WAP using function that add all odd numbers from 1 to n, n is given by the user.
n=int(input("enter the number " ))

def add(a):
    sum=0
    for i in range(1,a+1):
        if i%2!=0:
            sum=sum+i
            print ("sum for i=",i," is " ,sum)
    return sum

print("sum of odd number upto ",n," is ",add(n))

#Assingment 6.2: WAP using function that add all prime numbers from 1 to n, n given by the user.
n=int(input("enter the number " ))
def add(a):
    sum=0
    for i in range(2,a+1):
        flag=0
        for j in range(2,i//2+1):
            if i%j==0:
                flag=1
                break   
        if flag==0:
            sum=sum+i
            print("sum for i =  ",i," is " ,sum)
    return sum
print("sum is " ,add(n))