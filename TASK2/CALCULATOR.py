# TASK 2 ( CALCULATOR )
#syed Muhammad Zain Bin Faisal
"""
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.
"""
# now we have to create a main menu
print("<Welcome to Zain's calculator> ")
while True:  # loop to run continuously until a user wants to exit
    print(" Hi There, Select the Desired Operation: ")
    print("*****************************************")
    print("1 : ADDITION")
    print("2 : SUBTRACTION")
    print("3 : MULTIPLICATION")
    print("4 : DIVISION")
    print("5 : EXIT")

    choice = int(input("Enter Your Choice (1-5): "))
    # we need to make sure if the user press 5 directly ,it exits and does not ask to add number.
    if choice == 5:
        print(" THANK YOU FOR USING Zain's <CALCULATOR>")
        break
    else:
        val1 = float(input("enter the number : "))
        val2 = float(input("enter the number : "))

    if choice==1:
        result=val1+val2
        print("RESULT:", result)
    elif choice==2:
        result=val1-val2
        print("RESULT: ", result)
    elif choice==3:
        result=val1*val2
        print("RESULT: ", result)
    elif choice==4:
        if val2==0:
            print(" CANNOT DIVIDE BY ZERO !!! <ERROR> ")
        else:
            result=val1/val2
            print("RESULT: ", result)

