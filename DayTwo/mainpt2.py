with open("./DayTwo/input.txt", "r") as strategyGuide:
    total = 0
    games = strategyGuide.read().split("\n")
    for game in games:
        players = game.split(" ")
        roundTotal = 0

        # Comparisons for Rock
        if players[0] == "A" and players[1] == "X":
            roundTotal += 3 #Lose for scissors
        if players[0] == "A" and players[1] == "Y":
            roundTotal += 4 #Draw for rock
        if players[0] == "A" and players[1] == "Z":
            roundTotal += 8 #Win for paper

        # Comparisons for paper
        if players[0] == "B" and players[1] == "X":
            roundTotal += 1 #Loss for rock
        if players[0] == "B" and players[1] == "Y":
            roundTotal += 5 #Draw for paper
        if players[0] == "B" and players[1] == "Z":
            roundTotal += 9 #Win for scissors

        # Comparisons for scissors
        if players[0] == "C" and players[1] == "X":
            roundTotal += 2 #Loss for rock
        if players[0] == "C" and players[1] == "Y":
            roundTotal += 6 #Draw for paper
        if players[0] == "C" and players[1] == "Z":
            roundTotal += 7 #Loss for scissors

        total += roundTotal
        print(f"Round Total: {roundTotal}")

    print(f"Total: {total}")