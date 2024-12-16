# greatest of three number

# method 1
n1 = int(input("enter first number : "))
n2 = int(input("enter second number : "))
n3 = int(input("enter third number : "))

if n1 > n2 and n1 > n3:
    print(f"number {n1} is greater")
elif n2 > n1 and n2 > n3:
    print(f"number {n2} is greater")
else : 
    print(f"number {n3} is greater")
    
