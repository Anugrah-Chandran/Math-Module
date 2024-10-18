'''
Author : Anugrah Chandran
Date : 18-10-24
Description : Python program that uses functions from the math module to
 perform the following operations on a number provided by the user
'''
import math


number=int(input("Enter a number:"))
square_root=math.sqrt(number)
print("Square root of number",number,":",square_root)
factorial=math.factorial(number)
print("Factorial of number",number,":",factorial)
power=math.pow(number,2)
print("Power of number",number,":",power)