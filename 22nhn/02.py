# Authored by: PluxLight
# refactor: wonhyeongseo

def solution(balance, transaction, abnormal):
    users = {
        i: [[i, bal]]
        for i, bal in enumerate(balance, start=1)
    }

    for (source, destination, transaction_value) in transaction:
        sum_value = 0
        while sum_value < transaction_value:
            recent = users[source][-1]
            if recent[1] <= (to_pay := transaction_value - sum_value):
                value = recent[1]
                users[source].pop()
            else:
                value = to_pay
                recent[1] -= value
            users[destination].append([recent[0], value])
            sum_value += value

    return [
        sum(value
            for (key, value) in history
            if key not in abnormal)
        for history in users.values()
    ]


if __name__ == "__main__":
    balance = [30, 30, 30, 30]
    transaction = [[1, 2, 10], [2, 3, 20], [3, 4, 5], [3, 4, 30]]
    abnormal = [1]
    print(solution(balance, transaction, abnormal))  # [0, 20, 15, 55]
