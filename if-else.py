#print("hello world")
#print(13*56)
#nested if-else statement
num = int(input("Enter Your Number: "))
print(num)
if(num<0):
    print("Number is Negative")
elif(num>0):
    if(num<10) :
        print("Number is less than 10")
    elif(num>10 and num<=20):
        print("Number is in b/w range 10 to 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")   
##
##
#if-else statements
#idea1
num = int(input("Enter Your Number:"))
print(num)
if(num==0):
    print("Value is ZERO!")
elif(num<0):
    print("Value is NEGATIVE")
else:
    print("Value is POSITIVE")
                
#
#Match Case
#1
x = int(input("Enter the value:"))
match x:
    case 0:
        print("Value is ZERO!")
    case ("x<0"):
        print("Value is NEGATIVE")
    case _: #this is used for default case
        print("Value is POSITIVE")
#2

        