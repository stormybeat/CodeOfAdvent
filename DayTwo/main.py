with open("./DayTwo/input.txt", "r") as strategyGuide:
    total = 0
    games = strategyGuide.read().split("\n")
    for game in games:
        roundTotal = 0
        players = game.split(" ")


        # Comparisons for Rock
        if players[0] == "A" and players[1] == "X":
            roundTotal += 3 #Tie
        if players[0] == "A" and players[1] == "Y":
            roundTotal += 6 #W
        if players[0] == "A" and players[1] == "Z":
            roundTotal += 0 #L

        # Comparisons for paper
        if players[0] == "B" and players[1] == "X":
            roundTotal += 0 #L
        if players[0] == "B" and players[1] == "Y":
            roundTotal += 3 #Tie
        if players[0] == "B" and players[1] == "Z":
            roundTotal += 6 #W

        # Comparisons for scissors
        if players[0] == "C" and players[1] == "X":
            roundTotal += 6 #W
        if players[0] == "C" and players[1] == "Y":
            roundTotal += 0 #L
        if players[0] == "C" and players[1] == "Z":
            roundTotal += 3 #Tie
    
        # adding the value of RPS to score. 
        if players[1] == "X":
            roundTotal += 1
        if players[1] == "Y":
            roundTotal += 2
        if players[1] == "Z":
            roundTotal += 3

        total = roundTotal + total
    
        print(f"Round Total: {roundTotal}")
    print(f"Total: {total}")