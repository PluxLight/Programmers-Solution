def solution(balance, transaction, abnormal):
    answer = []
    users = {}

    for i, bal in enumerate(balance):
        users[i+1] = []
        users[i+1].append([i+1, bal])

    for ta in transaction:
        sum_value = 0

        while sum_value < ta[2]:
            key = users[ta[0]][-1][0]

            if users[ta[0]][-1][1] <= ta[2] - sum_value:
                value = users[ta[0]][-1][1]
                users[ta[0]].pop()
            else:
                value = ta[2] - sum_value
                users[ta[0]][-1][1] = users[ta[0]][-1][1] - value
        
            users[ta[1]].append([key, value])
            sum_value += value

    for user, golds in users.items():
        sum_gold = 0

        for gold in golds:
            if gold[0] not in abnormal:
                sum_gold += gold[1]

        answer.append(sum_gold)



    return answer



if __name__ == "__main__":
    balance = [30, 30, 30, 30]
    transaction = [[1, 2, 10], [2, 3, 20], [3, 4, 5], [3, 4, 30]]
    abnormal = [1]
    print(solution(balance, transaction, abnormal))



# a = {}
# a[1] = []

# a[1].append([0,1])

# print(a[1][-1][1])

# a[1].pop()

# print(a[1])