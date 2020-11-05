def age_print(age,name,today):

    """Python function that prints user name and age
     with given inputs
     
     Keywords arguments:
     age ---  The age of the user
     name --- The name of the user
     today --- The current year
     
     
    """
    
    try:
        
        if age>0:  #this checks if the age is greater than zero

            birth = today - age   #variable birth declaration
            
            decade_ago = today - 10 #variable decade_ago substacts 10 years from the current year
            
            decade_ago_age = age - 10 # variable  decade_ago_age calculates the age of the user in the past 10 year
            
            print(f"Hello {name} you are {age} years old")
            
            print(f"Your year of birth is {birth}")
            
            print(f"As you are {age} years old,you are an adult")
            
            print(f"In {decade_ago} you were {decade_ago_age} years old ")
            
            for year in range(50):    # the loop iterates through 50 years

                future_year = today + year # calculates the future year 

                age = age + 1       # calculate the new ages for each future year

                print(f"In {future_year} you'll be {age} years old ") 

        elif age < 0:

            print("Please enter correct age") #prompt the user to enter a correct age

    except:

        print("Something went wrong")