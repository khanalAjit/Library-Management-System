import Split

def display_Books():
    count = 0
    print("We have following books available: ")
    print("")
    for i in range (len(Split.bookName)):
        count += 1
        print(count,".",Split.bookName[i]," by ",Split.authorName[i], " for $",Split.price[i])
        print("")
    
