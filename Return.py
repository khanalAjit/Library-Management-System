import DaT
import Split

def return_Book():
    while(True):
        fName = input("Enter the first name of the returner: ")
        if fName.isalpha():
            break
        else:
            print("Names cannot have special characters.")

    while(True):
        lName = input("Enter the last name of the returner: ")
        print("")
        if lName.isalpha():
            break
        else:
            print("Names cannot have special characters.")


    a = "Borrower - "+fName+"_"+lName+".txt"

    try:
        with open(a,"r") as file:
            lines = file.readlines()
            lines = [a.strip('$') for a in lines]

        with open(a,"r") as file:
            data = file.read()
            print(data)
    except:
        print("Borrower not found.")
        return_Book()
    
    Return_Text = "Returner - "+fName+"_"+lName+".txt"

    with open(Return_Text,"w+") as formatr:
        formatr.write("\t |************ Library Management System************| \n\n")
        formatr.write("\t\t ---> Book Returned By: "+fName+"\n\n")
        formatr.write("\t\t ---> Return Date: "+DaT.Date()+"\n")
        formatr.write("\t\t ---> Return Time: "+DaT.Time()+"\n\n")
        formatr.write("    ----------------------------------------------------------------------- \n")
        formatr.write(" | S.N.\t | Book Name \t\t\t | Author Name \t\t | Price($) \n")
        formatr.write("    ----------------------------------------------------------------------- \n")

    total_price = 0.0
    for i in range (len(Split.bookName)):
        if Split.bookName[i] in data:
            with open(Return_Text,"a") as formatr:
                formatr.write(" | "+str(i+1)+". \t | "+Split.bookName[i]+"\t\t | "+Split.authorName[i]+" \t\t | "+Split.price[i]+"\t |\n")
                formatr.write("    ----------------------------------------------------------------------- \n")

                Split.quantity[i] = int(Split.quantity[i]) + 1
            
            total_price = total_price + float(Split.price[i])

    

    print("Has the borrowed time for the book expired?")
    print("Type 'Y' if it has expired and type 'N' if it hasn't")
    status = input("Type here: ")

    if(status.upper() == 'Y'):
        print("For how many days has the borrowed books expired for?")
        exp_days = int(input("Type Here: "))

        fine = 0.5 * exp_days

        with open(Return_Text,"a") as formatr:
            formatr.write("\t\t\t\t --->Delayed Return Fine = $"+str(fine)+"\n")

        total_price = total_price + fine

    

    print("")
    print("Grand Total = $"+str(total_price))

    with open(Return_Text,"a") as formatr:
        formatr.write("\t\t\t\t ---> Grand Total = $"+str(total_price)+"\n")
    
    with open("Stock.txt","w+") as txt_file:
        for i in range (len(Split.bookName)):
            txt_file.write(Split.bookName[i] + "," +Split.authorName[i]+ ","+ str(Split.quantity[i])+ ",$" +Split.price[i]+"\n")

 
