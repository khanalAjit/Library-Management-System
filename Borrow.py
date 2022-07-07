import DaT
import Split

def borrow_Book():
    loop = True
    choice_list = []
    totalPrice = 0
    success = False
    count = 0

    while(True):
        fName = input("Enter the first name of the borrower: ")
        if fName.isalpha():
            break
        else:
            print("Names cannot have special characters.")

    while(True):
        lName = input("Enter the last name of the borrower: ")
        print("")
        if lName.isalpha():
            break
        else:
            print("Names cannot have special characters.")

    Borrow_Text = "Borrower - "+fName+"_"+lName+".txt"

    with open(Borrow_Text,"w+") as formatb:
        formatb.write("\t|*********** Library Management Systems ***********| \n")
        formatb.write("\t\t\t\t\t Islington College \n\n")
        formatb.write(" \t\t ---> Book Borrowed By: "+fName+ " "+lName+"\n\n")
        formatb.write(" \t\t ---> Borrowed Date: "+DaT.Date()+" \n")
        formatb.write(" \t\t ---> Borrowed Time: "+DaT.Time()+"\n\n")
        formatb.write("\t----------------------------------------------------------------\n")
        formatb.write(" | S.N.\t | Book Name \t\t\t\t | Author Name \t\t | Price($) \n")
        formatb.write("\t----------------------------------------------------------------\n")
    
    while success == False:
        while loop == True:
            quit_borrow = False
            print("")
            print("Select from the options given below: ")
            print ("")

            for i in range(len(Split.bookName)):
                print("Enter ",i,"to borrow: ",Split.bookName[i])
            print("")
            
            try:
                a = int(input("Enter your choice: "))
                for i in range(len(choice_list)):
                    if(a == choice_list[i]):
                        print("You can't borrow the same book.")
                        quit_borrow = True
                        break
            
                while quit_borrow == False:
                    choice_list.append(a)
                    count = count+1
                    
                    print("")
                    try:
                        if(int(Split.quantity[a]) > 0):
                            totalPrice += float(Split.price[a])
                            print("The book ",Split.bookName[a], " has been issued for ",fName)
                            print("")
                            with open(Borrow_Text,"a") as formatb:
                                formatb.write(" | "+str(count)+". \t | "+Split.bookName[a]+" \t\t\t | "+Split.authorName[a]+ " \t\t | "+Split.price[a]+"\t| \n")
                                formatb.write("\t----------------------------------------------------------------\n")

                            Split.quantity[a] = int(Split.quantity[a])-1
                            with open("Stock.txt","w+") as bupdate:
                                for i in range (len(Split.bookName)):
                                    bupdate.write(Split.bookName[i]+","+Split.authorName[i]+","+str(Split.quantity[i])+","+"$"+Split.price[i]+"\n")
                                    success = False
                                    loop = False
                                    quit_borrow = True
                                         
                            
                            print("Do you want to borrow more books?")
                            extra_choice = input("Enter 'Y' if Yes and 'N' if No : ")

                            if(extra_choice.upper() == "Y"):
                                if(count <= len(Split.bookName) - 1):
                                    loop = True
                                    quit_borrow = False
                                    break
                                else:
                                    print("")
                                    print("You've borrowed all the available books.")
                                    print("")
                                    print("We will be adding more books in our collection soon.")
                                    print("")
                                    print("Enjoy reading the books.")
                                    print("")

                                    quit_borrow = True
                                    loop = False
                                    success = True
                                    break
                                   

                            elif(extra_choice.upper() == "N"):
                                print("")
                                print("Enjoy the book.")
                                quit_borrow = True
                                loop = False
                                success = True
                                break
                            

                            else:
                                print("Please enter the values given in the option.")
                                loop = True

                        else:
                            print("We do not have the required book in the stock. Sorry!")
                            success = False
                            borrow_Book()
                            

                    except IndexError:
                        print("")
                        print("Please enter the number given in the option.")
                        quit_borrow = True
                        success = False
                        loop = True

            except ValueError:
                print("")
                print("Please enter the suggested value.")
                print("Avoid the use of special characters.")
                success = False
                loop = True
                
                


    with open(Borrow_Text,"a") as formatb:
        formatb.write(" | \t\t\t\t\t ---> Total Price is $"+str(totalPrice) )
