
# method 1
age = int(input("enter a age for 'method 1' : "))

if age >= 18:
    print("eligible for voting")
else:
    print("not eligible for voting")
    
    
# -----------------------------------------------------------

# method 2

age = int(input("enter a age for 'method 2' : "))

result=  "eligible for voting" if age >= 18 else "not eligible for voting"    
print(result)