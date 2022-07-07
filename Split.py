def split():
    global bookName
    global authorName
    global quantity
    global price

    bookName = []
    authorName = []
    quantity = []
    price = []


    with open("Stock.txt","r") as books:
        lines = books.readlines()
        lines = [s.strip('\n') for s in lines]

        for i in range(len(lines)):
            count = 0
            for j in lines[i].split(','):
                if(count == 0):
                    bookName.append(j)
                elif(count == 1):
                    authorName.append(j)
                elif(count == 2):
                    quantity.append(j)
                elif (count == 3):
                    price.append(j.strip("$"))
                count+=1



