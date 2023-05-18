with open("./input.txt", "r") as handle:
    calTotalList = []
    myList = handle.read().splitLines()
    for m in myList:
        elfsCals = m.split("\n")
        newList = []
        totalCals = 0
        for everything in elfsCals:
            newList.append(int(everything))
            for number in newList:
                totalCals = totalCals+number
        calTotalList.append(totalCals)
    print(sorted(calTotalList))
