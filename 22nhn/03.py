from collections import deque
import sys
limit_number = 200001
sys.setrecursionlimit(limit_number)

def run_maze(maze, query):
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, 1, -1]
    
    queues = deque([])

    x_maze = len(maze[0])
    y_maze = len(maze)

    temp = list(map(str, query.split()))
    start = [int(temp[0]) - 1, int(temp[1]) - 1]
    end = [int(temp[2]) - 1, int(temp[3]) - 1]
    visit = [start]
    able = list(temp[4])

    queues.append([start[0], start[1], 1])

    while queues:
        now = queues.popleft()

        if now[:2] == end:
            return now[2]

        for i in range(4):
            next_maze = [now[0] + dy[i], now[1] + dx[i]]
            
            if  0 <= next_maze[0] < y_maze and 0 <= next_maze[1] < x_maze:
                if next_maze not in visit and maze[next_maze[0]][next_maze[1]] in able:
                    queues.append([next_maze[0], next_maze[1], now[2] + 1])
                    visit.append(next_maze)

    return -1

def solution(maze, queries):
    answer = []

    for q in queries:
        answer.append( run_maze(maze, q) )

    return answer




if __name__ == "__main__":
    maze = ["AAA", "ABB", "ABA"]
    queries = ["1 1 1 3 A", "1 3 3 1 A", "1 1 3 3 A", "1 1 3 3 AB"]

    print(solution(maze, queries))


# a = deque([])
# a.append('asd')
# a.append('bds')

# print(a)


# a = [1, 2, 3]
# b = [1, 2]

# if a[:2] == b:
#     print('ok')
