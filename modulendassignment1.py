# 1. Define a function calculate_average(marks)
# function to find average
def calculate_average(marks):
    return sum(marks) / len(marks)

marks=[55,66,77,88,99]
avarage=calculate_average(marks)
print(avarage)

# output is = 77.0




# 2. Define another function get_grade(average)

print("___welcome to grade calculator___")

# using while loop to run morethan once until the user stop
while True:
    # using error handling
    try:
        # input maybe floating number
        average=float(input("enter your average mark:"))
    
        if 0 <= average <=100:  
    
           if average >=90:
            print("congratulation your grade is A")
    
           elif average >=80:
            print("congratulation your grade is B") 
    
           elif average >=70:
            print("congratulation your grade is C")
    
           elif average >=60:  
            print("congratulation your grade is D") 
    
           else:
            print("you failed, try hard next time")    
        else :
            print("invalid input : enter a mark (0 to 100)")
            continue

    except ValueError:
        print("value error : invalid input")
        continue
   
    again=input("do again? enter yes or no :")
    if again !="yes":
       print("thank you")
       break
        




# input = 90
# output = grade A



# 3. In the main program:

# function to calculate the average 
def calculate_average(marks):
    average= sum(marks)/len(marks)
    return average

# function to determine the grade
def determine_grade(average):

    if average >90:
        return "A"
    elif average >80:
        return "B"
    elif average >70:
        return "C"
    elif average >60:
        return "D"
    else:
        return "F"

# using while loop to run morethan once until user stop the loop
while True:
    # input maybe floating number
    a=float(input("enter the mark of maths :"))
    b=float(input("enter the mark of chemistry :"))
    c=float(input("enter the mark of physics :"))
    d=float(input("enter the mark of biology :"))
    e=float(input("enter the mark of english :"))

#  if user give a wrong input using error handling
    try: 
        marks=[a,b,c,d,e]        
        average=calculate_average(marks)
        grade=determine_grade(average)

        print(f"your average = {average}")
        print(f"your grade = {grade}")

    except ValueError:
        print("ValueError:enter the mark (0 to 100)")
    
    again=input("find again? enter yes or no")
    if again !="yes":
        print("thank you")
        break



# input = [60,67,78,89,90] 
# output = your average = 76.8
#          your grade = c 




# PYTHON PROGRAMMING

# MODULE END ASSIGNMENT 1

# Assignment Title: Student Grade Management System

# i writed three python programs to find average and grade and one main program.
# simple code to understand everyone and purpose of reusable.
# i used = functions
#          conditional statements
#          collect input from user

# in the 1. Define a function calculate_average(marks)
# we used def function and send arguments to the parameter.
# and we return sum(marks) / len(marks)  to calculate_average and we got the output.


# in 2. Define another function get_grade(average)
# we used def function and collect argument from user by through input. and send to parameter.
# we used while loop and error handling to protect from unwanted input and user can use morethan once.
# and the program gave the output in the basis of user input.


# in the main program
# we did what we do before. we write a program to find average and also find the grade.
# we collected 5 numeric marks from user through input buildin function.
# after that we used that marks to find the average and return average and find the grade.
# we used same while loop and error handling..