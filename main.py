import Display
import Borrow
import Borrower_Data
import Split
import Return
import Returner_Data


def start():
    while(True):
       
        print("  |*****************   Welcome to the Library Management System    *****************|")
        print("\t\t\t\t Of Islington College ")
        print("\t------------------------------------------------------------------------")
        print("")

        print("\t --->Enter 1: To display available books.")
        print("")
        print("\t --->Enter 2: To borrow a book.")
        print("")
        print("\t --->Enter 3: To return a book.")
        print("")
        print("\t --->Enter 4: To create Borrower's bill.")
        print("")
        print("\t --->Enter 5: To create Returner's bill.")
        print("")
        print("\t --->Enter 6: To exit the Library.")
        print("\t------------------------------------------------------------------------")

        try:
            print("")
            choice = int(input("Please enter your choice."))
            print()

            if(choice == 1):
                Split.split()
                Display.display_Books()
                print("")

            elif(choice == 2):
                Split.split()
                Borrow.borrow_Book()
                print("")


            elif(choice == 3):
                Split.split()
                Return.return_Book()
                print("")

            elif(choice == 4):
                Borrower_Data.display_bdata()

            elif(choice == 5):
                Returner_Data.display_rdata()

            elif(choice == 6):
                print("")
                print("Thank You for visiting our Library. Hope to see you soon.")
                print("")
                print("Keep Reading! Keep Dreaming! Keep Smiling")
                break

        except ValueError:
            print("Please enter the choice given in the options.")

start()

            


        





