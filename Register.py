def register(): #This function asks user the details of the books to store in the stock file
    a = 0 
    i = int(input("\nEnter number of books you want to register:"))
    reg = open("BookDetails.txt","a")
    while (a < i):
        name = str(input("\nEnter name of the book:"))
        auth = str(input("\nEnter name of the author:"))
        while True:
            num = str(input("\nEnter number of books:"))
            try:
                num = int(num)
                break
            except:
                print("\nPlease enter integer value for number of books.\n")
        while True:
            rate = str(input("\nEnter rent rate per day of the book:"))
            try:
                rate = int(rate)
                break
            except:
                print("\nPlease enter integer value for rate.\n")
        reg.write(name+","+auth+","+str(num)+","+str(int(rate))+"\n")#writing the book details in the stock file
        print("")
        a = a+1
    print("\nThe books are registered successfully.\n")
    reg.close()
    
