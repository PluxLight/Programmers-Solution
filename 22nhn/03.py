# Authored by: wonhyeongseo
DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # left right up down


def solution(plan: list, queries: list) -> list:
    """Calculate shortest path given plan and queries."""
    answer = []
    for query in queries:
        entrance, exit_, open_doors = interpret(query)
        answer.append(
            shortest_path(
                make_maze(plan, open_doors),
                entrance,
                exit_
            )
        )
    return answer


def interpret(query: str) -> tuple:
    """Interpret query for post-processing."""
    t = query.split()
    sx, sy, ex, ey = [int(i) - 1 for i in t[:-1]]
    return (sx, sy), (ex, ey), t[-1]


def make_maze(plan: list, open_doors: str) -> list:
    """Label maze based on plan and charcode for open doors."""
    return [
        [door in open_doors for door in floor]
        for floor in plan
    ]


def shortest_path(maze: list, entrance: tuple, exit_: tuple) -> int:
    """How many steps to reach exit of a maze from entrance."""
    def make_step(n: int) -> None:
        """Breadth-first search."""
        nonlocal to_search
        if to_search:
            temp = []
            for (x, y) in to_search:
                for (dx, dy) in DELTAS:
                    if (
                        -1 < x+dx < floors and
                        -1 < y+dy < doors and
                        journal[x+dx][y+dy] == 0 and
                        maze[x+dx][y+dy]
                    ):
                        journal[x+dx][y+dy] = n + 1
                        temp.append((x+dx, y+dy))
            to_search = temp
        else:
            raise EOFError("No doors to open.")

    floors, doors = len(maze), len(maze[0])
    journal = [
        [0 for _ in range(doors)]
        for _ in range(floors)
    ]
    journal[entrance[0]][entrance[1]] = 1
    to_search = [(entrance[0], entrance[1])]

    n = 0
    while journal[exit_[0]][exit_[1]] == 0:
        n += 1
        try:
            make_step(n)
        except EOFError:
            return -1
    else:
        return journal[exit_[0]][exit_[1]]


if __name__ == "__main__":
    maze = ["AAA", "ABB", "ABA"]
    queries = ["1 1 1 3 A", "1 3 3 1 A", "1 1 3 3 A", "1 1 3 3 AB"]

    print(solution(maze, queries))
