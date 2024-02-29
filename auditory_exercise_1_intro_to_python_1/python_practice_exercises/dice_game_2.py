def dice_game_from_input():
    players = ["p1", "p2", "p3", "p4"]
    rolls = []
    while len(players) > 1:
        scores = {}
        for i in range(len(players)):
            roll_str = input(f"Enter dice rolls for {players[i]} (format: dice1 dice2): ")
            roll = tuple(map(int, roll_str.split()))
            rolls.append(roll)
            total = sum(roll)
            if players[i] in scores:
                scores[players[i]] += total
            else:
                scores[players[i]] = total
        min_score = min(scores.values())
        min_players = [player for player in scores if scores[player] == min_score]
        if len(min_players) == 1:
            players.remove(min_players[0])
        else:
            min_round_scores = {}
            for i in range(len(players)):
                if players[i] in min_players:
                    roll_str = input(f"Enter dice rolls for {players[i]} (format: dice1 dice2): ")
                    roll = tuple(map(int, roll_str.split()))
                    rolls.append(roll)
                    if players[i] in min_round_scores:
                        min_round_scores[players[i]] += sum(roll)
                    else:
                        min_round_scores[players[i]] = sum(roll)
            min_round_player = min(min_round_scores, key=min_round_scores.get)
            players.remove(min_round_player)
    return players[0]


# Пример
print(dice_game_from_input())
