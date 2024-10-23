def fun():  
    def function(): 
        print("Please write your details bellow")
        age = int(input("Please write how old are you: "))
        if age < 18:
            print("You are to small, Try at nexr Try")
            return function()
        elif age > 18:
            print("You a to old")
            return age
        else:
            print("You have a perfect age")
            return age

                    

    def function2(age):
        name = str(input("Please write a name: "))
        if len(name) < 3:
            print("Your name is to small")
            rep = str(input("Did you want to return the process?  Y/N: "))
            if rep == "Y":
                return fun
            if rep == "N":
                return 
        
        if len(name) <= 12:
            print("Your name is correct")
            print("Your name is: ", name, "and your age is: ", age, "year")
            rep = str(input("Did you want to repeat the process?  Y/N: "))
            if rep == "Y":
                return fun
            if rep == "N":
                return 
        if len(name) > 12:
            print("Your name is to long")
            return name
    
    age = function()
    function2(age)
        
fun()