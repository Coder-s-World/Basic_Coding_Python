# all operaions

# 1. addition
# 2. substraction
# 3. multiplication
# 4. exponent
# 5. division
# 6. module
# 7. floor division
# 8. power

num1 = int(input(" enter first number : "))
num2 = int(input(" enter second number : "))

choice = int(input( " enter the choice : "))


print(" ")

if choice == 1 :
    sum = num1 + num2
    print("the choice is addition")
    print(f"the sum of numbers is : {sum}")
    
elif choice == 2 :
    sub = num1 - num2
    print("the choice is substraction")
    print(f"the substraction of numbers is :{sub} ")
    
elif choice == 3 :
    mult = num1 * num2
    print("the choice is multiplication")
    print(f"the multiplication of numbers is : {mult}")
    
elif choice == 4 :
    expo = num1 ** num2
    print("the choice is exponent")
    print(f"the exponent of numbers is : {expo}")
    
elif choice == 5 :
    div = num1 / num2
    print("the choice is division")
    print(f"the division of numbers is : {div} ")
    
elif choice == 6 :
    floor_div = num1 // num2
    print("the choice is floor division")
    print(f"the floor division of numbers is : {floor_div}")
    
elif choice == 7 :
    print("the choice is power of number")
    power = (num1 , num2)
    print(f"the power of numbers is : {pow}")
    
else:
    
    print(" choice is not entered ")


# method 2
print(""" 
      
      
      
      """)


number1 = int(input("enter first number : "))
number2 = int(input("enter second number : "))

# addition 
sum = number1 + number2 
print("addition of number is : ", sum)

# substraction 
sub = number1 - number2 
print("substraction  of number is : ", sub)

#multiplication
mult = number1 * number2 
print("multiplication of number is : ", mult)

# division
div = number1 / number2 
print("division of number is : ", div)

# floor division
floor_div = number1 // number2 
print("floor division of number is : ", floor_div)

# power
power = ( number1 , number2 ) 
print("power of number is : ", power)

# exponent
expo = number1 ** number2 
print("exponent of number is : ", expo)
