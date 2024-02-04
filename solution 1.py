# function
# file operation
# exception handling
def Daughter():
    try:
        look = open("daughter.txt","r")
        print(look.read())
    except IOError :
        print("file not found")
    except :
        print ("something went wrong. Try again!")

# function
# file operation
# exception handling
def Son():
    try:
        look = open("son.txt","r")
        print(look.read())
    except IOError :
        print("file not found")
    except :
        print ("something went wrong. Try again!")

# function
# input validation
# while and for loops
# if else conditions
# spliting a string into list
def Question():
    Ask = ""
    while (Ask == ""):
        Ask = input("Ask question : ")
        i = 0
        split = Ask.split(" ")
        new_list = []
        for word in split:
            a = word.lower()
            new_list.append(a)
        if "daughter" in new_list :
            Daughter()
            break
        elif "son" in new_list :
            Son()
            break
        else:
            print("Invalid Question. Follow the rules please.")
            
# main function
# while loop
# if else condition
def menu():
    choice = ""
    while (choice != "quit"):
        new = input("Would you like to ask a question or quit? ")
        if new.lower() != "quit" :
            choice = ""
            Question()
        else:
            choice = new.lower()

    print("Thank you. You have quit the stimulation.")

# function
# file operation
# exception handling
def start():
    try:
        look = open("start.txt","r")
        print(look.read())
    except IOError :
        print("file not found")
    except :
        print ("something went wrong. Try again!")

# calling a function
start()
menu()


                
