# method 1

perc = int(input("enter the marks for 'method 1' : "))

if perc < 0 or perc > 100 :
    print(" invalid ")
elif perc <= 39 : 
    print(" grade f")
elif perc <= 44 :
    print(" grade p")
elif perc <= 49 : 
    print(" grade c")
elif perc <= 54 : 
    print(" grade b")
elif perc <=  59 : 
    print(" grade b+")
elif perc <=  69 : 
    print(" grade a")
elif perc <=  79 : 
    print(" grade a+")
else :
    print("grade 0 ")


# method 2

perc = int(input("enter the marks for 'method 2' : "))

if perc < 0 or perc > 100 :
    print(" invalid ")
elif perc >= 0 and  perc <= 39 : 
    print(" grade f")
elif perc >= 40 and perc <= 44 :
    print(" grade p")
elif perc >= 45 and perc <= 49 : 
    print(" grade c")
elif perc >=50 and perc <= 54 : 
    print(" grade b")
elif perc >= 55 and perc <=  59 : 
    print(" grade b+")
elif perc >= 60 and perc <=  69 : 
    print(" grade a")
elif perc >= 70 and perc <=  79 : 
    print(" grade a+")
else :
    print("grade 0 ")

     
 