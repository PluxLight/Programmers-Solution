def check_cards(card1, card2, other):
    sum_cards = list(set(card1 + card2))
    count = []

    if other:
        if len(sum_cards) == 10:
            return 0
        else:
            return 1
    else:
        for card in card1:
            if card in card2 and card not in count:
                count.append(card)

        if len(count) >= 2:
            return 1
        else:
            return 0



def solution(cards1, cards2):
    answer = 0
    n = len(cards1)
    value = 0

    answer += check_cards(cards1[0], cards2[0], True)

    for i in range(1, n):
        value += check_cards(cards1[i], cards2[i], True)
        value += check_cards(cards1[i], cards1[i-1], False)
        value += check_cards(cards2[i], cards2[i-1], False)

        if value > 0:
            answer += 1
    
        value = 0
        
    return answer




if __name__ == "__main__":
    cards1 = [[13, 21, 24, 29, 50], [1, 12, 20, 21, 32], [16, 26, 34, 46, 52], [9, 11, 16, 16, 21], [3, 8, 10, 16, 20]]
    cards2 = [[5, 10, 15, 41, 49], [6, 14, 15, 19, 46], [5, 42, 43, 51, 52], [5, 6, 11, 13, 45], [5, 9, 11, 13, 45]]
    print(solution(cards1, cards2))