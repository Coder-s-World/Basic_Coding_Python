# number is positive or negative
# method 1

num = int(input("enter a number for 'method 1' : "))
if num > 0 :
    print("number is positive")
elif num < 0 :
    print("number is negative")
else:
    print("number is zero")

# method 2  

num = int(input("enter a number for 'method 2' : "))
if num >= 0 :
    if num == 0 :
        print("number is zero")
    else:
        print("number is positive")
else :
    print("number is negative")
    
    