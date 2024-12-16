# take a number from user using input 
number = int(input("enter number of which you want to print table :"))

# used for loop to iterate sequence
for i in range(1,10+1):
    res = number * i
    print(number ,"*",i,"=",res)
