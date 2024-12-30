# Write a program to print all numbers between two intervals, namely min and max. But, with a special condition that if any number in the range while getting printed becomes divisible by 13 then you must not print anything further and stop. (Do this using the Break Statement)

# break statement : when the given condition becames truw it will exit from loop entirely without executing the remaining code.(Break: Stops the entire loop execution, no further iterations occur).

# using for loop

min_for = int(input("enter starting number :"))
max_for = int(input("enter finishing number : "))

for i in range(min, max+1):
    if i % 13 == 0 :
        break
    print( i , end = " ")

#  using while loop

min_while = int(input("enter starting number :"))
max_while = int(input("enter finishing number : "))


while min_while < max_while :
    if min_while % 13 == 0:
        break
    print(min_while , end = " ")
    min_while = min_while + 1
    