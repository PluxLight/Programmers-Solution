import sys
limit_number = 200001
sys.setrecursionlimit(limit_number)
answer = 0

def dfs(n, players, power, k, vsplayer, stack_win, stack_lose):
    global answer
    
    if n <= vsplayer:
        answer = max(answer, power)
        return

    if stack_lose > n // 2:
        return

    if players[vsplayer] <= power:
        dfs(n, players, power + stack_win, k, vsplayer + 1, stack_win + 1, stack_lose) # win

    if k * (n-vsplayer) >= int((vsplayer+1+n)/2*(n-vsplayer)):
        dfs(n, players, power + k, k, vsplayer + 1, 1, stack_lose + 1) # lose

    

def solution(players, power, k):
    n = len(players)

    if k * n >= int((1+n)/2*n):
        return k * n + power

    dfs(n, players, power, k, 0, 1, 0) # n, players, power, k, vs n-th player, win stack, lose stack
    
    return answer






if __name__ == "__main__":
    # players = [10, 11, 15, 14, 16, 18, 19, 20]
    players = [10, 11]
    power = 10
    k = 2

    print( solution(players, power, k) )
