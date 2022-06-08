from datetime import date #importing date and time from python library
from datetime import datetime
import os
def returning(): #This function opens the file where the details of the borrower is stored and performs necessary calculations to complete the transaction
    print("*****For returning books******\nPlease enter the following fields.")
    global name
    name = str(input("Name: "))
    global phone
    phone = str(input("Phone: "))
    detail = open(phone+" "+name+".txt","r+") #opening the text file where the borrowed transaction is stored
    global info     #declaring variable info as global to access in other functions as well
    info = detail.read().splitlines() #reading every line of the text file stored in detail
    global amnt     #declaring amnt as global for access in other functions as well
    amnt = info[3].split(":") #slitting line 2 by ':'
    print("\nThe books you had borrowed are:\n")
    for i in range(int(amnt[1])):
        print(info[4+i]) #displaying the borrowed books
    bdate = info[2].split(":") #extracting the borrowed date from the text file
    rdate = datetime.today() #extracting todays date
    borrowed_date = datetime.strptime(bdate[1],"%Y-%m-%d")#arranging the extracted borrowed date and arranging in specific order
    days = (rdate - borrowed_date).days #calculating total days consumed
    print("\nYou borrowed the books on:"+str(borrowed_date))
    print("\nToday's date is:"+str(rdate))
    total_fine = 0
    if days>10: #calculating fine if days consumed is greater thean 10
        for i in range(int(amnt[1])):
            con = info[4+i].split(":")
            price = ''.join(filter(str.isdigit,con[3]))
            fine = (10/100)*float(price)*(days-10)
            total_fine = total_fine+fine
        print("\nSince you failed to return the book within 10 days,")
        print("\nYou will have to pay total fine of $ "+str(total_fine)) #Displaying the fine to be paid
    else:
        print("\nThank you for returning the books in time.")

def restocking(): #This function add the required book to the stock
    book_details = [] #declaring an array
    details = open("BookDetails.txt","r") #opening the stock text file as readable
    lines = details.readlines()
    for each in lines:
        detail = each.split(",")
        book_details.append(detail) #adding the content into the array
    details.close()

    for j in range(len(book_details)):
        for k in range(int(amnt[1])):
            a = info[4+k].split(",")
            b = a[0].split(":")
            c = b[1]
            if book_details[j][0]==c:
                number = ''.join(filter(str.isdigit,a[1])) #filtering the integer from the list a
                book_details[j][2] = int(book_details[j][2])+int(number) #adding the returned number of books in the index containing numbers of books
        
    
    stock = open("BookDetails.txt","w")
    for i in range(len(book_details)):
        stock.write(book_details[i][0]+","+book_details[i][1]+","+str(book_details[i][2])+","+book_details[i][3]) #Rewriting the stock text file with added number of books
    stock.close()
    os.remove(phone+" "+name+".txt")
    print("\n*****The stock has been updated******")
    print("\n*****THANK YOU!******")
