def dice_game(rolls):
    players = ["p1", "p2", "p3", "p4"]
    while len(players) > 1:
        scores = {}
        for i, roll in enumerate(rolls):
            total = sum(roll)
            if players[i % len(players)] in scores:
                scores[players[i % len(players)]] += total
            else:
                scores[players[i % len(players)]] = total
        min_score = min(scores.values())
        min_players = [player for player in scores if scores[player] == min_score]
        if len(min_players) == 1:
            players.remove(min_players[0])
        else:
            min_round_scores = {}
            for i, roll in enumerate(rolls):
                if players[i % len(players)] in min_players:
                    if players[i % len(players)] in min_round_scores:
                        min_round_scores[players[i % len(players)]] += sum(roll)
                    else:
                        min_round_scores[players[i % len(players)]] = sum(roll)
            min_round_player = min(min_round_scores, key=min_round_scores.get)
            players.remove(min_round_player)
    return players[0]


# Пример
print(dice_game([(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (4, 3), (1, 5), (1, 5), (5, 6), (2, 2)]))  # ➞ "p1"
