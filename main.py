#!/usr/bin/env python3


<<<<<<< HEAD
def mul(x,y):
	return x*y
=======
def sum(x,y):
	return x+y
>>>>>>> 21256527c7d6e76b83cd4f5f9bcf27951c06132d


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
<<<<<<< HEAD
  	z=mul(w,n)
  	print("The Multiplication : ",z)
=======
  	z=sum(w,n)
  	print("The sum : ",z)
>>>>>>> 21256527c7d6e76b83cd4f5f9bcf27951c06132d

else:
      print("1 num",w)
      print("2 num ",n)
