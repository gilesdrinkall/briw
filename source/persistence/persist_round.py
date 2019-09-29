def persist_round(drink_round):
    file = open("round.txt", "w")
    file.write("\n".join(drink_round.round))
    file.close()
    print("\n\nRound saved!")