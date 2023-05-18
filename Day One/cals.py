with open("./input.txt", "r") as handle:
    calTotalList = []
    myList = handle.read().split("\n\n")
    for m in myList:
        elfsCals = m.split("\n")
        newList = []
        totalCals = 0
        for everything in elfsCals:
            if not everything:
                continue
            newList.append(int(everything))
        for number in newList:
            totalCals = totalCals+number
        calTotalList.append(totalCals)
    print(sorted(calTotalList))
