# Write a program to print all numbers between two intervals, namely low and high. But, with a special condition that numbers divisible by 5 must not be printed and skipped. (Do this using continue Statement).

#using for loop

min_for = int(input("enter initiating number : "))
max_for = int(input("enter ending number : "))

for i in range(min, max+1):
    if i % 5 == 0 :
        continue
    print(i)

# using while loop


min_while = int(input("enter initiating number : "))
max_while = int(input("enter ending number : "))

while min_while < max_while :
    if min_while % 5 == 0 : # checking condition
        min_while+=1 # if condition become true value will be increment by 1
        continue   
    print(min_while , end = " ") # incremented value will print
    min_while = min_while + 1 