# Authored by: wonhyeongseo

def problematic_deck_between_players(first_player: list, second_player: list) -> bool:
    temp = []
    temp.extend(first_player)
    temp.extend(second_player)
    return len(set(temp)) < len(temp)


def problematic_deck_between_rounds(last_round: list, this_round: list) -> bool:
    return len(set(last_round) & set(this_round)) > 1


def solution(cards1, cards2):
    answer = 0
    last_rounds = ([], [])
    for first_player, second_player in zip(cards1, cards2):
        if (problematic_deck_between_players(first_player, second_player) or
            problematic_deck_between_rounds(last_rounds[0], first_player) or
                problematic_deck_between_rounds(last_rounds[1], second_player)):
            answer += 1
        last_rounds = first_player, second_player

    return answer


if __name__ == "__main__":
    cards1 = [[13, 21, 24, 29, 50], [1, 12, 20, 21, 32], [
        16, 26, 34, 46, 52], [9, 11, 16, 16, 21], [3, 8, 10, 16, 20]]
    cards2 = [[5, 10, 15, 41, 49], [6, 14, 15, 19, 46], [
        5, 42, 43, 51, 52], [5, 6, 11, 13, 45], [5, 9, 11, 13, 45]]
    print(solution(cards1, cards2))
