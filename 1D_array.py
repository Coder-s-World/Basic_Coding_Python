

no_of_element = int(input("enter the number of element you want to enter : "))
array=[]
for i in range(no_of_element) :
    array.append(int(input()))

print("the number of elements are : ")

for i in range(no_of_element):
    print(array[i], end = " ")
    
# print(array) - it will print in list format