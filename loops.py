# for loop
#logics start from loop
for i in range(20): # here range have to be mentioned
    print(i)
    print(i+1)
#for nth range for loop print upto (n-1)th element    
name = "Supriti Mondal"
for char in name:
    print(char)
    
#if-else within for loop
for i in range(10):
    if(i==5):
        print("Value is 5")
    else:
        print(i)
superheroes = ["Spiderman","superman","Ironman","Loki","Hulk"]   
for i in superheroes:
    print(i)
    for r in i:
        print(r)         
for i in range(1,20):
    print(i) # it prints from 1 to (n-1)th position
for i in range(1,20,2):
    print(i) # it prints from 1 to (n-1)th position with a gap of 2)
    
    
##while loop    
'''i=0 # assign of initiation
while(i<=15): #loop making
    print(i)
    i=i+1 # propagation of loop
####This is aa very important example
i = int(input("Enter the number:")) 
while(i<=50):
    i = int(input("Enter the number:")) 

    #print(i)
#print("Loop is over") 
'''  
#else statement with while loop
count = 5
while(count>=0):
    print(count)
    count=count-1
else:
    print("Loop is over")  
# when statement is false then only else condition is executed
      


