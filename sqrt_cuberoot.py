# import math module to access mathematical function 
import math
number = int(input("enter the number : "))
print(" ")

# find out the square
square = number * number
print(f"square of number({number}) is : ",square)

#-----------------------------------------------------

# find out the square root - The square root of any numerical value is a value that on self multiplication results in the original number

square_root = math.sqrt(number)
print(f"square root of number({number}) is : ",square_root)

#--------------------------------------------------------

# find out the cube root
cube_root = number ** (1/3)
print(f"cube root of number({number}) is : ",cube_root)

