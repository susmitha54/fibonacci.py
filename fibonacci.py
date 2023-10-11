######## Problem 2 ###############
#Write a program that prints out the Fibonacci sequence up to a given number.
#example 1,2,3,5,8 , next number is the sum of previous two numbers.



num=int(input("Enter the number:"))
a=-1
b=1
for i in range(num):
    c=a+b
    a=b
    b=c
    print(c)    
