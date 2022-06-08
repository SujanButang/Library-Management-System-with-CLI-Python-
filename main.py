import Register             #importing necessary files
import Borrow
import Return
def main_program():         #defining function main_program()
    con = str(input("\nPresss 'Enter' to continue"))
    while True:
        choice = input ("Please press:\n1. To Register new Book. \n2. To check available books and borrow.\n3. To return books.\n4. To exit the program.\n") #Taking input from user to perform the desired action
        try:
            choice = int(choice)
            if choice < 1 or choice > 4:
                raise ValueError
        except ValueError:
            print("\nPlease enter correct input format.") #message display while any error occured in the input
        if choice == 1:
            print("\nYou selected to register book.")
            Register.register() #calling specific function of spectific python file
            continue_program()
        elif choice == 2:
            Borrow.stock()
            Borrow.borrow()
            Borrow.condition()
            Borrow.borrow_details()
            continue_program()
        elif choice == 3:
            Return.returning()
            Return.restocking()
            continue_program()
        elif choice == 4:
            quit()                  #closing the program
            
def continue_program():         #This function asks the user either to continue the program or to exit the program
    try:
        check = str(input("\nPress 'Y' to continue the program and 'X' to close the program.\n"))
        if check.upper()=="Y":      #If user chooses to continue program, it restarts the entire program from the beginning as a loop
            main_program()
        elif check.upper() == "X":
            quit()
        else:
            raise ValueError
    except:
        print ("\nPlease input in correct format")
            
        
