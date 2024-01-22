import time # time is a builtin module in python
Time=int(time.strftime("%H:%M:%S"))
print(Time)
Time1=int(time.strftime("%H"))
print(Time1)
Time2=int(time.strftime("%M"))
print(Time2)
Time3=int(time.strftime("%S"))
print(Time3)
if ("Time=<10:00:00"):
    print("Good Morning")
elif("Time>=13:00:00"):
    print("Good Afternoon")
elif("Time>=17:00:00 and Time<=19:00:00"):
    print("Good Evening")
else:
    print("Good Night")       
    