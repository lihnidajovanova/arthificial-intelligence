def majority_votes(votes):
    if not votes:
        return None

    majority_count = len(votes) // 2 + 1

    for vote in set(votes):
        if votes.count(vote) >= majority_count:
            return vote

    return None


if __name__ == '__main__':
    votes = input("Внесете ги гласовите разделени со празно место: ").split()
    print(majority_votes(votes))
