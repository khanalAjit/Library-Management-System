import Return
import Split

def display_rdata():
    count = 5
    success = False
    while success == False:
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

        a = "Returner - "+fName+"_"+lName+".txt"

        try:
            with open(a,"r") as file:
                lines = file.readlines()
                lines = [a.strip('$') for a in lines]

            with open(a,"r") as file:
                data = file.read()
                print(data)
                print("")
                print("")
                success = True
        except:
            print("Returner not found. Try Again!")
            count -= 1
            print("Remaining Try: ",count)
            if(count >= 1):
                success = False
            else:
                success = True
                print("Returner Not Found. Try Again Later")
                print("")