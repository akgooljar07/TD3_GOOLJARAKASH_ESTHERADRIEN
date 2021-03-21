#!/usr/bin/env python3



def add(x,y):
	return x+y

def mul(x,y):
    return x*y


try:

   num1,num2=(input("enter 2 number : ")).split( )
   w=int(num1)
   n=int(num2)
   print("Choose 1 / 2 : ")
   print("1.Addition")
   print("2.Multiplication")
   choice = int(input("Choose Your Operation : "))
except (ValueError):

   print("Please input  2 numbers !")
   num1,num2=(input("enter 2 number : ")).split( )
   w=int(num1)
   n=int(num2)
   choice = int(input("Choose Your Operation :  "))


if (choice== 1 ):
  	z=add(w,n)
  	print("The sum : ",z)

else:
    	m=mul(w,n)
    	print("The Multiplication : ",m)
