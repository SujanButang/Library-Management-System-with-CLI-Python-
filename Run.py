import main                             #importing main.py file
welcome = open("Welcome.txt",'r')       #opening Welcome.txt file ass readable
print (welcome.read())                  #displaying the content of welcome.txt file
welcome.close()                         #closing the txt file
main.main_program()                     #Calling function main_program() of main.py
