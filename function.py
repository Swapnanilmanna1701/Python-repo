def greeting(name1, name2):
    print(f"{name1} loves {name2} beyond your imagination!!!") #f-string is used here
greeting("Swapnanil","Supriti")   
'''syntax: def f_name (parameter1, parameter2):
                print(f"{parameter1} loves {parameter2} beyond your imagination!!!")
            f_name(arg1, arg2) 
    def:it's a keyword used for user defined function           
'''
def invoice(username, salary, id):
    print(f"{username} having {id} getting {salary} per month")
invoice("Swapnanil","50000","01")    
invoice("Supriti","80000", "02") 


#return in function
def operation(x,y):
    z = x+y
    return z
operation("10","20")

