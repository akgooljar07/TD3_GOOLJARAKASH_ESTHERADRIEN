#!/usr/bin/env python3


def mul(x,y):
	return x*y


try:

   num1,num2=(input("enter 2 number : ")).split( )
   w=int(num1)
   n=int(num2)
   choice = input("Choose yes/no")
except (ValueError):

   print("Please input  2 numbers !")
   num1,num2=(input("enter 2 number : ")).split( )
   w=int(num1)
   n=int(num2)
   choice = input("Choose yes/no  ")


if (choice== "yes" ):
  	z=mul(w,n)
  	print("The Multiplication : ",z)

else:
      print("1 num",w)
      print("2 num ",n)
