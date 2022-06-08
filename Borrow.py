from datetime import date      #importing date and time from python library
from datetime import datetime
from datetime import timedelta
global selected_book           #Declaring a dictionary as global so to access it anywhere necessary
selected_book = {}  
count = 0                      
def stock():
    global book_details         #Declaring an array as global
    book_details = []
    stock = open("BookDetails.txt","r") #opening the text file with list of books
    lines = stock.readlines()       #reading each line in the text file and storing it in the variable lines as list
    for each in lines:
        detail = each.split(",")    #splitting every line with ',' and storing the splitted value in variable detail 
        book_details.append(detail) #Adding the value in details to the array book_details 
    stock.close()
    print("\nBooks available are:\n") #displaying the available list of books
    for i in range (len (book_details)):
        print (str(i+1)+"."+book_details[i][0]+" Author:"+book_details[i][1]+" Available QTY:"+book_details[i][2]+" Rate per day: $"+book_details[i][3])

def borrow():       #This function asks the user on which book and how many to borrow and at the same time rewrites the stock with subtracted number of books
    print("\nWhich of the above listed books do you want to borrow?")
    while True:
        choice = str(input("\nEnter the serial number of the book you want to borrow:")) ##Asking user on which book to borrow
        try:
            choice = int(choice)
            if choice > len(book_details) or choice ==0:
                raise ValueError
            break
        except ValueError: #Exception handling if any invalid input is entered
            print("\nPlease enter serial number in integer and within the range from 1 to "+str(len(book_details)))
    print("You selected the book "+book_details[choice-1][0])
    while True:
        number = str(input("\nHow many of the books do you want?"))     #Asking user on how many of the selected book is to be borrowed
        try:
            number = int(number)
            if number > int(book_details[choice-1][2]):
                print ("\nSorry,number exceeded the available number of the book.")
            break
        except ValueError:
            print("\n Please enter valid integer.") #Exception handling
            
    book_details[choice-1][2] = int(book_details[choice-1][2]) - number #Subtracting the available number of books by selected numbers of books to borrow
    selected_book[book_details[choice-1][0]] = number           #Adding the selected number of books to the dictionary
    global count        #Accesing the variable count declared outside the function
    count = count+1
    
    reduce=open("BookDetails.txt","w")                        
    for i in range(len(book_details)): #Rewriting the file with book details with subtracted number of books
        reduce.write(book_details[i][0]+","+book_details[i][1]+","+str(book_details[i][2])+","+str(book_details[i][3]))
    reduce.close()
    
def condition():    #This function asks the user if they want to borrow more books as well and loops the program from stock() function if user agrees
    while True:
        try:
            condition = str(input("Do you want to borrow other books as well?(Y/N)"))
            if condition.upper() == "Y":
                stock()
                borrow()
            elif condition.upper() == "N":
                break
            else:
                raise ValueError
        except ValueError:
            print("\nPlease enter 'Y' for Yes or 'N' for No.") #Exception handling

    
    

def borrow_details(): #This function asks the name and phone number of the borrower and writes it in new file with all the details
    print("*****For the preparation of transaction***** ")
    name = str(input("\nPlease enter your name:")) #Asking user their name
    while True:
        phone = str(input("\nPlease enter your phone number:"))#Asking phone number
        try:
            phone = int(phone)
            break
        except:
            print ("Please enter phone number in correct format.")#Exception handling on invalid number entered
    borrowed_date = date.today()
    Bill = open(str(phone)+" "+name+".txt","w") #Creating a new text file for the transaction
    Bill.write("Name: "+name+"\nPhone No: "+str(phone)+"\nBorrowed Date:"+str(borrowed_date)+"\n Number of books: "+str(count))#Writing the details of the borrower
    total = 0.0
    for each in selected_book.keys():
        Bill.write("\nBook name:"+each+","+" Number:"+str(selected_book[each])+",") #Writing the name and number of books borrowed
        for i in range (len(book_details)):
            if each == book_details[i][0]:
                price = float(selected_book[each])*float(book_details[i][3]) #calculating price of the books
                total = total+price   #calculating total price of the transaction
                Bill.write(" Price: $ "+str(price))
    returnDate = borrowed_date+timedelta(days=10) #calculating the returning date
    Bill.write("\nTotal: $ "+str(total)+"\nReturn Date: "+str(returnDate)) # writing total amount and return date on the file
    Bill.write("\nThe books are to be returned within 10 days.\n Submission after that shall be fined 10% of the price each day.")#small note for the borrower
    print("\nYour details are registered successfully in file named:"+str(phone)+name)
    Bill.close()
                
        


        
            
            
            
